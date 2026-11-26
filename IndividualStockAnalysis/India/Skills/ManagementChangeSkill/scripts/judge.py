"""
judge.py — one cached, strict-JSON question to the reading model.

The mechanical read finds candidates; the judge reads the COMPLETE
documents of a company and decides. Every answer is cached under a stamp
of the documents, the model and the prompt version, so a re-run asks only
what changed. The model is `MGMT_JUDGE_MODEL`, else `ANALYST_MODEL`, else
claude-opus-5, run through the `claude` CLI; no key is ever stored here.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import threading
from pathlib import Path

HERE = Path(__file__).resolve().parent
CACHE = HERE.parent / ".judge_cache.json"
MODEL = os.environ.get("MGMT_JUDGE_MODEL", os.environ.get("ANALYST_MODEL", "claude-opus-5"))
_LOCK = threading.Lock()
_MEM: dict | None = None


def available() -> bool:
    return shutil.which("claude") is not None


def _cache() -> dict:
    global _MEM
    if _MEM is None:
        try:
            _MEM = json.loads(CACHE.read_text()) if CACHE.exists() else {}
        except json.JSONDecodeError:
            _MEM = {}
    return _MEM


def parse_json(out: str) -> dict | None:
    """The first complete JSON object in the answer, tolerant of code
    fences, prose around it and trailing commas; None when there is none."""
    text = re.sub(r"```(?:json)?", "", out or "")
    dec = json.JSONDecoder()
    for m in re.finditer(r"\{", text):
        chunk = text[m.start():]
        try:
            obj, _ = dec.raw_decode(chunk)
        except json.JSONDecodeError:
            try:
                obj, _ = dec.raw_decode(re.sub(r",\s*([}\]])", r"\1", chunk))
            except json.JSONDecodeError:
                continue
        if isinstance(obj, dict) and obj:
            return obj
    return None


def stamp_of(*parts: str) -> str:
    return hashlib.md5(("\x1f".join(parts) + MODEL).encode("utf-8", "replace")).hexdigest()


def ask(key: str, stamp: str, prompt: str, allow_ai: bool = True, runner=None, require: tuple[str, ...] = ()) -> dict:
    """{'status': 'cached' | 'judged' | 'not assessed' | 'judge failed: …', **answer}.
    A malformed answer is asked once more. `require` names the top-level keys
    the answer must have: when a model's JSON is broken, the first object
    that parses can be an INNER one (an 'incoming' block), and that is a
    malformed answer, not an answer."""
    with _LOCK:
        hit = _cache().get(key) or {}
    if hit.get("stamp") == stamp and all(k in hit.get("answer", {}) for k in require):
        return {"status": "cached", **hit["answer"]}
    if not allow_ai or (runner is None and not available()):
        return {"status": "not assessed", "note": "judge not run — mechanical read only"}
    answer, failure = None, "unparseable"
    for attempt in range(2):
        q = prompt if attempt == 0 else (
            prompt + "\n\nYour previous answer was not valid JSON. Reply with ONE JSON object only — "
                     "no prose before or after it, no code fence, every string value properly escaped.")
        try:
            if runner is not None:
                out = runner(q)
            else:
                proc = subprocess.run(["claude", "-p", "--model", MODEL], input=q,
                                      capture_output=True, text=True, timeout=900)
                if proc.returncode != 0:
                    return {"status": f"judge failed: {(proc.stderr or proc.stdout or '')[-160:]}"}
                out = proc.stdout
        except Exception as e:                             # noqa: BLE001
            return {"status": f"judge failed: {e}"}
        answer = parse_json(out)
        if answer is not None and not all(k in answer for k in require):
            answer = None
        if answer is not None:
            break
        failure = "bad json" if "{" in (out or "") else "unparseable"
    if answer is None:
        return {"status": f"judge failed: {failure}"}
    with _LOCK:
        cache = _cache()
        cache[key] = {"stamp": stamp, "answer": answer}
        tmp = CACHE.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(cache, indent=1, ensure_ascii=False))
        tmp.replace(CACHE)
    return {"status": "judged", **answer}


def ok(res: dict | None) -> bool:
    return bool(res) and res.get("status") in ("judged", "cached")

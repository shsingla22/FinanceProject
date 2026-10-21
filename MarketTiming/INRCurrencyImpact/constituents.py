"""Current constituent lists for Nifty 50, Nifty Midcap 100 and Nifty
Smallcap 100, captured from the Screener.in public CNXMIDCAP / CNXSMALLCA /
NIFTY constituent pages (which mirror the official NSE Indices lists).

NSE ticker symbols are stored bare; the `.NS` suffix expected by Yahoo
Finance is appended at fetch time. Index membership changes semi-annually
- this snapshot is used as a fixed reference universe for the analysis.
"""

NIFTY_50 = [
    "RELIANCE", "HDFCBANK", "BHARTIARTL", "ICICIBANK", "SBIN",
    "TCS", "BAJFINANCE", "LT", "HINDUNILVR", "INFY",
    "SUNPHARMA", "MARUTI", "ADANIPORTS", "M&M", "AXISBANK",
    "NTPC", "ITC", "TITAN", "KOTAKBANK", "ONGC",
    "ULTRACEMCO", "HCLTECH", "ADANIENT", "BEL", "JSWSTEEL",
    "BAJAJ-AUTO", "POWERGRID", "BAJAJFINSV", "NESTLEIND", "COALINDIA",
    "TATASTEEL", "ASIANPAINT", "ETERNAL", "HINDALCO", "SHRIRAMFIN",
    "WIPRO", "GRASIM", "EICHERMOT", "SBILIFE", "INDIGO",
    "JIOFIN", "TRENT", "TECHM", "HDFCLIFE", "TMPV",
    "TATACONSUM", "APOLLOHOSP", "CIPLA", "DRREDDY", "MAXHEALTH",
]

NIFTY_MIDCAP_100 = [
    # Page 1
    "ICICIAMC", "BSE", "POWERINDIA", "BHEL", "POLYCAB",
    "GROWW", "IDEA", "GVT&D", "INDIANB", "LUPIN",
    "MARICO", "INDUSTOWER", "HEROMOTOCO", "GMRAIRPORT", "LGELECT",
    "MANKIND", "JSWENERGY", "ASHOKLEY", "BHARATFORG", "WAAREEENER",
    "ABCAPITAL", "ICICIGI", "AUROPHARMA", "LENSKART", "DABUR",
    # Page 2
    "SRF", "PERSISTENT", "MCX", "OFSS", "HINDPETRO",
    "NHPC", "HAVELLS", "NMDC", "NYKAA", "AUBANK",
    "PAYTM", "SAIL", "OIL", "POLICYBZR", "LTF",
    "SWIGGY", "SUZLON", "NATIONALUM", "FORTIS", "FEDERALBNK",
    "INDUSINDBK", "YESBANK", "ATGL", "LAURUSLABS", "ALKEM",
    # Page 3
    "GLENMARK", "DIXON", "BANKINDIA", "PHOENIXLTD", "BIOCON",
    "PRESTIGE", "NAUKRI", "RVNL", "SBICARD", "OBEROIRLTY",
    "IDFCFIRSTB", "COLPAL", "COFORGE", "MFSL", "TIINDIA",
    "VMM", "COROMANDEL", "UPL", "MRF", "APLAPOLLO",
    "GODREJPROP", "MOTILALOFS", "BDL", "KEI", "PATANJALI",
    # Page 4
    "RADICO", "PIIND", "SUPREMEIND", "HUDCO", "M&MFIN",
    "PREMIERENE", "360ONE", "COCHINSHIP", "TATACOMM", "IRCTC",
    "VOLTAS", "ASTRAL", "MPHASIS", "PAGEIND", "CONCOR",
    "KALYANKJIL", "GODFRYPHLP", "IREDA", "TATAINVEST", "BLUESTARCO",
    "LICHSGFIN", "JUBLFOOD", "EXIDEIND", "TATAELXSI", "KPITTECH",
]

NIFTY_SMALLCAP_100 = [
    # Page 1
    "MEESHO", "IDBI", "HINDCOPPER", "PIRAMALFIN", "POONAWALLA",
    "ASTERDM", "NH", "NAVINFLUOR", "ATHERENERG", "SONACOMS",
    "DELHIVERY", "WELCORP", "GRSE", "CHOLAHLDNG", "BANDHANBNK",
    "PWL", "GLAND", "HSCL", "STARHEALTH", "AMBER",
    "ANANDRATHI", "KAYNES", "IKS", "ANGELONE", "NUVAMA",
    # Page 2
    "KARURVYSYA", "PNBHOUSING", "ITI", "MRPL", "LALPATHLAB",
    "FORCEMOT", "WOCKPHARMA", "NBCC", "MANAPPURAM", "TENNIND",
    "CDSL", "TATATECH", "PPLPHARMA", "AEGISLOG", "NETWEB",
    "CESC", "CREDITACC", "SAILIFE", "HBLENGINE", "DATAPATTNS",
    "NEULANDLAB", "IGL", "GESHIP", "PINELABS", "RAMCOCEM",
    # Page 3
    "AFFLE", "GMDCLTD", "NATCOPHARM", "RBLBANK", "SAGILITY",
    "SARDAEN", "CAMS", "GPIL", "URBANCO", "ANANTRAJ",
    "TATACHEM", "IIFL", "CUB", "SYNGENE", "FSL",
    "CGCL", "CROMPTON", "TRITURBINE", "COHANCE", "CASTROLIND",
    "BRIGADE", "CHAMBLFERT", "AARTIIND", "INOXWIND", "REDINGTON",
    # Page 4
    "IFCI", "JYOTICNC", "JSWCEMENT", "DEEPAKFERT", "OLAELEC",
    "ARE&M", "JBMA", "BEML", "KEC", "KFINTECH",
    "ABREL", "PGEL", "IRCON", "APTUS", "DEVYANI",
    "FIVESTAR", "JMFINANCIL", "SIGNATURE", "AFCONS", "FIRSTCRY",
    "ZENSARTECH", "BLS", "RPOWER", "WHIRLPOOL", "SWANCORP",
]


def to_yahoo(ticker: str) -> str:
    """Return the Yahoo Finance ticker for an NSE symbol. Yahoo encodes
    '&' as '%26' in some symbols (e.g. M&M -> M%26M.NS) but yfinance also
    accepts the literal '&' form for most tickers — try literal first."""
    return f"{ticker}.NS"

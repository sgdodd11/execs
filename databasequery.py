# Packages import
import pandas as pd 
import wrds 

# Connect to WRDS
db = wrds.Connection()

# SQL query to perform (allegedly very efficient) join
params = {
    "seniority": (5, 6, 7),
    "tickers": (
        "AA", "AAL", "AAP", "AAPL", "ABBV", "ABG", "ABM", "ABNB", "ABT", "ACI", "ACM",
        "ADBE", "ADI", "ADM", "ADP", "AEE", "AEP", "AES", "AFG", "AFL", "AGCO", "AIG",
        "AIZ", "AJG", "ALB", "ALK", "ALL", "ALLY", "ALV", "AMAT", "AMD", "AMGN", "AMP",
        "AMRK", "AMT", "AMZN", "AN", "ANDE", "APA", "APD", "APH", "APO", "ARKO", "ARMK",
        "ARW", "ATUS", "AVGO", "AVT", "AVY", "AXP", "AZO", "BA", "BAC", "BAH", "BALL",
        "BAX", "BBWI", "BBY", "BDX", "BECN", "BEN", "BERY", "BGST", "BIIB", "BJ", "BK",
        "BKNG", "BKR", "BLDR", "BLK", "BMY", "BRKA", "BSX", "BURL", "BWA", "BX", "C",
        "CAG", "CAH", "CAR", "CARR", "CASY", "CAT", "CBRE", "CCK", "CDW", "CE", "CEG",
        "CFG", "CHK", "CHRW", "CHTR", "CHWY", "CI", "CINF", "CL", "CLF", "CLR", "CLX",
        "CMC", "CMCSA", "CMG", "CMI", "CMS", "CNC", "CNP", "CNXC", "COF", "COP", "COR",
        "COST", "CPB", "CPNG", "CRM", "CSCO", "CSX", "CTAS", "CTSH", "CTVA", "CVNA",
        "CVS", "CVX", "CYH", "CZR", "D", "DAL", "DAN", "DASH", "DD", "DE", "DELL",
        "DFS", "DG", "DGX", "DHI", "DHR", "DINO", "DIS", "DK", "DKS", "DLTR", "DOV",
        "DOW", "DRI", "DTE", "DUK", "DVA", "DVN", "DXC", "EA", "EBAY", "ECL", "ED",
        "EIX", "EL", "ELV", "EME", "EMN", "EMR", "EOG", "EPD", "EQH", "EQIX", "ES",
        "ET", "ETR", "EXC", "EXPD", "EXPE", "F", "FANG", "FAST", "FCNCA", "FCX", "FDX",
        "FE", "FI", "FIS", "FITB", "FL", "FLR", "FMCC", "FNF", "FNMA", "FOXA", "GD",
        "GE", "GEHC", "GILD", "GIS", "GLP", "GLW", "GM", "GNW", "GOOGL", "GPC", "GPI",
        "GPK", "GPN", "GPS", "GS", "GT", "GWW", "GXO", "HAL", "HBAN", "HCA", "HD",
        "HES", "HIG", "HII", "HLT", "HON", "HPE", "HPQ", "HRL", "HSIC", "HSY", "HTZ",
        "HUM", "IBKR", "IBM", "ICE", "IEP", "IFF", "INGR", "INTC", "INTU", "IP", "IPG",
        "IQV", "ISRG", "ITW", "J", "JBHT", "JBL", "JBLU", "JEF", "JLL", "JNJ", "JPM",
        "JWN", "K", "KD", "KDP", "KEY", "KHC", "KKR", "KLAC", "KMB", "KMI", "KMX", "KNX",
        "KO", "KR", "KSS", "L", "LAD", "LDOS", "LEA", "LEN", "LH", "LHX", "LKQ", "LLY",
        "LMT", "LNC", "LNG", "LOW", "LPLA", "LRCX", "LSXMA", "LULU", "LUMN", "LUV",
        "LVS", "LYV", "M", "MA", "MAN", "MAR", "MAS", "MCD", "MCHP", "MCK", "MDLZ",
        "MET", "META", "MGM", "MHK", "MKL", "MMC", "MMM", "MNST", "MO", "MOH", "MOS",
        "MPC", "MRK", "MS", "MSFT", "MSI", "MTB", "MTZ", "MU", "MUSA", "NEE", "NEM",
        "NFLX", "NGL", "NKE", "NOC", "NOV", "NOW", "NRG", "NSC", "NSIT", "NTRS", "NUE",
        "NVDA", "NVR", "NWL", "NWSA", "NYCB", "OC", "ODP", "OI", "OKE", "OMC", "OMI",
        "ON", "ORCL", "ORI", "ORLY", "OSK", "OTIS", "OVV", "OXY", "PAG", "PAGP", "PARA",
        "PARR", "PBF", "PCAR", "PCG", "PEG", "PEP", "PFE", "PFG", "PFGC", "PG", "PGR",
        "PH", "PHM", "PII", "PKG", "PLD", "PM", "PNC", "PPG", "PPL", "PRU", "PSX",
        "PVH", "PWR", "PXD", "PYPL", "QCOM", "QRTEA", "R", "RADCQ", "REGN", "RF",
        "RGA", "RJF", "ROK", "ROST", "RPM", "RS", "RSG", "RTX", "RUSHB", "SAH", "SAIC",
        "SANM", "SATS", "SBUX", "SCHW", "SEB", "SHW", "SJM", "SKX", "SMCI", "SNEX",
        "SNX", "SO", "SPGI", "SPTN", "SQ", "SRE", "STLD", "STT", "STZ", "SWK", "SYF",
        "SYK", "SYY", "T", "TAP", "TFC", "TGT", "THC", "THO", "TJX", "TMHC", "TMO",
        "TOL", "TRGP", "TRV", "TSCO", "TSLA", "TSN", "TXN", "TXT", "UAL", "UBER",
        "UFPI", "UGI", "UHS", "ULTA", "UNFI", "UNH", "UNM", "UNP", "UPS", "URI", "USB",
        "USFD", "V", "VFC", "VLO", "VMC", "VOYA", "VRTX", "VST", "VTRS", "VZ", "W",
        "WAB", "WBA", "WBD", "WCC", "WDAY", "WDC", "WEC", "WFC", "WHR", "WKC", "WLK",
        "WM", "WMB", "WMT", "WRB", "WSM", "WSO", "WY", "X", "XEL", "XOM", "XPO", "XYL",
        "YUMC", "ZBH", "ZTS"
    )
}


##############################################################
###         QUERY FOR FULL 5, 6, 7 DATA
##############################################################

df = db.raw_sql(
    """
    SELECT c.*, b.*
    FROM revelio_individual.individual_user c
    JOIN (
        SELECT b.*
        FROM revelio_individual.individual_positions b
        JOIN (
            SELECT rcid
            FROM revelio_common.company_mapping
            WHERE ticker IN %(tickers)s
        ) a ON b.rcid = a.rcid
        WHERE b.seniority IN %(seniority)s AND b.country = 'United States'
    ) b ON c.user_id = b.user_id
    """,
    params=params
)

memory_bytes = df.memory_usage(deep=True).sum()

# Convert to gigabytes (GB)
memory_gb = memory_bytes / (1024 ** 3)
print(f"DataFrame size: {memory_gb:.4f} GB")

# Export individual_user data.
df.to_csv("data/revelio_user_pos_fortune500US_567.csv.gz", index=False, compression='gzip')



##############################################################
###         QUERY FOR 7 DATA
###############################################################
 
# df_7s = db.raw_sql(
#     """
#     SELECT c.*, b.*
#     FROM revelio_individual.individual_user c
#     JOIN (
#         SELECT b.*
#         FROM revelio_individual.individual_positions b
#         JOIN (
#             SELECT rcid
#             FROM revelio_common.company_mapping
#             WHERE ticker IN %(tickers)s
#         ) a ON b.rcid = a.rcid
#         WHERE b.seniority = 7 AND b.country = 'United States'
#     ) b ON c.user_id = b.user_id
#     """,
#     params=params
# )

# Export individual_user data.
# df_7s.to_csv("data/revelio_user_pos_fortune500US_7.csv.gz", index=False, compression='gzip')
"""
=====================================================
Threat Intelligence Aggregator
Configuration File
=====================================================
"""

from pathlib import Path

# ---------------------------------------------------
# Project Directories
# ---------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

FEEDS_DIR = BASE_DIR / "FEEDS"
OUTPUT_DIR = BASE_DIR / "OUTPUT"
REPORTS_DIR = BASE_DIR / "REPORTS"

FEEDS_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)
REPORTS_DIR.mkdir(exist_ok=True)

# ---------------------------------------------------
# OSINT Threat Feeds
# ---------------------------------------------------

THREAT_FEEDS = {
    "EmergingThreats":
        "https://rules.emergingthreats.net/blockrules/compromised-ips.txt",

    "OpenPhish":
        "https://openphish.com/feed.txt",

    "URLHaus":
        "https://urlhaus.abuse.ch/downloads/text/",

    "FeodoTracker":
        "https://feodotracker.abuse.ch/downloads/ipblocklist.txt"
}

# ---------------------------------------------------
# Severity Thresholds
# ---------------------------------------------------

HIGH_THRESHOLD = 3
MEDIUM_THRESHOLD = 2
LOW_THRESHOLD = 1

# ---------------------------------------------------
# Output Files
# ---------------------------------------------------

NORMALIZED_CSV = OUTPUT_DIR / "normalized_iocs.csv"
CORRELATED_CSV = OUTPUT_DIR / "correlated_iocs.csv"

IP_BLOCKLIST = OUTPUT_DIR / "ip_blocklist.txt"
DOMAIN_BLOCKLIST = OUTPUT_DIR / "domain_blocklist.txt"
URL_BLOCKLIST = OUTPUT_DIR / "url_blocklist.txt"
HASH_BLOCKLIST = OUTPUT_DIR / "hash_blocklist.txt"

STATISTICS_JSON = OUTPUT_DIR / "statistics.json"

SOC_REPORT = REPORTS_DIR / "soc_report.csv"
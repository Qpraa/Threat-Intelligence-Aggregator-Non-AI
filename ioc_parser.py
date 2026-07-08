"""
ioc_parser.py
-----------------------------
Extracts Indicators of Compromise (IOCs) from downloaded threat feeds.

Author: Final Year Project
Project: Threat Intelligence Aggregator
"""

import re
from pathlib import Path
from collections import defaultdict

from config import FEEDS_DIR


class IOCParser:

    def __init__(self):
        self.feed_directory = FEEDS_DIR

        # IOC storage
        self.iocs = defaultdict(set)

        # Regular Expressions
        self.patterns = {

            "ips": re.compile(
                r"\b(?:25[0-5]|2[0-4]\d|1?\d?\d)"
                r"(?:\.(?:25[0-5]|2[0-4]\d|1?\d?\d)){3}\b"
            ),

            "domains": re.compile(
                r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b"
            ),

            "urls": re.compile(
                r"https?://[^\s\"'>]+"
            ),

            "md5": re.compile(
                r"\b[a-fA-F0-9]{32}\b"
            ),

            "sha1": re.compile(
                r"\b[a-fA-F0-9]{40}\b"
            ),

            "sha256": re.compile(
                r"\b[a-fA-F0-9]{64}\b"
            )
        }

    # ---------------------------------------

    def parse_file(self, file_path):

        try:

            with open(file_path, "r", encoding="utf-8", errors="ignore") as file:

                data = file.read()

            for ioc_type, pattern in self.patterns.items():

                matches = pattern.findall(data)

                for item in matches:
                    self.iocs[ioc_type].add(item)

        except Exception as e:

            print(f"[ERROR] {file_path} -> {e}")

    # ---------------------------------------

    def parse_directory(self):

        if not self.feed_directory.exists():

            print("Feed directory not found.")

            return self.iocs

        files = list(self.feed_directory.glob("*"))

        print(f"\nParsing {len(files)} feed files...\n")

        for file in files:

            if file.is_file():

                print(f"Reading: {file.name}")

                self.parse_file(file)

        return self.iocs

    # ---------------------------------------

    def statistics(self):

        print("\n========== IOC Statistics ==========\n")

        total = 0

        for key, values in self.iocs.items():

            print(f"{key.upper():10}: {len(values)}")

            total += len(values)

        print("----------------------------------")

        print(f"TOTAL IOCs : {total}")

        print("----------------------------------")

    # ---------------------------------------

    def get_iocs(self):

        return self.iocs


# ===============================================

if __name__ == "__main__":

    parser = IOCParser()

    parser.parse_directory()

    parser.statistics()
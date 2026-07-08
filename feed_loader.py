"""
feed_loader.py

Downloads threat intelligence feeds from OSINT sources.
Supports:
    • URLHaus
    • Emerging Threats
    • Custom TXT feeds

Author: Threat Intelligence Aggregator
"""

import requests
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

# Directory to store downloaded feeds
FEED_DIR = "feeds"

os.makedirs(FEED_DIR, exist_ok=True)


class FeedLoader:

    def __init__(self):
        self.feeds = {
            "urlhaus":
                "https://urlhaus.abuse.ch/downloads/text/",

            "emerging_ips":
                "https://rules.emergingthreats.net/blockrules/compromised-ips.txt"
        }

    def download_feed(self, name, url):

        filename = os.path.join(FEED_DIR, f"{name}.txt")

        try:

            logging.info(f"Downloading {name}")

            response = requests.get(url, timeout=30)

            response.raise_for_status()

            with open(filename, "w", encoding="utf-8") as f:
                f.write(response.text)

            logging.info(f"Saved -> {filename}")

            return filename

        except Exception as e:

            logging.error(f"{name} failed : {e}")

            return None

    def download_all(self):

        downloaded = []

        for name, url in self.feeds.items():

            file = self.download_feed(name, url)

            if file:
                downloaded.append(file)

        return downloaded


if __name__ == "__main__":

    loader = FeedLoader()

    files = loader.download_all()

    print("\nDownloaded Files:\n")

    for f in files:
        print(f)
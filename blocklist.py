"""
Generate IOC Blocklists
"""

from config import IP_BLOCKLIST
from config import DOMAIN_BLOCKLIST
from config import URL_BLOCKLIST
from config import HASH_BLOCKLIST


class BlocklistGenerator:

    def generate(self, normalized):

        with open(IP_BLOCKLIST, "w") as f:
            f.write("\n".join(normalized["ips"]))

        with open(DOMAIN_BLOCKLIST, "w") as f:
            f.write("\n".join(normalized["domains"]))

        with open(URL_BLOCKLIST, "w") as f:
            f.write("\n".join(normalized["urls"]))

        with open(HASH_BLOCKLIST, "w") as f:
            f.write("\n".join(normalized["hashes"]))

        print("[+] Blocklists generated")
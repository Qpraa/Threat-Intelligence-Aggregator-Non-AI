"""
Generate Statistics
"""

import json

from config import STATISTICS_JSON


class Statistics:

    def generate(self, normalized):

        stats = {

            "Total_IPs": len(normalized["ips"]),
            "Total_Domains": len(normalized["domains"]),
            "Total_URLs": len(normalized["urls"]),
            "Total_Hashes": len(normalized["hashes"]),

            "Total_IOCs":
                len(normalized["ips"])
                + len(normalized["domains"])
                + len(normalized["urls"])
                + len(normalized["hashes"])
        }

        with open(STATISTICS_JSON, "w") as f:

            json.dump(stats, f, indent=4)

        print("[+] Statistics generated")

        return stats
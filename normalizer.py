"""
Normalize extracted IOCs
"""

import pandas as pd
from config import NORMALIZED_CSV


class IOCNormalizer:

    def normalize(self, parsed):

        normalized = {}

        normalized["ips"] = sorted(set(parsed["ips"]))
        normalized["domains"] = sorted(set(parsed["domains"]))
        normalized["urls"] = sorted(set(parsed["urls"]))
        normalized["hashes"] = sorted(set(parsed["hashes"]))

        rows = []

        for ip in normalized["ips"]:
            rows.append({"Type": "IP", "Value": ip})

        for d in normalized["domains"]:
            rows.append({"Type": "Domain", "Value": d})

        for u in normalized["urls"]:
            rows.append({"Type": "URL", "Value": u})

        for h in normalized["hashes"]:
            rows.append({"Type": "Hash", "Value": h})

        df = pd.DataFrame(rows)
        df.to_csv(NORMALIZED_CSV, index=False)

        print(f"[+] Normalized IOC file saved to {NORMALIZED_CSV}")

        return normalized
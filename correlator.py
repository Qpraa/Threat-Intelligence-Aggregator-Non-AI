"""
Correlate IOCs and assign occurrence count
"""

import pandas as pd
from collections import Counter

from config import CORRELATED_CSV


class IOCorrelator:

    def correlate(self, normalized):

        rows = []

        for ioc_type, values in normalized.items():

            counts = Counter(values)

            for value, count in counts.items():

                rows.append({
                    "IOC_Type": ioc_type,
                    "IOC": value,
                    "Occurrences": count
                })

        df = pd.DataFrame(rows)

        df.to_csv(CORRELATED_CSV, index=False)

        print(f"[+] Correlated IOC file saved to {CORRELATED_CSV}")

        return df
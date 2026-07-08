"""
Assign severity levels
"""

from config import HIGH_THRESHOLD
from config import MEDIUM_THRESHOLD


class SeverityAssigner:

    def assign(self, dataframe):

        severity = []

        for count in dataframe["Occurrences"]:

            if count >= HIGH_THRESHOLD:
                severity.append("HIGH")

            elif count >= MEDIUM_THRESHOLD:
                severity.append("MEDIUM")

            else:
                severity.append("LOW")

        dataframe["Severity"] = severity

        return dataframe
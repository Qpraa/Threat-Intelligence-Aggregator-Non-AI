"""
Generate SOC Report
"""

from config import SOC_REPORT


class ReportGenerator:

    def generate(self, dataframe):

        dataframe.to_csv(SOC_REPORT, index=False)

        print(f"[+] SOC Report saved to {SOC_REPORT}")
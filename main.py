"""
Threat Intelligence Aggregator
Main Controller
"""

from feed_loader import FeedLoader
from ioc_parser import IOCParser
from normalizer import IOCNormalizer
from correlator import IOCorrelator
from severity import SeverityAssigner
from blocklist import BlocklistGenerator
from stats import Statistics
from report_generator import ReportGenerator


def main():

    print("\n======================================")
    print(" Threat Intelligence Aggregator ")
    print("======================================\n")

    # Step 1 - Download feeds
    loader = FeedLoader()
    loader.download_all()

    # Step 2 - Parse IOCs
    parser = IOCParser()
    parsed = parser.parse_directory()

    # Step 3 - Normalize
    normalizer = IOCNormalizer()
    normalized = normalizer.normalize(parsed)

    # Step 4 - Correlate
    correlator = IOCorrelator()
    correlated = correlator.correlate(normalized)

    # Step 5 - Severity
    severity = SeverityAssigner()
    correlated = severity.assign(correlated)

    # Step 6 - Blocklists
    block = BlocklistGenerator()
    block.generate(normalized)

    # Step 7 - Statistics
    stats = Statistics()
    stats.generate(normalized)

    # Step 8 - Report
    report = ReportGenerator()
    report.generate(correlated)

    print("\n======================================")
    print(" Project Completed Successfully ")
    print("======================================\n")


if __name__ == "__main__":
    main()
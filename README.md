# Threat Intelligence Aggregator (Non-AI)

## Project Overview

Threat Intelligence Aggregator (Non-AI) is a Python-based cybersecurity project that collects, processes, and analyzes threat intelligence from multiple Open Source Intelligence (OSINT) feeds. The system extracts Indicators of Compromise (IOCs) such as malicious IP addresses, URLs, domains, and file hashes, normalizes the data, correlates repeated indicators, assigns severity levels, and generates reports and defensive blocklists.

This project is completely rule-based and does not use Artificial Intelligence or Machine Learning.

---

## Features

- Collects threat intelligence from multiple OSINT feeds
- Extracts Indicators of Compromise (IOCs)
- Normalizes threat data
- Correlates repeated indicators
- Assigns Low, Medium, and High severity
- Generates IP, Domain, URL, and Hash blocklists
- Creates SOC reports and statistics

---

## Technologies Used

- Python 3
- Pandas
- Requests

---

## Project Structure

```
Threat_Intelligence_Aggregator/
│
├── _FEEDS/
├── OUTPUT/
├── REPORTS/
├── blocklist.py
├── config.py
├── correlator.py
├── feed_loader.py
├── ioc_parser.py
├── main.py
├── normalizer.py
├── report_generator.py
├── severity.py
├── stats.py
├── requirements.txt
└── README.md
```

---

## Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/Threat-Intelligence-Aggregator.git
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the project

```bash
python main.py
```

---

## Output

The project generates:

- Normalized IOC Dataset
- Correlated IOC Report
- IP Blocklist
- Domain Blocklist
- URL Blocklist
- Hash Blocklist
- SOC Report
- Statistics Report

---

## Future Enhancements

- STIX/TAXII Integration
- SIEM Integration
- Automated Feed Updates
- Real-time Dashboard
- Alerting System

---

## Author

**Abhishek Choudhary**

Unified Mentor Internship Project

Domain: Cyber Security
## Project Report

The detailed project report is available in this repository.

**Project Report:** [Threat Intelligence Aggregator Project Report](Threat_Intelligence_Aggregator_Project_Report.pdf)
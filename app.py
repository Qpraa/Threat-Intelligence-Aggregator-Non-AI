import streamlit as st
import pandas as pd

st.set_page_config(page_title="Threat Intelligence Aggregator", layout="wide")

st.title("🛡️ Threat Intelligence Aggregator (Non-AI)")

st.write("""
This project aggregates and processes cyber threat intelligence from multiple
Open Source Intelligence (OSINT) feeds.

### Features
- IOC Parsing
- IOC Correlation
- Threat Severity Classification
- Blocklist Generation
- Report Generation
""")

uploaded_file = st.file_uploader("Upload an IOC CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Data")
    st.dataframe(df)

    st.subheader("Statistics")
    st.write(f"Total Records: {len(df)}")

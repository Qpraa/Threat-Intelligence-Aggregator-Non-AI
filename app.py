import streamlit as st
import pandas as pd
import os
import json

st.set_page_config(
    page_title="Threat Intelligence Aggregator",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Threat Intelligence Aggregator (Non-AI)")
st.markdown("### Cyber Threat Intelligence Dashboard")

st.markdown("---")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select",
    [
        "Dashboard",
        "Threat Feeds",
        "Output Files",
        "Reports",
        "About"
    ]
)

# ==========================
# Dashboard
# ==========================

if page == "Dashboard":

    st.header("Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    normalized = "OUTPUT/normalized_iocs.csv"
    correlated = "OUTPUT/correlated_iocs.csv"
    stats = "OUTPUT/statistics.json"

    total_iocs = 0
    correlated_iocs = 0

    if os.path.exists(normalized):
        df = pd.read_csv(normalized)
        total_iocs = len(df)

    if os.path.exists(correlated):
        df2 = pd.read_csv(correlated)
        correlated_iocs = len(df2)

    col1.metric("Total IOCs", total_iocs)
    col2.metric("Correlated IOCs", correlated_iocs)

    if os.path.exists(stats):

        with open(stats) as f:
            data = json.load(f)

        col3.metric("Unique Types", len(data))
        col4.metric("Statistics", "Available")

    else:

        col3.metric("Unique Types", 0)
        col4.metric("Statistics", "Unavailable")

    st.markdown("---")

    st.subheader("Upload IOC CSV")

    uploaded = st.file_uploader(
        "Upload CSV",
        type="csv"
    )

    if uploaded:

        dataframe = pd.read_csv(uploaded)

        st.success("File Uploaded Successfully")

        st.dataframe(dataframe)

        st.write("Rows:", len(dataframe))
        st.write("Columns:", len(dataframe.columns))

# ==========================
# Threat Feeds
# ==========================

elif page == "Threat Feeds":

    st.header("Threat Intelligence Feeds")

    feed_folder = "_FEEDS"

    if os.path.exists(feed_folder):

        files = os.listdir(feed_folder)

        for file in files:

            st.success(file)

    else:

        st.warning("Feed folder not found.")

# ==========================
# Output
# ==========================

elif page == "Output Files":

    st.header("Generated Output")

    folder = "OUTPUT"

    if os.path.exists(folder):

        files = os.listdir(folder)

        for file in files:

            st.success(file)

            path = os.path.join(folder,file)

            if file.endswith(".csv"):

                df = pd.read_csv(path)

                st.dataframe(df)

    else:

        st.warning("No output generated.")

# ==========================
# Reports
# ==========================

elif page == "Reports":

    st.header("SOC Reports")

    folder = "REPORTS"

    if os.path.exists(folder):

        reports = os.listdir(folder)

        for report in reports:

            st.success(report)

    else:

        st.warning("No reports found.")

# ==========================
# About
# ==========================

else:

    st.header("About")

    st.write("""
Threat Intelligence Aggregator is a Python-based Cyber Security project.

Features:

• IOC Parsing

• IOC Correlation

• Severity Classification

• Blocklist Generation

• Report Generation

• SOC Report Generation

Technology:

Python

Pandas

Requests

Streamlit
""")

import streamlit as st

st.set_page_config(layout="wide")

st.title("📊 Excel Dashboard View")

# Paste your Google Sheets embed link
sheet_url = "https://docs.google.com/spreadsheets/d/1FI4z0-dOfIT_NcWLKbpf1imzBKh3NCuY/edit?gid=1105156781#gid=1105156781"

st.components.v1.iframe(sheet_url, height=1300)
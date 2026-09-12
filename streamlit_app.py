import streamlit as st

st.set_page_config(
    page_title="GL Audit Analyzer",
    page_icon="🔎",
    layout="wide"
)

st.title("🔎 GL Audit Analyzer")

st.write(
    "Upload your General Ledger and let the system identify "
    "potential audit risks."
)

st.divider()

uploaded_file = st.file_uploader(
    "Upload your General Ledger",
    type=["xlsx", "xls", "csv"]
)

if uploaded_file is not None:
    st.success("File uploaded successfully!")

    st.write("Filename:", uploaded_file.name)

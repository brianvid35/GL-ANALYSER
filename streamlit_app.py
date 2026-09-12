import streamlit as st
import pandas as pd
import io

st.set_page_config(
    page_title="GL Audit Analyzer",
    page_icon="🔎",
    layout="wide"
)

st.title("🔎 GL Audit Analyzer")
st.write("Upload your General Ledger and analyze its transactions.")

st.divider()

uploaded_file = st.file_uploader(
    "Upload your General Ledger",
    type=["xlsx", "xls", "csv"]
)

if uploaded_file is not None:

    st.success("File uploaded successfully!")

    # Read the uploaded file
    try:
        if uploaded_file.name.lower().endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.subheader("📊 General Ledger Preview")

        st.write(
            f"**Number of transactions:** {len(df):,}"
        )

        st.write(
            f"**Number of columns:** {len(df.columns)}"
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    except Exception as e:
        st.error(f"Unable to read the file: {e}")

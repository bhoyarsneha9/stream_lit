import streamlit as st
import pandas as pd

st.set_page_config(page_title="Bank Expense Categorizer", layout="wide")

st.title("🏦 Bank Account Expense Manager")
st.markdown("Upload your bank CSV and categorize your expenses by navigation channels.")

# Upload CSV
uploaded_file = st.file_uploader("Upload your Bank Statement (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Basic check for necessary columns
    if not set(["Date", "Description", "Amount"]).issubset(df.columns):
        st.error("CSV must contain 'Date', 'Description', and 'Amount' columns.")
    else:
        df['Category'] = ""

        st.subheader("🔍 Review & Categorize Transactions")

        # Manual category assignment
        for idx, row in df.iterrows():
            with st.expander(f"{row['Date']} | {row['Description']} | ${row['Amount']}"):
                category = st.selectbox(
                    f"Select category for transaction {idx + 1}",
                    options=["", "Food", "Transport", "Rent", "Shopping", "Utilities", "Entertainment", "Other"],
                    key=idx
                )
                df.at[idx, 'Category'] = category

        # Show categorized summary
        if st.button("✅ Show Summary by Category"):
            if df['Category'].eq("").any():
                st.warning("Some transactions are uncategorized.")
            else:
                st.success("Categorized Summary")
                for cat in df['Category'].unique():
                    cat_df = df[df['Category'] == cat]
                    with st.expander(f"📂 {cat} - Total: ${cat_df['Amount'].sum():.2f}"):
                        st.dataframe(cat_df)

        # Option to download categorized data
        st.download_button(
            "📥 Download Categorized Data",
            data=df.to_csv(index=False),
            file_name="categorized_expenses.csv",
            mime="text/csv"
        )
else:
    st.info("Please upload a CSV to begin.")

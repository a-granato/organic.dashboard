from scrapers.nemlig_scraper import scrape_nemlig_data

import streamlit as st

st.set_page_config(page_title="Organic Dashboard", layout="wide")
st.title("Welcome to the Organic Dashboard")
st.header("Live Data from Nemlig.com")

if st.button("Run Scraper"):
    data = scrape_nemlig_data()
    st.write("Scraped Data:")
    st.dataframe(data)

st.write("This is your live data dashboard. More features coming soon!")

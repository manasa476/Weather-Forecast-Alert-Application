import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Weather Dashboard", layout="wide")

st.title("🌦 Weather Forecast Dashboard")

city = st.text_input("Enter City Name", "Mumbai")

report_file = f"reports/{city}_weather_report.csv"

if os.path.exists(report_file):

    df = pd.read_csv(report_file)

    st.subheader("Weather Forecast Data")

    st.dataframe(df)

    st.subheader("Temperature Chart")

    st.line_chart(df["Temperature"])

    st.subheader("Humidity Chart")

    st.bar_chart(df["Humidity"])

    st.subheader("Weather Summary")

    st.write(df[["DateTime", "Weather"]])

else:

    st.error("No report found. Run main.py first.")
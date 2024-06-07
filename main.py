import streamlit as st
import requests, os
from dotenv import load_dotenv

def configure():
    load_dotenv()

def main():
    configure()
    response = requests.get(os.getenv("url"))
    data = response.json()[0]["pos"]
    st.title(data)

main()
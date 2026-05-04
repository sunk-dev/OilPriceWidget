
import requests
from bs4 import BeautifulSoup
import streamlit as st
url='https://www.opinet.co.kr/glopcoilSelect.do#'
response=requests.get(url)

def crawling_oil_price():
    if response.status_code==200:
        html=response.text
        soup=BeautifulSoup(html,'html.parser')
        title=soup.select_one('#glopcoilVO > div:nth-child(5) > table')
        return title
    else: 
        return response.status_code
st.set_page_config(page_title="International Oil Price  Wiget", layout="centered")  
st.title(f"국제 유가 위젯")
st.html(crawling_oil_price())


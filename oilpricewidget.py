
import requests
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd
from urllib.parse import urljoin # 상대 경로를 절대 경로로 바꿀 때 사용
url='https://www.opinet.co.kr/glopcoilSelect.do#'
response=requests.get(url)

def crawling_oil_price():
    if response.status_code==200:
        html=response.text
        soup=BeautifulSoup(html,'html.parser')
        title=soup.select_one('#glopcoilVO > div:nth-child(5) > table')
        df=pd.read_html(str(title)[0])
        return df
    else: 
        return response.status_code
#crawling_oil_price()
result=crawling_oil_price()
st.set_page_config(page_title="International Oil Price  Wiget", layout="centered")  
st.title(f"국제 유가 위젯")
st.html(crawling_oil_price())

 

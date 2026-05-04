
import requests
from bs4 import BeautifulSoup
import streamlit as st
from urllib.parse import urljoin # 상대 경로를 절대 경로로 바꿀 때 사용
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
#crawling_oil_price()
result=crawling_oil_price()
st.set_page_config(page_title="International Oil Price  Wiget", layout="centered")  
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container { padding: 10px !important; } /* 노션 안에서 답답하지 않게 살짝 여백 */
    
    /* 타이틀 크기 강제 고정 */
    h1 {
        font-size: 18px !important; 
        color: #37352f;
        margin-bottom: 10px !important;
    }

    caption { display: none !important; }

    table { width: 100% !important; border-collapse: collapse; font-size: 12px; }
    th, td { padding: 6px; border: 1px solid #e9e9e7; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 2. 타이틀 표시 (st.title 대신 마크다운 사용)
st.markdown("# ⛽ 국제 유가 정보")

# 3. 데이터 표시 (Markdown/HTML 사용)
table_html = crawling_oil_price()
st.markdown(table_html, unsafe_allow_html=True)
 

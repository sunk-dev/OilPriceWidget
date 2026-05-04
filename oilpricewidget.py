
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
st.h3(f"국제 유가 위젯")
st.markdown("""
    <style>
    /* 스트림릿 기본 요소 숨기기 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container { padding: 0 !important; }
    
    /* 테이블 커스텀 디자인 */
    table {
        width: 100% !important;
        border-collapse: collapse;
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 13px;
        color: #37352f; /* 노션 기본 글자색 */
    }
    th {
        background-color: #f7f6f3; /* 노션 강조 배경색 */
        padding: 8px;
        border: 1px solid #e9e9e7;
    }
    td {
        padding: 8px;
        border: 1px solid #e9e9e7;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 데이터 표시 (Markdown/HTML 사용)
table_html = crawling_oil_price()
st.markdown(table_html, unsafe_allow_html=True)
 

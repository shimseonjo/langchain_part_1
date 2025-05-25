import streamlit as st

from stock_info import Stock
from search import stock_search
from reporting_service import investment_report

class SearchResult:
    def __init__(self, item):
        self.item = item

    @property
    def symbol(self):
        return self.item['Symbol']
    
    @property
    def name(self):
        return self.item['Name']
    
    def __str__(self):
        return f"{self.symbol}: {self.name}"


st.title("서학 개미를 위한 AI 투자보고서 생성 서비스")

query = st.text_input("회사명", "Apple")
hits = stock_search(query)['hits']
search_results = [SearchResult(hit) for hit in hits]

selected = st.selectbox("검색 결과 리스트", search_results)

tabs = ["회사 기본 정보", "AI 투자 보고서"]
tab1, tab2 = st.tabs(tabs)

with tab1:
    stock = Stock(selected.symbol)
    st.header(selected)

    st.write(stock.get_basic_info())
    st.write(stock.get_financial_statement())

with tab2:
    st.header("AI 투자 보고서")
    if st.button("보고서 생성"):
        with st.spinner():
            report = investment_report(selected.name, selected.symbol)
            st.success('Done')
        st.write(report)

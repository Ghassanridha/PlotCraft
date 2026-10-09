import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="PlotCraft UI", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# قراءة ملف الـ HTML الخارجي وعرضه بشكل كامل وآمن
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    components.html(html_code, height=680, scrolling=False)
except FileNotFoundError:
    st.error("الرجاء التأكد من وجود ملف index.html في نفس المجلد.")

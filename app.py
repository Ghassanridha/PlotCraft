import streamlit as st

# إخفاء زر "إدارة التطبيق" والشريط العائم الخاص بـ Streamlit فقط
st.markdown("""
    <style>
        /* إخفاء شريط الزر العائم في أسفل التطبيق */
        div[data-testid="stToolbar"],
        div[class*="viewerBadge"],
        button[kind="header"],
        #MainMenu,
        footer {
            display: none !important;
            visibility: hidden !important;
        }
        
        /* استهداف شارة "إدارة التطبيق" بالأسفل وتثبيت إخفائها */
        iframe ~ div:last-child {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# ضع باقي كود تطبيقك (Components أو HTML) هنا كما هو...

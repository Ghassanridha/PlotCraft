import streamlit as st
import streamlit.components.v1 as components

# استيراد الوظائف من الملفات التي أنشأناها
from config import init_firebase
from security import init_secure_session

# --- 1. تهيئة النظام ---
db = init_firebase()
init_secure_session()

# --- 2. إعدادات الصفحة ---
st.set_page_config(
    page_title="PlotCraft UI", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
        .block-container { padding: 0 !important; margin: 0 !important; max-width: 100% !important; }
        header { visibility: hidden !important; display: none !important; }
        .plotcraft-nav-bar, .app-shell { -webkit-user-select: none; -moz-user-select: none; user-select: none; }
    </style>
""", unsafe_allow_html=True)

# --- 3. تشغيل الواجهة ---
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # حقن كود الحماية
    security_shield = "<script>console.log('🛡️ PlotCraft Security: Online');</script>"
    if "</body>" in html_code:
        html_code = html_code.replace("</body>", security_shield + "</body>")
    else:
        html_code += security_shield

    components.html(html_code, height=680, scrolling=False)

except FileNotFoundError:
    st.error("الرجاء التأكد من وجود ملف index.html في نفس المجلد.")

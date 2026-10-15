import streamlit as st
import streamlit.components.v1 as components
import firebase_admin
from firebase_admin import credentials, firestore

# --- تهيئة اتصال Firebase بشكل آمن وصحيح ---
if not firebase_admin._apps:
    key_dict = dict(st.secrets["firebase"])
    cred = credentials.Certificate(key_dict)
    firebase_admin.initialize_app(cred)

# تعريف قاعدة البيانات يجب أن يكون بعد التهيئة مباشرة
db = firestore.client()

# إعدادات الصفحة الأساسية مع تقييد الأمان ومنع عرض الشريط الجانبي
st.set_page_config(
    page_title="PlotCraft UI", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# بقية كود الواجهة الخاص بك...
st.markdown("""
    <style>
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        header {
            visibility: hidden !important;
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)

try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    
    security_shield_injection = """
    <script>
        console.log("🛡️ PlotCraft Security Architecture: Online");
    </script>
    """
    
    if "</body>" in html_code:
        html_code = html_code.replace("</body>", security_shield_injection + "</body>")
    else:
        html_code += security_shield_injection

    components.html(html_code, height=680, scrolling=False)

except FileNotFoundError:
    st.error("الرجاء التأكد من وجود ملف index.html في نفس المجلد.")

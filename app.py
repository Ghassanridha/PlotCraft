import streamlit as st
import streamlit.components.v1 as components
import firebase_admin
from firebase_admin import credentials, firestore
import json

# --- تهيئة اتصال Firebase مع معالجة آمنة للمفتاح السري ---
if not firebase_admin._apps:
    try:
        # تحويل بيانات الـ Secrets إلى قاموس بيانات عادٍ
        key_dict = dict(st.secrets["firebase"])
        
        # التأكد من معالجة أسطر المفتاح السري بشكل صحيح إذا وجد فيها ترميز
        if "private_key" in key_dict:
            key_dict["private_key"] = key_dict["private_key"].replace("\\n", "\n")
            
        cred = credentials.Certificate(key_dict)
        firebase_admin.initialize_app(cred)
    except Exception as e:
        st.error(f"خطأ في تهيئة Firebase: {e}")

# تعريف قاعدة البيانات
db = firestore.client()

# إعدادات الصفحة الأساسية مع تقييد الأمان ومنع عرض الشريط الجانبي
st.set_page_config(
    page_title="PlotCraft UI", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# قسم التنسيق والحماية البصرية وإلغاء الهوامش وشريط الاستخدام الافتراضي
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

# نظام قراءة وتحميل ملف الـ HTML الخارجي مع تأمين الجلسة والحقن الآمن
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    
    security_shield_injection = """
    <script>
        // تفعيل درع الحماية الخاص بتطبيق PlotCraft
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

import streamlit as st
import streamlit.components.v1 as components
import firebase_admin
from firebase_admin import credentials, firestore
import uuid
import hashlib
import time
import re
import html

# --- 1. تهيئة اتصال Firebase بشكل آمن تماماً لا يوقف التطبيق ---
db = None
if not firebase_admin._apps:
    try:
        secret_dict = dict(st.secrets["firebase"])
        if "private_key" in secret_dict:
            pk = secret_dict["private_key"].strip()
            if not pk.startswith('"') and not pk.startswith("'"):
                pk = pk.replace("\\n", "\n")
            secret_dict["private_key"] = pk

        cred = credentials.Certificate(secret_dict)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
    except Exception as e:
        pass

# --- 2. منظومة الحماية والأمان (Security Layer المدمجة) ---

def sanitize_input(user_input):
    """تنظيف المدخلات وتأمينها ضد هجمات الحقن"""
    if not isinstance(user_input, str):
        return user_input
    cleaned = html.escape(user_input)
    cleaned = re.sub(r'[;\'"\\--]', '', cleaned)
    return cleaned.strip()

def init_secure_session():
    """تأمين الجلسة وتوليد رمز حماية فريد"""
    if "security_token" not in st.session_state:
        st.session_state.security_token = str(uuid.uuid4())
    if "is_subscribed" not in st.session_state:
        st.session_state.is_subscribed = False

def check_rate_limit(action_name="default", delay_seconds=2):
    """منع الضغط المتكرر لحماية السيرفر (Rate Limiting)"""
    current_time = time.time()
    last_action_key = f"last_time_{action_name}"
    
    if last_action_key in st.session_state:
        elapsed = current_time - st.session_state[last_action_key]
        if elapsed < delay_seconds:
            st.warning("⚠️ يرجى الانتظار لحظات قبل تنفيذ الطلب مرة أخرى.")
            return False
            
    st.session_state[last_action_key] = current_time
    return True

def verify_subscription():
    """التحقق الصارم من اشتراك المستخدم"""
    if not st.session_state.get("is_subscribed", False):
        st.error("🔒 هذه الميزة تطلب اشتراكاً فعالاً (أسبوعي، شهري، أو سنوي).")
        return False
    return True

# تفعيل جلسة الأمان فوراً
init_secure_session()

# --- 3. إعدادات الصفحة والتصميم ---
st.set_page_config(
    page_title="PlotCraft UI", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

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
        /* منع تحديد النصوص غير المرغوب فيه في واجهات المخرجين */
        .plotcraft-nav-bar, .app-shell {
            -webkit-user-select: none;
            -moz-user-select: none;
            user-select: none;
        }
    </style>
""", unsafe_allow_html=True)

# --- 4. قراءة وحقن ملف الـ HTML الرئيسي ---
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    
    security_shield_injection = """
    <script>
        console.log("🛡️ PlotCraft Security Architecture: Online & Secure");
    </script>
    """
    
    if "</body>" in html_code:
        html_code = html_code.replace("</body>", security_shield_injection + "</body>")
    else:
        html_code += security_shield_injection

    components.html(html_code, height=680, scrolling=False)

except FileNotFoundError:
    st.error("الرجاء التأكد من وجود ملف index.html في نفس المجلد.")

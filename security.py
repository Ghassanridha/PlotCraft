import streamlit as st
import re
from datetime import datetime

def sanitize_input(user_input):
    """
    تنظيف المدخلات من المستخدم لمنع الحقن الضار (Injection Attacks).
    """
    if not user_input:
        return ""
    # إزالة الرموز الخطرة
    cleaned = re.sub(r'[<>\"\'%;()&+]', '', str(user_input))
    return cleaned.strip()

def init_secure_session():
    """
    تهيئة جلسة آمنة للمستخدم.
    تقوم بإنشاء متغيرات الجلسة الأساسية إذا لم تكن موجودة.
    """
    if 'user_id' not in st.session_state:
        st.session_state.user_id = None
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'last_request_time' not in st.session_state:
        st.session_state.last_request_time = None

def check_rate_limit(max_requests=5, time_window=60):
    """
    فحص عدد الطلبات لمنع الإفراط في الاستخدام (Rate Limiting).
    
    Args:
        max_requests: الحد الأقصى للطلبات المسموح بها
        time_window: النافذة الزمنية بالثواني
    
    Returns:
        True إذا كان المستخدم ضمن الحد المسموح، False إذا تجاوز
    """
    now = datetime.now()
    if st.session_state.last_request_time:
        time_diff = (now - st.session_state.last_request_time).total_seconds()
        if time_diff < time_window:
            return False
    st.session_state.last_request_time = now
    return True

def verify_subscription(db, user_id):
    """
    التحقق من صلاحية اشتراك المستخدم من Firebase.
    
    Args:
        db: كائن قاعدة بيانات Firestore
        user_id: معرف المستخدم
    
    Returns:
        True إذا كان الاشتراك صالحاً، False إذا لم يكن
    """
    if not db or not user_id:
        return False
    
    try:
        user_doc = db.collection('users').document(user_id).get()
        if user_doc.exists:
            user_data = user_doc.to_dict()
            return user_data.get('subscription_active', False)
    except Exception as e:
        print(f"Subscription check error: {e}")
    
    return False


import streamlit as st

st.set_page_config(
    page_title="بلوت كرافت",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- تنسيق الـ CSS المضمون والنظيف ---
st.markdown("""
    <style>
        [data-testid="stSidebarNav"], [data-testid="collapsedControl"], section[data-testid="stSidebar"] {
            display: none !important;
        }
        header, button[kind="header"] {
            display: none !important;
        }
        .block-container {
            padding-top: 1rem !important;
            padding-bottom: 2rem !important;
            max-width: 440px !important;
            margin: auto !important;
            background-color: #07090e !important;
        }
        @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;900&display=swap');
        html, body, [class*="css"] {
            font-family: 'Tajawal', sans-serif;
            direction: rtl;
            background-color: #07090e;
            color: #ffffff;
        }
    </style>
""", unsafe_allow_html=True)

# --- 1. الهيدر العلوي ---
c1, c2 = st.columns([1, 1])
with c1:
    st.markdown("✨ **ترقية**")
with c2:
    st.markdown("<div style='text-align: left; font-weight: 900;'>بلوت كرافت 🎬</div>", unsafe_allow_html=True)

st.markdown("---")

# --- 2. بطاقة الترحيب السينمائية ---
st.markdown("""
    <div style="background: linear-gradient(135deg, #0f172a 0%, #07090e 100%); padding: 22px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.1); text-align: right; margin-bottom: 15px;">
        <div style="font-size: 12px; color: #94a3b8; font-weight: 500; margin-bottom: 6px;">مساء الخير، أيها المخرج</div>
        <div style="font-size: 18px; font-weight: 900; color: #ffffff;">أي قصة سنصنع اليوم؟</div>
    </div>
""", unsafe_allow_html=True)

# --- 3. البطاقات الرئيسية (سريع / خطوة بخطوة) ---
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("""
        <div style="background: #12151c; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; padding: 14px; text-align: right; height: 95px;">
            <span style="font-size: 8px; background: rgba(255,255,255,0.1); padding: 2px 6px; border-radius: 4px; color: #cbd5e1;">Pro only</span>
            <div style="font-size: 13px; font-weight: bold; color: #fff; margin-top: 8px;">سريع</div>
            <div style="font-size: 9px; color: #64748b;">إدخال واحد، فيميو كامل</div>
        </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown("""
        <div style="background: #12151c; border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; padding: 14px; text-align: right; height: 95px;">
            <div style="font-size: 13px; font-weight: bold; color: #fff; margin-top: 14px;">خطوة بخطوة</div>
            <div style="font-size: 9px; color: #64748b;">راجع كل خطوة</div>
        </div>
    """, unsafe_allow_html=True)

# --- 4. قسم إلهام بلوت كرافت ---
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 20px; margin-bottom: 10px;">
        <span style="font-size: 10px; color: #64748b;">عرض الكل ></span>
        <span style="font-size: 14px; font-weight: 900; color: #ffffff;">إلهام بلوت كرافت</span>
    </div>
""", unsafe_allow_html=True)

# --- 5. بوسترات الأفلام الثلاثة ---
img_cols = st.columns(3)

with img_cols[0]:
    st.markdown("""
        <div style="background: #12151c; border-radius: 12px; height: 160px; border: 1px solid rgba(255,255,255,0.08); display: flex; align-items: flex-end; justify-content: center; text-align: center; padding: 10px;">
            <span style="font-size: 8px; font-weight: bold; color: #94a3b8;">THE SECRET BILLIONAIRE</span>
        </div>
    """, unsafe_allow_html=True)

with img_cols[1]:
    st.markdown("""
        <div style="background: #12151c; border-radius: 12px; height: 160px; border: 1px solid rgba(255,255,255,0.08); display: flex; align-items: flex-end; justify-content: center; text-align: center; padding: 10px;">
            <span style="font-size: 8px; font-weight: bold; color: #ffffff;">THE WRONG DOOR</span>
        </div>
    """, unsafe_allow_html=True)

with img_cols[2]:
    st.markdown("""
        <div style="background: #12151c; border-radius: 12px; height: 160px; border: 1px solid rgba(255,255,255,0.08); display: flex; align-items: flex-end; justify-content: center; text-align: center; padding: 10px;">
            <span style="font-size: 8px; font-weight: bold; color: #94a3b8;">INVITATION</span>
        </div>
    """, unsafe_allow_html=True)

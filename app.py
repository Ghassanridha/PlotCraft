import streamlit as st

st.set_page_config(
    page_title="بلوت كرافت",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
        [data-testid="stSidebarNav"], [data-testid="collapsedControl"], section[data-testid="stSidebar"] {
            display: none !important;
        }
        header, button[kind="header"] {
            display: none !important;
        }
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 2rem !important;
            max-width: 440px !important;
            margin: auto !important;
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

# --- 1. الهيدر العلوي والخلفية السينمائية المتكاملة ---
st.markdown("""
    <div style="background: linear-gradient(180deg, rgba(7, 9, 14, 0.1) 0%, rgba(7, 9, 14, 0.9) 75%, #07090e 100%), 
                url('https://images.unsplash.com/photo-1534447677768-be436bb09401?q=80&w=1000&auto=format&fit=crop') center/cover;
                padding: 16px 14px; border-radius: 0 0 22px 22px; margin-bottom: 12px; text-align: right;">
        
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
            <div style="background: rgba(255,255,255,0.1); backdrop-filter: blur(8px); padding: 4px 10px; border-radius: 18px; display: inline-flex; align-items: center; gap: 4px; border: 1px solid rgba(255,255,255,0.12);">
                <span style="font-size: 9px;">✨</span>
                <span style="font-size: 10px; font-weight: bold;">ترقية</span>
            </div>
            <div style="font-weight: 900; font-size: 14px; color: #ffffff;">
                بلوت كرافت 🎬
            </div>
        </div>

        <div style="margin-top: 35px; margin-bottom: 10px;">
            <div style="font-size: 12px; color: #cbd5e1; font-weight: 500; margin-bottom: 3px;">مساء الخير، أيها المخرج</div>
            <div style="font-size: 16px; font-weight: 900; color: #ffffff;">أي قصة سنصنع اليوم؟</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 2. بطاقات الخيارات الرئيسية ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div style="background: rgba(18, 22, 31, 0.7); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 14px; padding: 12px; text-align: right; height: 90px; position: relative;">
            <div style="position: absolute; top: 8px; left: 8px; background: rgba(255,255,255,0.1); padding: 2px 5px; border-radius: 4px; font-size: 7px; color: #e2e8f0;">Pro only</div>
            <div style="font-size: 12px; font-weight: bold; color: #fff; margin-bottom: 2px;">سريع</div>
            <div style="font-size: 8px; color: #94a3b8;">إدخال واحد، فيميو كامل</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style="background: rgba(18, 22, 31, 0.7); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 14px; padding: 12px; text-align: right; height: 90px;">
            <div style="font-size: 12px; font-weight: bold; color: #fff; margin-bottom: 2px;">خطوة بخطوة</div>
            <div style="font-size: 8px; color: #94a3b8;">راجع كل خطوة</div>
        </div>
    """, unsafe_allow_html=True)

# --- 3. قسم إلهام بلوت كرافت ---
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 18px; margin-bottom: 10px; padding: 0 2px;">
        <span style="font-size: 9px; color: #94a3b8; cursor: pointer;">عرض الكل ></span>
        <span style="font-size: 13px; font-weight: 900; color: #ffffff;">إلهام بلوت كرافت</span>
    </div>
""", unsafe_allow_html=True)

# بطاقات الأفلام الإلهامية
cols_cards = st.columns(3)
with cols_cards[0]:
    st.markdown("""
        <div style="background: linear-gradient(180deg, rgba(20,24,33,0.7) 0%, rgba(10,12,16,0.95) 100%); border-radius: 12px; height: 160px; border: 1px solid rgba(255,255,255,0.06); display: flex; align-items: flex-end; justify-content: center; text-align: center; padding: 8px;">
            <span style="font-size: 8px; font-weight: bold; color: #94a3b8; line-height: 1.2;">THE SECRET BILLIONAIRE</span>
        </div>
    """, unsafe_allow_html=True)

with cols_cards[1]:
    st.markdown("""
        <div style="background: linear-gradient(180deg, rgba(20,24,33,0.7) 0%, rgba(10,12,16,0.95) 100%); border-radius: 12px; height: 160px; border: 1px solid rgba(255,255,255,0.06); display: flex; align-items: flex-end; justify-content: center; text-align: center; padding: 8px;">
            <span style="font-size: 8px; font-weight: bold; color: #ffffff; line-height: 1.2;">THE WRONG DOOR</span>
        </div>
    """, unsafe_allow_html=True)

with cols_cards[2]:
    st.markdown("""
        <div style="background: linear-gradient(180deg, rgba(20,24,33,0.7) 0%, rgba(10,12,16,0.95) 100%); border-radius: 12px; height: 160px; border: 1px solid rgba(255,255,255,0.06); display: flex; align-items: flex-end; justify-content: center; text-align: center; padding: 8px;">
            <span style="font-size: 8px; font-weight: bold; color: #94a3b8; line-height: 1.2;">INVITATION</span>
        </div>
    """, unsafe_allow_html=True)

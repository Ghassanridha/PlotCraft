import streamlit as st

st.set_page_config(
    page_title="بلوت كرافت",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# تخصيص التصميم بدقة مطابقة تماماً للصورة
st.markdown("""
    <style>
        [data-testid="stSidebarNav"], [data-testid="collapsedControl"], section[data-testid="stSidebar"] {
            display: none !important;
        }
        button[kind="header"] {
            display: none !important;
        }
        .block-container {
            padding-top: 1rem !important;
            padding-bottom: 120px !important;
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

        /* شريط التنقل السفلي العائم بنفس التصميم والقياسات */
        .fixed-bottom-nav {
            position: fixed;
            bottom: 15px;
            left: 50%;
            transform: translateX(-50%);
            width: 92%;
            max-width: 410px;
            background-color: rgba(18, 21, 28, 0.95);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 40px;
            padding: 6px 10px;
            z-index: 99999;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .nav-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            color: #8c96a5;
            font-size: 10px;
            font-weight: 500;
            text-decoration: none;
            flex: 1;
            padding: 6px 0;
        }
        
        .nav-item.active {
            color: #ffffff;
            background: rgba(255, 255, 255, 0.09);
            border-radius: 30px;
            font-weight: 700;
        }
    </style>
""", unsafe_allow_html=True)

# --- 1. رأس الصفحة العلوي ---
col_h1, col_h2 = st.columns([1, 1])
with col_h1:
    st.markdown("""
        <div style="background: rgba(255,255,255,0.07); padding: 4px 10px; border-radius: 20px; display: inline-flex; align-items: center; gap: 4px; border: 1px solid rgba(255,255,255,0.08);">
            <span style="font-size: 9px;">✨</span>
            <span style="font-size: 10px; font-weight: bold;">ترقية</span>
        </div>
    """, unsafe_allow_html=True)
with col_h2:
    st.markdown("""
        <div style="text-align: left; font-weight: 900; font-size: 14px; color: #ffffff; padding-top: 4px;">
            بلوت كرافت 🎬
        </div>
    """, unsafe_allow_html=True)

# --- 2. قسم الترحيب والخلفية ---
st.markdown("""
    <div style="background: linear-gradient(180deg, rgba(15, 23, 42, 0.5) 0%, rgba(7, 9, 14, 0.95) 100%), 
                radial-gradient(circle at 25% 25%, rgba(56, 189, 248, 0.2) 0%, transparent 65%);
                padding: 18px 14px; border-radius: 18px; border: 1px solid rgba(255,255,255,0.08); margin-top: 8px; margin-bottom: 12px; text-align: right;">
        <div style="font-size: 12px; color: #94a3b8; font-weight: 500; margin-bottom: 3px;">مساء الخير، أيها المخرج</div>
        <div style="font-size: 15px; font-weight: 900; color: #ffffff;">أي قصة سنصنع اليوم؟</div>
    </div>
""", unsafe_allow_html=True)

# --- 3. بطاقات الخيارات الرئيسية (سريع / خطوة بخطوة) ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 14px; padding: 12px; text-align: right; height: 88px; position: relative;">
            <div style="position: absolute; top: 8px; left: 8px; background: rgba(255,255,255,0.08); padding: 1px 5px; border-radius: 4px; font-size: 7px; color: #94a3b8;">Pro only</div>
            <div style="font-size: 12px; font-weight: bold; color: #fff; margin-bottom: 2px;">سريع</div>
            <div style="font-size: 8px; color: #64748b;">إدخال واحد، فيميو كامل</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 14px; padding: 12px; text-align: right; height: 88px;">
            <div style="font-size: 12px; font-weight: bold; color: #fff; margin-bottom: 2px;">خطوة بخطوة</div>
            <div style="font-size: 8px; color: #64748b;">راجع كل خطوة</div>
        </div>
    """, unsafe_allow_html=True)

# --- 4. قسم إلهام بلوت كرافت ---
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 18px; margin-bottom: 8px;">
        <span style="font-size: 9px; color: #64748b; cursor: pointer;">عرض الكل ></span>
        <span style="font-size: 13px; font-weight: 900; color: #ffffff;">إلهام بلوت كرافت</span>
    </div>
""", unsafe_allow_html=True)

# بطاقات القصص
cols_cards = st.columns(3)
with cols_cards[0]:
    st.markdown("""
        <div style="background: #12151c; border-radius: 10px; height: 150px; border: 1px solid rgba(255,255,255,0.06); display: flex; align-items: center; justify-content: center; text-align: center; padding: 6px;">
            <span style="font-size: 9px; font-weight: bold; color: #94a3b8;">THE SECRET BILLIONAIRE</span>
        </div>
    """, unsafe_allow_html=True)

with cols_cards[1]:
    st.markdown("""
        <div style="background: #12151c; border-radius: 10px; height: 150px; border: 1px solid rgba(255,255,255,0.06); display: flex; align-items: center; justify-content: center; text-align: center; padding: 6px;">
            <span style="font-size: 9px; font-weight: bold; color: #ffffff;">THE WRONG DOOR</span>
        </div>
    """, unsafe_allow_html=True)

with cols_cards[2]:
    st.markdown("""
        <div style="background: #12151c; border-radius: 10px; height: 150px; border: 1px solid rgba(255,255,255,0.06); display: flex; align-items: center; justify-content: center; text-align: center; padding: 6px;">
            <span style="font-size: 9px; font-weight: bold; color: #94a3b8;">INVITATION</span>
        </div>
    """, unsafe_allow_html=True)

# --- 5. شريط التنقل السفلي المطابق للصورة تماماً ---
st.markdown("""
    <div class="fixed-bottom-nav">
        <a href="#" class="nav-item">
            <span>✨</span>
            <span style="font-size: 9px; margin-top: 1px;">إدارة التطبيق</span>
        </a>
        <a href="#" class="nav-item">
            <span>🛠️</span>
            <span style="font-size: 9px; margin-top: 1px;">الأدوات</span>
        </a>
        <a href="#" class="nav-item">
            <span>📁</span>
            <span style="font-size: 9px; margin-top: 1px;">الأعمال</span>
        </a>
        <a href="#" class="nav-item active">
            <span>🏠</span>
            <span style="font-size: 9px; margin-top: 1px;">الصفحة الرئيسية</span>
        </a>
    </div>
""", unsafe_allow_html=True)

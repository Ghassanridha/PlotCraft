import streamlit as st

st.set_page_config(
    page_title="بلوت كرافت",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# تخصيص التصميم وإزالة القوائم الجانبية وضبط التناسق العام
st.markdown("""
    <style>
        [data-testid="stSidebarNav"], [data-testid="collapsedControl"], section[data-testid="stSidebar"] {
            display: none !important;
        }
        button[kind="header"] {
            display: none !important;
        }
        .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 3rem !important;
            max-width: 100% !important;
        }
        
        @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;900&display=swap');
        html, body, [class*="css"] {
            font-family: 'Tajawal', sans-serif;
            direction: rtl;
            background-color: #0b0d12;
            color: #ffffff;
        }
    </style>
""", unsafe_allow_html=True)

# إدارة التنقل أو عرض الأقسام بترتيب صحيح
if 'options_list' not in st.session_state:
    st.session_state.options_list = [
        "الخيار الأول (نمط بصري)",
        "الخيار الثاني (جودة عالية)",
        "الخيار الثالث (مؤثرات صوتية)"
    ]

# 1. المحتوى الرئيسي في الأعلى
st.markdown("""
    <div style="background: linear-gradient(180deg, rgba(11,13,18,0.3) 0%, rgba(11,13,18,0.95) 85%, #0b0d12 100%); padding: 18px 16px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.1); margin-bottom: 15px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <span style="font-weight: 900; font-size: 14px; color: #ffffff;">بلوت كرافت</span>
            <span style="background: rgba(255,255,255,0.1); padding: 3px 10px; border-radius: 20px; font-size: 10px; font-weight: bold; border: 1px solid rgba(255,255,255,0.15);">ترقية ✨</span>
        </div>
        <h1 style="font-size: 12px; font-weight: 600; color: #cbd5e1; margin-bottom: 2px;">مساء الخير، أيها المخرج</h1>
        <h2 style="font-size: 14px; font-weight: 900; color: #ffffff;">أي قصة سنصنع اليوم؟</h2>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.07); border: 1px solid rgba(255, 255, 255, 0.12); border-radius: 14px; padding: 12px; text-align: right; margin-bottom: 15px;">
            <h3 style="font-size: 11px; font-weight: bold; margin-bottom: 2px; color: #fff;">خطوة بخطوة</h3>
            <p style="font-size: 8px; color: #94a3b8; margin:0;">راجع كل خطوة</p>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.07); border: 1px solid rgba(255, 255, 255, 0.12); border-radius: 14px; padding: 12px; text-align: right; margin-bottom: 15px;">
            <h3 style="font-size: 11px; font-weight: bold; margin-bottom: 2px; color: #fff;">سريع</h3>
            <p style="font-size: 8px; color: #94a3b8; margin:0;">إدخال واحد، فيديو كامل</p>
        </div>
    """, unsafe_allow_html=True)

# فاصل أنيق
st.markdown("<hr style='border: 0; border-top: 1px solid rgba(255,255,255,0.1); margin: 20px 0;'>", unsafe_allow_html=True)

# 2. قسم الأدوات والخيارات (تم وضعه تحت المحتوى تماماً كما طلبت)
st.markdown("<h2 style='font-size: 15px; font-weight: 900; margin-bottom: 12px;'>الأدوات والخيارات النشطة</h2>", unsafe_allow_html=True)

st.markdown("""
    <div style="background: rgba(255,255,255,0.04); padding: 16px; border-radius: 14px; border: 1px solid rgba(255,255,255,0.08); margin-bottom: 15px;">
""", unsafe_allow_html=True)

if st.session_state.options_list:
    for opt in st.session_state.options_list:
        st.markdown(f"""
            <div style="background: rgba(255, 255, 255, 0.07); padding: 10px 14px; border-radius: 8px; margin-bottom: 8px; font-size: 12px; border: 1px solid rgba(255, 255, 255, 0.1);">
                <span>{opt}</span>
            </div>
        """, unsafe_allow_html=True)
else:
    st.markdown("<p style='font-size: 11px; color: #9ca3af; text-align: center; padding: 10px;'>لا توجد خيارات متبقية</p>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

if st.button("حذف جميع الخيارات", type="primary", use_container_width=True):
    st.session_state.options_list = []
    st.rerun()

# 3. أزرار التنقل الرئيسية في أسفل الصفحة بشكل مرتب وطبيعي
st.markdown("<br>", unsafe_allow_html=True)
nav_col1, nav_col2, nav_col3, nav_col4 = st.columns(4)

with nav_col1:
    st.button("الرئيسية", use_container_width=True)
with nav_col2:
    st.button("الأدوات", use_container_width=True)
with nav_col3:
    st.button("الاعمال", use_container_width=True)
with nav_col4:
    st.button("⭐", use_container_width=True)

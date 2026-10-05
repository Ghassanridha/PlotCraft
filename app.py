import streamlit as st

st.set_page_config(
    page_title="بلوت كرافت",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# تخصيص التصميم وإخفاء القوائم الجانبية، مع تثبيت شريط التنقل السفلي الحقيقي
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
            padding-bottom: 90px !important; /* ترك مساحة للمحتوى حتى لا يختفي خلف الشريط السفلي */
            max-width: 100% !important;
        }
        
        /* تنسيق عام للخطوط العربية */
        @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;900&display=swap');
        html, body, [class*="css"] {
            font-family: 'Tajawal', sans-serif;
            direction: rtl;
            background-color: #0b0d12;
            color: #ffffff;
        }

        /* شريط التنقل السفلي الثابت على شاشة المتصفح بالكامل */
        .fixed-bottom-nav {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #12141c;
            border-top: 1px solid rgba(255, 255, 255, 0.15);
            padding: 10px 14px;
            display: flex;
            align-items: center;
            gap: 8px;
            z-index: 99999;
        }
    </style>
""", unsafe_allow_html=True)

# إدارة التنقل بين الشاشات باستخدام الـ Session State
if 'current_screen' not in st.session_state:
    st.session_state.current_screen = 'home'

if 'options_list' not in st.session_state:
    st.session_state.options_list = [
        "الخيار الأول (نمط بصري)",
        "الخيار الثاني (جودة عالية)",
        "الخيار الثالث (مؤثرات صوتية)"
    ]

# محتوى الشاشات
if st.session_state.current_screen == 'home':
    # واجهة الصفحة الرئيسية
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
            <div style="background: rgba(255, 255, 255, 0.07); border: 1px solid rgba(255, 255, 255, 0.12); border-radius: 14px; padding: 12px; text-align: right;">
                <h3 style="font-size: 11px; font-weight: bold; margin-bottom: 2px; color: #fff;">خطوة بخطوة</h3>
                <p style="font-size: 8px; color: #94a3b8; margin:0;">راجع كل خطوة</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div style="background: rgba(255, 255, 255, 0.07); border: 1px solid rgba(255, 255, 255, 0.12); border-radius: 14px; padding: 12px; text-align: right;">
                <h3 style="font-size: 11px; font-weight: bold; margin-bottom: 2px; color: #fff;">سريع</h3>
                <p style="font-size: 8px; color: #94a3b8; margin:0;">إدخال واحد، فيديو كامل</p>
            </div>
        """, unsafe_allow_html=True)

elif st.session_state.current_screen == 'tools':
    st.markdown("<h2 style='font-size: 16px; font-weight: 900; margin-bottom: 14px;'>الأدوات وإدارة الخيارات</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div style="background: rgba(255,255,255,0.05); padding: 18px; border-radius: 14px; border: 1px solid rgba(255,255,255,0.1);">
            <h3 style="font-size: 13px; font-weight: 900; margin-bottom: 12px; color: #fff;">قائمة الخيارات النشطة</h3>
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

elif st.session_state.current_screen == 'works':
    st.markdown("<h2 style='font-size: 16px; font-weight: 900; margin-bottom: 14px;'>الاعمال</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 220px;">
            <p style="font-size: 12px; color: #9ca3af;">لا توجد أعمال محفوظة</p>
        </div>
    """, unsafe_allow_html=True)

elif st.session_state.current_screen == 'custom':
    st.markdown("""
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 250px;">
            <div style="background: #12141c; border: 2px solid #ffffff; border-radius: 20px; padding: 25px; width: 100%; max-width: 280px; text-align: center; box-shadow: 0 8px 30px rgba(0,0,0,0.9);">
                <h3 style="font-size: 14px; font-weight: 900; color: #ffffff; margin-bottom: 8px;">القسم المخصص</h3>
                <p style="font-size: 10px; color: #9ca3af; margin: 0;">هذا الزر مستقل بذاته تماماً.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)


# شريط الأزرار السفلي الثابت في أسفل نافذة المتصفح تماماً
st.markdown('<div class="fixed-bottom-nav">', unsafe_allow_html=True)
col_b1, col_b2, col_b3, col_b4 = st.columns([1, 1, 1, 0.4])

with col_b1:
    if st.button("الصفحة الرئيسية", use_container_width=True, type="secondary" if st.session_state.current_screen != 'home' else "primary"):
        st.session_state.current_screen = 'home'
        st.rerun()

with col_b2:
    if st.button("الأدوات", use_container_width=True, type="secondary" if st.session_state.current_screen != 'tools' else "primary"):
        st.session_state.current_screen = 'tools'
        st.rerun()

with col_b3:
    if st.button("الاعمال", use_container_width=True, type="secondary" if st.session_state.current_screen != 'works' else "primary"):
        st.session_state.current_screen = 'works'
        st.rerun()

with col_b4:
    if st.button("⭐", use_container_width=True, type="secondary" if st.session_state.current_screen != 'custom' else "primary"):
        st.session_state.current_screen = 'custom'
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="بلوت كرافت", layout="centered")

# إدارة الحالة للانتقال بين الشاشات والنوافذ المنبثقة
if 'screen' not in st.session_state:
    st.session_state.screen = 'home'
if 'modal' not in st.session_state:
    st.session_state.modal = None  # يمكن أن تكون 'characters' أو 'story'

# تنسيقات التصميم المتطابقة مع صورك
st.markdown("""
    <style>
        #MainMenu, header, footer {visibility: hidden;}
        .block-container {padding: 0 !important; max-width: 450px;}
        body { background-color: #0b0f19; direction: rtl; font-family: Tahoma, sans-serif; color: #fff; }
        .app-container { background-color: #0b0f19; padding: 20px; min-height: 100vh; }
        
        .welcome-card {
            background-color: #141824; border: 1px solid #1e293b; border-radius: 14px; padding: 20px; margin-bottom: 15px; text-align: right;
        }
        .welcome-card p { font-size: 15px; line-height: 1.6; color: #e2e8f0; margin: 0; }
        
        .mode-grid { display: flex; gap: 12px; margin-bottom: 15px; }
        .mode-box {
            flex: 1; background-color: #141824; border: 1px solid #1e293b; border-radius: 14px; padding: 18px 12px; text-align: right; cursor: pointer; color: white;
        }
        
        .ai-box { background-color: #141824; border: 1px solid #1e293b; border-radius: 14px; padding: 15px; margin-bottom: 15px; text-align: right; }
        .ai-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }
        .ai-title { color: #ff2a85; font-size: 14px; font-weight: bold; }
        .ai-icon { width: 35px; height: 35px; background: linear-gradient(135deg, #ff2a85, #7928ca); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 11px; font-weight: bold; }
        .ai-text { font-size: 12px; color: #94a3b8; line-height: 1.5; margin: 0; }
        
        .setup-box { background-color: #141824; border: 1px solid #1e293b; border-radius: 14px; padding: 15px; text-align: right; }
        .setup-top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px; }
        .setup-title { font-size: 15px; font-weight: bold; }
        .counter-badge { background-color: #1e293b; color: #94a3b8; padding: 2px 8px; border-radius: 8px; font-size: 11px; }
        .setup-sub { font-size: 11px; color: #64748b; margin-bottom: 15px; }
        
        .row-item { background-color: #1a2234; border-radius: 10px; padding: 12px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }
        .row-info { display: flex; align-items: center; gap: 10px; }
        .circle-radio { width: 12px; height: 12px; border: 2px solid #475569; border-radius: 50%; }
        .row-text h4 { font-size: 13px; margin: 0 0 2px 0; color: #fff; }
        .row-text p { font-size: 11px; margin: 0; color: #94a3b8; }
        
        .popup-box { background-color: #161b26; border: 1px solid #ff2a85; border-radius: 12px; padding: 15px; margin-bottom: 15px; text-align: right; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="app-container">', unsafe_allow_html=True)

# ----------------- الشاشة الرئيسية -----------------
if st.session_state.screen == 'home':
    st.markdown('<div style="text-align: right; font-size: 18px; font-weight: bold; margin-bottom: 20px;">بلوت كرافت</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="welcome-card">
            <p>مساء الخير، أيها المخرج<br>أي قصة سنصنع اليوم؟</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div class="mode-box">
                <div style="font-size: 20px; margin-bottom: 8px;">⚡</div>
                <div style="font-size: 14px; font-weight: bold; margin-bottom: 4px;">سريع</div>
                <div style="font-size: 10px; color: #94a3b8;">إدخال واحد، فيديو كامل</div>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        # زر "خطوة بخطوة" للانتقال للواجهة المطلوبة
        if st.button("🚗 خطوة بخطوة\nراجع كل خطوة", use_container_width=True, key="step_main_btn"):
            st.session_state.screen = 'step'
            st.session_state.modal = None
            st.rerun()

# ----------------- الشاشة الثانية (تفاصيل خطوة بخطوة) -----------------
elif st.session_state.screen == 'step':
    if st.button("➔ رجوع للرئيسية", key="back_home"):
        st.session_state.screen = 'home'
        st.session_state.modal = None
        st.rerun()
        
    # مساعد AI بلوت كرافت
    st.markdown("""
        <div class="ai-box">
            <div class="ai-header">
                <div class="ai-title">مساعد AI بلوت كرافت</div>
                <div class="ai-icon">AI+</div>
            </div>
            <p class="ai-text">عزيزي المخرج، ما نوع القصة التي تريد إنشاؤها؟ اكتب فكرتك ودع بلوت كرافت يحولها إلى واقع.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # تفاعل إضافات الشخصيات (إرفاق صورتين كحد أقصى)
    if st.session_state.modal == 'characters':
        st.markdown("""
            <div class="popup-box">
                <h4 style="font-size: 13px; margin-bottom: 8px; color: #ff2a85;">إضافة الشخصيات (بحد أقصى صورتين)</h4>
            </div>
        """, unsafe_allow_html=True)
        uploaded_files = st.file_uploader("اختر الصور", type=["png", "jpg", "jpeg"], accept_multiple_files=True, key="char_files")
        if uploaded_files and len(uploaded_files) > 2:
            st.warning("عذراً، الحد الأقصى هو صورتان فقط!")
        if st.button("إغلاق نافذة الشخصيات", key="close_char"):
            st.session_state.modal = None
            st.rerun()

    # تفاعل الحكاية (كتابة بلا حدود)
    elif st.session_state.modal == 'story':
        st.markdown("""
            <div class="popup-box">
                <h4 style="font-size: 13px; margin-bottom: 8px; color: #ff2a85;">اكتب قصتك (عربي أو إنجليزي بلا حدود)</h4>
            </div>
        """, unsafe_allow_html=True)
        story_text = st.text_area("أدخل تفاصيل الحكاية هنا:", label_visibility="collapsed", height=120)
        
        col_s1, col_s2 = st.columns([3, 1])
        with col_s2:
            if st.button("التالي", use_container_width=True, key="story_next_btn"):
                st.success("تم حفظ الحكاية بنجاح!")
        with col_s1:
            if st.button("إغلاق", key="close_story"):
                st.session_state.modal = None
                st.rerun()

    # الصندوق الأساسي لإعداد القصة
    st.markdown("""
        <div class="setup-box">
            <div class="setup-top">
                <span class="setup-title">إعداد القصة</span>
                <span class="counter-badge">0/2</span>
            </div>
            <div class="setup-sub">أضف الشخصيات والقصة أولاً، ثم اختر المدة والنسبة:</div>
    """, unsafe_allow_html=True)
    
    # صف الشخصيات
    col_c1, col_c2 = st.columns([4, 1])
    with col_c1:
        st.markdown("""
            <div class="row-item" style="margin-bottom:0;">
                <div class="row-info">
                    <div class="circle-radio"></div>
                    <div class="row-text">
                        <h4>الشخصيات</h4>
                        <p>أضف شخصيتين بحد أقصى</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    with col_c2:
        if st.button("⬆ إضافة", key="btn_add_char", use_container_width=True):
            st.session_state.modal = 'characters'
            st.rerun()

    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    # صف الحكاية
    col_st1, col_st2 = st.columns([4, 1])
    with col_st1:
        st.markdown("""
            <div class="row-item" style="margin-bottom:0;">
                <div class="row-info">
                    <div class="circle-radio"></div>
                    <div class="row-text">
                        <h4>الحكاية</h4>
                        <p>اضغط لكتابة قصتك</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    with col_st2:
        if st.button("✏ إضافة", key="btn_add_story", use_container_width=True):
            st.session_state.modal = 'story'
            st.rerun()

    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
    
    # زر التالي العام في الأسفل
    if st.button("التالي", use_container_width=True, key="main_next_btn"):
        st.info("الرجاء إكمال إعداد الشخصيات والحكاية أولاً.")

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

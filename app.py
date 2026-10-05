import streamlit as st

# إعداد الصفحة بدون الهوامش الافتراضية ليعرض التصميم كاملاً
st.set_page_config(page_title="بلوت كرافت", layout="centered")

# إدارة الحالة للانتقال بين الشاشات
if 'screen' not in st.session_state:
    st.session_state.screen = 'home'

# كود التصميم بالكامل (CSS و HTML) لضمان مطابقة الصور تماماً
st.markdown("""
    <style>
        /* إخفاء الهوامش وأدوات ستريمليت المزعجة */
        #MainMenu, header, footer {visibility: hidden;}
        .block-container {padding: 0 !important; max-width: 450px;}
        
        body {
            background-color: #0b0f19;
            direction: rtl;
            font-family: Tahoma, sans-serif;
            color: #fff;
        }
        .app-container {
            background-color: #0b0f19;
            padding: 20px;
            min-height: 100vh;
        }
        /* الهيدر */
        .header-title {
            text-align: right;
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        /* صندوق الترحيب */
        .welcome-card {
            background-color: #141824;
            border: 1px solid #1e293b;
            border-radius: 14px;
            padding: 20px;
            margin-bottom: 15px;
            text-align: right;
        }
        .welcome-card p {
            font-size: 15px;
            line-height: 1.6;
            color: #e2e8f0;
            margin: 0;
        }
        /* مربعات الخيارات الرئيسية */
        .mode-grid {
            display: flex;
            gap: 12px;
            margin-bottom: 15px;
        }
        .mode-box {
            flex: 1;
            background-color: #141824;
            border: 1px solid #1e293b;
            border-radius: 14px;
            padding: 18px 12px;
            text-align: right;
            cursor: pointer;
            text-decoration: none;
            color: white;
            display: block;
        }
        .mode-box:hover {
            border-color: #ff2a85;
        }
        /* صندوق مساعد AI */
        .ai-box {
            background-color: #141824;
            border: 1px solid #1e293b;
            border-radius: 14px;
            padding: 15px;
            margin-bottom: 15px;
            position: relative;
        }
        .ai-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
        }
        .ai-title {
            color: #ff2a85;
            font-size: 14px;
            font-weight: bold;
        }
        .ai-icon {
            width: 35px;
            height: 35px;
            background: linear-gradient(135deg, #ff2a85, #7928ca);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 12px;
            font-weight: bold;
        }
        .ai-text {
            font-size: 12px;
            color: #94a3b8;
            line-height: 1.5;
            margin: 0;
        }
        /* صندوق إعداد القصة */
        .setup-box {
            background-color: #141824;
            border: 1px solid #1e293b;
            border-radius: 14px;
            padding: 15px;
        }
        .setup-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 5px;
        }
        .setup-title {
            font-size: 15px;
            font-weight: bold;
        }
        .counter-badge {
            background-color: #1e293b;
            color: #94a3b8;
            padding: 2px 8px;
            border-radius: 8px;
            font-size: 11px;
        }
        .setup-sub {
            font-size: 11px;
            color: #64748b;
            margin-bottom: 15px;
        }
        /* عناصر الشخصيات والحكاية */
        .row-item {
            background-color: #1a2234;
            border-radius: 10px;
            padding: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }
        .row-info {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .circle-radio {
            width: 12px;
            height: 12px;
            border: 2px solid #475569;
            border-radius: 50%;
        }
        .row-text h4 {
            font-size: 13px;
            margin: 0 0 2px 0;
            color: #fff;
        }
        .row-text p {
            font-size: 11px;
            margin: 0;
            color: #94a3b8;
        }
        .action-btn {
            background-color: #222d44;
            color: #fff;
            border: none;
            padding: 5px 12px;
            border-radius: 6px;
            font-size: 11px;
            cursor: pointer;
        }
        /* زر التالي وزر الرجوع */
        .next-main-btn {
            width: 100%;
            background-color: #1e293b;
            color: #64748b;
            border: none;
            padding: 12px;
            border-radius: 10px;
            font-size: 14px;
            font-weight: bold;
            margin-top: 10px;
            cursor: pointer;
        }
        .back-link {
            color: #fff;
            text-decoration: none;
            font-size: 18px;
            margin-bottom: 15px;
            display: inline-block;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="app-container">', unsafe_allow_html=True)

# ----------------- الشاشة الأولى (الرئيسية) -----------------
if st.session_state.screen == 'home':
    st.markdown('<div class="header-title">بلوت كرافت</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="welcome-card">
            <p>مساء الخير، أيها المخرج<br>أي قصة سنصنع اليوم؟</p>
        </div>
    """, unsafe_allow_html=True)
    
    # استخدام أعمدة بايثون الشفافة لتوجيه الضغط على زر "خطوة بخطوة" بدقة
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
        # زر شفاف فوق المربع الثاني لضمان الانتقال السلس بالشكل المطلوب
        if st.button("خطوة بخطوة\nراجع كل خطوة", use_container_width=True, key="step_btn"):
            st.session_state.screen = 'step'
            st.rerun()

# ----------------- الشاشة الثانية (الخطوات وإعداد القصة) -----------------
elif st.session_state.screen == 'step':
    if st.button("➔ رجوع", key="back_btn"):
        st.session_state.screen = 'home'
        st.rerun()
        
    # صندوق مساعد AI
    st.markdown("""
        <div class="ai-box">
            <div class="ai-header">
                <div class="ai-title">مساعد AI بلوت كرافت</div>
                <div class="ai-icon">AI+</div>
            </div>
            <p class="ai-text">عزيزي المخرج، ما نوع القصة التي تريد إنشاؤها؟ اكتب فكرتك ودع بلوت كرافت يحولها إلى واقع.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # صندوق إعداد القصة
    st.markdown("""
        <div class="setup-box">
            <div class="setup-top">
                <span class="setup-title">إعداد القصة</span>
                <span class="counter-badge">0/2</span>
            </div>
            <div class="setup-sub">أضف الشخصيات والقصة أولاً، ثم اختر المدة والنسبة:</div>
            
            <div class="row-item">
                <div class="row-info">
                    <div class="circle-radio"></div>
                    <div class="row-text">
                        <h4>الشخصيات</h4>
                        <p>أضف شخصيتين بحد أقصى</p>
                    </div>
                </div>
                <button class="action-btn">⬆ إضافة</button>
            </div>
            
            <div class="row-item">
                <div class="row-info">
                    <div class="circle-radio"></div>
                    <div class="row-text">
                        <h4>الحكاية</h4>
                        <p>اضغط لكتابة قصتك</p>
                    </div>
                </div>
                <button class="action-btn">✏ إضافة</button>
            </div>
            
            <button class="next-main-btn">التالي</button>
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

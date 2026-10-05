import streamlit as st

# إعداد الصفحة وتفعيل تصميم الواجهة المخصص
st.set_page_config(page_title="بلوت كرافت", layout="centered")

# تخزين الحالة لمعرفة أي شاشة نعرض (الرئيسية أو شاشة الخطوات)
if 'current_screen' not in st.session_state:
    st.session_state.current_screen = 'home'

# تنسيقات الـ CSS للواجهة الداكنة والشاشات
st.markdown("""
    <style>
        /* إخفاء عناصر Streamlit الافتراضية للتنظيف */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        .main-container {
            background-color: #0b0f19;
            color: #ffffff;
            padding: 20px;
            border-radius: 12px;
            font-family: Tahoma, sans-serif;
            direction: rtl;
        }
        .welcome-box {
            background: linear-gradient(135deg, rgba(30,30,45,0.6), rgba(15,15,25,0.8));
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            text-align: right;
            border: 1px solid rgba(255,255,255,0.05);
        }
        .welcome-box p {
            font-size: 16px;
            line-height: 1.6;
            color: #e2e8f0;
        }
        .mode-card {
            background-color: #161b26;
            border: 1px solid #2a3447;
            border-radius: 12px;
            padding: 20px 15px;
            text-align: right;
            margin-bottom: 10px;
        }
        .ai-box {
            background-color: #1a1625;
            border-radius: 12px;
            padding: 15px;
            margin-bottom: 20px;
            border: 1px solid rgba(255,42,133,0.2);
        }
        .ai-title {
            color: #ff2a85;
            font-size: 14px;
            font-weight: bold;
        }
        .ai-desc {
            font-size: 13px;
            line-height: 1.5;
            color: #cbd5e1;
            margin-top: 8px;
        }
        .setup-box {
            background-color: #141824;
            border: 1px solid #1e293b;
            border-radius: 12px;
            padding: 15px;
        }
        .item-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #1a2234;
            border-radius: 8px;
            padding: 12px;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# محتوى الصفحة
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# ----------------- الشاشة الرئيسية -----------------
if st.session_state.current_screen == 'home':
    st.markdown('<div style="text-align: right; font-size: 20px; font-weight: bold; margin-bottom: 20px;">بلوت كرافت</div>', unsafe_allow_html=True)
    
    st.markdown('''
        <div class="welcome-box">
            <p>مساء الخير، أيها المخرج<br>أي قصة سنصنع اليوم؟</p>
        </div>
    ''', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('''
            <div class="mode-card">
                <span style="font-size: 24px;">⚡</span>
                <h3 style="font-size: 15px; margin: 5px 0;">سريع</h3>
                <p style="font-size: 11px; color: #94a3b8; margin: 0;">إدخال واحد، فيديو كامل</p>
            </div>
        ''', unsafe_allow_html=True)
    
    with col2:
        # زر خطوة بخطوة للانتقال
        if st.button("🚗 خطوة بخطوة\nراجع كل خطوة", use_container_width=True):
            st.session_state.current_screen = 'step'
            st.rerun()

# ----------------- شاشة إعداد القصة والتفاصيل -----------------
elif st.session_state.current_screen == 'step':
    if st.button("➔ رجوع"):
        st.session_state.current_screen = 'home'
        st.rerun()
        
    # صندوق مساعد AI مع القائمة المنسدلة باستخدام Streamlitselectbox
    st.markdown('<div class="ai-box">', unsafe_allow_html=True)
    col_t1, col_t2 = st.columns([4, 1])
    with col_t1:
        st.markdown('<div class="ai-title">مساعد AI بلوت كرافت</div>', unsafe_allow_html=True)
    with col_t2:
        # قائمة منسدلة بدل الكود المعقد لتفادي الأخطاء في بايثون
        ai_menu = st.selectbox("المساعد", ["شعار دائرة أولاً", "خيارات أخرى"], label_visibility="collapsed")
        
    st.markdown('<div class="ai-desc">عزيزي المخرج، ما نوع القصة التي تريد إنشاؤها؟ اكتب فكرتك ودع بلوت كرافت يحولها إلى واقع.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # صندوق إعداد القصة
    st.markdown('''
        <div class="setup-box">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <span style="font-size: 15px; font-weight: bold;">إعداد القصة</span>
                <span style="background-color: #1e293b; color: #94a3b8; padding: 2px 10px; border-radius: 10px; font-size: 11px;">0/2</span>
            </div>
            <p style="font-size: 11px; color: #64748b; margin-bottom: 15px;">أضف الشخصيات والقصة أولاً، ثم اختر المدة والنسبة:</p>
            
            <div class="item-row">
                <div>
                    <h4 style="font-size: 13px; color: #fff; margin: 0 0 2px 0;">الشخصيات</h4>
                    <p style="font-size: 11px; color: #94a3b8; margin: 0;">أضف شخصيتين بحد أقصى</p>
                </div>
            </div>
            
            <div class="item-row">
                <div>
                    <h4 style="font-size: 13px; color: #fff; margin: 0 0 2px 0;">الحكاية</h4>
                    <p style="font-size: 11px; color: #94a3b8; margin: 0;">اضغط لكتابة قصتك</p>
                </div>
            </div>
        </div>
    ''', unsafe_allow_html=True)
    
    # زر التالي
    if st.button("التالي", use_container_width=True):
        st.success("تم الانتقال بنجاح")

st.markdown('</div>', unsafe_allow_html=True)

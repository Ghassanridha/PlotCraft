import streamlit as st

# إعداد الصفحة وتنسيقها لتشبه واجهة التطبيق المظلمة (Dark Mode)
st.set_page_config(
    page_title="PlotCraft UI - Streamlit",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# تخصيص التصميم عبر CSS ليكون مطابقاً تماماً لواجهة Google Play الأصلية
st.markdown("""
<style>
    .stApp {
        background-color: #121212;
        color: #ffffff;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    .main-container {
        max-width: 420px;
        margin: 0 auto;
        padding: 10px;
    }
    .top-bar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 12px 0;
        border-bottom: 1px solid #2b2b2b;
        margin-bottom: 15px;
    }
    .card-box {
        background-color: #1e1e1e;
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 12px;
        border: 1px solid #2c2c2c;
    }
    .row-item {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 12px 0;
        border-bottom: 1px solid #252525;
        cursor: pointer;
    }
    .row-item:hover {
        background-color: #1a1a1a;
    }
    .sub-text {
        color: #9aa0a6;
        font-size: 13px;
    }
    .title-text {
        color: #ffffff;
        font-size: 15px;
        font-weight: 500;
    }
    .stButton>button {
        width: 100%;
        background-color: #8ab4f8;
        color: #202124;
        border-radius: 24px;
        font-weight: bold;
        border: none;
        padding: 12px;
    }
    .stButton>button:hover {
        background-color: #aecbfa;
    }
</style>
""", unsafe_allow_html=True)

# تهيئة حالة الجلسة (Session State) للتنقل بين الواجهات وحفظ الإعدادات
if 'view' not in st.session_state:
    st.session_state.view = 'main'  # الخيارات: 'main', 'payment_methods', 'redeem', 'paypal', 'card', 'buy_google', 'request_pay'

if 'use_google_balance' not in st.session_state:
    st.session_state.use_google_balance = True

if 'selected_payment' not in st.session_state:
    st.session_state.selected_payment = "Mastercard-0709"

# حاوية التطبيق الرئيسية
with st.container():
    
    # ----------------------------------------------------
    # الواجهة الأولى: شاشة الاشتراك الرئيسية (PlotCraft Pro Weekly)
    # ----------------------------------------------------
    if st.session_state.view == 'main':
        col_close, col_title = st.columns([1, 10])
        with col_close:
            if st.button("✕", key="close_main"):
                pass
        with col_title:
            st.markdown("<p style='text-align: right; color: #9aa0a6; margin: 0; font-size: 14px;'>Google Play</p>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # أيقونة التطبيق وتفاصيله
        col_icon, col_details = st.columns([1, 4])
        with col_icon:
            st.markdown("""
                <div style="background-color: #333333; width: 45px; height: 45px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 12px; color: #fff; border: 1px solid #555;">
                    PLOT
                </div>
            """, unsafe_allow_html=True)
        with col_details:
            st.markdown("**PlotCraft Pro Weekly**<br><span class='sub-text'>PlotCraft: AI Short Drama Maker</span>", unsafe_allow_html=True)
        
        st.markdown("---")
        
        col_p1, col_p2 = st.columns(2)
        with col_p1:
            st.markdown("**US$/week 9.99**<br><span class='sub-text'>بالإضافة إلى الضريبة</span>", unsafe_allow_html=True)
        with col_p2:
            st.markdown("<div style='text-align: right;'>بدءاً من اليوم<br><span class='sub-text'>إضافة الضريبة ⓘ</span></div>", unsafe_allow_html=True)
            
        st.markdown("---")
        
        st.markdown("""
        <div class='sub-text' style='line-height: 1.6;'>
        • يمكنك الإلغاء في أي وقت في صفحة "الاشتراكات" على Google Play<br>
        • سيستخدم رصيدك في Google Play لتحصيل الرسوم اليوم. وأي رسوم متبقية ستحصل من طريقة الدفع الموضحة أدناه.<br>
        • ستحصل رسوم عمليات التجديد من طريقة الدفع الأساسية
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # خانة النقاط
        col_r1, col_r2 = st.columns([4, 1])
        with col_r1:
            st.markdown("<span style='font-size: 14px;'>كسب ١١ نقطة إضافية</span>", unsafe_allow_html=True)
        with col_r2:
            st.markdown("🟡🟩🟦🟥", unsafe_allow_html=True)
            
        st.markdown("---")
        
        # صندوق وسيلة الدفع (عند النقر عليه يفتح شاشة طرق الدفع)
        payment_box = st.container()
        with payment_box:
            col_m1, col_m2, col_m3 = st.columns([1, 6, 1])
            with col_m1:
                st.markdown("💳")
            with col_m2:
                st.markdown(f"**{st.session_state.selected_payment}**<br><span class='sub-text'>رصيد Google Play: US$ 0.16</span>", unsafe_allow_html=True)
            with col_m3:
                if st.button("➔", key="go_to_payment"):
                    st.session_state.view = 'payment_methods'
                    st.rerun()
                    
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class='sub-text' style='font-size: 11px; text-align: center;'>
        عند النقر على "اشتراك"، فإن هذا يعني موافقتك على تجديد اشتراكك تلقائياً إلى أن يتم إلغاؤه. سنعلمك في حال تغير السعر، وذلك استناداً لما هو موضح في "بنود خدمة Google Play". <a href='#' style='color: #8ab4f8;'>التعرف على كيفية إلغاء الاشتراك</a>. المزيد
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("اشتراك"):
            st.success("تم إرسال طلب الاشتراك بنجاح عبر بلوت كرافت (PlotCraft)!")

    # ----------------------------------------------------
    # الواجهة الثانية: شاشة طرق الدفع الكاملة (طرق الدفع)
    # ----------------------------------------------------
    elif st.session_state.view == 'payment_methods':
        col_back, col_title = st.columns([1, 10])
        with col_back:
            if st.button("←", key="back_to_main"):
                st.session_state.view = 'main'
                st.rerun()
        with col_title:
            st.markdown("<h3 style='text-align: right; margin: 0; font-size: 18px;'>طرق الدفع</h3>", unsafe_allow_html=True)
            
        st.markdown("<p style='text-align: right; color: #9aa0a6; font-size: 13px;'>ahhanaa70@gmail.com</p>", unsafe_allow_html=True)
        st.markdown("---")
        
        # اختيار طريقة الدفع الرئيسية
        col_chk, col_name, col_logo = st.columns([1, 6, 2])
        with col_chk:
            st.markdown("✅")
        with col_name:
            st.markdown("**Mastercard-0709**")
        with col_logo:
            st.markdown("💳")
            
        st.markdown("---")
        
        # مفتاح تفعيل/تعطيل رصيد جوجل بلاي
        col_sw_lbl, col_sw = st.columns([4, 1])
        with col_sw_lbl:
            st.markdown("**US$ 0,16: Google Play رصيد**")
        with col_sw:
            use_balance = st.toggle("", value=st.session_state.use_google_balance, key="toggle_bal")
            st.session_state.use_google_balance = use_balance
            
        st.markdown("---")
        st.markdown("<p class='sub-text' style='text-align: right;'>إضافة طريقة دفع إلى حسابك على Google</p>", unsafe_allow_html=True)
        
        # خيار استخدام الرمز
        if st.button("🎫  استخدام الرمز", key="btn_redeem"):
            st.session_state.view = 'redeem'
            st.rerun()
            
        # خيار إضافة PayPal
        if st.button("🅿️  إضافة PayPal", key="btn_paypal"):
            st.session_state.view = 'paypal'
            st.rerun()
            
        # خيار إضافة بطاقة
        if st.button("💳  إضافة بطاقة   |   VISA  MC  DISCOVER  + أخرى", key="btn_card"):
            st.session_state.view = 'card'
            st.rerun()
            
        # خيار شراء رصيد Google Play
        if st.button("▶️  شراء رصيد Google Play", key="btn_buy_google"):
            st.session_state.view = 'buy_google'
            st.rerun()
            
        # خيار طلب الدفع من مستخدم آخر
        if st.button("👥  طلب الدفع من مستخدم آخر\n<span style='font-size:11px; color:#9aa0a6;'>غير متوفرة لشراء الاشتراكات</span>", key="btn_request"):
            st.session_state.view = 'request_pay'
            st.rerun()

    # ----------------------------------------------------
    # الواجهة الفرعية 1: استخدام الرمز (Redeem Code)
    # ----------------------------------------------------
    elif st.session_state.view == 'redeem':
        if st.button("← رجوع", key="back_from_redeem"):
            st.session_state.view = 'payment_methods'
            st.rerun()
        st.markdown("### استخدام رمز الاسترداد")
        code_input = st.text_input("أدخل الرمز الخاص بك هنا:")
        if st.button("تحقق واسترداد"):
            if code_input:
                st.success("تم تطبيق الرمز بنجاح على حسابك في بلوت كرافت!")
            else:
                st.warning("الرجاء إدخال الرمز أولاً.")

    # ----------------------------------------------------
    # الواجهة الفرعية 2: إضافة حساب PayPal
    # ----------------------------------------------------
    elif st.session_state.view == 'paypal':
        if st.button("← رجوع", key="back_from_paypal"):
            st.session_state.view = 'payment_methods'
            st.rerun()
        st.markdown("### ربط حساب PayPal")
        pp_email = st.text_input("البريد الإلكتروني لحساب PayPal:")
        if st.button("ربط الحساب"):
            if pp_email:
                st.success("تم ربط حساب PayPal بنجاح!")
            else:
                st.warning("الرجاء إدخال البريد الإلكتروني.")

    # ----------------------------------------------------
    # الواجهة الفرعية 3: إضافة بطاقة بنكية
    # ----------------------------------------------------
    elif st.session_state.view == 'card':
        if st.button("← رجوع", key="back_from_card"):
            st.session_state.view = 'payment_methods'
            st.rerun()
        st.markdown("### إضافة بطاقة بنكية جديدة")
        card_num = st.text_input("رقم البطاقة (Card Number)")
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            st.text_input("تاريخ الانتهاء (MM/YY)")
        with col_c2:
            st.text_input("رمز الأمان (CVC)")
        if st.button("حفظ البطاقة"):
            st.success("تمت إضافة البطاقة البنكية بنجاح!")

    # ----------------------------------------------------
    # الواجهة الفرعية 4: شراء رصيد Google Play
    # ----------------------------------------------------
    elif st.session_state.view == 'buy_google':
        if st.button("← رجوع", key="back_from_buy"):
            st.session_state.view = 'payment_methods'
            st.rerun()
        st.markdown("### شراء رصيد Google Play")
        amount = st.selectbox("اختر القيمة المراد شراؤها:", ["$5.00", "$10.00", "$25.00", "$50.00", "$100.00"])
        if st.button("إتمام عملية الشراء"):
            st.success(f"تمت عملية شراء رصيد بقيمة {amount} بنجاح!")

    # ----------------------------------------------------
    # الواجهة الفرعية 5: طلب الدفع من مستخدم آخر
    # ----------------------------------------------------
    elif st.session_state.view == 'request_pay':
        if st.button("← رجوع", key="back_from_req"):
            st.session_state.view = 'payment_methods'
            st.rerun()
        st.markdown("### طلب الدفع من مستخدم آخر")
        st.info("هذه الميزة غير متوفرة لشراء الاشتراكات حالياً.")
        target_email = st.text_input("البريد الإلكتروني للشخص المراد إرسال الطلب إليه:")
        if st.button("إرسال الطلب"):
            if target_email:
                st.success("تم إرسال طلب الدفع بنجاح!")
            else:
                st.warning("الرجاء إدخال البريد الإلكتروني.")

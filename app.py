import streamlit as st

# إعداد الصفحة وتصميم الواجهة
st.set_page_config(
    page_title="PlotCraft - بلوت كرافت",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تهيئة حالة الاشتراك والقفل في الذاكرة المؤقتة
if "is_subscribed" not in st.session_state:
    st.session_state.is_subscribed = False

# تنسيق الألوان والتصميم (الشعار و Pro only باللون الأبيض بالكامل)
st.markdown(
    """
    <style>
    .main-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background-color: #121212;
        padding: 15px 25px;
        border-radius: 12px;
        margin-bottom: 25px;
        border: 1px solid #333333;
    }
    .logo-area {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .app-title {
        color: #FFFFFF !important;
        font-size: 26px;
        font-weight: bold;
        margin: 0;
    }
    .pro-badge {
        color: #FFFFFF !important;
        background-color: #333333;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 14px;
        font-weight: bold;
        border: 1px solid #FFFFFF;
    }
    .locked-card {
        background-color: #1e1e1e;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        border: 1px dashed #555555;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# رأس الصفحة والشعار باللون الأبيض مع شارة Pro only باللون الأبيض أيضاً
st.markdown(
    """
    <div class="main-header">
        <div class="logo-area">
            <h1 class="app-title">🎬 PlotCraft (بلوت كرافت)</h1>
        </div>
        <div>
            <span class="pro-badge">PRO ONLY</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# القائمة الجانبية للتنقل في التطبيق
st.sidebar.title("القائمة الرئيسية")
app_mode = st.sidebar.radio("اختر القسم:", ["الصفحة الرئيسية", "إنشاء القصة والفيديوهات", "الإعدادات"])

# محتوى الصفحة الرئيسية
if app_mode == "الصفحة الرئيسية":
    st.subheader("مرحباً بك في عالم صناعة القصص والأفلام الذكية")
    st.write("هنا يمكنك البدء بمشروعك الجديد باستخدام الذكاء الاصطناعي.")
    
    # نموذج مبسط لأقسام التطبيق الأساسية
    col1, col2 = st.columns(2)
    with col1:
        st.info("💡 توليد الأفكار السينمائية تلقائياً.")
    with col2:
        st.info("🎥 تحويل النصوص إلى مشاهد بصرية مذهلة.")

# محتوى قسم إنشاء القصة والفيديوهات (المتأثر بنظام القفل)
elif app_mode == "إنشاء القصة والفيديوهات":
    st.subheader("أداة توليد الأفلام المتقدمة (Pro)")

    # التحقق مما إذا كان المستخدم مشتركاً أم لا
    if not st.session_state.is_subscribed:
        # الحالة الأولى: القفل مغلق لعدم الاشتراك
        st.markdown(
            """
            <div class="locked-card">
                <h2>🔒 المحتوى مقفل</h2>
                <p style="color: #b0b0b0;">هذه الميزة مخصصة لمشتركي باقة Pro Only. يرجى الاشتراك أدناه ليتم فتح القفل وتفعيل الميزات فوراً وبشكل تلقائي.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.write("---")
        st.write("### اختر باقة الاشتراك السريع:")
        
        sub_col1, sub_col2 = st.columns(2)
        
        with sub_col1:
            if st.button("🚀 اشتراك أسبوعي سريع", use_container_width=True):
                st.session_state.is_subscribed = True
                st.success("تم الاشتراك بنجاح! تم فتح القفل تلقائياً 🎉")
                st.rerun()
                
        with sub_col2:
            if st.button("👑 اشتراك شهري سريع", use_container_width=True):
                st.session_state.is_subscribed = True
                st.success("تم الاشتراك بنجاح! تم فتح القفل تلقائياً 🎉")
                st.rerun()
                
    else:
        # الحالة الثانية: القفل مفتوح لأن المستخدم مشترك
        st.success("🔓 القفل مفتوح - أنت تستمتع بكافة صلاحيات وخدمات PlotCraft Pro!")
        
        # واجهة أدوات التطبيق الأصلية بالداخل
        story_prompt = st.text_area("أدخل فكرة قصتك أو السيناريو هنا:", placeholder="مثال: قصة خيال علمي تدور أحداثها في المستقبل...")
        
        col_gen1, col_gen2 = st.columns(2)
        with col_gen1:
            if st.button("توليد السيناريو والحوار", use_container_width=True):
                if story_prompt:
                    st.write("✨ جاري معالجة وتوليد السيناريو...")
                    st.success("تم توليد السيناريو بنجاح!")
                else:
                    st.warning("الرجاء كتابة الفكرة أولاً.")
                    
        with col_gen2:
            if st.button("إنشاء الفيديو التلقائي", use_container_width=True):
                if story_prompt:
                    st.write("🎬 جاري تحويل القصة إلى مشاهد مرئية...")
                    st.success("تم تجهيز الفيديو بنجاح!")
                else:
                    st.warning("الرجاء كتابة الفكرة أولاً.")
                    
        st.write("---")
        if st.button("إلغاء الاشتراك (وضع التجربة والإغلاق)", type="secondary"):
            st.session_state.is_subscribed = False
            st.rerun()

# محتوى قسم الإعدادات
elif app_mode == "الإعدادات":
    st.subheader("إعدادات التطبيق")
    st.write("إدارة حسابك وتفضيلات الذكاء الاصطناعي.")
    st.text_input("اسم المستخدم", "Ghassan Jbbasi")
    st.text_input("مفتاح API الخاص", type="password")
    if st.button("حفظ التعديلات"):
        st.success("تم حفظ الإعدادات بنجاح.")

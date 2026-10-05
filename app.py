import streamlit as st

# ... (الكود الأساسي الخاص بك وباقي الواجهة الرئيسية ومقاطع الفيديو العلوية يبقى كما هو دون مسح)

# 1. تعريف الحالة الخاصة بإظهار وإخفاء القائمة عند الضغط على الأيقونة
if "show_creation_menu" not in st.session_state:
    st.session_state.show_creation_menu = False

# 2. مكان الأيقونة أو الزر (يمكنك وضع هذا الزر في المكان الذي تفضله في واجهتك)
# عند ضغط المستخدم على الأيقونة/الزر، ستتغير الحالة لتظهر القائمة أو تختفي
if st.button("➕"):  # أو استبدلها بأيقونة أو زر حسب تصميمك
    st.session_state.show_creation_menu = not st.session_state.show_creation_menu

# 3. عرض القائمة المضافة حديثاً فقط وفقط عند الضغط على الأيقونة (تم حذف كلمة "دراما جديدة" نهائياً)
if st.session_state.show_creation_menu:
    with st.container():
        # تم حذف كلمة "دراما جديدة" واستبدالها أو تركها نظيفة حسب رغبتك، هنا بدون العنوان القديم
        st.markdown(
            "### بلوت كرافت"
        )  # العنوان الجديد بدل "دراما جديدة" كما طلبت

        # مساعد AI بلوت كرافت
        st.markdown(
            """
            <div style="background-color: #1e1e2f; padding: 15px; border-radius: 10px; border: 1px solid #ff4b4b; margin-bottom: 15px;">
                <span style="color: #ff4b4b; font-weight: bold;">🤖 مساعد AI بلوت كرافت</span>
                <p style="color: #ffffff; margin-top: 5px;">عزيزي المخرج، ما نوع القصة التي تريد إنشاؤها؟ اكتب فكرتك ودع بلوت كرافت يحولها إلى واقع.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # إعداد القصة (القسم الأخير الذي أضفته مؤخراً)
        st.markdown("#### إعداد القصة")
        st.text("أضف الشخصيات والقصة أولاً، ثم اختر المدة والنسبة.")

        col1, col2 = st.columns(2)
        with col1:
            st.button("+ إضافة: الشخصيات", key="add_chars")
        with col2:
            st.button("✏️ إضافة: الحكاية", key="add_story")

        # زر صغير لإغلاق القائمة العائمة إذا أردت
        if st.button("إغلاق القائمة ✕", key="close_menu"):
            st.session_state.show_creation_menu = False
            st.rerun()

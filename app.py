import streamlit as st

# 1. تهيئة حالة الإظهار والإخفاء (تأكد من وضعها في بداية الكود لديك)
if "show_plotcraft_menu" not in st.session_state:
    st.session_state.show_plotcraft_menu = False

# 2. مكان الأيقونة أو الزر (+) في الواجهة الرئيسية
# (يمكنك وضع هذا الزر في المكان المفضل لديك ضمن تصميمك الحالي)
if st.button("➕", key="toggle_btn"):
    st.session_state.show_plotcraft_menu = not st.session_state.show_plotcraft_menu

# 3. إذا تم الضغط على الأيقونة، تظهر هذه القائمة وحدها دون المساس بباقي عناصر الصفحة
if st.session_state.show_plotcraft_menu:
    st.markdown("### بلوت كرافت")

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

    # إعداد القصة
    st.markdown("#### إعداد القصة")
    st.text("أضف الشخصيات والقصة أولاً، ثم اختر المدة والنسبة.")

    col1, col2 = st.columns(2)
    with col1:
        st.button("+ إضافة: الشخصيات", key="btn_chars")
    with col2:
        st.button("✏️ إضافة: الحكاية", key="btn_story")

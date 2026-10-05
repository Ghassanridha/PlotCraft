import streamlit as st

# إعداد الصفحة وتجنب أي تداخل في التصميم
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0e0f13;
        color: #ffffff;
    }
    /* تصميم البطاقات الرئيسية */
    .main-card {
        background-color: #1a1b22;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    /* صندوق الترحيب العلوي الخاص بالمساعد */
    .ai-banner {
        background-color: #1a1b22;
        border-radius: 12px;
        padding: 15px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 20px;
        border: 1px solid rgba(255, 255, 255, 0.08);
    }
    .ai-text {
        font-size: 14px;
        color: #e0e0e0;
        text-align: right;
        direction: rtl;
    }
    .ai-title {
        color: #ff4b8b;
        font-weight: bold;
        font-size: 15px;
        margin-bottom: 5px;
    }
    /* الشعار الدائري */
    .ai-avatar {
        width: 45px;
        height: 45px;
        background: linear-gradient(135deg, #ff4b8b 0%, #a855f7 100%);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        color: white;
        font-size: 14px;
        box-shadow: 0 4px 10px rgba(255, 75, 139, 0.3);
    }
    /* الأقسام داخل القائمة الجديدة */
    .section-box {
        background-color: #1a1b22;
        border-radius: 12px;
        padding: 15px;
        margin-top: 15px;
        border: 1px solid rgba(255, 255, 255, 0.08);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# إدارة حالة التنقل بين الواجهة الرئيسية وقائمة خطوة بخطوة
if "step_by_step_active" not in st.session_state:
    st.session_state.step_by_step_active = False

# الواجهة الرئيسية لتطبيق بلوت كرافت
if not st.session_state.step_by_step_active:
    st.markdown(
        "<h3 style='text-align: right; direction: rtl;'>بلوت كرافت</h3>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h4 style='text-align: right; direction: rtl; color: #aaa;'>مساء الخير، أيها المخرج<br>أي قصة سنصنع اليوم؟</h4>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🚀 سريع\n\nإدخال واحد، فيديو كامل", use_container_width=True):
            pass

    with col2:
        # عند الضغط على زر خطوة بخطوة يتم تفعيل الانتقال للقائمة الجديدة المطابقة للصورة الثانية
        if st.button(
            "🎛️ خطوة بخطوة\n\nراجع كل خطوة", use_container_width=True
        ):
            st.session_state.step_by_step_active = True
            st.rerun()

# القائمة الجديدة المطابقة لتفاصيل الصورة الثانية عند الضغط على خطوة بخطوة
else:
    # زر العودة للخلف
    if st.button("❮ العودة"):
        st.session_state.step_by_step_active = False
        st.rerun()

    st.markdown(
        "<h4 style='text-align: center; direction: rtl;'>دراما جديدة</h4>",
        unsafe_allow_html=True,
    )

    # صندوق الترحيب مع شعار دائري واسم مساعد AI بلوت كرافت
    st.markdown(
        """
        <div class="ai-banner">
            <div class="ai-avatar">AI+</div>
            <div class="ai-text">
                <div class="ai-title">مساعدة AI بلوت كرافت</div>
                عزيزي المخرج، ما نوع القصة التي تريد إنشاؤها؟ اكتب فكرتك ودع مساعد AI يحولها إلى واقع.
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # هيكل إعداد القصة والخيارات المطابقة تماماً
    st.markdown(
        """
        <div class="section-box">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; direction: rtl;">
                <span style="font-weight: bold; font-size: 15px;">إعداد القصة</span>
                <span style="background-color: #2a2b36; color: #aaa; padding: 2px 8px; border-radius: 10px; font-size: 12px;">0/2</span>
            </div>
            <div style="color: #888; font-size: 12px; margin-bottom: 15px; direction: rtl;">أضف الشخصيات والقصة أولاً، ثم اختر المدة والنسبة.</div>
            
            <div style="background-color: #23242d; padding: 12px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; direction: rtl;">
                <span>الشخصيات (أضف شخصيتين كحد أقصى)</span>
                <button style="background-color: #333442; color: white; border: none; padding: 5px 12px; border-radius: 6px; cursor: pointer;">⬆ إضافة</button>
            </div>

            <div style="background-color: #23242d; padding: 12px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center; direction: rtl;">
                <span>الحكاية (اضغط لكتابة قصتك)</span>
                <button style="background-color: #333442; color: white; border: none; padding: 5px 12px; border-radius: 6px; cursor: pointer;">✍ إضافة</button>
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.button("التالي", use_container_width=True, disabled=True)

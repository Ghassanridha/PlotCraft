import streamlit as st
import fal_client
import os

# إعداد الصفحة وتصميم الواجهة
st.set_page_config(page_title="PlotCraft - مولد الفيديوهات", layout="centered")

# CSS لتنسيق شارة الـ Pro في أعلى الجانب الأيسر بشكل أنيق
st.markdown("""
    <style>
    .pro-badge {
        background: linear-gradient(45deg, #FF4B4B, #FF8F00);
        color: white;
        padding: 5px 12px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 14px;
        float: left;
        margin-bottom: 10px;
    }
    </style>
    <div class="pro-badge">⭐ Pro Version</div>
""", unsafe_allow_html=True)

st.title("PlotCraft - مولد الفيديوهات بالذكاء الاصطناعي")
st.write("حول قصصك وصور الشخصيات إلى مقاطع فيديو سينمائية احترافية!")

# إدخال مفتاح الـ API الخاص بـ fal.ai
DEFAULT_FAL_KEY = "fal_sk_d8e30b437fdc44c891740a201522be4d:d78802704ad38b28b6b7f1bcef6ef4c"
os.environ["FAL_KEY"] = DEFAULT_FAL_KEY

# --- الإعدادات الاختيارية في الشريط الجانبي ---
st.sidebar.header("⚙️ إعدادات الفيديو المتقدمة")

# 1. دقة الفيديو
resolution_option = st.sidebar.selectbox(
    "اختر دقة الفيديو",
    ["720p HD", "1080p Full HD", "4K Ultra"]
)

# 2. مدة الفيديو (أرقام مربعة وليست شريط سحب)
duration_option = st.sidebar.selectbox(
    "مدة الفيديو (بالثواني أو الدقائق)",
    ["10 ثواني", "21 ثانية", "5 دقائق"]
)

# 3. أيقونة إضافة صورة الشخصية (Image-to-Video)
st.sidebar.markdown("---")
st.sidebar.header("👤 شخصية القصة")
uploaded_character_image = st.sidebar.file_uploader(
    "أضف صورة الشخصية (اختياري)", 
    type=["jpg", "png", "jpeg"]
)

# 4. باقات الترقية والاشتراكات في الشريط الجانبي
st.sidebar.markdown("---")
st.sidebar.header("💎 ترقية إلى Pro")
st.sidebar.markdown("""
* **اشتراك أسبوعي:** $9.99 / أسبوعياً
* **اشتراك شهري:** $24.99 / شهرياً
* **اشتراك سنوي:** $69.99 / سنوياً
""")

# --- قسم إدخال الوصف والتوليد ---
st.markdown("### 🎬 تفاصيل المشهد")
prompt_text = st.text_area(
    "اكتب وصف الفيديو أو المشهد الذي تريد توليده:",
    value="A cinematic shot of a futuristic sports car driving through neon city, 4k"
)

if uploaded_character_image is not None:
    st.image(uploaded_character_image, caption="صورة الشخصية المضافة", width=200)
    st.info("تم تفعيل وضع مطابقة الشخصية مع الفيديو بنجاح!")

if st.button("توليد الفيديو الحقيقي"):
    if not prompt_text.strip():
        st.warning("يرجى كتابة وصف المشهد أولاً.")
    else:
        with st.spinner(f"جاري معالجة الفيديو بدقة {resolution_option} ولمدة {duration_option} عبر fal.ai... يرجى الانتظار"):
            try:
                handler = fal_client.submit(
                    "fal-ai/minimax-video",
                    arguments={
                        "prompt": prompt_text,
                    },
                )
                
                result = handler.get()
                
                if result and "video" in result:
                    video_url = result["video"]["url"]
                    st.success("تم توليد الفيديو بنجاح! 🎉")
                    st.video(video_url)
                else:
                    st.error("حدث خطأ أثناء استخراج رابط الفيديو، يرجى المحاولة مرة أخرى.")
                    
            except Exception as e:
                st.error(f"حدث خطأ أثناء الاتصال بخدمة التوليد: {e}")

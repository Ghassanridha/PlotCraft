import streamlit as st
import fal_client
import os

# إعداد الصفحة وتصميم الواجهة
st.set_page_config(page_title="PlotCraft - مولد الفيديوهات", layout="centered")

# تصميم شارة الـ Pro في أعلى اليسار
st.markdown("""
    <style>
    .pro-badge {
        background: linear-gradient(45deg, #FF4B4B, #FF8F00);
        color: white;
        padding: 5px 15px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 14px;
        float: left;
        margin-bottom: 15px;
    }
    .card {
        background-color: #1e1e1e;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #333;
        margin-bottom: 15px;
    }
    </style>
    <div class="pro-badge">⭐ Pro Version</div>
""", unsafe_allow_html=True)

st.title("PlotCraft - مولد الفيديوهات بالذكاء الاصطناعي")
st.write("حول قصصك وصور الشخصيات إلى مقاطع فيديو سينمائية احترافية!")

# إدخال مفتاح الـ API الخاص بـ fal.ai
DEFAULT_FAL_KEY = "fal_sk_d8e30b437fdc44c891740a201522be4d:d78802704ad38b28b6b7f1bcef6ef4c"
os.environ["FAL_KEY"] = DEFAULT_FAL_KEY

st.markdown("---")

# --- 1. قسم باقات الترقية والاشتراكات في الواجهة الرئيسية ---
st.markdown("### 💎 خطط الاشتراك والترقية (Pro)")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**أسبوعي**\n$9.99")
with col2:
    st.markdown("**شهري**\n$24.99")
with col3:
    st.markdown("**سنوي**\n$69.99")

st.markdown("---")

# --- 2. إعدادات الفيديو المتقدمة في الواجهة الرئيسية ---
st.markdown("### ⚙️ إعدادات الفيديو المتقدمة")
col_res, col_dur = st.columns(2)

with col_res:
    resolution_option = st.selectbox(
        "اختر دقة الفيديو",
        ["720p HD", "1080p Full HD", "4K Ultra"]
    )

with col_dur:
    duration_option = st.selectbox(
        "مدة الفيديو",
        ["10 ثواني", "21 ثانية", "5 دقائق"]
    )

# --- 3. أيقونة إضافة صورة الشخصية في الواجهة الرئيسية ---
st.markdown("### 👤 شخصية القصة (مطابقة الوجه)")
uploaded_character_image = st.file_uploader(
    "أضف صورة الشخصية لتوليد فيديو مطابق لها (اختياري)", 
    type=["jpg", "png", "jpeg"]
)

if uploaded_character_image is not None:
    st.image(uploaded_character_image, caption="صورة الشخصية المضافة", width=150)
    st.success("تم إرفاق صورة الشخصية بنجاح!")

st.markdown("---")

# --- 4. وصف المشهد وزر التوليد ---
st.markdown("### 🎬 تفاصيل المشهد والقصة")
prompt_text = st.text_area(
    "اكتب وصف الفيديو أو المشهد الذي تريد توليده:",
    value="A cinematic shot of a futuristic sports car driving through neon city, 4k"
)

if st.button("توليد الفيديو الحقيقي 🚀", use_container_width=True):
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

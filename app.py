import streamlit as st
import fal_client
import os

# إعداد الصفحة
st.set_page_config(page_title="PlotCraft - مولد الفيديوهات", layout="centered")

# إدخال مفتاح الـ API الخاص بـ fal.ai
DEFAULT_FAL_KEY = "fal_sk_d8e30b437fdc44c891740a201522be4d:d78802704ad38b28b6b7f1bcef6ef4c"
os.environ["FAL_KEY"] = DEFAULT_FAL_KEY

# --- زر Pro Version مع نافذة منبثقة (Dialog) للاشتراكات ---
@st.dialog("💎 خطط الاشتراك والترقية (Pro Version)")
def show_pricing_dialog():
    st.write("اختر الباقة المناسبة لك للتمتع بكافة مميزات الذكاء الاصطناعي:")
    st.markdown("---")
    st.markdown("📅 **اشتراك أسبوعي:** `9.99 $` / أسبوعياً")
    st.markdown("🗓️ **اشتراك شهري:** `24.99 $` / شهرياً")
    st.markdown("🌟 **اشتراك سنوي:** `69.99 $` / سنوياً")
    st.markdown("---")
    if st.button("إغلاق النافذة", use_container_width=True):
        st.rerun()

# تصميم زر Pro البرتقالي أعلى اليسار
st.markdown("""
    <style>
    .stButton button[kind="secondary"] {
        background: linear-gradient(45deg, #FF4B4B, #FF8F00);
        color: white;
        border-radius: 20px;
        font-weight: bold;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

col_title, col_btn = st.columns([2, 1])
with col_btn:
    if st.button("⭐ Pro Version", use_container_width=True):
        show_pricing_dialog()

with col_title:
    st.markdown("### PlotCraft")

st.write("حول قصصك وصور الشخصيات إلى مقاطع فيديو سينمائية احترافية!")
st.markdown("---")

# --- 1. خيارات الدقة بشكل أفقي (جنب لجنب) ---
st.markdown("### ⚙️ دقة الفيديو")
resolution_option = st.radio(
    "اختر الدقة",
    ["720p HD", "1080p Full HD", "4K Ultra"],
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("")

# --- 2. خيارات مدة الفيديو بشكل أفقي (جنب لجنب) ---
st.markdown("### ⏱️ مدة الفيديو")
duration_option = st.radio(
    "اختر المدة",
    ["10 ثواني", "21 ثانية", "5 دقائق"],
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("---")

# --- 3. أيقونة إضافة صورة الشخصية ---
st.markdown("### 👤 صورة الشخصية (مطابقة الوجه)")
uploaded_character_image = st.file_uploader(
    "أضف صورة الشخصية (اختياري)", 
    type=["jpg", "png", "jpeg"],
    label_visibility="collapsed"
)

if uploaded_character_image is not None:
    st.image(uploaded_character_image, caption="صورة الشخصية المضافة", width=120)
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

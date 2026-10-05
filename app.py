import streamlit as st
import streamlit.components.v1 as components

# إعداد صفحة ستريمليت لإزالة الهوامش واستغلال الشاشة بالكامل
st.set_page_config(page_title="PlotCraft UI", layout="wide", initial_sidebar_state="collapsed")

# إزالة هوامش وتداخلات صفحة ستريمليت الافتراضية للجوال
st.markdown("""
    <style>
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

html_part1 = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>PlotCraft UI</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }
        body, html {
            width: 100%;
            height: 100%;
            background-color: #0b0f19;
            overflow-x: hidden;
        }
        .screen-view {
            display: none;
            width: 100%;
            min-height: 100vh;
            background-color: #0b0f19;
            flex-direction: column;
            padding-bottom: 90px;
        }
        .screen-view.active {
            display: flex;
        }
        .hero-box {
            position: relative;
            width: 100%;
            min-height: 52vh;
            background: linear-gradient(180deg, rgba(11,15,25,0.2) 0%, rgba(11,15,25,0.8) 75%, #0b0f19 100%),
                        url('https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=1080&auto=format&fit=crop') center/cover no-repeat;
            border-bottom-left-radius: 35px;
            border-bottom-right-radius: 35px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 24px 20px 20px 20px;
        }
        .top-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
        }
        .brand-title {
            color: #ffffff;
            font-size: 20px;
            font-weight: 700;
        }
        .upgrade-badge {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            padding: 8px 16px;
            border-radius: 25px;
            color: #ffffff;
            font-size: 14px;
            font-weight: 500;
            display: flex;
            align-items: center;
            gap: 6px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            cursor: pointer;
        }
        .welcome-section {
            text-align: right;
            margin-top: 15px;
        }
        .welcome-section h1 {
            color: #ffffff;
            font-size: 22px;
            font-weight: 700;
            line-height: 1.4;
            text-shadow: 0 2px 8px rgba(0,0,0,0.6);
        }
        .cards-row {
            display: flex;
            gap: 12px;
            width: 100%;
            margin-top: 20px;
        }
        .interactive-card {
            flex: 1;
            background: rgba(20, 25, 40, 0.65);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 18px;
            padding: 16px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            cursor: pointer;
        }
        .card-header-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 6px;
        }
        .card-title {
            color: #ffffff;
            font-size: 16px;
            font-weight: 700;
        }
        .card-subtitle {
            color: #94a3b8;
            font-size: 12px;
        }
        .card-title-group-left {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
        }
        .inspiration-section {
            padding: 24px 20px;
        }
        .section-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
        }
        .section-title {
            color: #ffffff;
            font-size: 18px;
            font-weight: 700;
        }
        .view-all {
            color: #94a3b8;
            font-size: 13px;
        }
        .movies-carousel {
            display: flex;
            flex-direction: row-reverse;
            gap: 14px;
            overflow-x: auto;
            padding-bottom: 10px;
            scrollbar-width: none;
        }
        .movie-card {
            min-width: 130px;
            height: 190px;
            border-radius: 16px;
            overflow: hidden;
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            padding: 14px;
            border: 1px solid rgba(255,255,255,0.05);
        }
        .movie-card.m1 { background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), url('https://images.unsplash.com/photo-1534447677768-be436bb09401?q=80&w=300&auto=format&fit=crop') center/cover; }
        .movie-card.m2 { background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), url('https://images.unsplash.com/photo-1485846234645-a62644f84728?q=80&w=300&auto=format&fit=crop') center/cover; }
        .movie-card.m3 { background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), url('https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?q=80&w=300&auto=format&fit=crop') center/cover; }
        .movie-title {
            color: #ffffff;
            font-size: 10px;
            font-weight: 700;
            line-height: 1.2;
        }
    </style>
</head>
<body>
    <div id="homeScreen" class="screen-view active">
        <div class="hero-box">
            <div class="top-header">
                <div class="brand-title">PlotCraft</div>
                <div class="upgrade-badge" onclick="switchScreen('subscriptionScreen')">
                    <span>⭐</span> ترقية
                </div>
            </div>
            <div class="welcome-section">
                <h1>مساء الخير، أيها المخرج<br>أي قصة سنصنع اليوم؟</h1>
            </div>
            <div class="cards-row">
                <div class="interactive-card" onclick="switchScreen('stepByStepScreen')">
                    <div class="card-header-row">
                        <div class="card-title-group-left">
                            <div class="card-title">خطوة بخطوة</div>
                        </div>
                    </div>
                    <div class="card-subtitle">راجع كل خطوة</div>
                </div>
                <div class="interactive-card" onclick="switchScreen('subscriptionScreen')">
                    <div class="card-header-row">
                        <div class="card-title-group-left">
                            <div class="card-title">سريع</div>
                        </div>
                    </div>
                    <div class="card-subtitle">إدخال واحد، فيديو كامل</div>
                </div>
            </div>
        </div>
        <div class="inspiration-section">
            <div class="section-header">
                <div class="section-title">إلهام بلوت كرافت</div>
                <div class="view-all">عرض الكل ></div>
            </div>
            <div class="movies-carousel">
                <div class="movie-card m1"><div class="movie-title">THE DELIVERYMAN'S SECRET BILLIONAIRE</div></div>
                <div class="movie-card m2"><div class="movie-title">SECRET BILLIONAIRE</div></div>
                <div class="movie-card m3"><div class="movie-title">CYBER CITY</div></div>
            </div>
        </div>
    </div>
"""

html_part2 = """
    <div id="stepByStepScreen" class="screen-view">
        <div class="page-header" style="display:flex; align-items:center; justify-content:space-between; padding:20px; border-bottom:1px solid rgba(255,255,255,0.08); background:rgba(11, 15, 25, 0.75);">
            <button class="back-btn" onclick="switchScreen('homeScreen')">✕</button>
            <div class="page-title-text" style="color:#fff; font-weight:700;">خطوة بخطوة</div>
            <div style="width: 36px;"></div>
        </div>
        <div class="step-container" style="padding: 20px; display: flex; flex-direction: column; gap: 16px;">
            <div style="background: #141824; border: 1px solid #1e293b; border-radius: 16px; padding: 16px;">
                <div style="color: #ff2a85; font-size: 14px; font-weight: 700; margin-bottom: 8px;">مساعد AI بلوت كرافت</div>
                <div style="color: #94a3b8; font-size: 12px; line-height: 1.5;">عزيزي المخرج، استمتع بإنشاء وتخصيص تفاصيل فيلمك خطوة بخطوة.</div>
            </div>
        </div>
    </div>

    <div id="subscriptionScreen" class="screen-view">
        <div style="position: relative; width: 100%; height: 220px; overflow: hidden; border-bottom-left-radius: 30px; border-bottom-right-radius: 30px; display: flex; flex-direction: column; justify-content: space-between;">
            <video autoplay muted loop playsinline style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; z-index: 1; opacity: 0.65;">
                <source src="https://assets.mixkit.co/videos/preview/mixkit-digital-animation-of-screens-with-lights-31955-large.mp4" type="video/mp4">
            </video>
            <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(180deg, rgba(11,15,25,0.2) 0%, rgba(11,15,25,0.85) 90%, #0b0f19 100%); z-index: 2;"></div>
            
            <div style="position: relative; z-index: 3; padding: 16px 20px; display: flex; flex-direction: column; justify-content: space-between; height: 100%;">
                <div style="display: flex; align-items: center; justify-content: space-between; width: 100%;">
                    <button onclick="switchScreen('homeScreen')" style="background: rgba(255,255,255,0.15); border: none; color: #fff; width: 36px; height: 36px; border-radius: 50%; cursor: pointer; display: flex; align-items: center; justify-content: center;">✕</button>
                    <div style="color: #ffffff; font-size: 18px; font-weight: 700;">ترقية الحساب</div>
                    <div style="width: 36px;"></div>
                </div>
                <div style="text-align: center; margin-bottom: 10px;">
                    <div style="color: #ffffff; font-size: 18px; font-weight: 700; margin-bottom: 4px;">حول أفكارك إلى PlotCraft</div>
                    <div style="color: #cbd5e1; font-size: 12px;">أنشئ كل لقطة وعدلها وأكملها بسرعة.</div>
                </div>
            </div>
        </div>

        <div style="padding: 20px; display: flex; flex-direction: column; gap: 16px; position: relative; z-index: 2;">
            <div style="display: flex; flex-direction: column; gap: 12px;">
                <div onclick="selectPlan(this)" style="background: rgba(20, 25, 40, 0.85); border: 1.5px solid rgba(255, 255, 255, 0.15); border-radius: 16px; padding: 16px; cursor: pointer;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <div style="color: #ffffff; font-size: 15px; font-weight: 700;">PlotCraft Pro Weekly</div>
                        <div style="background: rgba(255, 255, 255, 0.12); padding: 4px 10px; border-radius: 10px; color: #ffffff; font-size: 12px;">9.99 دولار / أسبوع</div>
                    </div>
                    <div style="color: #94a3b8; font-size: 12px;">500 ساعة معتمدة / أسبوعياً</div>
                </div>
                
                <div onclick="selectPlan(this)" style="background: rgba(20, 25, 40, 0.85); border: 1.5px solid rgba(255, 255, 255, 0.15); border-radius: 16px; padding: 16px; cursor: pointer; position: relative;">
                    <div style="position: absolute; top: 12px; left: 12px; background: #3b82f6; color: #fff; font-size: 10px; padding: 2px 8px; border-radius: 8px;">جديد</div>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <div style="color: #ffffff; font-size: 15px; font-weight: 700;">PlotCraft Pro Monthly</div>
                        <div style="background: rgba(255, 255, 255, 0.12); padding: 4px 10px; border-radius: 10px; color: #ffffff; font-size: 12px;">29.99 دولار / شهر</div>
                    </div>
                    <div style="color: #94a3b8; font-size: 12px;">1800 نقطة / شهرياً</div>
                </div>
            </div>

            <button onclick="alert('تم اختيار الاشتراك بنجاح!')" style="width: 100%; background: linear-gradient(135deg, #ff5722 0%, #ff9800 100%); color: #ffffff; font-size: 15px; font-weight: 700; padding: 14px; border-radius: 20px; border: none; cursor: pointer; text-align: center; margin-top: 10px;">اشتراك</button>
        </div>
    </div>

    <div style="position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0b0f19; padding: 10px 15px; display: flex; justify-content: center; align-items: center; z-index: 999999; direction: rtl;">
        <div style="background-color: #161b22; border: 1px solid #30363d; border-radius: 35px; display: flex; justify-content: space-around; align-items: center; padding: 8px 15px; flex-grow: 1; max-width: 380px;">
            <a href="#" onclick="switchScreen('homeScreen')" style="color: #ffffff; font-size: 13px; text-decoration: none; font-weight: bold;">الرئيسية</a>
            <a href="#" onclick="switchScreen('subscriptionScreen')" style="color: #8b949e; font-size: 13px; text-decoration: none;">الترقية</a>
        </div>
    </div>

    <script>
        function switchScreen(screenId) {
            var screens = document.querySelectorAll('.screen-view');
            screens.forEach(s => s.classList.remove('active'));
            document.getElementById(screenId).classList.add('active');
            window.scrollTo(0, 0);
        }
        function selectPlan(element) {
            var cards = document.querySelectorAll('[onclick="selectPlan(this)"]');
            cards.forEach(c => c.style.borderColor = "rgba(255, 255, 255, 0.15)");
            element.style.borderColor = "#ff5722";
        }
    </script>
</body>
</html>
"""

# دمج الأجزاء وعرضها داخل تطبيق ستريمليت بشكل آمن تماماً
full_html = html_part1 + html_part2
components.html(full_html, height=750, scrolling=True)

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

# كود HTML و CSS مع إضافة الأيقونة بجانب بطاقة "خطوة بخطوة"
html_code = """
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
            overflow: hidden;
        }

        .mobile-screen {
            width: 100vw;
            height: 100vh;
            background-color: #0b0f19;
            position: relative;
            display: flex;
            flex-direction: column;
            overflow-y: auto;
            overflow-x: hidden;
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
        }

        .card-header-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 6px;
        }

        .card-title-group {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .card-title {
            color: #ffffff;
            font-size: 16px;
            font-weight: 700;
        }

        /* تصميم أيقونة الروبوت الجديدة داخل بطاقة خطوة بخطوة */
        .step-bot-icon {
            width: 22px;
            height: 22px;
            background: #cbd5e1;
            mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20 9V7c0-1.1-.9-2-2-2h-3c0-1.7-1.3-3-3-3S9 3.3 9 5H6c-1.1 0-2 .9-2 2v2c-1.7 0-3 1.3-3 3s1.3 3 3 3v2c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2v-2c1.7 0 3-1.3 3-3s-1.3-3-3-3zm-11 5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zm6 0c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"/></svg>') no-repeat center;
            -webkit-mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20 9V7c0-1.1-.9-2-2-2h-3c0-1.7-1.3-3-3-3S9 3.3 9 5H6c-1.1 0-2 .9-2 2v2c-1.7 0-3 1.3-3 3s1.3 3 3 3v2c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2v-2c1.7 0 3-1.3 3-3s-1.3-3-3-3zm-11 5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zm6 0c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"/></svg>') no-repeat center;
            background-size: contain;
        }

        .card-subtitle {
            color: #94a3b8;
            font-size: 12px;
            font-weight: 400;
        }

        .pro-badge-small {
            background: rgba(255, 255, 255, 0.2);
            padding: 3px 8px;
            border-radius: 8px;
            color: #ffffff;
            font-size: 10px;
            font-weight: 600;
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

        .movies-carousel::-webkit-scrollbar {
            display: none;
        }

        .movie-card {
            min-width: 130px;
            height: 190px;
            background: #1a2236;
            border-radius: 16px;
            overflow: hidden;
            position: relative;
            box-shadow: 0 4px 12px rgba(0,0,0,0.4);
            border: 1px solid rgba(255,255,255,0.05);
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            padding: 14px;
        }

        .movie-card.m1 {
            background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), 
                        url('https://images.unsplash.com/photo-1534447677768-be436bb09401?q=80&w=300&auto=format&fit=crop') center/cover;
        }

        .movie-card.m2 {
            background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), 
                        url('https://images.unsplash.com/photo-1485846234645-a62644f84728?q=80&w=300&auto=format&fit=crop') center/cover;
        }

        .movie-card.m3 {
            background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), 
                        url('https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?q=80&w=300&auto=format&fit=crop') center/cover;
        }

        .movie-title {
            color: #ffffff;
            font-size: 10px;
            font-weight: 700;
            text-shadow: 0 2px 4px rgba(0,0,0,0.8);
            line-height: 1.2;
        }

        .bottom-nav-container {
            position: sticky;
            bottom: 0;
            width: 100%;
            background: #0b0f19;
            padding: 10px 15px 15px 15px;
            display: flex;
            gap: 10px;
            align-items: center;
            margin-top: auto;
        }

        .nav-group-box {
            flex: 1;
            background: rgba(20, 25, 40, 0.85);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 22px;
            padding: 6px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .nav-item-text {
            color: #94a3b8;
            font-size: 13px;
            padding: 10px 14px;
            border-radius: 16px;
            cursor: pointer;
            text-align: center;
            flex: 1;
        }

        .nav-item-text.active {
            background: rgba(255, 255, 255, 0.15);
            color: #ffffff;
            font-weight: 600;
        }

        .nav-single-box {
            width: 52px;
            height: 52px;
            background: rgba(20, 25, 40, 0.85);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 18px;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
            cursor: pointer;
        }

        .custom-movie-icon {
            width: 24px;
            height: 24px;
            background: #94a3b8;
            mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M18 4H6c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm-9 11V9l6 3-6 3z"/></svg>') no-repeat center;
            -webkit-mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M18 4H6c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm-9 11V9l6 3-6 3z"/></svg>') no-repeat center;
            background-size: contain;
        }

        .custom-sparkle {
            position: absolute;
            top: 6px;
            left: 6px;
            width: 14px;
            height: 14px;
            background: #3b82f6;
            mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 0l3.5 8.5L24 12l-8.5 3.5L12 24l-3.5-8.5L0 12l8.5-3.5z"/></svg>') no-repeat center;
            -webkit-mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 0l3.5 8.5L24 12l-8.5 3.5L12 24l-3.5-8.5L0 12l8.5-3.5z"/></svg>') no-repeat center;
            background-size: contain;
        }
    </style>
</head>
<body>

    <div class="mobile-screen">
        <div class="hero-box">
            <div class="top-header">
                <div class="brand-title">بلوت كرافت</div>
                <div class="upgrade-badge">
                    <span>⭐</span> ترقية
                </div>
            </div>

            <div class="welcome-section">
                <h1>مساء الخير، أيها المخرج<br>أي قصة سنصنع اليوم؟</h1>
            </div>

            <div class="cards-row">
                <!-- بطقة خطوة بخطوة مع الأيقونة الجديدة بجانب العنوان -->
                <div class="interactive-card">
                    <div class="card-header-row">
                        <div class="card-title-group">
                            <span class="step-bot-icon"></span>
                            <div class="card-title">خطوة بخطوة</div>
                        </div>
                    </div>
                    <div class="card-subtitle">راجع كل خطوة</div>
                </div>

                <div class="interactive-card">
                    <div class="card-header-row">
                        <div class="card-title">سريع</div>
                        <div class="pro-badge-small">Pro only</div>
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
                <div class="movie-card m1">
                    <div class="movie-title">THE DELIVERYMAN'S SECRET BILLIONAIRE</div>
                </div>
                <div class="movie-card m2">
                    <div class="movie-title">SECRET BILLIONAIRE</div>
                </div>
                <div class="movie-card m3">
                    <div class="movie-title">CYBER CITY</div>
                </div>
            </div>
        </div>

        <div class="bottom-nav-container">
            <div class="nav-group-box">
                <div class="nav-item-text active">الصفحة الرئيسية</div>
                <div class="nav-item-text">الأدوات</div>
                <div class="nav-item-text">الأعمال</div>
            </div>

            <div class="nav-single-box">
                <span class="custom-sparkle"></span>
                <span class="custom-movie-icon"></span>
            </div>
        </div>
    </div>

</body>
</html>
"""

components.html(html_code, height=750, scrolling=True)

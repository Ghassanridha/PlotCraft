import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="بلوت كرافت", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0 !important; margin: 0 !important;}
    </style>
""", unsafe_allow_html=True)

app_html = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PlotCraft</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');
        
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Cairo', sans-serif;
        }
        
        body {
            background-color: #0b0c10;
            color: #ffffff;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
        }
        
        .mobile-screen {
            width: 100%;
            max-width: 390px;
            height: 810px;
            background-color: #0b0c10;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            box-shadow: 0 0 30px rgba(0,0,0,0.8);
            border-radius: 30px;
            border: 1px solid #1f222e;
            padding: 12px 0;
        }
        
        /* الهيدر العلوي */
        .top-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 18px;
        }
        
        .app-brand {
            font-size: 16px;
            font-weight: 700;
            color: #ffffff;
        }
        
        .upgrade-btn {
            background-color: rgba(255, 255, 255, 0.08);
            color: #ffffff;
            font-size: 11px;
            font-weight: 600;
            padding: 5px 12px;
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.12);
            display: flex;
            align-items: center;
            gap: 5px;
        }
        
        /* قسم البطل */
        .hero-box {
            position: relative;
            margin: 6px 16px;
            border-radius: 22px;
            overflow: hidden;
            padding: 20px 18px;
            background-image: linear-gradient(to bottom, rgba(11, 12, 16, 0.35), rgba(11, 12, 16, 0.96)), 
                              url('https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=800&auto=format&fit=crop');
            background-size: cover;
            background-position: center;
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        
        .hero-text {
            text-align: right;
            margin-bottom: 16px;
        }
        
        .hero-subtitle {
            color: #cfd0d5;
            font-size: 13.5px;
            font-weight: 400;
            margin-bottom: 2px;
        }
        
        .hero-title {
            color: #ffffff;
            font-size: 20px;
            font-weight: 700;
            line-height: 1.3;
        }
        
        /* البطاقتان: خطوة بخطوة يمين، سريع يسار */
        .cards-row {
            display: flex;
            gap: 10px;
        }
        
        .card-item {
            flex: 1;
            background: rgba(18, 20, 28, 0.75);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 14px;
            padding: 12px;
            position: relative;
            text-align: right;
        }
        
        .card-item.right-card {
            order: 1; /* خطوة بخطوة في اليمين */
        }
        
        .card-item.left-card {
            order: 2; /* سريع في اليسار */
        }
        
        .pro-tag {
            position: absolute;
            top: 8px;
            left: 8px;
            background: rgba(255, 255, 255, 0.12);
            font-size: 8.5px;
            font-weight: 600;
            padding: 2px 5px;
            border-radius: 5px;
            color: #cccccc;
        }
        
        .card-icon {
            font-size: 16px;
            margin-bottom: 6px;
            display: inline-block;
        }
        
        .card-heading {
            font-size: 13.5px;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 2px;
        }
        
        .card-subtext {
            font-size: 10px;
            color: #9e9fa6;
            line-height: 1.2;
        }
        
        /* عنوان قسم الإلهام */
        .section-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 18px;
        }
        
        .section-name {
            font-size: 15px;
            font-weight: 700;
            color: #ffffff;
        }
        
        .section-action {
            font-size: 12px;
            color: #888990;
            font-weight: 600;
        }
        
        /* قائمة الأفلام */
        .movies-container {
            display: flex;
            gap: 10px;
            padding: 0 16px;
            direction: rtl;
            justify-content: space-between;
        }
        
        .movie-card {
            width: 31%;
            height: 175px;
            border-radius: 12px;
            overflow: hidden;
            position: relative;
            border: 1px solid rgba(255, 255, 255, 0.08);
            background-color: #151720;
            flex-shrink: 0;
        }
        
        .movie-card img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        
        .movie-title-box {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            padding: 8px 4px;
            background: linear-gradient(to top, rgba(0,0,0,0.95) 15%, transparent 100%);
            font-size: 9px;
            font-weight: 700;
            text-align: center;
            color: #ffffff;
            letter-spacing: 0.3px;
        }
        
        /* الشريط السفلي الثابت */
        .bottom-nav-wrapper {
            padding: 0 16px;
            width: 100%;
        }
        
        .nav-inner {
            background-color: #151720;
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 40px;
            padding: 5px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 10px 25px rgba(0,0,0,0.8);
        }
        
        .nav-button {
            flex: 1;
            text-align: center;
            color: #888990;
            font-size: 11px;
            font-weight: 600;
            padding: 7px 4px;
        }
        
        .nav-button-active {
            flex: 1;
            text-align: center;
            background-color: #ffffff;
            color: #121318;
            font-size: 11px;
            font-weight: 700;
            padding: 7px 6px;
            border-radius: 30px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.3);
        }
    </style>
</head>
<body>

    <div class="mobile-screen">
        
        <!-- الهيدر العلوي -->
        <div class="top-header">
            <div class="app-brand">بلوت كرافت</div>
            <div class="upgrade-btn">
                <span>✦</span> ترقية
            </div>
        </div>

        <!-- قسم البطل -->
        <div class="hero-box">
            <div class="hero-text">
                <div class="hero-subtitle">مساء الخير، أيها المخرج</div>
                <div class="hero-title">أي قصة سنصنع اليوم؟</div>
            </div>
            
            <div class="cards-row">
                <!-- بطاقة خطوة بخطوة (يمين)[span_1](start_span)[span_1](end_span) -->
                <div class="card-item right-card">
                    <div class="card-icon">💬</div>
                    <div class="card-heading">خطوة بخطوة</div>
                    <div class="card-subtext">راجع كل خطوة</div>
                </div>
                
                <!-- بطاقة سريع (يسار)[span_2](start_span)[span_2](end_span) -->
                <div class="card-item left-card">
                    <div class="pro-tag">Pro only</div>
                    <div class="card-icon">🪄</div>
                    <div class="card-heading">سريع</div>
                    <div class="card-subtext">إدخال واحد، فيديو كامل</div>
                </div>
            </div>
        </div>

        <!-- عنوان قسم الإلهام -->
        <div class="section-header">
            <div class="section-name">إلهام بلوت كرافت</div>
            <div class="section-action">عرض الكل &gt;</div>
        </div>

        <!-- قائمة الأفلام -->
        <div class="movies-container">
            <div class="movie-card">
                <img src="https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=400&auto=format&fit=crop">
                <div class="movie-title-box">SECRET BILLIONAIRE</div>
            </div>
            <div class="movie-card">
                <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=400&auto=format&fit=crop">
                <div class="movie-title-box">THE WRONG DOOR</div>
            </div>
            <div class="movie-card">
                <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=400&auto=format&fit=crop">
                <div class="movie-title-box">INVITATION</div>
            </div>
        </div>

        <!-- الشريط السفلي الثابت -->
        <div class="bottom-nav-wrapper">
            <div class="nav-inner">
                <div class="nav-button">الصفحة الرئيسية</div>
                <div class="nav-button">الأعمال</div>
                <div class="nav-button-active">الأدوات</div>
            </div>
        </div>

    </div>

</body>
</html>
"""

components.html(app_html, height=830, scrolling=False)

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
            min-height: 100vh;
        }
        
        .mobile-screen {
            width: 100%;
            max-width: 400px;
            height: 840px;
            background-color: #0b0c10;
            position: relative;
            overflow-y: auto;
            overflow-x: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            box-shadow: 0 0 30px rgba(0,0,0,0.8);
            border-radius: 30px;
            border: 1px solid #1f222e;
        }
        
        .mobile-screen::-webkit-scrollbar {
            display: none;
        }
        
        /* الهيدر العلوي: ترقية يمين، اسم التطبيق والشعار يسار */
        .top-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 18px 20px 10px 20px;
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
        
        .app-brand {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 16px;
            font-weight: 700;
        }
        
        .brand-logo {
            width: 22px;
            height: 22px;
            background: #222530;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        .brand-logo svg {
            width: 12px;
            height: 12px;
            fill: #fff;
        }
        
        /* قسم البطل */
        .hero-box {
            position: relative;
            margin: 10px 16px;
            border-radius: 24px;
            overflow: hidden;
            padding: 24px 20px;
            background-image: linear-gradient(to bottom, rgba(11, 12, 16, 0.35), rgba(11, 12, 16, 0.96)), 
                              url('https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=800&auto=format&fit=crop');
            background-size: cover;
            background-position: center;
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        
        .hero-text {
            text-align: right;
            margin-bottom: 22px;
        }
        
        .hero-subtitle {
            color: #cfd0d5;
            font-size: 14px;
            font-weight: 400;
            margin-bottom: 4px;
        }
        
        .hero-title {
            color: #ffffff;
            font-size: 21px;
            font-weight: 700;
            line-height: 1.3;
        }
        
        /* البطاقتان: سريع يمين، خطوة بخطوة يسار */
        .cards-row {
            display: flex;
            gap: 12px;
        }
        
        .card-item {
            flex: 1;
            background: rgba(18, 20, 28, 0.75);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 14px;
            position: relative;
            text-align: right;
        }
        
        .card-item.right-card {
            order: 1;
        }
        
        .card-item.left-card {
            order: 2;
        }
        
        .pro-tag {
            position: absolute;
            top: 10px;
            left: 10px;
            background: rgba(255, 255, 255, 0.12);
            font-size: 9px;
            font-weight: 600;
            padding: 2px 6px;
            border-radius: 6px;
            color: #cccccc;
        }
        
        .card-icon {
            font-size: 18px;
            margin-bottom: 8px;
            display: inline-block;
        }
        
        .card-heading {
            font-size: 14px;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 3px;
        }
        
        .card-subtext {
            font-size: 10.5px;
            color: #9e9fa6;
            line-height: 1.25;
        }
        
        /* عنوان قسم الإلهام: إلهام بلوت كرافت يمين، عرض الكل يسار */
        .section-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 20px 10px 20px;
        }
        
        .section-name {
            font-size: 16px;
            font-weight: 700;
            color: #ffffff;
        }
        
        .section-action {
            font-size: 12.5px;
            color: #888990;
            font-weight: 600;
        }
        
        /* قائمة الأفلام الأفقية */
        .movies-container {
            display: flex;
            gap: 12px;
            overflow-x: auto;
            padding: 0 16px 15px 16px;
            scrollbar-width: none;
            direction: rtl;
        }
        
        .movies-container::-webkit-scrollbar {
            display: none;
        }
        
        .movie-card {
            min-width: 125px;
            height: 195px;
            border-radius: 14px;
            overflow: hidden;
            position: relative;
            border: 1px solid rgba(255, 255, 255, 0.08);
            flex-shrink: 0;
            background-color: #151720;
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
            padding: 10px 8px;
            background: linear-gradient(to top, rgba(0,0,0,0.92) 15%, transparent 100%);
            font-size: 10px;
            font-weight: 700;
            text-align: center;
            color: #ffffff;
            letter-spacing: 0.5px;
        }
        
        /* الشريط السفلي */
        .bottom-nav-wrapper {
            position: sticky;
            bottom: 16px;
            left: 0;
            right: 0;
            padding: 0 16px;
            margin-top: auto;
            z-index: 100;
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
            padding: 8px 4px;
        }
        
        .nav-button-active {
            flex: 1;
            text-align: center;
            background-color: #ffffff;
            color: #121318;
            font-size: 11px;
            font-weight: 700;
            padding: 8px 6px;
            border-radius: 30px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.3);
        }
    </style>
</head>
<body>

    <div class="mobile-screen">
        
        <!-- الهيدر العلوي -->
        <div class="top-header">
            <div class="upgrade-btn">
                <span>✦</span> ترقية
            </div>
            <div class="app-brand">
                <span>بلوت كرافت</span>
                <div class="brand-logo">
                    <svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
                </div>
            </div>
        </div>

        <!-- قسم البطل -->
        <div class="hero-box">
            <div class="hero-text">
                <div class="hero-subtitle">مساء الخير، أيها المخرج</div>
                <div class="hero-title">أي قصة سنصنع اليوم؟</div>
            </div>
            
            <div class="cards-row">
                <!-- بطاقة سريع (يمين) -->
                <div class="card-item right-card">
                    <div class="pro-tag">Pro only</div>
                    <div class="card-icon">🪄</div>
                    <div class="card-heading">سريع</div>
                    <div class="card-subtext">إدخال واحد، فيديو كامل</div>
                </div>
                
                <!-- بطاقة خطوة بخطوة (يسار) -->
                <div class="card-item left-card">
                    <div class="card-icon">💬</div>
                    <div class="card-heading">خطوة بخطوة</div>
                    <div class="card-subtext">راجع كل خطوة</div>
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
                <div class="movie-title-box">THE DELIVERYMAN'S SECRET BILLIONAIRE</div>
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

        <!-- الشريط السفلي -->
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

components.html(app_html, height=860, scrolling=False)

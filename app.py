import streamlit as st
import streamlit.components.v1 as components

# إعداد صفحة ستريمليت لإزالة الهوامش واستغلال الشاشة بالكامل
st.set_page_config(page_title="PlotCraft UI", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        header {visibility: hidden;}
        #stDecoration {display: none;}
    </style>
""", unsafe_allow_html=True)

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
            overflow-x: hidden;
            color: #ffffff;
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

        /* --- واجهة الأعمال المطابقة للتعديلات المطلوبة --- */
        #worksScreen {
            background-color: #0b0f19;
            display: none;
            flex-direction: column;
            min-height: 100vh;
            padding: 20px;
            align-items: center;
        }
        #worksScreen.active {
            display: flex;
        }

        .works-top-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
            padding-bottom: 20px;
        }
        .works-title-header {
            font-size: 20px;
            font-weight: bold;
            text-align: right;
        }
        .works-upgrade-simple {
            background-color: #141824;
            color: #94a3b8;
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 13px;
            cursor: pointer;
        }

        .works-tabs-container {
            display: flex;
            background: #141824;
            border-radius: 30px;
            padding: 4px;
            width: 100%;
            max-width: 360px;
            margin-bottom: 80px;
            border: 1px solid rgba(255,255,255,0.08);
            direction: rtl;
        }

        .works-tab {
            flex: 1;
            text-align: center;
            padding: 10px 0;
            font-size: 13px;
            font-weight: 600;
            color: #94a3b8;
            border-radius: 25px;
            cursor: pointer;
            transition: 0.2s;
        }

        .works-tab.active {
            background: #252b3b;
            color: #ffffff;
        }

        .works-empty-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            flex-grow: 1;
            text-align: center;
            margin-top: 40px;
        }

        .works-box-icon {
            width: 90px;
            height: 90px;
            margin-bottom: 24px;
            opacity: 0.8;
            background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%2364748b" stroke-width="1.5"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg>') no-repeat center;
            background-size: contain;
        }

        .works-empty-text-sub {
            color: #64748b;
            font-size: 13px;
            margin-bottom: 35px;
        }

        /* زر إنشاء قصة (مستطيل صغير، أبيض على أسود غامق) */
        .works-create-btn-small {
            width: 100%;
            max-width: 220px;
            background-color: #ffffff;
            color: #000000;
            font-size: 13px;
            font-weight: 700;
            padding: 10px 16px;
            border-radius: 12px;
            border: none;
            cursor: pointer;
            text-align: center;
            margin: 0 auto;
            display: block;
            box-shadow: 0 2px 8px rgba(0,0,0,0.3);
        }
        .works-create-btn-small:active {
            transform: scale(0.97);
            background-color: #e2e8f0;
        }

        /* شريط التنقل السفلي */
        .bottom-nav {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 75px;
            background: #0f1523;
            border-top: 1px solid rgba(255,255,255,0.08);
            display: flex;
            justify-content: space-around;
            align-items: center;
            z-index: 1000;
            padding-bottom: 10px;
        }

        .nav-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: #64748b;
            font-size: 11px;
            cursor: pointer;
            gap: 4px;
            flex: 1;
        }

        .nav-item.active {
            color: #3b82f6;
        }

        .nav-icon {
            width: 22px;
            height: 22px;
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
        }
    </style>
</head>
<body>

    <!-- الشاشة الرئيسية -->
    <div id="homeScreen" class="screen-view active">
        <div class="hero-box">
            <div class="top-header">
                <div class="brand-title">PlotCraft</div>
                <div class="upgrade-badge">ترقية</div>
            </div>
            <div class="welcome-section">
                <h1>اصنع قصتك وفيديوهاتك بكل سهولة</h1>
            </div>
        </div>
    </div>

    <!-- شاشة الأعمال (تم تعديلها حسب طلبك بالكامل) -->
    <div id="worksScreen" class="screen-view">
        <div class="works-top-header">
            <div class="works-upgrade-simple">ترقية</div>
            <div class="works-title-header">الأعمال</div>
        </div>

        <!-- التبويبات: المشاريع باليمين، مكتبة الوسائط باليسار -->
        <div class="works-tabs-container">
            <div class="works-tab active" id="tabProjects" onclick="switchTab('projects')">المشاريع</div>
            <div class="works-tab" id="tabMedia" onclick="switchTab('media')">مكتبة الوسائط</div>
        </div>

        <div class="works-empty-content">
            <div class="works-box-icon"></div>
            <div class="works-empty-text-sub">ستظهر هنا مشاريعك الخاصة بك.</div>
            <button class="works-create-btn-small">إنشاء قصة</button>
        </div>
    </div>

    <!-- شريط التنقل السفلي -->
    <div class="bottom-nav">
        <div class="nav-item" onclick="switchScreen('home', this)">
            <div class="nav-icon" style="background: currentColor; mask: url('data:image/svg+xml;utf8,<svg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 24 24\' fill=\'none\' stroke=\'currentColor\' stroke-width=\'2\'><path d=\'M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z\'></path></svg>') no-repeat center; -webkit-mask: url('data:image/svg+xml;utf8,<svg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 24 24\' fill=\'none\' stroke=\'currentColor\' stroke-width=\'2\'><path d=\'M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z\'></path></svg>') no-repeat center;"></div>
            <span>الرئيسية</span>
        </div>
        <div class="nav-item active" onclick="switchScreen('works', this)">
            <div class="nav-icon" style="background: currentColor; mask: url('data:image/svg+xml;utf8,<svg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 24 24\' fill=\'none\' stroke=\'currentColor\' stroke-width=\'2\'><rect x=\'2\' y=\'7\' width=\'20\' height=\'14\' rx=\'2\' ry=\'2\'></rect><path d=\'M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16\'></path></svg>') no-repeat center; -webkit-mask: url('data:image/svg+xml;utf8,<svg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 24 24\' fill=\'none\' stroke=\'currentColor\' stroke-width=\'2\'><rect x=\'2\' y=\'7\' width=\'20\' height=\'14\' rx=\'2\' ry=\'2\'></rect><path d=\'M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16\'></path></svg>') no-repeat center;"></div>
            <span>الأعمال</span>
        </div>
    </div>

    <script>
        function switchScreen(screenName, element) {
            document.querySelectorAll('.screen-view').forEach(s => s.classList.remove('active'));
            document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
            
            if(screenName === 'home') {
                document.getElementById('homeScreen').classList.add('active');
            } else if(screenName === 'works') {
                document.getElementById('worksScreen').classList.add('active');
            }
            element.classList.add('active');
        }

        function switchTab(tabName) {
            document.getElementById('tabProjects').classList.remove('active');
            document.getElementById('tabMedia').classList.remove('active');
            if(tabName === 'projects') {
                document.getElementById('tabProjects').classList.add('active');
            } else {
                document.getElementById('tabMedia').classList.add('active');
            }
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=850, scrolling=False)

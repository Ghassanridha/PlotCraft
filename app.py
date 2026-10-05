import streamlit as st
import streamlit.components.v1 as components

# إعداد صفحة ستريمليت لملء الشاشة
st.set_page_config(page_title="PlotCraft UI", layout="centered", initial_sidebar_state="collapsed")

# كود HTML و CSS المصمم خصيصاً ليطابق أبعاد 1080 × 2340 بدقة تامة
html_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PlotCraft UI</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }

        body {
            background-color: #0b0f19;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
        }

        /* حاوية الهاتف بأبعاد 1080px عرض و 2340px ارتفاع */
        .mobile-screen {
            width: 1080px;
            height: 2340px;
            background-color: #0b0f19;
            position: relative;
            display: flex;
            flex-direction: column;
            overflow-y: auto;
            overflow-x: hidden;
            box-shadow: 0 0 50px rgba(0,0,0,0.8);
        }

        /* صندوق الخلفية العلوي الموحد (Hero Box) */
        .hero-box {
            position: relative;
            width: 100%;
            height: 1100px;
            background: linear-gradient(180deg, rgba(11,15,25,0.4) 0%, rgba(11,15,25,0.8) 70%, #0b0f19 100%),
                        url('https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=1080&auto=format&fit=crop') center/cover no-repeat;
            border-bottom-left-radius: 60px;
            border-bottom-right-radius: 60px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 70px 50px 60px 50px;
        }

        /* الشريط العلوي */
        .top-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
        }

        .upgrade-badge {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            padding: 16px 32px;
            border-radius: 40px;
            color: #ffffff;
            font-size: 28px;
            font-weight: 500;
            display: flex;
            align-items: center;
            gap: 12px;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .brand-title {
            color: #ffffff;
            font-size: 42px;
            font-weight: 700;
        }

        /* الترحيب */
        .welcome-section {
            text-align: right;
            margin-top: 100px;
        }

        .welcome-section h1 {
            color: #ffffff;
            font-size: 64px;
            font-weight: 700;
            line-height: 1.3;
            text-shadow: 0 4px 12px rgba(0,0,0,0.5);
        }

        /* صف البطاقتين داخل صندوق الخلفية في الأسفل تماماً */
        .cards-row {
            display: flex;
            gap: 30px;
            width: 100%;
            margin-top: auto;
        }

        .interactive-card {
            flex: 1;
            background: rgba(20, 25, 40, 0.65);
            backdrop-filter: blur(25px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 35px;
            padding: 40px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .interactive-card:hover {
            background: rgba(30, 38, 60, 0.8);
            border-color: rgba(255, 255, 255, 0.3);
        }

        .card-header-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }

        .card-title {
            color: #ffffff;
            font-size: 38px;
            font-weight: 700;
        }

        .card-subtitle {
            color: #94a3b8;
            font-size: 26px;
            font-weight: 400;
        }

        .pro-badge-small {
            background: rgba(255, 255, 255, 0.2);
            padding: 6px 16px;
            border-radius: 12px;
            color: #ffffff;
            font-size: 20px;
            font-weight: 600;
        }

        /* قسم الإلهام والأفلام */
        .inspiration-section {
            padding: 60px 50px;
            flex: 1;
        }

        .section-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 40px;
        }

        .section-title {
            color: #ffffff;
            font-size: 44px;
            font-weight: 700;
        }

        .view-all {
            color: #94a3b8;
            font-size: 30px;
            cursor: pointer;
        }

        .movies-carousel {
            display: flex;
            gap: 30px;
            overflow-x: auto;
            padding-bottom: 20px;
        }

        .movie-card {
            min-width: 310px;
            height: 460px;
            background: #1a2236;
            border-radius: 30px;
            overflow: hidden;
            position: relative;
            box-shadow: 0 10px 25px rgba(0,0,0,0.4);
            border: 1px solid rgba(255,255,255,0.05);
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            padding: 30px;
        }

        .movie-card.m1 {
            background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.8) 100%), 
                        url('https://images.unsplash.com/photo-1536440136628-849c177e76a1?q=80&w=400&auto=format&fit=crop') center/cover;
        }

        .movie-card.m2 {
            background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.8) 100%), 
                        url('https://images.unsplash.com/photo-1485846234645-a62644f84728?q=80&w=400&auto=format&fit=crop') center/cover;
        }

        .movie-card.m3 {
            background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.8) 100%), 
                        url('https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?q=80&w=400&auto=format&fit=crop') center/cover;
        }

        .movie-title {
            color: #ffffff;
            font-size: 28px;
            font-weight: 700;
            text-shadow: 0 2px 5px rgba(0,0,0,0.8);
        }

        /* شريط التنقل السفلي الثابت */
        .bottom-nav {
            position: sticky;
            bottom: 0;
            width: 100%;
            background: rgba(15, 22, 36, 0.95);
            backdrop-filter: blur(20px);
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            padding: 35px 50px;
            display: flex;
            justify-content: space-around;
            align-items: center;
        }

        .nav-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px;
            color: #64748b;
            font-size: 24px;
            cursor: pointer;
        }

        .nav-item.active {
            color: #ffffff;
        }

        .nav-icon {
            font-size: 36px;
        }
    </style>
</head>
<body>

    <div class="mobile-screen">
        <!-- صندوق الخلفية العلوي الموحد -->
        <div class="hero-box">
            <div class="top-header">
                <div class="upgrade-badge">
                    <span>⭐</span> ترقية
                </div>
                <div class="brand-title">بلوت كرافت</div>
            </div>

            <div class="welcome-section">
                <h1>مساء الخير، أيها المخرج<br>أي قصة سنصنع اليوم؟</h1>
            </div>

            <!-- البطاقتان في أسفل صندوق الخلفية تماماً -->
            <div class="cards-row">
                <div class="interactive-card">
                    <div class="card-header-row">
                        <div class="card-title">سريع</div>
                        <div class="pro-badge-small">Pro only</div>
                    </div>
                    <div class="card-subtitle">إدخال واحد، فيديو كامل</div>
                </div>

                <div class="interactive-card">
                    <div class="card-header-row">
                        <div class="card-title">خطوة بخطوة</div>
                    </div>
                    <div class="card-subtitle">راجع كل خطوة</div>
                </div>
            </div>
        </div>

        <!-- قسم إلهام بلوت كرافت -->
        <div class="inspiration-section">
            <div class="section-header">
                <div class="section-title">إلهام بلوت كرافت</div>
                <div class="view-all">عرض الكل ></div>
            </div>

            <div class="movies-carousel">
                <div class="movie-card m1">
                    <div class="movie-title">THE WRONG DOOR</div>
                </div>
                <div class="movie-card m2">
                    <div class="movie-title">SECRET BILLIONAIRE</div>
                </div>
                <div class="movie-card m3">
                    <div class="movie-title">CYBER CITY</div>
                </div>
            </div>
        </div>

        <!-- شريط التنقل السفلي -->
        <div class="bottom-nav">
            <div class="nav-item">
                <div class="nav-icon">🎬</div>
                <span>استوديو</span>
            </div>
            <div class="nav-item">
                <div class="nav-icon">📁</div>
                <span>الأعمال</span>
            </div>
            <div class="nav-item">
                <div class="nav-icon">⚙️</div>
                <span>الأدوات</span>
            </div>
            <div class="nav-item active">
                <div class="nav-icon">🏠</div>
                <span>الصفحة الرئيسية</span>
            </div>
        </div>
    </div>

</body>
</html>
"""

# عرض المكون داخل تطبيق Streamlit بالأبعاد المطلوبة 1080x2340
components.html(html_code, height=900, scrolling=True)

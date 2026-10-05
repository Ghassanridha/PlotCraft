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

# كود HTML و CSS مع شريط التنقل السفلي المطابق تماماً للصورة
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

        /* حاوية الهاتف تملأ شاشة الجوال بالكامل */
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

        /* صندوق الخلفية العلوي الموحد (Hero Box) مطابق للصورة الأصلية تماماً */
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

        /* الشريط العلوي */
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

        /* الترحيب */
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

        /* صف البطاقتين */
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

        .card-title {
            color: #ffffff;
            font-size: 16px;
            font-weight: 700;
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

        /* قسم الإلهام والأفلام */
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
                        url('https://images.unsplash.com/photo-1536440136628-849c177e76a1?q=80&w=300&auto=format&fit=crop') center/cover;
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
            font-size: 11px;
            font-weight: 700;
            text-shadow: 0 2px 4px rgba(0,0,0,0.8);
        }

        /* حاوية الشريط السفلي بالكامل */
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

        /* 1. المستطيل الكبير الذي يضم الثلاثة أزرار معاً */
        .nav-group-box {
            flex: 1;
            background: rgba(20, 25, 40, 0.85);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 24px;
            padding: 6px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        /* الأزرار داخل المستطيل الكبير */
        .nav-item-inner {
            display: flex;
            align-items: center;
            gap: 6px;
            color: #94a3b8;
            font-size: 13px;
            padding: 10px 14px;
            border-radius: 18px;
            cursor: pointer;
        }

        /* الزر النشط داخل المستطيل (الصفحة الرئيسية) */
        .nav-item-inner.active {
            background: rgba(255, 255, 255, 0.15);
            color: #ffffff;
            font-weight: 600;
        }

        /* 2. المربع الرابع المنفصل تماماً عنهم في أقصى اليسار */
        .nav-single-box {
            width: 52px;
            height: 52px;
            background: rgba(20, 25, 40, 0.85);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #94a3b8;
            cursor: pointer;
        }

        /* رسم الأيقونات بدقة متناهية مطابقة للصورة */
        .icon-home {
            width: 16px;
            height: 16px;
            display: inline-block;
            background: currentColor;
            mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>') no-repeat center;
            -webkit-mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>') no-repeat center;
        }

        .icon-tools {
            width: 16px;
            height: 16px;
            display: inline-block;
            background: currentColor;
            mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58c.18-.14.23-.41.12-.61l-1.92-3.32c-.12-.22-.37-.29-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54c-.04-.24-.24-.41-.48-.41h-3.84c-.24 0-.43.17-.47.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96c-.22-.08-.47 0-.59.22L2.74 8.87c-.12.21-.08.47.12.61l2.03 1.58c-.05.3-.09.63-.09.94s.02.64.07.94l-2.03 1.58c-.18.14-.23.41-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z"/></svg>') no-repeat center;
            -webkit-mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58c.18-.14.23-.41.12-.61l-1.92-3.32c-.12-.22-.37-.29-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54c-.04-.24-.24-.41-.48-.41h-3.84c-.24 0-.43.17-.47.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96c-.22-.08-.47 0-.59.22L2.74 8.87c-.12.21-.08.47.12.61l2.03 1.58c-.05.3-.09.63-.09.94s.02.64.07.94l-2.03 1.58c-.18.14-.23.41-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z"/></svg>') no-repeat center;
        }

        .icon-works {
            width: 16px;
            height: 16px;
            display: inline-block;
            background: currentColor;
            mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20 6h-8l-2-2H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm0 12H4V8h16v10z"/></svg>') no-repeat center;
            -webkit-mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20 6h-8l-2-2H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm0 12H4V8h16v10z"/></svg>') no-repeat center;
        }

        .icon-extra {
            width: 18px;
            height: 18px;
            display: inline-block;
            background: currentColor;
            mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg>') no-repeat center;
            -webkit-mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg>') no-repeat center;
        }
    </style>
</head>
<body>

    <div class="mobile-screen">
        <!-- صندوق الخلفية العلوي الموحد -->
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
                <div class="interactive-card">
                    <div class="card-header-row">
                        <div class="card-title">خطوة بخطوة</div>
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

        <!-- الشريط السفلي المطابق تماماً للصورة: مستطيل كبير للثلاثة أزرار ومربع منفصل رابع -->
        <div class="bottom-nav-container">
            <!-- 1. المستطيل الكبير الذي يضم 3 أزرار معاً -->
            <div class="nav-group-box">
                <!-- أقصى اليمين: الصفحة الرئيسية (نشطة) -->
                <div class="nav-item-inner active">
                    <span>الصفحة الرئيسية</span>
                    <span class="icon-home"></span>
                </div>
                <!-- في المنتصف: الأدوات -->
                <div class="nav-item-inner">
                    <span>الأدوات</span>
                    <span class="icon-tools"></span>
                </div>
                <!-- يسار المستطيل: الأعمال -->
                <div class="nav-item-inner">
                    <span>الأعمال</span>
                    <span class="icon-works"></span>
                </div>
            </div>

            <!-- 2. المربع الرابع المنفصل في أقصى اليسار -->
            <div class="nav-single-box">
                <span class="icon-extra"></span>
            </div>
        </div>
    </div>

</body>
</html>
"""

components.html(html_code, height=750, scrolling=True)

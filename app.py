import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="بلوت كرافت", page_icon="🎬", layout="centered")

# تنسيق التصميم بالكامل مطابق للصورة الأصلية
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stApp {
        background-color: #0b0c10;
        color: #ffffff;
        font-family: 'Cairo', sans-serif;
    }
    
    /* حاوية الجوال العامة */
    .mobile-container {
        max-width: 410px;
        margin: 0 auto;
        background-color: #0b0c10;
        min-height: 850px;
        position: relative;
        padding-bottom: 100px;
    }
    
    /* شريط العنوان العلوي */
    .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 20px;
    }
    
    .upgrade-btn {
        background-color: rgba(255, 255, 255, 0.1);
        color: #ffffff;
        font-size: 12px;
        padding: 5px 12px;
        border-radius: 20px;
        display: flex;
        align-items: center;
        gap: 5px;
        border: 1px solid rgba(255, 255, 255, 0.15);
    }
    
    .app-title {
        font-size: 16px;
        font-weight: bold;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    /* قسم التحية والخلفية */
    .hero-section {
        position: relative;
        border-radius: 24px;
        overflow: hidden;
        margin: 10px 16px;
        padding: 24px 20px;
        background-image: linear-gradient(to bottom, rgba(11, 12, 16, 0.3), rgba(11, 12, 16, 0.95)), 
                          url('https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=800&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .hero-text-container {
        text-align: right;
        margin-bottom: 25px;
    }
    
    .hero-subtitle {
        color: #cfd0d5;
        font-size: 15px;
        margin-bottom: 5px;
    }
    
    .hero-title {
        color: #ffffff;
        font-size: 22px;
        font-weight: bold;
    }
    
    /* البطوتان الصغيرتان في المنتصف */
    .options-row {
        display: flex;
        gap: 12px;
    }
    
    .option-card {
        flex: 1;
        background: rgba(20, 22, 30, 0.75);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 16px;
        padding: 14px;
        position: relative;
    }
    
    .pro-badge {
        position: absolute;
        top: 10px;
        left: 10px;
        background: rgba(255, 255, 255, 0.15);
        font-size: 9px;
        padding: 2px 6px;
        border-radius: 6px;
        color: #ddd;
    }
    
    .option-title {
        font-size: 15px;
        font-weight: bold;
        margin-bottom: 4px;
        text-align: right;
    }
    
    .option-desc {
        font-size: 11px;
        color: #aaaaaa;
        text-align: right;
        line-height: 1.3;
    }
    
    /* قسم إلهام بلوت كرافت */
    .section-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 20px;
        margin-top: 10px;
    }
    
    .section-title {
        font-size: 17px;
        font-weight: bold;
    }
    
    .section-more {
        font-size: 13px;
        color: #888888;
        cursor: pointer;
    }
    
    /* قائمة الأفلام الأفقية */
    .movies-scroll {
        display: flex;
        gap: 12px;
        overflow-x: auto;
        padding: 0 16px;
        scrollbar-width: none;
    }
    
    .movies-scroll::-webkit-scrollbar {
        display: none;
    }
    
    .movie-card {
        min-width: 130px;
        height: 200px;
        border-radius: 14px;
        overflow: hidden;
        position: relative;
        border: 1px solid rgba(255, 255, 255, 0.1);
        flex-shrink: 0;
    }
    
    .movie-card img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    
    .movie-title-overlay {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 10px;
        background: linear-gradient(to top, rgba(0,0,0,0.9), transparent);
        font-size: 11px;
        font-weight: bold;
        text-align: center;
        color: white;
    }
    
    /* شريط التنقل السفلي */
    .bottom-nav-container {
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 90%;
        max-width: 380px;
        display: flex;
        gap: 10px;
        z-index: 999;
    }
    
    .nav-pill {
        flex: 1;
        background-color: rgba(22, 23, 29, 0.95);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 40px;
        padding: 6px 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.8);
    }
    
    .nav-item {
        flex: 1;
        text-align: center;
        color: #888888;
        font-size: 11px;
        font-weight: 600;
        padding: 8px 4px;
    }
    
    .nav-item-active {
        flex: 1;
        text-align: center;
        background-color: #ffffff;
        color: #121318;
        font-size: 11px;
        font-weight: bold;
        padding: 8px 6px;
        border-radius: 30px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }
    
    .extra-nav-btn {
        width: 50px;
        background-color: rgba(22, 23, 29, 0.95);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 25px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.8);
        color: #ccc;
    }
    </style>

    <div class="mobile-container">
        <!-- شريط علوي -->
        <div class="top-bar">
            <div class="upgrade-btn">
                <span>✨</span> ترقية
            </div>
            <div class="app-title">
                بلوت كرافت <span>🎬</span>
            </div>
        </div>

        <!-- قسم التحية والبطاقات -->
        <div class="hero-section">
            <div class="hero-text-container">
                <div class="hero-subtitle">مساء الخير، أيها المخرج</div>
                <div class="hero-title">أي قصة سنصنع اليوم؟</div>
            </div>
            
            <div class="options-row">
                <!-- بطاقة سريع -->
                <div class="option-card">
                    <div class="pro-badge">Pro only</div>
                    <div style="margin-bottom: 8px; color: #a270ff;">🪄</div>
                    <div class="option-title">سريع</div>
                    <div class="option-desc">إدخال واحد، فيديو كامل</div>
                </div>
                
                <!-- بطاقة خطوة بخطوة -->
                <div class="option-card">
                    <div style="margin-bottom: 8px; color: #5090ff;">💬</div>
                    <div class="option-title">خطوة بخطوة</div>
                    <div class="option-desc">راجع كل خطوة</div>
                </div>
            </div>
        </div>

        <!-- عنوان القائمة الأفقي -->
        <div class="section-header">
            <div class="section-more">عرض الكل ></div>
            <div class="section-title">إلهام بلوت كرافت</div>
        </div>

        <!-- قائمة الأفلام والقصص -->
        <div class="movies-scroll">
            <div class="movie-card">
                <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=400&auto=format&fit=crop">
                <div class="movie-title-overlay">INVITATION</div>
            </div>
            <div class="movie-card">
                <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=400&auto=format&fit=crop">
                <div class="movie-title-overlay">THE WRONG DOOR</div>
            </div>
            <div class="movie-card">
                <img src="https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=400&auto=format&fit=crop">
                <div class="movie-title-overlay">SECRET BILLIONAIRE</div>
            </div>
        </div>

        <!-- شريط التنقل السفلي -->
        <div class="bottom-nav-container">
            <div class="extra-nav-btn">✨</div>
            <div class="nav-pill">
                <div class="nav-item">الصفحة الرئيسية</div>
                <div class="nav-item">الأعمال</div>
                <div class="nav-item-active">الأدوات</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

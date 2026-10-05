import streamlit as st

st.set_page_config(
    page_title="بلوت كرافت",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
        /* إخفاء القائمة الجانبية وعناصر ستريمليت الافتراضية بالكامل */
        [data-testid="stSidebarNav"], [data-testid="collapsedControl"], section[data-testid="stSidebar"] {
            display: none !important;
        }
        button[kind="header"] {
            display: none !important;
        }
        .block-container {
            padding: 0rem !important;
            max-width: 100% !important;
            overflow: hidden;
        }
        iframe {
            width: 100% !important;
            max-width: 100% !important;
        }
    </style>
""", unsafe_allow_html=True)

html_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>بلوت كرافت</title>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;900&display=swap" rel="stylesheet">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { 
            font-family: 'Tajawal', sans-serif; 
            background-color: #0b0d12; 
            color: #ffffff;
            width: 100vw;
            height: 100vh;
            overflow: hidden;
        }
        .main-container {
            display: flex;
            flex-direction: column;
            height: 100vh;
            position: relative;
        }
        .content-scrollable {
            flex-grow: 1;
            overflow-y: auto;
            padding-bottom: 70px;
        }
        .no-scrollbar::-webkit-scrollbar { display: none; }
        
        /* شريط المتصفح العلوي */
        .top-browser-bar {
            background-color: #12141c;
            padding: 8px 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 11px;
            color: #9ca3af;
            border-bottom: 1px solid rgba(255,255,255,0.08);
            flex-shrink: 0;
        }
        
        /* الهيدر العلوي (الترحيب والاسم والترقية) */
        .hero-section {
            background: linear-gradient(180deg, rgba(11,13,18,0.3) 0%, rgba(11,13,18,0.95) 85%, #0b0d12 100%),
                        url('https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?auto=format&fit=crop&w=800&q=80');
            background-size: cover;
            background-position: center;
            padding: 14px 16px;
            border-bottom-left-radius: 20px;
            border-bottom-right-radius: 20px;
            flex-shrink: 0;
        }
        
        /* البطاقات الزجاجية للخيارات السريعة */
        .glass-box {
            background: rgba(255, 255, 255, 0.07);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 14px;
            padding: 12px;
            position: relative;
            text-align: right;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .glass-box:hover {
            border-color: rgba(255, 255, 255, 0.3);
            background: rgba(255, 255, 255, 0.1);
        }

        .screen { display: none; width: 100%; flex-direction: column; }
        .screen.active { display: flex; }
        
        /* أزرار التنقل السفلية الثابتة */
        .custom-nav-tabs {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            display: flex;
            gap: 8px;
            padding: 10px 16px;
            background: rgba(11, 13, 18, 0.95);
            backdrop-filter: blur(12px);
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            z-index: 100;
        }
        .tab-btn {
            flex: 1;
            padding: 10px 6px;
            text-align: center;
            font-family: 'Tajawal', sans-serif;
            font-size: 11px;
            font-weight: 500;
            color: #9ca3af;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .tab-btn.active {
            background: #000000;
            color: #ffffff;
            font-weight: 900;
            border: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: 0 4px 12px rgba(0,0,0,0.5);
        }
    </style>
</head>
<body>

    <div class="main-container">
        
        <!-- شريط المتصفح العلوي -->
        <div class="top-browser-bar">
            <div style="display: flex; align-items: center; gap: 6px; font-size: 10px; letter-spacing: 0.5px;">
                <span>...</span>
                <span style="color: #e2e8f0; font-weight: bold;">CONNECTING</span>
            </div>
            <div style="display: flex; align-items: center; gap: 12px; font-size: 13px;">
                <span>Share</span>
                <span>⭐</span>
                <span>✏️</span>
                <span>🐱</span>
                <span>⋮</span>
            </div>
        </div>

        <!-- المحتوى القابل للتمرير -->
        <div class="content-scrollable no-scrollbar">
            
            <!-- الشاشة الرئيسية -->
            <div id="home-screen" class="screen active">
                
                <!-- 1. الترحيب والاسم والترقية في مكانها الأصلي في الأعلى تماماً -->
                <div class="hero-section">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                        <div style="font-weight: 900; font-size: 14px; letter-spacing: 0.5px; color: #ffffff;">
                            بلوت كرافت
                        </div>
                        <span style="background: rgba(255,255,255,0.1); padding: 3px 10px; border-radius: 20px; font-size: 10px; font-weight: bold; border: 1px solid rgba(255,255,255,0.15);">ترقية ✨</span>
                    </div>

                    <div style="text-align: right;">
                        <h1 style="font-size: 12px; font-weight: 600; line-height: 1.3; color: #cbd5e1; margin-bottom: 2px;">مساء الخير، أيها المخرج</h1>
                        <h2 style="font-size: 14px; font-weight: 900; color: #ffffff;">أي قصة سنصنع اليوم؟</h2>
                    </div>
                </div>

                <!-- 2. باقي الأقسام (مربعات الخيارات وقسم الإلهام) نزلت لتحت -->
                <div style="padding: 14px 16px;">
                    
                    <!-- مربعات الخيارات السريعة -->
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 20px;">
                        <div class="glass-box">
                            <div style="font-size: 14px; margin-bottom: 4px; text-align: right;">💬</div>
                            <h3 style="font-size: 11px; font-weight: bold; margin-bottom: 2px;">خطوة بخطوة</h3>
                            <p style="font-size: 8px; color: #94a3b8;">راجع كل خطوة</p>
                        </div>
                        <div class="glass-box">
                            <span style="position: absolute; top: 6px; left: 8px; font-size: 6px; background: rgba(0,0,0,0.5); padding: 2px 5px; border-radius: 8px; color: #cbd5e1; font-weight: bold; border: 1px solid rgba(255,255,255,0.1);">Pro</span>
                            <div style="font-size: 14px; margin-bottom: 4px; text-align: right;">⚡</div>
                            <h3 style="font-size: 11px; font-weight: bold; margin-bottom: 2px;">سريع</h3>
                            <p style="font-size: 8px; color: #94a3b8;">إدخال واحد، فيديو كامل</p>
                        </div>
                    </div>

                    <!-- قسم إلهام بلوت كرافت -->
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <h3 style="font-size: 13px; font-weight: 800; color: #ffffff;">إلهام بلوت كرافت</h3>
                        <span style="font-size: 10px; color: #9ca3af; font-weight: bold; cursor: pointer;">عرض الكل <</span>
                    </div>

                    <div style="display: flex; gap: 10px; overflow-x: auto; padding-bottom: 4px;" class="no-scrollbar">
                        
                        <!-- البطاقة الأولى -->
                        <div style="min-width: 160px; width: 160px; height: 230px; border-radius: 16px; background-image: url('https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=350&q=80'); background-size: cover; background-position: center; position: relative; padding: 12px; display: flex; flex-direction: column; justify-content: flex-end; border: 1px solid rgba(255,255,255,0.15); flex-shrink: 0;">
                            <div style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.9), rgba(0,0,0,0.1)); border-radius: 16px;"></div>
                            <span style="position: relative; z-index: 10; font-size: 10px; font-weight: 900; text-align: center; color: #ffffff;">THE DELIVERYMAN</span>
                        </div>

                        <!-- البطاقة الثانية -->
                        <div style="min-width: 160px; width: 160px; height: 230px; border-radius: 16px; background-image: url('https://images.unsplash.com/photo-1536440136628-849c177e76a1?auto=format&fit=crop&w=350&q=80'); background-size: cover; background-position: center; position: relative; padding: 12px; display: flex; flex-direction: column; justify-content: flex-end; border: 1px solid rgba(255,255,255,0.15); flex-shrink: 0;">
                            <div style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.9), rgba(0,0,0,0.1)); border-radius: 16px;"></div>
                            <span style="position: relative; z-index: 10; font-size: 10px; font-weight: 900; text-align: center; color: #ffffff;">THE WRONG DOOR</span>
                        </div>

                        <!-- البطاقة الثالثة -->
                        <div style="min-width: 160px; width: 160px; height: 230px; border-radius: 16px; background-image: url('https://images.unsplash.com/photo-1485846234645-a62644f84728?auto=format&fit=crop&w=350&q=80'); background-size: cover; background-position: center; position: relative; padding: 12px; display: flex; flex-direction: column; justify-content: flex-end; border: 1px solid rgba(255,255,255,0.15); flex-shrink: 0;">
                            <div style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.9), rgba(0,0,0,0.1)); border-radius: 16px;"></div>
                            <span style="position: relative; z-index: 10; font-size: 10px; font-weight: 900; text-align: center; color: #ffffff;">CYBERPUNK CITY</span>
                        </div>

                    </div>
                </div>

            </div>

            <!-- شاشة الأدوات -->
            <div id="tools-screen" class="screen" style="padding: 16px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
                    <h1 style="font-size: 15px; font-weight: 900;">الأدوات</h1>
                    <span style="background: rgba(255,255,255,0.1); padding: 5px 14px; border-radius: 20px; font-size: 11px; font-weight: bold;">ترقية ✨</span>
                </div>
                <div style="background: rgba(255,255,255,0.05); padding: 18px; border-radius: 14px; border: 1px solid rgba(255,255,255,0.1);">
                    <h3 style="font-size: 13px; font-weight: 900;">ميزات الأدوات المتقدمة</h3>
                </div>
            </div>

            <!-- شاشة الأعمال -->
            <div id="works-screen" class="screen" style="padding: 16px;">
                <div style="display: flex; justify-content: flex-end; margin-bottom: 14px;">
                    <span style="background: rgba(99, 102, 241, 0.2); color: #818cf8; padding: 6px 16px; border-radius: 20px; font-size: 11px; font-weight: bold; cursor: pointer;">+ مشروع جديد</span>
                </div>
                <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 220px;">
                    <p style="font-size: 12px; color: #9ca3af;">لا توجد أعمال محفوظة</p>
                </div>
            </div>

        </div>

        <!-- أزرار التنقل السفلية الثابتة -->
        <div class="custom-nav-tabs">
            <button id="btn-home" onclick="switchScreen('home')" class="tab-btn active">الصفحة الرئيسية</button>
            <button id="btn-tools" onclick="switchScreen('tools')" class="tab-btn">الأدوات</button>
            <button id="btn-works" onclick="switchScreen('works')" class="tab-btn">الاعمال</button>
        </div>

    </div>

    <script>
        function switchScreen(screenName) {
            document.getElementById('home-screen').classList.remove('active');
            document.getElementById('tools-screen').classList.remove('active');
            document.getElementById('works-screen').classList.remove('active');
            
            document.getElementById('btn-home').classList.remove('active');
            document.getElementById('btn-tools').classList.remove('active');
            document.getElementById('btn-works').classList.remove('active');

            if (screenName === 'home') {
                document.getElementById('home-screen').classList.add('active');
                document.getElementById('btn-home').classList.add('active');
            } else if (screenName === 'tools') {
                document.getElementById('tools-screen').classList.add('active');
                document.getElementById('btn-tools').classList.add('active');
            } else if (screenName === 'works') {
                document.getElementById('works-screen').classList.add('active');
                document.getElementById('btn-works').classList.add('active');
            }
        }
    </script>
</body>
</html>
"""

st.components.v1.html(html_code, height=800, scrolling=False)

import streamlit as st

st.set_page_config(
    page_title="بلوت كرافت",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
        [data-testid="stSidebarNav"], [data-testid="collapsedControl"], section[data-testid="stSidebar"] {
            display: none !important;
        }
        header, button[kind="header"], [data-testid="stHeader"] {
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
            border: none !important;
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
            overflow-y: auto;
            padding-bottom: 110px;
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
        }
        
        /* قسم الهيدر العلوي */
        .hero-section {
            background: linear-gradient(180deg, rgba(11,13,18,0.3) 0%, rgba(11,13,18,0.95) 85%, #0b0d12 100%),
                        url('https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?auto=format&fit=crop&w=800&q=80');
            background-size: cover;
            background-position: center;
            padding: 14px 16px;
            border-bottom-left-radius: 20px;
            border-bottom-right-radius: 20px;
        }
        
        /* الصناديق الزجاجية للخيارات */
        .glass-box {
            background: rgba(255, 255, 255, 0.07);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 14px;
            padding: 12px;
            position: relative;
            text-align: right;
        }

        .screen { display: none; width: 100%; flex-direction: column; }
        .screen.active { display: flex; }
        
        /* شريط التنقل السفلي */
        .nav-bar {
            position: fixed;
            bottom: 15px;
            left: 50%;
            transform: translateX(-50%);
            width: 92%;
            max-width: 400px;
            background: rgba(18, 21, 30, 0.9);
            backdrop-filter: blur(25px);
            -webkit-backdrop-filter: blur(25px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 9999px;
            display: flex;
            padding: 5px;
            z-index: 999;
            box-shadow: 0 10px 30px rgba(0,0,0,0.8);
        }
        .nav-item {
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            padding: 8px 4px;
            border-radius: 9999px;
            font-size: 11px;
            font-weight: 500;
            color: #9ca3af;
            background: transparent;
            border: none;
            cursor: pointer;
            transition: all 0.25s ease;
            white-space: nowrap;
        }
        .nav-item.active {
            background: rgba(255, 255, 255, 0.15);
            color: #ffffff;
            font-weight: 700;
            border: 1px solid rgba(255, 255, 255, 0.2);
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

        <div style="width: 100%;">
            
            <!-- الشاشة الرئيسية -->
            <div id="home-screen" class="screen active">
                <div class="hero-section">
                    <!-- الصف العلوي: الاسم يمين، والترقية يسار -->
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                        <div style="font-weight: 900; font-size: 15px; letter-spacing: 0.5px; color: #ffffff;">
                            بلوت كرافت
                        </div>
                        <span style="background: rgba(255,255,255,0.1); padding: 4px 12px; border-radius: 20px; font-size: 10px; font-weight: bold; border: 1px solid rgba(255,255,255,0.15);">ترقية ✨</span>
                    </div>

                    <!-- الترحيب -->
                    <div style="margin-bottom: 14px; text-align: right;">
                        <h1 style="font-size: 13px; font-weight: 600; line-height: 1.3; color: #cbd5e1; margin-bottom: 2px;">مساء الخير، أيها المخرج</h1>
                        <h2 style="font-size: 15px; font-weight: 900; color: #ffffff;">أي قصة سنصنع اليوم؟</h2>
                    </div>

                    <!-- مربعات الخيارات السريعة -->
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                        <div class="glass-box">
                            <div style="font-size: 15px; margin-bottom: 2px; text-align: right;">💬</div>
                            <h3 style="font-size: 11px; font-weight: bold; margin-bottom: 1px;">خطوة بخطوة</h3>
                            <p style="font-size: 8px; color: #94a3b8;">راجع كل خطوة</p>
                        </div>
                        <div class="glass-box">
                            <span style="position: absolute; top: 6px; left: 8px; font-size: 6px; background: rgba(0,0,0,0.5); padding: 2px 5px; border-radius: 8px; color: #cbd5e1; font-weight: bold; border: 1px solid rgba(255,255,255,0.1);">Pro</span>
                            <div style="font-size: 15px; margin-bottom: 2px; text-align: right;">⚡</div>
                            <h3 style="font-size: 11px; font-weight: bold; margin-bottom: 1px;">سريع</h3>
                            <p style="font-size: 8px; color: #94a3b8;">إدخال واحد، فيديو كامل</p>
                        </div>
                    </div>
                </div>

                <!-- قسم إلهام بلوت كرافت (3 صور كبيرة بجانب بعض بشكل مرتب) -->
                <div style="padding: 14px 16px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                        <h3 style="font-size: 13px; font-weight: 800; color: #ffffff;">إلهام بلوت كرافت</h3>
                        <span style="font-size: 10px; color: #9ca3af; font-weight: bold;">عرض الكل <</span>
                    </div>

                    <div style="display: flex; gap: 10px; overflow-x: auto; padding-bottom: 4px;" class="no-scrollbar">
                        
                        <!-- الصورة الأولى -->
                        <div style="min-width: 125px; width: 125px; height: 185px; border-radius: 14px; background-image: url('https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=350&q=80'); background-size: cover; background-position: center; position: relative; padding: 10px; display: flex; flex-direction: column; justify-content: flex-end; border: 1px solid rgba(255,255,255,0.15); flex-shrink: 0;">
                            <div style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.9), rgba(0,0,0,0.1)); border-radius: 14px;"></div>
                            <span style="position: relative; z-index: 10; font-size: 8px; font-weight: 900; text-align: center; color: #ffffff;">THE DELIVERYMAN</span>
                        </div>

                        <!-- الصورة الثانية -->
                        <div style="min-width: 125px; width: 125px; height: 185px; border-radius: 14px; background-image: url('https://images.unsplash.com/photo-1536440136628-849c177e76a1?auto=format&fit=crop&w=350&q=80'); background-size: cover; background-position: center; position: relative; padding: 10px; display: flex; flex-direction: column; justify-content: flex-end; border: 1px solid rgba(255,255,255,0.15); flex-shrink: 0;">
                            <div style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.9), rgba(0,0,0,0.1)); border-radius: 14px;"></div>
                            <span style="position: relative; z-index: 10; font-size: 8px; font-weight: 900; text-align: center; color: #ffffff;">THE WRONG DOOR</span>
                        </div>

                        <!-- الصورة الثالثة -->
                        <div style="min-width: 125px; width: 125px; height: 185px; border-radius: 14px; background-image: url('https://images.unsplash.com/photo-1485846234645-a62644f84728?auto=format&fit=crop&w=350&q=80'); background-size: cover; background-position: center; position: relative; padding: 10px; display: flex; flex-direction: column; justify-content: flex-end; border: 1px solid rgba(255,255,255,0.15); flex-shrink: 0;">
                            <div style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.9), rgba(0,0,0,0.1)); border-radius: 14px;"></div>
                            <span style="position: relative; z-index: 10; font-size: 8px; font-weight: 900; text-align: center; color: #ffffff;">CYBERPUNK CITY</span>
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
                    <span style="background: rgba(99, 102, 241, 0.2); color: #818cf8; padding: 6px 16px; border-radius: 20px; font-size: 11px; font-weight: bold;">+ مشروع جديد</span>
                </div>
                <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 220px;">
                    <p style="font-size: 12px; color: #9ca3af;">لا توجد أعمال محفوظة</p>
                </div>
            </div>

        </div>

        <!-- الشريط السفلي -->
        <nav class="nav-bar">
            <button id="btn-home" onclick="switchScreen('home')" class="nav-item active">
                <span>الرئيسية</span>
                <span>🏠</span>
            </button>
            <button id="btn-tools" onclick="switchScreen('tools')" class="nav-item">
                <span>الأدوات</span>
                <span>🛠</span>
            </button>
            <button id="btn-works" onclick="switchScreen('works')" class="nav-item">
                <span>الأعمال</span>
                <span>💼</span>
            </button>
        </nav>

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

st.components.v1.html(html_code, height=710, scrolling=False)

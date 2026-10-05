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
        button[kind="header"] {
            display: none !important;
        }
        .block-container {
            padding: 0rem !important;
            max-width: 100% !important;
            overflow: hidden;
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
        body, html { 
            font-family: 'Tajawal', sans-serif; 
            background-color: #0b0d12; 
            color: #ffffff;
            width: 100%;
            height: 100%;
        }
        .main-container {
            display: flex;
            flex-direction: column;
            width: 100%;
            min-height: 100vh;
        }
        .no-scrollbar::-webkit-scrollbar { display: none; }
        
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
        
        .custom-nav-tabs {
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 12px 14px;
            background: #12141c;
            border-bottom: 1px solid rgba(255, 255, 255, 0.15);
            position: sticky;
            top: 0;
            z-index: 999;
        }
        
        .tab-btn {
            flex: 1;
            height: 42px;
            text-align: center;
            font-family: 'Tajawal', sans-serif;
            font-size: 11px;
            font-weight: 500;
            color: #9ca3af;
            background: #000000;
            border: 1.5px solid #ffffff;
            border-radius: 8px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s ease;
        }
        .tab-btn.active {
            background: #161922;
            color: #ffffff;
            font-weight: 900;
            border: 1.5px solid #ffffff;
            box-shadow: 0 0 12px rgba(255,255,255,0.3);
        }

        .custom-icon-tab {
            width: 45px;
            height: 42px;
            background: #000000;
            border: 1.5px solid #ffffff;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s ease;
            flex-shrink: 0;
        }
        .custom-icon-tab.active {
            background: #161922;
            border: 1.5px solid #ffffff;
            box-shadow: 0 0 12px rgba(255,255,255,0.3);
        }

        .hero-section {
            background: linear-gradient(180deg, rgba(11,13,18,0.3) 0%, rgba(11,13,18,0.95) 85%, #0b0d12 100%),
                        url('https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?auto=format&fit=crop&w=800&q=80');
            background-size: cover;
            background-position: center;
            padding: 14px 16px;
            border-bottom-left-radius: 20px;
            border-bottom-right-radius: 20px;
        }
        
        .screen { display: none; width: 100%; flex-direction: column; }
        .screen.active { display: flex; }

        /* تنسيق زر الحذف */
        .delete-all-btn {
            background-color: #dc2626;
            color: white;
            border: none;
            padding: 12px 20px;
            font-family: 'Tajawal', sans-serif;
            font-size: 13px;
            font-weight: bold;
            border-radius: 10px;
            cursor: pointer;
            width: 100%;
            transition: background 0.2s;
            margin-top: 15px;
        }
        .delete-all-btn:hover {
            background-color: #b91c1c;
        }

        .option-item {
            background: rgba(255, 255, 255, 0.07);
            padding: 10px 14px;
            border-radius: 8px;
            margin-bottom: 8px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 12px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
    </style>
</head>
<body>

    <div class="main-container">
        
        <div class="top-browser-bar">
            <div style="display: flex; align-items: center; gap: 6px; font-size: 10px; letter-spacing: 0.5px;">
                <span>...</span>
                <span style="color: #e2e8f0; font-weight: bold;">CONNECTING</span>
            </div>
            <div style="display: flex; align-items: center; gap: 12px; font-size: 13px;">
                <span>Share</span>
                <span>⭐</span>
                <span>✏</span>
                <span>🐱</span>
                <span>⋮</span>
            </div>
        </div>

        <!-- شريط التنقل العلوي -->
        <div class="custom-nav-tabs">
            <button id="btn-home" onclick="switchScreen('home')" class="tab-btn active">الصفحة الرئيسية</button>
            <button id="btn-tools" onclick="switchScreen('tools')" class="tab-btn">الأدوات</button>
            <button id="btn-works" onclick="switchScreen('works')" class="tab-btn">الاعمال</button>
            
            <button id="btn-custom" onclick="switchScreen('custom')" class="custom-icon-tab" title="الزر المخصص">
                <div style="position: relative; width: 22px; height: 22px; display: flex; align-items: center; justify-content: center;">
                    <div style="width: 18px; height: 18px; background: #9ca3af; border-radius: 4px; display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden;">
                        <div style="width: 0; height: 0; border-top: 3px solid transparent; border-bottom: 3px solid transparent; border-right: 6px solid #0b0d12; transform: translateX(1px);"></div>
                        <div style="position: absolute; right: 0; top: 0; bottom: 0; width: 4px; background: repeating-linear-gradient(to bottom, #9ca3af, #9ca3af 2px, #4b5563 2px, #4b5563 4px);"></div>
                    </div>
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="#3b82f6" xmlns="http://www.w3.org/2000/svg" style="position: absolute; top: -5px; left: -4px;">
                        <path d="M12 0L14.59 9.41L24 12L14.59 14.59L12 24L9.41 14.59L0 12L9.41 9.41L12 0Z"/>
                    </svg>
                </div>
            </button>
        </div>

        <div>
            
            <!-- الشاشة الرئيسية -->
            <div id="home-screen" class="screen active">
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

                <div style="padding: 14px 16px 10px 16px;">
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                        <div style="background: rgba(255, 255, 255, 0.07); border: 1px solid rgba(255, 255, 255, 0.12); border-radius: 14px; padding: 12px; text-align: right;">
                            <h3 style="font-size: 11px; font-weight: bold; margin-bottom: 2px;">خطوة بخطوة</h3>
                            <p style="font-size: 8px; color: #94a3b8;">راجع كل خطوة</p>
                        </div>
                        <div style="background: rgba(255, 255, 255, 0.07); border: 1px solid rgba(255, 255, 255, 0.12); border-radius: 14px; padding: 12px; text-align: right;">
                            <h3 style="font-size: 11px; font-weight: bold; margin-bottom: 2px;">سريع</h3>
                            <p style="font-size: 8px; color: #94a3b8;">إدخال واحد، فيديو كامل</p>
                        </div>
                    </div>
                </div>

                <div style="padding: 20px 16px 40px 16px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                        <h3 style="font-size: 13px; font-weight: 800; color: #ffffff;">إلهام بلوت كرافت</h3>
                        <span style="font-size: 10px; color: #9ca3af; font-weight: bold;">عرض الكل <</span>
                    </div>

                    <div style="display: flex; gap: 10px; overflow-x: auto; padding-bottom: 4px;" class="no-scrollbar">
                        <div style="min-width: 160px; width: 160px; height: 230px; border-radius: 16px; background-image: url('https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=350&q=80'); background-size: cover; background-position: center; position: relative; padding: 12px; display: flex; flex-direction: column; justify-content: flex-end; border: 1px solid rgba(255,255,255,0.15); flex-shrink: 0;">
                            <div style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.9), rgba(0,0,0,0.1)); border-radius: 16px;"></div>
                            <span style="position: relative; z-index: 10; font-size: 10px; font-weight: 900; text-align: center; color: #ffffff;">THE DELIVERYMAN</span>
                        </div>
                        <div style="min-width: 160px; width: 160px; height: 230px; border-radius: 16px; background-image: url('https://images.unsplash.com/photo-1536440136628-849c177e76a1?auto=format&fit=crop&w=350&q=80'); background-size: cover; background-position: center; position: relative; padding: 12px; display: flex; flex-direction: column; justify-content: flex-end; border: 1px solid rgba(255,255,255,0.15); flex-shrink: 0;">
                            <div style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.9), rgba(0,0,0,0.1)); border-radius: 16px;"></div>
                            <span style="position: relative; z-index: 10; font-size: 10px; font-weight: 900; text-align: center; color: #ffffff;">THE WRONG DOOR</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- شاشة الأدوات (تحتوي على قائمة الخيارات وزر الحذف) -->
            <div id="tools-screen" class="screen" style="padding: 20px;">
                <h1 style="font-size: 15px; font-weight: 900; margin-bottom: 14px;">الأدوات وإدارة الخيارات</h1>
                <div style="background: rgba(255,255,255,0.05); padding: 18px; border-radius: 14px; border: 1px solid rgba(255,255,255,0.1);">
                    <h3 style="font-size: 13px; font-weight: 900; margin-bottom: 12px;">قائمة الخيارات النشطة</h3>
                    
                    <!-- حاوية الخيارات -->
                    <div id="options-container">
                        <div class="option-item"><span>الخيار الأول (نمط بصري)</span></div>
                        <div class="option-item"><span>الخيار الثاني (جودة عالية)</span></div>
                        <div class="option-item"><span>الخيار الثالث (مؤثرات صوتية)</span></div>
                    </div>

                    <!-- زر حذف جميع الخيارات -->
                    <button class="delete-all-btn" onclick="deleteAllOptions()">حذف جميع الخيارات</button>
                </div>
            </div>

            <!-- شاشة الأعمال -->
            <div id="works-screen" class="screen" style="padding: 20px;">
                <h1 style="font-size: 15px; font-weight: 900; margin-bottom: 14px;">الاعمال</h1>
                <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 220px;">
                    <p style="font-size: 12px; color: #9ca3af;">لا توجد أعمال محفوظة</p>
                </div>
            </div>

            <!-- شاشة الزر المخصص -->
            <div id="custom-screen" class="screen" style="padding: 20px;">
                <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 300px;">
                    <div style="background: #12141c; border: 2px solid #ffffff; border-radius: 20px; padding: 25px; width: 100%; max-width: 280px; text-align: center; box-shadow: 0 8px 30px rgba(0,0,0,0.9);">
                        <h3 style="font-size: 14px; font-weight: 900; color: #ffffff; margin-bottom: 8px;">القسم المخصص</h3>
                        <p style="font-size: 10px; color: #9ca3af;">هذا الزر مستقل بذاته تماماً.</p>
                    </div>
                </div>
            </div>

        </div>

    </div>

    <script>
        function switchScreen(screenName) {
            document.getElementById('home-screen').classList.remove('active');
            document.getElementById('tools-screen').classList.remove('active');
            document.getElementById('works-screen').classList.remove('active');
            document.getElementById('custom-screen').classList.remove('active');
            
            document.getElementById('btn-home').classList.remove('active');
            document.getElementById('btn-tools').classList.remove('active');
            document.getElementById('btn-works').classList.remove('active');
            document.getElementById('btn-custom').classList.remove('active');

            if (screenName === 'home') {
                document.getElementById('home-screen').classList.add('active');
                document.getElementById('btn-home').classList.add('active');
            } else if (screenName === 'tools') {
                document.getElementById('tools-screen').classList.add('active');
                document.getElementById('btn-tools').classList.add('active');
            } else if (screenName === 'works') {
                document.getElementById('works-screen').classList.add('active');
                document.getElementById('btn-works').classList.add('active');
            } else if (screenName === 'custom') {
                document.getElementById('custom-screen').classList.add('active');
                document.getElementById('btn-custom').classList.add('active');
            }
        }

        // الدالة المسؤولة عن حذف جميع الخيارات
        function deleteAllOptions() {
            const container = document.getElementById('options-container');
            container.innerHTML = '<p style="font-size: 11px; color: #9ca3af; text-align: center; padding: 10px;">لا توجد خيارات متبقية</p>';
        }
    </script>
</body>
</html>
"""

st.components.v1.html(html_code, height=850, scrolling=True)

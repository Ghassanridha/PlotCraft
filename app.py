import streamlit as st

st.set_page_config(
    page_title="بلوت كرافت",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
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
            background-color: #05070a; 
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
            /* مساحة كافية بالأسفل حتى ما يختفي أي شي ورا النافبار */
            padding-bottom: 90px;
        }
        .hero-section {
            background: linear-gradient(135deg, rgba(20, 25, 40, 0.9), rgba(5, 7, 10, 0.95)),
                        url('https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?auto=format&fit=crop&w=800&q=80');
            background-size: cover;
            background-position: center;
            /* تثبيت المسافة العلوية بدقة حتى يبقى الاسم بمكانه المرتب */
            padding: 50px 16px 12px 16px;
            border-bottom-left-radius: 24px;
            border-bottom-right-radius: 24px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
        }
        .glass-box {
            background: rgba(255, 255, 255, 0.06);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 10px;
            position: relative;
        }
        .screen { display: none; width: 100%; flex-direction: column; }
        .screen.active { display: flex; }
        
        .nav-bar {
            position: fixed;
            bottom: 12px;
            left: 50%;
            transform: translateX(-50%);
            width: 92%;
            max-width: 400px;
            background: rgba(15, 18, 28, 0.95);
            backdrop-filter: blur(25px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 9999px;
            display: flex;
            padding: 5px;
            z-index: 999;
            box-shadow: 0 10px 30px rgba(0,0,0,0.6);
        }
        .nav-item {
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            padding: 9px 6px;
            border-radius: 9999px;
            font-size: 12px;
            font-weight: 500;
            color: #9ca3af;
            background: transparent;
            border: none;
            cursor: pointer;
            transition: all 0.2s ease;
            white-space: nowrap;
        }
        .nav-item.active {
            background: #ffffff;
            color: #05070a;
            font-weight: 700;
            box-shadow: 0 4px 15px rgba(255, 255, 255, 0.25);
        }
        .no-scrollbar::-webkit-scrollbar { display: none; }
    </style>
</head>
<body>

    <div class="main-container">
        
        <div style="width: 100%;">
            
            <!-- الشاشة الرئيسية -->
            <div id="home-screen" class="screen active">
                <div class="hero-section">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <span style="font-weight: 900; font-size: 14px;">بلوت كرافت</span>
                        <span style="background: rgba(255,255,255,0.1); padding: 4px 12px; border-radius: 20px; font-size: 11px; font-weight: bold; border: 1px solid rgba(255,255,255,0.15);">ترقية ✨</span>
                    </div>

                    <div style="margin-bottom: 10px;">
                        <h1 style="font-size: 14px; font-weight: 900; line-height: 1.3; margin-bottom: 2px;">مساء الخير، أيها المخرج</h1>
                        <h2 style="font-size: 14px; font-weight: 900;">أي قصة سنصنع اليوم؟</h2>
                    </div>

                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                        <div class="glass-box">
                            <span style="position: absolute; top: 6px; left: 8px; font-size: 8px; background: rgba(0,0,0,0.5); padding: 2px 6px; border-radius: 10px; color: #a5b4fc; font-weight: bold;">Pro</span>
                            <div style="font-size: 15px; margin-bottom: 3px;">⚡</div>
                            <h3 style="font-size: 12px; font-weight: bold; margin-bottom: 2px;">سريع</h3>
                            <p style="font-size: 10px; color: #cbd5e1;">إدخال واحد، فيديو كامل</p>
                        </div>

                        <div class="glass-box">
                            <div style="font-size: 15px; margin-bottom: 3px;">💬</div>
                            <h3 style="font-size: 12px; font-weight: bold; margin-bottom: 2px;">خطوة بخطوة</h3>
                            <p style="font-size: 10px; color: #cbd5e1;">راجع كل خطوة</p>
                        </div>
                    </div>
                </div>

                <!-- قسم القصص -->
                <div style="padding: 12px 16px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <h3 style="font-size: 13px; font-weight: 800;">إلهام بلوت كرافت</h3>
                        <span style="font-size: 11px; color: #818cf8; font-weight: bold;">عرض الكل ></span>
                    </div>

                    <div style="display: flex; gap: 10px; overflow-x: auto; padding-bottom: 4px;" class="no-scrollbar">
                        <div style="min-width: 125px; height: 155px; border-radius: 12px; background-image: url('https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=300&q=80'); background-size: cover; background-position: center; position: relative; padding: 10px; display: flex; flex-direction: column; justify-content: flex-end; border: 1px solid rgba(255,255,255,0.1);">
                            <div style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.9), transparent); border-radius: 12px;"></div>
                            <span style="position: relative; z-index: 10; font-size: 10px; font-weight: 900;">THE WRONG DOOR</span>
                        </div>

                        <div style="min-width: 125px; height: 155px; border-radius: 12px; background-image: url('https://images.unsplash.com/photo-1536440136628-849c177e76a1?auto=format&fit=crop&w=300&q=80'); background-size: cover; background-position: center; position: relative; padding: 10px; display: flex; flex-direction: column; justify-content: flex-end; border: 1px solid rgba(255,255,255,0.1);">
                            <div style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.9), transparent); border-radius: 12px;"></div>
                            <span style="position: relative; z-index: 10; font-size: 10px; font-weight: 900;">THE DELIVERYMAN</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- شاشة الأدوات -->
            <div id="tools-screen" class="screen" style="padding: 16px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                    <h1 style="font-size: 14px; font-weight: 900;">الأدوات</h1>
                    <span style="background: rgba(255,255,255,0.1); padding: 5px 14px; border-radius: 20px; font-size: 11px; font-weight: bold;">ترقية ✨</span>
                </div>
                <div style="background: linear-gradient(to left, rgba(20,22,28,0.8), rgba(5,7,10,0.9)), url('https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&w=500&q=80'); background-size: cover; padding: 18px; border-radius: 14px; border: 1px solid rgba(255,255,255,0.15);">
                    <h3 style="font-size: 13px; font-weight: 900;">تأثيرات الفيديو</h3>
                </div>
            </div>

            <!-- شاشة الأعمال -->
            <div id="works-screen" class="screen" style="padding: 16px;">
                <div style="display: flex; justify-content: flex-end; margin-bottom: 12px;">
                    <span style="background: rgba(99, 102, 241, 0.2); color: #818cf8; padding: 6px 16px; border-radius: 20px; font-size: 11px; font-weight: bold;">+ مشروع جديد</span>
                </div>
                <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 180px;">
                    <p style="font-size: 12px; color: #9ca3af;">لا توجد أعمال بعد</p>
                </div>
            </div>

        </div>

        <!-- الشريط السفلي -->
        <nav class="nav-bar">
            <button id="btn-home" onclick="switchScreen('home')" class="nav-item active">🏠 الرئيسية</button>
            <button id="btn-tools" onclick="switchScreen('tools')" class="nav-item">🛠 الأدوات</button>
            <button id="btn-works" onclick="switchScreen('works')" class="nav-item">💼 الأعمال</button>
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

st.components.v1.html(html_code, height=730, scrolling=False)

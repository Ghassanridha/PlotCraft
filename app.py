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

# الجزء الأول: الهيكل الأساسي للأنماط (CSS) وشاشة الرئيسية
html_part1 = """
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
            text-shadow: 0 2px 8px rgba(0,0,0,0.6);
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
        .card-title-group-left {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
        }
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
            flex-direction: row-reverse;
            gap: 14px;
            overflow-x: auto;
            padding-bottom: 10px;
            scrollbar-width: none;
        }
        .movie-card {
            min-width: 130px;
            height: 190px;
            border-radius: 16px;
            overflow: hidden;
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            padding: 14px;
            border: 1px solid rgba(255,255,255,0.05);
        }
        .movie-card.m1 { background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), url('https://images.unsplash.com/photo-1534447677768-be436bb09401?q=80&w=300&auto=format&fit=crop') center/cover; }
        .movie-card.m2 { background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), url('https://images.unsplash.com/photo-1485846234645-a62644f84728?q=80&w=300&auto=format&fit=crop') center/cover; }
        .movie-card.m3 { background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), url('https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?q=80&w=300&auto=format&fit=crop') center/cover; }
        .movie-title {
            color: #ffffff;
            font-size: 10px;
            font-weight: 700;
            line-height: 1.2;
        }
        .back-btn { 
            background: rgba(255,255,255,0.15); 
            border: none; 
            color: #fff; 
            width: 36px; 
            height: 36px; 
            border-radius: 50%; 
            cursor: pointer; 
            display: flex; 
            align-items: center; 
            justify-content: center; 
        }
        .page-title-text { 
            color: #ffffff; 
            font-size: 18px; 
            font-weight: 700; 
        }
        .content-body { 
            padding: 20px; 
            display: flex; 
            flex-direction: column; 
            gap: 16px; 
            position: relative; 
            z-index: 2; 
        }
        .action-main-btn { 
            width: 100%; 
            background: linear-gradient(135deg, #ff5722 0%, #ff9800 100%); 
            color: #ffffff; 
            font-size: 15px; 
            font-weight: 700; 
            padding: 14px; 
            border-radius: 20px; 
            border: none; 
            cursor: pointer; 
            text-align: center; 
            margin-top: 10px; 
        }
    </style>
</head>
<body>
    <div id="homeScreen" class="screen-view active">
        <div class="hero-box">
            <div class="top-header">
                <div class="brand-title">PlotCraft</div>
                <div class="upgrade-badge" onclick="switchScreen('subscriptionScreen')">
                    <span>⭐</span> ترقية
                </div>
            </div>
            <div class="welcome-section">
                <h1>مساء الخير، أيها المخرج<br>أي قصة سنصنع اليوم؟</h1>
            </div>
            <div class="cards-row">
                <div class="interactive-card" onclick="switchScreen('stepByStepScreen')">
                    <div class="card-header-row">
                        <div class="card-title-group-left">
                            <div class="card-title">خطوة بخطوة</div>
                        </div>
                    </div>
                    <div class="card-subtitle">راجع كل خطوة</div>
                </div>
                <div class="interactive-card" onclick="switchScreen('subscriptionScreen')">
                    <div class="card-header-row">
                        <div class="card-title-group-left">
                            <div class="card-title">سريع</div>
                        </div>
                    </div>
                    <div class="card-subtitle">إدخال واحد، فيديو كامل</div>
                </div>
            </div>
        </div>
        <div class="inspiration-section">
            <div class="section-header">
                <div class="section-title">إلهام بلوت كرافت</div>
                <div class="view-all">عرض الكل ></div>
            </div>
            <div class="movies-carousel">
                <div class="movie-card m1"><div class="movie-title">THE DELIVERYMAN'S SECRET BILLIONAIRE</div></div>
                <div class="movie-card m2"><div class="movie-title">SECRET BILLIONAIRE</div></div>
                <div class="movie-card m3"><div class="movie-title">CYBER CITY</div></div>
            </div>
        </div>
    </div>
"""

# الجزء الثاني: شاشة "خطوة بخطوة" مع رفع الصور والحكاية بالكامل
html_part2 = """
    <div id="stepByStepScreen" class="screen-view">
        <div class="page-header" style="display:flex; align-items:center; justify-content:space-between; padding:20px; border-bottom:1px solid rgba(255,255,255,0.08); background:rgba(11, 15, 25, 0.75);">
            <button class="back-btn" onclick="switchScreen('homeScreen')">✕</button>
            <div class="page-title-text">خطوة بخطوة</div>
            <div style="width: 36px;"></div>
        </div>

        <div style="padding: 20px; display: flex; flex-direction: column; gap: 16px;">
            <div style="background: #141824; border: 1px solid #1e293b; border-radius: 16px; padding: 16px; display: flex; flex-direction: column; gap: 8px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="color: #ff2a85; font-size: 14px; font-weight: 700;">مساعد AI بلوت كرافت</div>
                    <div style="width: 32px; height: 32px; background: linear-gradient(135deg, #ff2a85, #7928ca); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 11px;">AI+</div>
                </div>
                <div style="color: #94a3b8; font-size: 12px; line-height: 1.5;">عزيزي المخرج، استمتع بإنشاء وتخصيص تفاصيل فيلمك خطوة بخطوة بدقة احترافية عالية.</div>
            </div>

            <div style="background: #141824; border: 1px solid #1e293b; border-radius: 16px; padding: 16px; display: flex; flex-direction: column; gap: 12px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="color: #ffffff; font-size: 15px; font-weight: 700;">إعداد القصة</div>
                    <div style="background-color: #1e293b; color: #94a3b8; padding: 3px 10px; border-radius: 10px; font-size: 11px; font-weight: 600;">0/2</div>
                </div>
                <div style="color: #64748b; font-size: 11px;">أضف الشخصيات والحكاية أولاً، ثم أكمل الخطوات:</div>

                <div style="background: #1a2234; border-radius: 12px; padding: 12px; display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <h4 style="color: #ffffff; font-size: 13px; font-weight: 700; margin-bottom: 2px;">الشخصيات</h4>
                        <p style="color: #94a3b8; font-size: 11px;">أضف صورتين كحد أقصى لشخصيات القصة</p>
                    </div>
                    <button onclick="toggleUpload()" style="background: rgba(59, 130, 246, 0.15); color: #3b82f6; border: 1px solid rgba(59, 130, 246, 0.3); padding: 6px 14px; border-radius: 8px; font-size: 12px; font-weight: 600; cursor: pointer;">إضافة</button>
                </div>

                <div id="charUploadSection" style="display: none; background: #111827; border: 1px dashed #374151; border-radius: 10px; padding: 12px; text-align: center; color: #94a3b8; font-size: 12px;">
                    <p style="margin-bottom: 6px; font-weight: bold; color:#fff;">قم بإرفاق صورتين كحد أقصى للشخصيات:</p>
                    <input type="file" id="charFiles" accept="image/*" multiple onchange="checkMaxImages(this)" style="color: #cbd5e1; font-size: 11px;">
                </div>

                <div style="background: #1a2234; border-radius: 12px; padding: 12px; display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <h4 style="color: #ffffff; font-size: 13px; font-weight: 700; margin-bottom: 2px;">الحكاية</h4>
                        <p style="color: #94a3b8; font-size: 11px;">اكتب أو صف حبكة قصتك هنا</p>
                    </div>
                    <button onclick="toggleStoryInput()" style="background: rgba(59, 130, 246, 0.15); color: #3b82f6; border: 1px solid rgba(59, 130, 246, 0.3); padding: 6px 14px; border-radius: 8px; font-size: 12px; font-weight: 600; cursor: pointer;">إضافة</button>
                </div>

                <textarea id="storyTextarea" style="display: none; width: 100%; background: #111827; border: 1px solid #374151; border-radius: 10px; padding: 12px; color: #ffffff; font-size: 13px; outline: none; resize: vertical; min-height: 100px; text-align: right;" placeholder="اكتب تفاصيل القصة هنا..."></textarea>
            </div>

            <div style="display: flex; justify-content: flex-end; margin-top: 10px;">
                <button onclick="alert('تم حفظ الخطوات بنجاح!')" style="background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%); color: #ffffff; font-size: 14px; font-weight: 700; padding: 10px 24px; border-radius: 12px; border: none; cursor: pointer; box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);">التالي</button>
            </div>
        </div>
    </div>
"""

# الجزء الثالث: شاشة الاشتراكات مع الفيديو المتحرك (بركان/طاقة) وخطط الاشتراك الكاملة
html_part3 = """
    <div id="subscriptionScreen" class="screen-view">
        <div style="position: relative; width: 100%; height: 220px; overflow: hidden; border-bottom-left-radius: 30px; border-bottom-right-radius: 30px; display: flex; flex-direction: column; justify-content: space-between;">
            <video autoplay muted loop playsinline style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; z-index: 1; opacity: 0.65;">
                <source src="https://assets.mixkit.co/videos/preview/mixkit-digital-animation-of-screens-with-lights-31955-large.mp4" type="video/mp4">
            </video>
            <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(180deg, rgba(11,15,25,0.2) 0%, rgba(11,15,25,0.85) 90%, #0b0f19 100%); z-index: 2;"></div>
            
            <div style="position: relative; z-index: 3; padding: 16px 20px; display: flex; flex-direction: column; justify-content: space-between; height: 100%;">
                <div style="display: flex; align-items: center; justify-content: space-between; width: 100%;">
                    <button class="back-btn" onclick="switchScreen('homeScreen')">✕</button>
                    <div class="page-title-text">ترقية الحساب</div>
                    <div style="width: 36px;"></div>
                </div>
                <div style="text-align: center; margin-bottom: 10px;">
                    <div style="color: #ffffff; font-size: 18px; font-weight: 700; margin-bottom: 4px; text-shadow: 0 2px 8px rgba(0,0,0,0.8);">حول أفكارك إلى PlotCraft</div>
                    <div style="color: #cbd5e1; font-size: 12px; text-shadow: 0 2px 6px rgba(0,0,0,0.8);">أنشئ كل لقطة وعدلها وأكملها بسرعة.</div>
                </div>
            </div>
        </div>

        <div class="content-body">
            <div style="display: flex; flex-direction: column; gap: 12px;">
                <!-- الاشتراك الأسبوعي -->
                <div class="plan-card selected" onclick="selectPlan(this)" style="background: rgba(20, 25, 40, 0.85); border: 1.5px solid #ff5722; border-radius: 16px; padding: 16px; cursor: pointer; position: relative;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <div style="color: #ffffff; font-size: 15px; font-weight: 700;">PlotCraft Pro Weekly</div>
                        <div style="background: rgba(255, 255, 255, 0.12); padding: 4px 10px; border-radius: 10px; color: #ffffff; font-size: 12px; font-weight: 600;">9.99 دولار / أسبوع</div>
                    </div>
                    <div style="color: #94a3b8; font-size: 12px;">500 ساعة معتمدة / أسبوعياً، جرب PlotCraft</div>
                </div>

                <!-- الاشتراك الشهري -->
                <div class="plan-card" onclick="selectPlan(this)" style="background: rgba(20, 25, 40, 0.85); border: 1.5px solid rgba(255, 255, 255, 0.15); border-radius: 16px; padding: 16px; cursor: pointer; position: relative;">
                    <div style="position: absolute; top: 12px; left: 12px; background: #3b82f6; color: #fff; font-size: 10px; padding: 2px 8px; border-radius: 8px; font-weight: 600;">جديد</div>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <div style="color: #ffffff; font-size: 15px; font-weight: 700;">PlotCraft Pro Monthly</div>
                        <div style="background: rgba(255, 255, 255, 0.12); padding: 4px 10px; border-radius: 10px; color: #ffffff; font-size: 12px; font-weight: 600;">29.99 دولار / شهر</div>
                    </div>
                    <div style="color: #94a3b8; font-size: 12px;">1800 نقطة / شهرياً، مثالي للمبدعين</div>
                </div>

                <!-- الاشتراك السنوي -->
                <div class="plan-card" onclick="selectPlan(this)" style="background: rgba(20, 25, 40, 0.85); border: 1.5px solid rgba(255, 255, 255, 0.15); border-radius: 16px; padding: 16px; cursor: pointer; position: relative;">
                    <div style="position: absolute; top: 12px; left: 12px; background: linear-gradient(135deg, #ff5722, #ff9800); color: #fff; font-size: 10px; padding: 2px 8px; border-radius: 8px; font-weight: 600;">الأفضل قيمة</div>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <div style="color: #ffffff; font-size: 15px; font-weight: 700;">PlotCraft Pro Annual</div>
                        <div style="background: rgba(255, 255, 255, 0.12); padding: 4px 10px; border-radius: 10px; color: #ffffff; font-size: 12px; font-weight: 600;">69.99 دولار / سنة</div>
                    </div>
                    <div style="color: #94a3b8; font-size: 12px;">5000 نقطة / سنوياً، إمكانيات غير محدودة</div>
                </div>
            </div>

            <button class="action-main-btn" onclick="switchScreen('paymentScreen')">اشتراك</button>
        </div>
    </div>
"""

# الجزء الرابع: واجهة تفاصيل الدفع البنكي، شريط التنقل السفلي، والوظائف التفاعلية (JS)
html_part4 = """
    <div id="paymentScreen" class="screen-view">
        <div class="page-header" style="display:flex; align-items:center; justify-content:space-between; padding:20px; border-bottom:1px solid rgba(255,255,255,0.08); background:rgba(11, 15, 25, 0.75);">
            <button class="back-btn" onclick="switchScreen('subscriptionScreen')">←</button>
            <div class="page-title-text">تفاصيل الدفع البنكي</div>
            <div style="width: 36px;"></div>
        </div>

        <div class="content-body">
            <div style="display: flex; flex-direction: column; gap: 14px;">
                <div style="display: flex; flex-direction: column; gap: 6px;">
                    <label style="color: #cbd5e1; font-size: 13px; font-weight: 600;">اسم البطاقة البنكية</label>
                    <input type="text" style="width: 100%; background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.15); border-radius: 12px; padding: 12px 14px; color: #ffffff; font-size: 14px; outline: none; text-align: right;" placeholder="الاسم كما يظهر على البطاقة">
                </div>
                <div style="display: flex; flex-direction: column; gap: 6px;">
                    <label style="color: #cbd5e1; font-size: 13px; font-weight: 600;">رقم البطاقة البنكية</label>
                    <input type="text" style="width: 100%; background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.15); border-radius: 12px; padding: 12px 14px; color: #ffffff; font-size: 14px; outline: none; text-align: right;" placeholder="**** **** **** ****" maxlength="19">
                </div>
                <div style="display: flex; gap: 10px;">
                    <div style="flex: 1; display: flex; flex-direction: column; gap: 6px;">
                        <label style="color: #cbd5e1; font-size: 13px; font-weight: 600;">تاريخ الانتهاء</label>
                        <input type="text" style="width: 100%; background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.15); border-radius: 12px; padding: 12px 14px; color: #ffffff; font-size: 14px; outline: none; text-align: right;" placeholder="MM/YY" maxlength="5">
                    </div>
                    <div style="flex: 1; display: flex; flex-direction: column; gap: 6px;">
                        <label style="color: #cbd5e1; font-size: 13px; font-weight: 600;">رمز البطاقة (CVV)</label>
                        <input type="password" style="width: 100%; background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.15); border-radius: 12px; padding: 12px 14px; color: #ffffff; font-size: 14px; outline: none; text-align: right;" placeholder="***" maxlength="4">
                    </div>
                </div>
                <button class="action-main-btn" onclick="confirmPayment()" style="margin-top: 15px;">تأكيد وإتمام الاشتراك</button>
            </div>
        </div>
    </div>

    <!-- شريط التنقل السفلي الثابت -->
    <div style="position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0b0f19; padding: 10px 15px; display: flex; justify-content: center; align-items: center; gap: 12px; z-index: 999999; box-sizing: border-box; direction: rtl; box-shadow: 0 -4px 15px rgba(0,0,0,0.6);">
        <div style="background-color: #161b22; border: 1px solid #30363d; border-radius: 35px; display: flex; justify-content: space-around; align-items: center; padding: 8px 15px; flex-grow: 1; max-width: 380px;">
            <a href="#" onclick="switchScreen('homeScreen')" style="display: flex; align-items: center; gap: 6px; color: #ffffff; font-size: 13px; text-decoration: none; font-weight: bold;">الرئيسية</a>
            <a href="#" onclick="switchScreen('subscriptionScreen')" style="display: flex; align-items: center; gap: 6px; color: #8b949e; font-size: 13px; text-decoration: none;">الترقية</a>
        </div>
    </div>

    <script>
        function switchScreen(screenId) {
            var screens = document.querySelectorAll('.screen-view');
            screens.forEach(s => s.classList.remove('active'));
            document.getElementById(screenId).classList.add('active');
            window.scrollTo(0, 0);
        }

        function selectPlan(element) {
            var cards = document.querySelectorAll('.plan-card');
            cards.forEach(c => {
                c.style.borderColor = "rgba(255, 255, 255, 0.15)";
            });
            element.style.borderColor = "#ff5722";
        }

        function toggleUpload() {
            var box = document.getElementById('charUploadSection');
            box.style.display = (box.style.display === 'block') ? 'none' : 'block';
        }

        function checkMaxImages(input) {
            if (input.files.length > 2) {
                alert('عذراً، الحد الأقصى المسموح به هو صورتان فقط للشخصيات!');
                input.value = '';
            }
        }

        function toggleStoryInput() {
            var box = document.getElementById('storyTextarea');
            box.style.display = (box.style.display === 'block') ? 'none' : 'block';
        }

        function confirmPayment() {
            alert('تم تأكيد اشتراكك في PlotCraft بنجاح!');
            switchScreen('homeScreen');
        }
    </script>
</body>
</html>
"""

# دمج الأجزاء كاملة وعرضها داخل تطبيق ستريمليت
full_html = html_part1 + html_part2 + html_part3 + html_part4
components.html(full_html, height=750, scrolling=True)

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
        }

        .mobile-screen {
            width: 100vw;
            min-height: 100vh;
            background-color: #0b0f19;
            position: relative;
            display: flex;
            flex-direction: column;
            padding-bottom: 70px;
        }

        /* الشاشات المختلفة */
        .screen-view {
            display: none;
            width: 100%;
            min-height: 100vh;
            background-color: #0b0f19;
            flex-direction: column;
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
            transition: 0.2s;
        }

        .upgrade-badge:active {
            transform: scale(0.95);
            background: rgba(255, 255, 255, 0.3);
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

        .exact-bot-icon {
            width: 22px;
            height: 22px;
            background: #dbeafe;
            mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 11h-1V7c0-1.1-.9-2-2-2H8c-1.1 0-2 .9-2 2v4H5c-1.1 0-2 .9-2 2v4c0 1.1.9 2 2 2h1v1c0 .55.45 1 1 1s1-.45 1-1v-1h8v1c0 .55.45 1 1 1s1-.45 1-1v-1h1c1.1 0 2-.9 2-2v-4c0-1.1-.9-2-2-2zM8 7h8v4H8V7zm3 9c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm4 0c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1z"/></svg>') no-repeat center;
            -webkit-mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 11h-1V7c0-1.1-.9-2-2-2H8c-1.1 0-2 .9-2 2v4H5c-1.1 0-2 .9-2 2v4c0 1.1.9 2 2 2h1v1c0 .55.45 1 1 1s1-.45 1-1v-1h8v1c0 .55.45 1 1 1s1-.45 1-1v-1h1c1.1 0 2-.9 2-2v-4c0-1.1-.9-2-2-2zM8 7h8v4H8V7zm3 9c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm4 0c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1 z"/></svg>') no-repeat center;
            background-size: contain;
        }

        .card-title-group-left {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
        }

        .magic-wand-icon {
            width: 22px;
            height: 22px;
            background: #dbeafe;
            mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M7.5 5.6c-.3-.3-.8-.3-1.1 0-.3.3-.3.8 0 1.1 1.2 1.2 1.9 2.8 1.9 4.5 0 1.7-.7 3.3-1.9 4.5-.3.3-.3.8 0 1.1.3.3.8.3 1.1 0 1.5-1.5 2.3-3.5 2.3-5.6s-.8-4.1-2.3-5.6zm4.3-2.3c-.3-.3-.8-.3-1.1 0-.3.3-.3.8 0 1.1 2.2 2.2 3.4 5.1 3.4 8.2s-1.2 6-3.4 8.2c-.3.3-.3.8 0 1.1.3.3.8.3 1.1 0 2.6-2.6 4-6 4-9.3s-1.4-6.7-4-9.3zm4.4-2.3c-.3-.3-.8-.3-1.1 0-.3.3-.3.8 0 1.1 3.1 3.1 4.9 7.3 4.9 11.6s-1.8 8.5-4.9 11.6c-.3.3-.3.8 0 1.1.3.3.8.3 1.1 0 3.5-3.5 5.4-8.1 5.4-12.7s-1.9-9.2-5.4-12.7zm-7.6 15.6l-8.5 8.5c-.4.4-.4 1 0 1.4s1 .4 1.4 0l8.5-8.5c.4-.4.4-1 0-1.4s-1-.4-1.4 0zm11.4-11.4l-3.5 3.5c-.4.4-.4 1 0 1.4s1 .4 1.4 0l3.5-3.5c.4-.4.4-1 0-1.4s-1-.4-1.4 0zm-15 3.5l-3.5 3.5c-.4.4-.4 1 0 1.4s1 .4 1.4 0l3.5-3.5c.4-.4.4-1 0-1.4s-1-.4-1.4 0z"/></svg>') no-repeat center;
            -webkit-mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M7.5 5.6c-.3-.3-.8-.3-1.1 0-.3.3-.3.8 0 1.1 1.2 1.2 1.9 2.8 1.9 4.5 0 1.7-.7 3.3-1.9 4.5-.3.3-.3.8 0 1.1.3.3.8.3 1.1 0 1.5-1.5 2.3-3.5 2.3-5.6s-.8-4.1-2.3-5.6zm4.3-2.3c-.3-.3-.8-.3-1.1 0-.3.3-.3.8 0 1.1 2.2 2.2 3.4 5.1 3.4 8.2s-1.2 6-3.4 8.2c-.3.3-.3.8 0 1.1.3.3.8.3 1.1 0 2.6-2.6 4-6 4-9.3s-1.4-6.7-4-9.3zm4.4-2.3c-.3-.3-.8-.3-1.1 0-.3.3-.3.8 0 1.1 3.1 3.1 4.9 7.3 4.9 11.6s-1.8 8.5-4.9 11.6c-.3.3-.3.8 0 1.1.3.3.8.3 1.1 0 3.5-3.5 5.4-8.1 5.4-12.7s-1.9-9.2-5.4-12.7zm-7.6 15.6l-8.5 8.5c-.4.4-.4 1 0 1.4s1 .4 1.4 0l8.5-8.5c.4-.4.4-1 0-1.4s-1-.4-1.4 0zm11.4-11.4l-3.5 3.5c-.4.4-.4 1 0 1.4s1 .4 1.4 0l3.5-3.5c.4-.4.4-1 0-1.4s-1-.4-1.4 0zm-15 3.5l-3.5 3.5c-.4.4-.4 1 0 1.4s1 .4 1.4 0l3.5-3.5c.4-.4.4-1 0-1.4s-1-.4-1.4 0z"/></svg>') no-repeat center;
            background-size: contain;
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

        .movies-carousel::-webkit-scrollbar {
            display: none;
        }

        .movie-card {
            min-width: 130px;
            height: 190px;
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
                        url('https://images.unsplash.com/photo-1534447677768-be436bb09401?q=80&w=300&auto=format&fit=crop') center/cover;
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
            font-size: 10px;
            font-weight: 700;
            text-shadow: 0 2px 4px rgba(0,0,0,0.8);
            line-height: 1.2;
        }

        /* واجهة صفحة الاشتراكات الثابتة */
        .page-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 20px;
            border-bottom: 1px solid rgba(255,255,255,0.08);
        }

        .back-btn {
            background: rgba(255,255,255,0.1);
            border: none;
            color: #fff;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            font-size: 16px;
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
        }

        .plans-list {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .plan-card {
            background: rgba(20, 25, 40, 0.9);
            border: 1.5px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 16px;
            cursor: pointer;
            transition: 0.2s;
            position: relative;
        }

        .plan-card.selected {
            border-color: #3b82f6;
            background: rgba(30, 41, 75, 0.95);
            box-shadow: 0 0 15px rgba(59, 130, 246, 0.3);
        }

        .plan-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 6px;
        }

        .plan-name {
            color: #ffffff;
            font-size: 15px;
            font-weight: 700;
        }

        .plan-price {
            background: rgba(255, 255, 255, 0.1);
            padding: 4px 10px;
            border-radius: 10px;
            color: #ffffff;
            font-size: 12px;
            font-weight: 600;
        }

        .plan-desc {
            color: #94a3b8;
            font-size: 12px;
        }

        .new-tag {
            position: absolute;
            top: 12px;
            left: 12px;
            background: #3b82f6;
            color: #fff;
            font-size: 10px;
            padding: 2px 8px;
            border-radius: 8px;
            font-weight: 600;
        }

        .renewal-text {
            text-align: center;
            color: #64748b;
            font-size: 11px;
            margin-top: 4px;
        }

        .action-main-btn {
            width: 100%;
            background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
            color: #ffffff;
            font-size: 15px;
            font-weight: 700;
            padding: 14px;
            border-radius: 20px;
            border: none;
            cursor: pointer;
            text-align: center;
            box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
            margin-top: 10px;
        }

        /* حقول تفاصيل الدفع البنكي */
        .payment-form-box {
            display: flex;
            flex-direction: column;
            gap: 14px;
        }

        .form-group {
            display: flex;
            flex-direction: column;
            gap: 6px;
        }

        .form-label {
            color: #cbd5e1;
            font-size: 13px;
            font-weight: 600;
        }

        .form-input {
            width: 100%;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 12px;
            padding: 12px 14px;
            color: #ffffff;
            font-size: 14px;
            outline: none;
            text-align: right;
        }

        .form-input:focus {
            border-color: #3b82f6;
        }

        .form-row {
            display: flex;
            gap: 10px;
        }
    </style>
</head>
<body>

    <!-- الواجهة الرئيسية -->
    <div id="homeScreen" class="screen-view active">
        <div class="hero-box">
            <div class="top-header">
                <div class="brand-title">بلوت كرافت</div>
                <div class="upgrade-badge" onclick="switchScreen('subscriptionScreen')">
                    <span>⭐</span> ترقية
                </div>
            </div>

            <div class="welcome-section">
                <h1>مساء الخير، أيها المخرج<br>أي قصة سنصنع اليوم؟</h1>
            </div>

            <div class="cards-row">
                <div class="interactive-card">
                    <div class="card-header-row">
                        <div class="card-title-group-left">
                            <div class="card-title">خطوة بخطوة</div>
                            <span class="exact-bot-icon"></span>
                        </div>
                    </div>
                    <div class="card-subtitle">راجع كل خطوة</div>
                </div>

                <div class="interactive-card">
                    <div class="card-header-row">
                        <div class="card-title-group-left">
                            <div class="card-title">سريع</div>
                            <span class="magic-wand-icon"></span>
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
                <div class="movie-card m1">
                    <div class="movie-title">THE DELIVERYMAN'S SECRET BILLIONAIRE</div>
                </div>
                <div class="movie-card m2">
                    <div class="movie-title">SECRET BILLIONAIRE</div>
                </div>
                <div class="movie-card m3">
                    <div class="movie-title">CYBER CITY</div>
                </div>
            </div>
        </div>
    </div>

    <!-- واجهة الاشتراكات والباقات الثابتة -->
    <div id="subscriptionScreen" class="screen-view">
        <div class="page-header">
            <button class="back-btn" onclick="switchScreen('homeScreen')">✕</button>
            <div class="page-title-text">ترقية الحساب</div>
            <div style="width: 36px;"></div>
        </div>

        <div class="content-body">
            <div style="text-align: center; margin-bottom: 5px;">
                <div style="color: #ffffff; font-size: 18px; font-weight: 700; margin-bottom: 4px;">حول أفكارك إلى بلوت كرافت</div>
                <div style="color: #94a3b8; font-size: 12px;">أنشئ كل لقطة وعدلها وأكملها بسرعة.</div>
            </div>

            <div class="plans-list">
                <!-- الباقة الأسبوعية -->
                <div class="plan-card selected" onclick="selectPlan(this)">
                    <div class="plan-top">
                        <div class="plan-name">بلوت كرافت برو ويكلي</div>
                        <div class="plan-price">9.99 دولار أمريكي / أسبوع</div>
                    </div>
                    <div class="plan-desc">500 ساعة معتمدة / أسبوعياً، جرب بلوت كرافت</div>
                </div>

                <!-- الباقة الشهرية -->
                <div class="plan-card" onclick="selectPlan(this)">
                    <div class="new-tag">جديد</div>
                    <div class="plan-top">
                        <div class="plan-name">بلوت كرافت برو الشهرية</div>
                        <div class="plan-price">29.99 دولار أمريكي / شهر</div>
                    </div>
                    <div class="plan-desc">1800 نقطة / شهرياً، مثالي للاستخدام المنتظم للمبدعين</div>
                </div>

                <!-- الباقة السنوية -->
                <div class="plan-card" onclick="selectPlan(this)">
                    <div class="plan-top">
                        <div class="plan-name">بلوت كرافت برو السنوية</div>
                        <div class="plan-price">69.99 دولار أمريكي / سنة</div>
                    </div>
                    <div class="plan-desc">5000 رصيد / سنة، مثالي للمبدعين المحترفين</div>
                </div>
            </div>

            <div class="renewal-text">تجديد تلقائي، ويمكن الإلغاء في أي وقت</div>

            <button class="action-main-btn" onclick="switchScreen('paymentScreen')">اشتراك</button>
        </div>
    </div>

    <!-- واجهة تفاصيل الدفع البنكي الثابتة -->
    <div id="paymentScreen" class="screen-view">
        <div class="page-header">
            <button class="back-btn" onclick="switchScreen('subscriptionScreen')">←</button>
            <div class="page-title-text">تفاصيل الدفع البنكي</div>
            <div style="width: 36px;"></div>
        </div>

        <div class="content-body">
            <div class="payment-form-box">
                <div class="form-group">
                    <label class="form-label">اسم البطاقة البنكية</label>
                    <input type="text" class="form-input" placeholder="الاسم كما يظهر على البطاقة">
                </div>

                <div class="form-group">
                    <label class="form-label">رقم البطاقة البنكية</label>
                    <input type="text" class="form-input" placeholder="**** **** **** ****" maxlength="19">
                </div>

                <div class="form-row">
                    <div class="form-group" style="flex: 1;">
                        <label class="form-label">تاريخ الانتهاء</label>
                        <input type="text" class="form-input" placeholder="MM/YY" maxlength="5">
                    </div>
                    <div class="form-group" style="flex: 1;">
                        <label class="form-label">رمز البطاقة (CVV)</label>
                        <input type="password" class="form-input" placeholder="***" maxlength="4">
                    </div>
                </div>

                <button class="action-main-btn" onclick="confirmPayment()" style="margin-top: 15px;">تأكيد وإتمام الاشتراك</button>
            </div>
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
            cards.forEach(c => c.classList.remove('selected'));
            element.classList.add('selected');
        }

        function confirmPayment() {
            alert('تم تأكيد اشتراكك في بلوت كرافت بنجاح!');
            switchScreen('homeScreen');
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=750, scrolling=True)
st.markdown(
    """
    <style>
    .plotcraft-nav-bar {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #0b0f19;
        padding: 10px 15px;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 12px;
        z-index: 999999;
        box-sizing: border-box;
        direction: rtl;
        box-shadow: 0 -4px 15px rgba(0,0,0,0.6);
    }
    .plotcraft-nav-pill {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 35px;
        display: flex;
        justify-content: space-around;
        align-items: center;
        padding: 8px 15px;
        flex-grow: 1;
        max-width: 380px;
    }
    .plotcraft-nav-item {
        display: flex;
        align-items: center;
        gap: 6px;
        color: #8b949e;
        font-size: 13px;
        font-family: system-ui, -apple-system, sans-serif;
        text-decoration: none;
        cursor: pointer;
        white-space: nowrap;
    }
    .plotcraft-nav-item.active {
        color: #ffffff;
        font-weight: bold;
    }
    .plotcraft-nav-square {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 16px;
        width: 48px;
        height: 48px;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-shrink: 0;
        cursor: pointer;
        position: relative;
    }
    </style>

    <div class="plotcraft-nav-bar">
        <!-- الأزرار الثلاثة داخل المستطيل: الرئيسية (يمين)، الأدوات (وسط)، الأعمال (يسار) -->
        <div class="plotcraft-nav-pill">
            <!-- 1. الرئيسية -->
            <a href="#" class="plotcraft-nav-item active">
                <span>الرئيسية</span>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22" fill="none" stroke="#161b22" stroke-width="2"></polyline></svg>
            </a>
            
            <!-- 2. الأدوات -->
            <a href="#" class="plotcraft-nav-item">
                <span>الأدوات</span>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"></path></svg>
            </a>

            <!-- 3. الأعمال -->
            <a href="#" class="plotcraft-nav-item">
                <span>الأعمال</span>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
            </a>
        </div>

        <!-- الزر المربع المنفصل على اليسار مع أيقونة الفيديو والشارة المميزة -->
        <div class="plotcraft-nav-square">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#818cf8" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"></rect><line x1="7" y1="2" x2="7" y2="22"></line><line x1="17" y1="2" x2="17" y2="22"></line><line x1="2" y1="12" x2="22" y2="12"></line></svg>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

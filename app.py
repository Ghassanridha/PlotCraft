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
            cursor: pointer;
            transition: 0.2s;
        }

        .movie-card:active {
            transform: scale(0.96);
        }

        .movie-card.emily-cover { 
            background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(11,15,25,0.92) 100%), 
                        url('https://images.unsplash.com/photo-1509967419530-da38b4704bc6?q=80&w=300&auto=format&fit=crop') center/cover; 
            border: 1.5px solid rgba(59, 130, 246, 0.5);
        }
        .movie-card.m2 { background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), url('https://images.unsplash.com/photo-1485846234645-a62644f84728?q=80&w=300&auto=format&fit=crop') center/cover; }
        .movie-card.m3 { background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), url('https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?q=80&w=300&auto=format&fit=crop') center/cover; }

        .movie-title {
            color: #ffffff;
            font-size: 10px;
            font-weight: 700;
            text-shadow: 0 2px 4px rgba(0,0,0,0.8);
            line-height: 1.2;
        }

        /* نافذة عرض القصة المنبثقة */
        .story-modal-overlay {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(11, 15, 25, 0.85);
            backdrop-filter: blur(8px);
            z-index: 9999999;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .story-modal-overlay.active { display: flex; }
        .story-modal-content {
            background: #141824;
            border: 1px solid rgba(59, 130, 246, 0.3);
            border-radius: 20px;
            width: 100%; max-width: 500px; max-height: 85vh;
            display: flex; flex-direction: column; overflow: hidden;
            box-shadow: 0 10px 30px rgba(0,0,0,0.8);
        }
        .story-modal-header {
            display: flex; justify-content: space-between; align-items: center;
            padding: 16px 20px; border-bottom: 1px solid rgba(255,255,255,0.08); background: #1a2234;
        }
        .story-modal-title { color: #ffffff; font-size: 16px; font-weight: 700; }
        .story-modal-close {
            background: rgba(255,255,255,0.1); border: none; color: #fff; width: 32px; height: 32px;
            border-radius: 50%; cursor: pointer; display: flex; align-items: center; justify-content: center;
        }
        .story-modal-body {
            padding: 20px; overflow-y: auto; color: #cbd5e1; font-size: 13px; line-height: 1.8;
            text-align: left; direction: ltr; white-space: pre-line;
        }
        .story-modal-footer {
            padding: 14px 20px; background: #1a2234; border-top: 1px solid rgba(255,255,255,0.08);
            display: flex; justify-content: flex-end;
        }
        .copy-story-btn {
            background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%); color: #ffffff; border: none;
            padding: 10px 20px; border-radius: 12px; font-size: 13px; font-weight: 700; cursor: pointer;
        }

        /* شاشة الاشتراكات (الصورة الوسطى) */
        #subscriptionScreen {
            display: none;
            width: 100%;
            min-height: 100vh;
            background-color: #0b0f19;
            flex-direction: column;
            position: fixed;
            top: 0; left: 0;
            z-index: 99999;
            overflow-y: auto;
            padding-bottom: 40px;
        }
        #subscriptionScreen.active { display: flex; }

        .sub-header {
            display: flex; align-items: center; justify-content: space-between;
            padding: 16px 20px; border-bottom: 1px solid rgba(255,255,255,0.08); background: rgba(11, 15, 25, 0.9);
        }
        .back-btn {
            background: rgba(255,255,255,0.1); border: none; color: #fff; width: 36px; height: 36px;
            border-radius: 50%; font-size: 16px; cursor: pointer; display: flex; align-items: center; justify-content: center;
        }
        .sub-title-text { color: #ffffff; font-size: 17px; font-weight: 700; }
        
        .sub-body { padding: 20px; display: flex; flex-direction: column; gap: 16px; }
        
        .plans-container {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        .plan-box {
            background: rgba(20, 25, 40, 0.85);
            border: 1.5px solid rgba(255, 255, 255, 0.15);
            border-radius: 16px;
            padding: 16px;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: 0.2s;
        }
        .plan-box.selected {
            border-color: #3b82f6;
            background: rgba(30, 41, 75, 0.95);
        }
        .plan-info h3 { color: #fff; font-size: 15px; font-weight: 700; margin-bottom: 4px; }
        .plan-info p { color: #94a3b8; font-size: 12px; }
        .plan-price-tag {
            background: rgba(255, 255, 255, 0.12);
            padding: 6px 12px;
            border-radius: 10px;
            color: #fff;
            font-size: 13px;
            font-weight: 700;
        }
        .subscribe-now-btn {
            width: 100%;
            background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
            color: #fff;
            font-size: 15px;
            font-weight: 700;
            padding: 14px;
            border-radius: 20px;
            border: none;
            cursor: pointer;
            margin-top: 10px;
            box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
        }

        /* نافذة Google Play (الصورة الثانية) */
        .gplay-overlay {
            display: none;
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0, 0, 0, 0.75);
            z-index: 999999;
            align-items: flex-end;
        }
        .gplay-overlay.active { display: flex; }
        .gplay-sheet {
            background: #121316;
            width: 100%;
            border-top-left-radius: 28px;
            border-top-right-radius: 28px;
            padding: 16px 20px 28px 20px;
            color: #ffffff;
            display: flex;
            flex-direction: column;
            gap: 14px;
            max-height: 90vh;
            overflow-y: auto;
            box-shadow: 0 -10px 30px rgba(0,0,0,0.8);
            border-top: 1px solid rgba(255,255,255,0.08);
            text-align: right;
            direction: rtl;
        }
        .gplay-top-bar { display: flex; justify-content: space-between; align-items: center; width: 100%; }
        .gplay-close { background: none; border: none; color: #e8eaed; font-size: 20px; cursor: pointer; }
        .gplay-store-title { color: #e8eaed; font-size: 15px; font-weight: 500; }
        
        .gplay-app-header {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            gap: 6px;
            margin-top: 2px;
            margin-bottom: 4px;
        }
        .gplay-app-icon {
            width: 44px; height: 44px; background: #202124; border-radius: 12px;
            display: flex; align-items: center; justify-content: center; overflow: hidden;
            border: 1px solid rgba(255,255,255,0.1);
        }
        .gplay-app-icon img { width: 100%; height: 100%; object-fit: cover; }
        .gplay-app-details h3 { font-size: 15px; font-weight: 700; color: #e8eaed; margin-bottom: 2px; }
        .gplay-app-details p { font-size: 11px; color: #9aa0a6; }

        .gplay-price-row {
            display: flex; justify-content: space-between; align-items: center;
            font-size: 14px; font-weight: 600; color: #e8eaed; margin-top: 2px;
        }
        .gplay-tax-row {
            display: flex; justify-content: space-between; align-items: center;
            font-size: 12px; color: #9aa0a6; padding-bottom: 10px; border-bottom: 1px solid #2d3139;
        }
        .gplay-notes {
            display: flex; flex-direction: column; gap: 8px; font-size: 11px; color: #9aa0a6;
            line-height: 1.4; padding-bottom: 10px; border-bottom: 1px solid #2d3139;
        }
        .gplay-points-row {
            display: flex; justify-content: space-between; align-items: center; font-size: 12px; color: #e8eaed; padding: 2px 0;
        }
        .gplay-points-diamond { display: flex; gap: 3px; align-items: center; }

        /* سطر طريقة الدفع (الماستر والصورة باليمين والسهم باليسار) */
        .gplay-payment-box {
            display: flex; justify-content: space-between; align-items: center; padding: 8px 0; cursor: pointer;
        }
        .gplay-payment-info {
            display: flex; align-items: center; gap: 10px;
        }
        .gplay-subscribe-btn {
            width: 100%; background: #8ab4f8; color: #202124; font-size: 14px; font-weight: 700;
            padding: 12px; border-radius: 28px; border: none; cursor: pointer; text-align: center; margin-top: 6px;
        }

        /* قائمة طرق الدفع (الصورة الثالثة) */
        .payment-methods-overlay {
            display: none;
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.85);
            z-index: 9999999;
            justify-content: center; align-items: center;
            padding: 20px;
        }
        .payment-methods-overlay.active { display: flex; }
        .payment-methods-sheet {
            background: #121316;
            border-radius: 20px;
            width: 100%; max-width: 400px;
            padding: 20px;
            color: #ffffff;
            display: flex; flex-direction: column; gap: 16px;
            border: 1px solid rgba(255,255,255,0.1);
            text-align: right; direction: rtl;
            max-height: 90vh; overflow-y: auto;
        }
        .pm-header {
            display: flex; justify-content: space-between; align-items: center;
            border-bottom: 1px solid #2d3139; padding-bottom: 12px;
        }
        .pm-title { font-size: 16px; font-weight: 700; color: #fff; }
        .pm-close { background: none; border: none; color: #aaa; font-size: 18px; cursor: pointer; }
        .pm-email { font-size: 13px; color: #9aa0a6; margin-bottom: 4px; }
        
        .pm-item {
            display: flex; justify-content: space-between; align-items: center;
            padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05); cursor: pointer;
        }
        .pm-item-right { display: flex; align-items: center; gap: 10px; }
        .pm-item-left { display: flex; align-items: center; gap: 8px; }

        /* مفتاح تشغيل/إطفاء كوكل بلاي في الصورة الثالثة */
        .switch-container {
            display: flex; align-items: center; justify-content: space-between;
            padding: 8px 0; background: #1a1e29; border-radius: 10px; padding: 8px 12px; margin-top: 4px;
        }
        .switch {
            position: relative; display: inline-block; width: 44px; height: 24px;
        }
        .switch input { opacity: 0; width: 0; height: 0; }
        .slider {
            position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0;
            background-color: #4b5563; transition: .3s; border-radius: 24px;
        }
        .slider:before {
            position: absolute; content: ""; height: 18px; width: 18px; left: 3px; bottom: 3px;
            background-color: white; transition: .3s; border-radius: 50%;
        }
        input:checked + .slider { background-color: #3b82f6; }
        input:checked + .slider:before { transform: translateX(20px); }

        /* الحقول الإضافية للطرق (رمز الاسترداد، بايبال، البطاقة البنكية) */
        .dynamic-input-section {
            display: none;
            background: #1a1e29;
            padding: 14px;
            border-radius: 12px;
            margin-top: 10px;
            border: 1px solid rgba(59, 130, 246, 0.3);
            flex-direction: column;
            gap: 10px;
        }
        .dynamic-input-section.active { display: flex; }
        .dynamic-input-section input {
            width: 100%;
            padding: 10px;
            background: #11151f;
            border: 1px solid #374151;
            border-radius: 8px;
            color: #fff;
            font-size: 13px;
            outline: none;
            text-align: right;
        }
        .dynamic-save-btn {
            background: #3b82f6;
            color: #fff;
            border: none;
            padding: 8px;
            border-radius: 8px;
            font-weight: 700;
            cursor: pointer;
            text-align: center;
        }

        /* نافذة القصة */
        .story-view { display: none; padding: 20px; }
        .story-view.active { display: block; }
    </style>
</head>
<body>

    <!-- الشاشة الرئيسية -->
    <div id="homeScreen" class="screen-view active">
        <div class="hero-box">
            <div class="top-header">
                <div class="brand-title">بلوت كرافت</div>
                <div class="upgrade-badge" onclick="openSubscriptionScreen()">
                    <span>ترقية</span>
                    <span style="color: #fbbf24;">⭐</span>
                </div>
            </div>
            <div class="welcome-section">
                <h1>مساء الخير، أيها المخرج<br>أي قصة سنصنع اليوم؟</h1>
            </div>
        </div>

        <div style="padding: 0 20px;">
            <div class="cards-row">
                <div class="interactive-card">
                    <div class="card-header-row">
                        <div class="card-title">سريع</div>
                        <div class="exact-bot-icon"></div>
                    </div>
                    <div class="card-subtitle">إدخال واحد، فيديو كامل</div>
                </div>
                <div class="interactive-card">
                    <div class="card-header-row">
                        <div class="card-title-group-left">
                            <div class="magic-wand-icon"></div>
                            <div class="card-title">خطوة بخطوة</div>
                        </div>
                    </div>
                    <div class="card-subtitle">راجع كل خطوة</div>
                </div>
            </div>
        </div>

        <div class="inspiration-section">
            <div class="section-header">
                <div class="view-all">عرض الكل ></div>
                <div class="section-title">إلهام بلوت كرافت</div>
            </div>
            <div class="movies-carousel">
                <div class="movie-card emily-cover" onclick="openStoryModal('EMILY\\'S MILLIONAIRE', 'قصة إيميلي فتاة بسيطة تعمل في مقهى صغير بوسط المدينة، تتبدل حياتها بالكامل عندما تقابل رجل أعمال ثري يعجب بشغفها وإصرارها على النجاح رغم الظروف الصعبة، لتخوض معه رحلة مليئة بالمفاجآت والتحديات في عالم المال والأعمال.')">
                    <div class="movie-title">EMILY\\'S MILLIONAIRE</div>
                </div>
                <div class="movie-card m2" onclick="openStoryModal('SECRET BILLIONAIRE', 'شاب غامض يخفي ثروته الحقيقية ويهبط إلى الأحياء الشعبية ليعيش حياة طبيعية ويتعرف على المعنى الحقيقي للصداقة والحب، قبل أن تكتشف الحقيقة بطريقة مثيرة ومشوقة.')">
                    <div class="movie-title">SECRET BILLIONAIRE</div>
                </div>
                <div class="movie-card m3" onclick="openStoryModal('CYBER CITY', 'في مستقبل مظلم تحكمه التكنولوجيا وتقنيات الذكاء الاصطناعي الفائقة، يحاول مجموعة من المتمردين استعادة حرية البشرية وإسقاط النظام الرقمي المسيطر.')">
                    <div class="movie-title">CYBER CITY</div>
                </div>
            </div>
        </div>
    </div>

    <!-- شاشة الاشتراكات (عند الضغط على ترقية) -->
    <div id="subscriptionScreen">
        <div class="sub-header">
            <button class="back-btn" onclick="closeSubscriptionScreen()">✕</button>
            <div class="sub-title-text">اختر باقة الاشتراك</div>
            <div style="width: 36px;"></div>
        </div>
        <div class="sub-body">
            <div class="plans-container">
                <div class="plan-box selected" onclick="selectPlan(this, 'PlotCraft Pro Weekly', '9.99')">
                    <div class="plan-info">
                        <h3>باقة أسبوعية (Pro Weekly)</h3>
                        <p>وصول كامل لكافة ميزات الذكاء الاصطناعي</p>
                    </div>
                    <div class="plan-price-tag">$9.99 / أسبوع</div>
                </div>
                <div class="plan-box" onclick="selectPlan(this, 'PlotCraft Pro Monthly', '29.99')">
                    <div class="plan-info">
                        <h3>باقة شهرية (Pro Monthly)</h3>
                        <p>توفير أعلى مع سرعة معالجة قصوى</p>
                    </div>
                    <div class="plan-price-tag">$29.99 / شهر</div>
                </div>
                <div class="plan-box" onclick="selectPlan(this, 'PlotCraft Pro Yearly', '99.99')">
                    <div class="plan-info">
                        <h3>باقة سنوية (Pro Yearly)</h3>
                        <p>الخيار الأفضل للمخرجين المحترفين</p>
                    </div>
                    <div class="plan-price-tag">$99.99 / سنة</div>
                </div>
            </div>
            <button class="subscribe-now-btn" onclick="openGPlayModal()">متابعة والدفع عبر Google Play</button>
        </div>
    </div>

    <!-- نافذة Google Play (الصورة الثانية) -->
    <div id="gplayModal" class="gplay-overlay">
        <div class="gplay-sheet">
            <div class="gplay-top-bar">
                <button class="gplay-close" onclick="closeGPlayModal()">✕</button>
                <div class="gplay-store-title">Google Play</div>
            </div>
            
            <div class="gplay-app-header">
                <div class="gplay-app-icon">
                    <img src="https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=100&auto=format&fit=crop" alt="App Icon">
                </div>
                <div class="gplay-app-details">
                    <h3 id="gplayPlanTitle">PlotCraft Pro Weekly</h3>
                    <p>PlotCraft: AI Short Drama Maker</p>
                </div>
            </div>

            <div class="gplay-price-row">
                <span id="gplayPriceText">US$/week 9.99</span>
                <span>بدءاً من اليوم</span>
            </div>
            <div class="gplay-tax-row">
                <span>بالإضافة إلى الضريبة</span>
                <span>إضافة الضريبة ⓘ</span>
            </div>

            <div class="gplay-notes">
                <div>• يمكنك الإلغاء في أي وقت في صفحة "الاشتراكات" على Google Play</div>
                <div>• سيستخدم رصيدك في Google Play لتحصيل الرسوم اليوم. وأي رسوم متبقية ستُحصل من طريقة الدفع أدناه.</div>
                <div>• ستُحصل رسوم عمليات التجديد من طريقة الدفع الأساسية</div>
            </div>

            <div class="gplay-points-row">
                <div class="gplay-points-diamond">
                    <span style="color: #34d399;">🔶</span>
                    <span>كسب ١١ نقطة إضافية</span>
                </div>
            </div>

            <!-- طريقة الدفع في نافذة جوجل: الماستر باليمين والسهم باليسار -->
            <div class="gplay-payment-box" onclick="openPaymentMethodsModal()">
                <div style="font-size: 16px; color: #9aa0a6;">‹</div>
                <div class="gplay-payment-info">
                    <div style="text-align: right;">
                        <div style="font-size: 14px; font-weight: 700; color: #fff;">Mastercard-0709</div>
                        <div style="font-size: 12px; color: #9aa0a6;">رصيد Google Play: US$ 0.16</div>
                    </div>
                    <!-- الشعار باليمين -->
                    <div style="background: #fff; padding: 2px 6px; border-radius: 4px; display: flex; align-items: center;">
                        <span style="color: #eb001b; font-weight: bold; font-size: 12px;">MC</span>
                    </div>
                </div>
            </div>

            <div style="font-size: 11px; color: #9aa0a6; line-height: 1.4;">
                عند النقر على "اشتراك"، فإن هذا يعني موافقتك على تجديد اشتراكك تلقائياً إلى أن يتم إلغاؤه. سنعلمك في حال تغير السعر، وذلك استناداً لما هو موضح في "بنود خدمة Google Play". "يمكنك التعرف على كيفية إلغاء الاشتراك". <span style="color: #8ab4f8; cursor: pointer;">المزيد</span>
            </div>

            <button class="gplay-subscribe-btn" onclick="alert('تمت عملية الاشتراك بنجاح عبر بلوت كرافت!')">اشتراك</button>
        </div>
    </div>

    <!-- قائمة طرق الدفع (الصورة الثالثة) -->
    <div id="paymentMethodsModal" class="payment-methods-overlay">
        <div class="payment-methods-sheet">
            <div class="pm-header">
                <button class="pm-close" onclick="closePaymentMethodsModal()">✕</button>
                <div class="pm-title">طرق الدفع</div>
            </div>

            <div class="pm-email">ahhanaa70@gmail.com</div>

            <!-- خيار البطاقة الأساسية -->
            <div class="pm-item">
                <div class="pm-item-left">
                    <span style="color: #3b82f6; font-size: 16px;">✔</span>
                </div>
                <div class="pm-item-right">
                    <div style="font-size: 14px; font-weight: 700;">Mastercard-0709</div>
                    <div style="background:#fff; padding:2px 6px; border-radius:4px; color:#eb001b; font-weight:bold; font-size:11px;">MC</div>
                </div>
            </div>

            <!-- مفتاح تشغيل/إطفاء رصيد Google Play -->
            <div class="switch-container">
                <label class="switch">
                    <input type="checkbox" id="gplayBalanceToggle" checked onchange="toggleGPlayBalance()">
                    <span class="slider"></span>
                </label>
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 13px; color: #fff;">رصيد Google Play: US$ 0,16</span>
                    <span style="color: #3b82f6;">▶</span>
                </div>
            </div>

            <div style="font-size: 13px; color: #9aa0a6; margin-top: 10px;">إضافة طريقة دفع إلى حسابك على Google</div>

            <!-- استخدام الرمز -->
            <div class="pm-item" onclick="toggleInputSection('codeSection')">
                <div style="color: #9aa0a6;">›</div>
                <div class="pm-item-right">
                    <span style="font-size: 13px; color: #fff;">استخدام الرمز</span>
                    <span style="font-size: 14px;">⌨️</span>
                </div>
            </div>
            <div id="codeSection" class="dynamic-input-section">
                <input type="text" id="redeemCodeInput" placeholder="أدخل رمز الاسترداد (مثال: PLOT-XXXX-YYYY)">
                <button class="dynamic-save-btn" onclick="saveRedeemCode()">تفعيل الرمز</button>
            </div>

            <!-- إضافة PayPal -->
            <div class="pm-item" onclick="toggleInputSection('paypalSection')">
                <div style="color: #9aa0a6;">›</div>
                <div class="pm-item-right">
                    <span style="font-size: 13px; color: #fff;">إضافة PayPal</span>
                    <span style="font-size: 14px; color: #003087; font-weight: bold;">P</span>
                </div>
            </div>
            <div id="paypalSection" class="dynamic-input-section">
                <input type="email" id="paypalEmailInput" placeholder="أدخل البريد الإلكتروني لحساب PayPal">
                <button class="dynamic-save-btn" onclick="savePayPal()">ربط الحساب</button>
            </div>

            <!-- إضافة بطاقة بنكية (مع الشعارات في اليسار) -->
            <div class="pm-item" onclick="toggleInputSection('cardSection')">
                <div style="display: flex; align-items: center; gap: 4px;">
                    <span style="font-size: 10px; color: #9aa0a6;">+ أخرى</span>
                    <div style="background: #fff; padding: 1px 4px; border-radius: 3px; font-size: 9px; color: #1a1f71; font-weight: bold;">VISA</div>
                    <div style="background: #fff; padding: 1px 4px; border-radius: 3px; font-size: 9px; color: #eb001b; font-weight: bold;">MC</div>
                </div>
                <div class="pm-item-right">
                    <span style="font-size: 13px; color: #fff;">إضافة بطاقة</span>
                    <span style="font-size: 14px;">💳</span>
                </div>
            </div>
            <div id="cardSection" class="dynamic-input-section">
                <input type="text" placeholder="اسم حامل البطاقة (الاسم الثلاثي)">
                <input type="text" placeholder="رقم البطاقة (16 رقم)">
                <div style="display: flex; gap: 8px;">
                    <input type="text" placeholder="MM/YY">
                    <input type="password" placeholder="CVV" maxlength="4">
                </div>
                <button class="dynamic-save-btn" onclick="saveCard()">حفظ البطاقة</button>
            </div>

            <!-- شراقة رصيد -->
            <div class="pm-item">
                <div style="color: #9aa0a6;">›</div>
                <div class="pm-item-right">
                    <span style="font-size: 13px; color: #fff;">شراء رصيد Google Play</span>
                    <span>▶</span>
                </div>
            </div>
        </div>
    </div>

    <!-- نافذة قراءة القصة -->
    <div id="storyModal" class="story-modal-overlay">
        <div class="story-modal-content">
            <div class="story-modal-header">
                <button class="story-modal-close" onclick="closeStoryModal()">✕</button>
                <div id="modalStoryTitle" class="story-modal-title">عنوان القصة</div>
            </div>
            <div id="modalStoryBody" class="story-modal-body">
                تفاصيل القصة هنا...
            </div>
            <div class="story-modal-footer">
                <button class="copy-story-btn" onclick="copyStoryText()">نسخ تفاصيل القصة</button>
            </div>
        </div>
    </div>

    <script>
        let selectedPlanName = "PlotCraft Pro Weekly";
        let selectedPlanPrice = "9.99";

        function openSubscriptionScreen() {
            document.getElementById('subscriptionScreen').classList.add('active');
        }
        function closeSubscriptionScreen() {
            document.getElementById('subscriptionScreen').classList.remove('active');
        }

        function selectPlan(element, name, price) {
            document.querySelectorAll('.plan-box').forEach(el => el.classList.remove('selected'));
            element.classList.add('selected');
            selectedPlanName = name;
            selectedPlanPrice = price;
        }

        function openGPlayModal() {
            document.getElementById('gplayPlanTitle').innerText = selectedPlanName;
            document.getElementById('gplayPriceText').innerText = "US$/week " + selectedPlanPrice;
            document.getElementById('gplayModal').classList.add('active');
        }
        function closeGPlayModal() {
            document.getElementById('gplayModal').classList.remove('active');
        }

        function openPaymentMethodsModal() {
            document.getElementById('paymentMethodsModal').classList.add('active');
        }
        function closePaymentMethodsModal() {
            document.getElementById('paymentMethodsModal').classList.remove('active');
        }

        function toggleGPlayBalance() {
            const isChecked = document.getElementById('gplayBalanceToggle').checked;
            alert(isChecked ? "تم تشغيل رصيد Google Play" : "تم إطفاء رصيد Google Play");
        }

        function toggleInputSection(sectionId) {
            const section = document.getElementById(sectionId);
            const isActive = section.classList.contains('active');
            // إغلاق كل الحقول أولاً
            document.querySelectorAll('.dynamic-input-section').forEach(sec => sec.classList.remove('active'));
            if (!isActive) {
                section.classList.add('active');
            }
        }

        function saveRedeemCode() {
            const code = document.getElementById('redeemCodeInput').value;
            if(code.trim() === "") { alert("يرجى إدخال الرمز أولاً"); return; }
            alert("تم التحقق من الرمز بنجاح: " + code);
            document.getElementById('codeSection').classList.remove('active');
        }

        function savePayPal() {
            const email = document.getElementById('paypalEmailInput').value;
            if(email.trim() === "") { alert("يرجى إدخال البريد الإلكتروني"); return; }
            alert("تم ربط حساب PayPal بنجاح: " + email);
            document.getElementById('paypalSection').classList.remove('active');
        }

        function saveCard() {
            alert("تم حفظ البطاقة البنكية بنجاح وتشفير البيانات بأمان.");
            document.getElementById('cardSection').classList.remove('active');
        }

        function openStoryModal(title, text) {
            document.getElementById('modalStoryTitle').innerText = title;
            document.getElementById('modalStoryBody').innerText = text;
            document.getElementById('storyModal').classList.add('active');
        }
        function closeStoryModal() {
            document.getElementById('storyModal').classList.remove('active');
        }
        function copyStoryText() {
            const text = document.getElementById('modalStoryBody').innerText;
            navigator.clipboard.writeText(text);
            alert("تم نسخ تفاصيل القصة بنجاح!");
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=850, scrolling=True)

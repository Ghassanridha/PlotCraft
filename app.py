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
            -webkit-tap-highlight-color: transparent;
        }

        body, html {
            width: 100%;
            height: 100%;
            background-color: #0b0f19;
            overflow-x: hidden;
        }

        /* الشاشات المختلفة */
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
            border: 1px solid rgba(255, 255, 255, 0.2);
            cursor: pointer;
            transition: 0.2s;
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
            transition: 0.2s;
            position: relative;
        }

        .interactive-card:active {
            transform: scale(0.97);
            background: rgba(30, 40, 65, 0.85);
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
            mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 11h-1V7c0-1.1-.9-2-2-2H8c-1.1 0-2 .9-2 2v4H5c-1.1 0-2 .9-2 2v4c0 1.1.9 2 2 2h1v1c0 .55.45 1 1 1s1-.45 1-1v-1h8v1c0 .55.45 1 1 1s1-.45 1-1v-1h1c1.1 0 2-.9 2-2v-4c0-1.1-.9-2-2-2zM8 7h8v4H8V7zm3 9c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm4 0c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1 z"/></svg>') no-repeat center;
            -webkit-mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 11h-1V7c0-1.1-.9-2-2-2H8c-1.1 0-2 .9-2 2v4H5c-1.1 0-2 .9-2 2v4c0 1.1.9 2 2 2h1v1c0 .55.45 1 1 1s1-.45 1-1v-1h8v1c0 .55.45 1 1 1s1-.45 1-1v-1h1c1.1 0 2-.9 2-2v-4c0-1.1-.9-2-2-2zM8 7h8v4H8V7zm3 9c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm4 0c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1 z"/></svg>') no-repeat center;
            background-size: contain;
        }

        .speed-custom-icon {
            width: 22px;
            height: 22px;
            background: #ffffff;
            mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M4 14l3-3m0 0l3 3m-3-3v8"/><path d="M12 6c3.3 0 6 2.7 6 6s-2.7 6-6 6"/><path d="M15 3c4.97 0 9 4.03 9 9s-4.03 9-9 9"/></svg>') no-repeat center;
            -webkit-mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M4 14l3-3m0 0l3 3m-3-3v8"/><path d="M12 6c3.3 0 6 2.7 6 6s-2.7 6-6 6"/><path d="M15 3c4.97 0 9 4.03 9 9s-4.03 9-9 9"/></svg>') no-repeat center;
            background-size: contain;
        }

        .card-title-group-left {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
        }

        .pro-badge-top {
            display: flex;
            align-items: center;
            gap: 4px;
            background: rgba(255, 255, 255, 0.15);
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 3px 8px;
            border-radius: 10px;
            color: #ffffff;
            font-size: 10px;
            font-weight: 700;
            margin-bottom: 8px;
            width: fit-content;
        }

        .pro-lock-icon {
            width: 10px;
            height: 10px;
            background: #ffffff;
            mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>') no-repeat center;
            -webkit-mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>') no-repeat center;
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
            cursor: pointer;
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

        .movie-card.m1 { background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), url('https://images.unsplash.com/photo-1534447677768-be436bb09401?q=80&w=300&auto=format&fit=crop') center/cover; }
        .movie-card.m2 { background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), url('https://images.unsplash.com/photo-1485846234645-a62644f84728?q=80&w=300&auto=format&fit=crop') center/cover; }
        .movie-card.m3 { background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), url('https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?q=80&w=300&auto=format&fit=crop') center/cover; }

        .movie-title {
            color: #ffffff;
            font-size: 10px;
            font-weight: 700;
            text-shadow: 0 2px 4px rgba(0,0,0,0.8);
            line-height: 1.2;
        }

        /* --- واجهة الأعمال --- */
        #worksScreen {
            background-color: #0b0f19;
            display: none;
            flex-direction: column;
            min-height: 100vh;
            padding: 20px;
            align-items: center;
        }
        #worksScreen.active {
            display: flex;
        }

        .works-tabs-container {
            display: flex;
            background: #141824;
            border-radius: 30px;
            padding: 4px;
            width: 100%;
            max-width: 360px;
            margin-bottom: 80px;
            border: 1px solid rgba(255,255,255,0.08);
        }

        .works-tab {
            flex: 1;
            text-align: center;
            padding: 10px 0;
            font-size: 13px;
            font-weight: 600;
            color: #94a3b8;
            background: transparent;
            border-radius: 25px;
            cursor: pointer;
            transition: all 0.2s ease;
            user-select: none;
        }

        .works-tab.active {
            background: #1e2538 !important;
            color: #ffffff !important;
            font-weight: 700;
        }

        .works-empty-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            flex-grow: 1;
            text-align: center;
            margin-top: 40px;
        }

        .works-box-icon {
            width: 90px;
            height: 90px;
            margin-bottom: 24px;
            opacity: 0.8;
            background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%2364748b" stroke-width="1.5"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>') no-repeat center;
            background-size: contain;
        }

        .works-empty-text-sub {
            color: #64748b;
            font-size: 13px;
            margin-bottom: 35px;
        }

        .works-create-btn {
            width: 100%;
            max-width: 220px;
            background: #ffffff;
            color: #0b0f19;
            font-size: 14px;
            font-weight: 700;
            padding: 10px 16px;
            border-radius: 14px;
            border: none;
            cursor: pointer;
            text-align: center;
            box-shadow: 0 4px 15px rgba(255,255,255,0.15);
            transition: 0.2s;
        }
        .works-create-btn:active {
            transform: scale(0.98);
            background: #e2e8f0;
        }

        /* شاشة تفاصيل "خطوة بخطوة" */
        .step-container {
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .ai-assistant-card {
            background: #141824;
            border: 1px solid #1e293b;
            border-radius: 16px;
            padding: 16px;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .ai-header-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .ai-title {
            color: #ff2a85;
            font-size: 14px;
            font-weight: 700;
        }

        .ai-badge-circle {
            width: 32px;
            height: 32px;
            background: linear-gradient(135deg, #ff2a85, #7928ca);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
            font-size: 11px;
            box-shadow: 0 2px 8px rgba(255,42,133,0.4);
        }

        .ai-desc {
            color: #94a3b8;
            font-size: 12px;
            line-height: 1.5;
        }

        .story-setup-box {
            background: #141824;
            border: 1px solid #1e293b;
            border-radius: 16px;
            padding: 16px;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .setup-header-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .setup-main-title {
            color: #ffffff;
            font-size: 15px;
            font-weight: 700;
        }

        .counter-badge {
            background-color: #1e293b;
            color: #94a3b8;
            padding: 3px 10px;
            border-radius: 10px;
            font-size: 11px;
            font-weight: 600;
        }

        .setup-subtitle {
            color: #64748b;
            font-size: 11px;
        }

        .setup-row-item {
            background: #1a2234;
            border-radius: 12px;
            padding: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .item-info h4 {
            color: #ffffff;
            font-size: 13px;
            font-weight: 700;
            margin-bottom: 2px;
        }

        .item-info p {
            color: #94a3b8;
            font-size: 11px;
        }

        .action-add-btn {
            background: rgba(59, 130, 246, 0.15);
            color: #3b82f6;
            border: 1px solid rgba(59, 130, 246, 0.3);
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 600;
            cursor: pointer;
            transition: 0.2s;
        }

        .action-add-btn:active {
            transform: scale(0.95);
        }

        /* --- واجهة "إضافة شخصية" الجديدة --- */
        #addCharacterScreen {
            background-color: #0b0f19;
            display: none;
            flex-direction: column;
            min-height: 100vh;
            padding: 20px;
            position: relative;
        }
        #addCharacterScreen.active {
            display: flex;
        }
        .add-char-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
            padding-bottom: 15px;
            border-bottom: 1px solid rgba(255,255,255,0.08);
            margin-bottom: 20px;
        }
        .add-char-title {
            color: #ffffff;
            font-size: 18px;
            font-weight: 700;
        }
        .add-char-back {
            background: none;
            border: none;
            color: #fff;
            font-size: 20px;
            cursor: pointer;
        }

        .char-main-card {
            background: #141824;
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 20px;
            padding: 16px;
            display: flex;
            flex-direction: column;
            gap: 16px;
            margin-bottom: 16px;
        }
        .char-section-label {
            color: #ffffff;
            font-size: 15px;
            font-weight: 700;
            text-align: right;
        }
        
        /* المربع العلوي الكبير مع ضبط قياس الصورة تماماً لعدم قص الوجه */
        .char-big-upload-box {
            background: #1a2030;
            border: 1px dashed rgba(255,255,255,0.2);
            border-radius: 16px;
            height: 180px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 8px;
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }
        .char-big-upload-box img {
            width: 100%;
            height: 100%;
            object-fit: contain;
            background-color: #000;
            position: absolute;
            top: 0;
            left: 0;
        }
        .remove-big-img {
            position: absolute;
            top: 10px;
            left: 10px;
            background: rgba(0,0,0,0.7);
            color: #fff;
            border: none;
            width: 28px;
            height: 28px;
            border-radius: 50%;
            cursor: pointer;
            z-index: 5;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 14px;
        }

        .char-thumbs-row {
            display: flex;
            gap: 10px;
            overflow-x: auto;
            padding-bottom: 4px;
            direction: rtl;
            scrollbar-width: none;
        }
        .char-thumbs-row::-webkit-scrollbar { display: none; }
        
        .thumb-wrapper {
            position: relative;
            flex-shrink: 0;
        }
        .char-thumb-item {
            width: 55px;
            height: 55px;
            border-radius: 12px;
            object-fit: cover;
            border: 1.5px solid rgba(255,255,255,0.15);
            cursor: pointer;
            display: block;
        }
        .thumb-remove-badge {
            position: absolute;
            top: -4px;
            left: -4px;
            background: #ef4444;
            color: #fff;
            width: 18px;
            height: 18px;
            border-radius: 50%;
            font-size: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            border: 1px solid #fff;
            z-index: 2;
        }
        .char-add-role-box {
            width: 55px;
            height: 55px;
            border-radius: 12px;
            background: #1a2030;
            border: 1.5px dashed rgba(255,255,255,0.3);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: #94a3b8;
            font-size: 18px;
            cursor: pointer;
            flex-shrink: 0;
            gap: 2px;
        }
        .char-add-role-text { font-size: 10px; }

        .char-name-input {
            width: 100%;
            background: #1a2030;
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 14px;
            padding: 14px;
            color: #ffffff;
            font-size: 14px;
            outline: none;
            text-align: right;
        }
        .char-name-input::placeholder { color: #64748b; }

        .char-submit-btn-wrapper {
            position: fixed;
            bottom: 20px;
            left: 20px;
            right: 20px;
            z-index: 20;
        }
        .char-submit-btn {
            width: 100%;
            background: linear-gradient(135deg, #3b82f6 0%, #ec4899 100%);
            color: #ffffff;
            font-size: 16px;
            font-weight: 700;
            padding: 16px;
            border-radius: 24px;
            border: none;
            cursor: pointer;
            text-align: center;
            box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4);
        }

        /* قائمة اختيار المصدر: كاميرا باليمين، ألبوم باليسار */
        .source-modal {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.7);
            z-index: 999;
            align-items: center;
            justify-content: center;
        }
        .source-modal.show { display: flex; }
        .source-modal-content {
            background: #141824;
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 20px;
            padding: 20px;
            width: 90%;
            max-width: 320px;
            display: flex;
            flex-direction: column;
            gap: 14px;
            text-align: center;
        }
        .source-buttons-row {
            display: flex;
            gap: 10px;
            justify-content: space-between;
        }
        .source-btn {
            flex: 1;
            background: #1e2538;
            color: #fff;
            border: 1px solid rgba(255,255,255,0.1);
            padding: 12px 8px;
            border-radius: 12px;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 6px;
        }
        .source-btn:active { background: #2a344e; }

        /* واجهة صفحة الأدوات */
        #toolsScreen { background: #0b0f19; overflow-y: auto; }
        .tools-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 20px;
            background: rgba(11, 15, 25, 0.85);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid rgba(255,255,255,0.08);
        }
        .tools-header-title { color: #ffffff; font-size: 20px; font-weight: 700; }
        .tools-upgrade-btn { background: rgba(255, 255, 255, 0.12); border: 1px solid rgba(255, 255, 255, 0.2); padding: 6px 14px; border-radius: 20px; color: #ffffff; font-size: 13px; font-weight: 500; cursor: pointer; }
        .tools-body { padding: 16px; display: flex; flex-direction: column; gap: 16px; }
        .tool-card-item { position: relative; width: 100%; height: 180px; border-radius: 20px; overflow: hidden; display: flex; flex-direction: column; justify-content: flex-end; padding: 18px; box-shadow: 0 6px 20px rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.1); cursor: pointer; }
        .tool-card-1 { background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), url('https://images.unsplash.com/photo-1542751371-adc38448a05e?q=80&w=600&auto=format&fit=crop') center/cover no-repeat; }
        .tool-card-2 { background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), url('https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=600&auto=format&fit=crop') center/cover no-repeat; }
        .tool-info-box { position: relative; z-index: 2; }
        .tool-main-title { color: #ffffff; font-size: 17px; font-weight: 700; margin-bottom: 4px; text-shadow: 0 2px 4px rgba(0,0,0,0.8); }
        .tool-sub-desc { color: #cbd5e1; font-size: 12px; text-shadow: 0 1px 3px rgba(0,0,0,0.8); }
        .tool-arrow-icon { position: absolute; top: 16px; right: 16px; color: #ffffff; font-size: 16px; font-weight: bold; background: rgba(0,0,0,0.4); width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; backdrop-filter: blur(5px); }

        /* واجهة صفحة الاشتراكات */
        #subscriptionScreen { background: #0b0f19; overflow-y: auto; position: relative; }
        .animated-bg-container { position: absolute; top: 0; left: 0; width: 100%; height: 100%; overflow: hidden; z-index: 1; opacity: 0.35; pointer-events: none; }
        .explosion-glow { position: absolute; width: 300px; height: 300px; background: radial-gradient(circle, rgba(59,130,246,0.6) 0%, rgba(139,92,246,0.2) 50%, transparent 70%); border-radius: 50%; animation: pulseExplosion 4s infinite alternate ease-in-out; }
        .glow-1 { top: -50px; right: -50px; }
        .glow-2 { bottom: 100px; left: -80px; animation-delay: 2s; background: radial-gradient(circle, rgba(236,72,153,0.5) 0%, rgba(59,130,246,0.2) 50%, transparent 70%); }
        @keyframes pulseExplosion { 0% { transform: scale(1) translate(0, 0); opacity: 0.3; } 50% { transform: scale(1.4) translate(20px, 30px); opacity: 0.7; } 100% { transform: scale(1.1) translate(-10px, 15px); opacity: 0.4; } }

        .page-header-sub, .content-body-sub { position: relative; z-index: 2; }
        .page-header-sub { display: flex; align-items: center; justify-content: space-between; padding: 20px; border-bottom: 1px solid rgba(255,255,255,0.08); background: rgba(11, 15, 25, 0.75); backdrop-filter: blur(10px); }
        .back-btn-sub { background: rgba(255,255,255,0.1); border: none; color: #fff; width: 36px; height: 36px; border-radius: 50%; font-size: 16px; cursor: pointer; display: flex; align-items: center; justify-content: center; }
        .page-title-sub { color: #ffffff; font-size: 18px; font-weight: 700; }
        .content-body-sub { padding: 20px; display: flex; flex-direction: column; gap: 16px; }
        .plans-list { display: flex; flex-direction: column; gap: 12px; }
        .plan-card { background: rgba(20, 25, 40, 0.85); backdrop-filter: blur(12px); border: 1.5px solid rgba(255, 255, 255, 0.15); border-radius: 16px; padding: 16px; cursor: pointer; transition: 0.2s; position: relative; }
        .plan-card.selected { border-color: #3b82f6; background: rgba(30, 41, 75, 0.95); box-shadow: 0 0 20px rgba(59, 130, 246, 0.4); }
        .plan-top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px; }
        .plan-name { color: #ffffff; font-size: 15px; font-weight: 700; }
        .plan-price { background: rgba(255, 255, 255, 0.12); padding: 4px 10px; border-radius: 10px; color: #ffffff; font-size: 12px; font-weight: 600; }
        .plan-desc { color: #94a3b8; font-size: 12px; }
        .new-tag { position: absolute; top: 12px; left: 12px; background: #3b82f6; color: #fff; font-size: 10px; padding: 2px 8px; border-radius: 8px; font-weight: 600; }
        .best-value-tag { position: absolute; top: 12px; left: 12px; background: linear-gradient(135deg, #f59e0b, #ec4899); color: #fff; font-size: 10px; padding: 2px 8px; border-radius: 8px; font-weight: 600; }
        .action-main-btn { width: 100%; background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%); color: #ffffff; font-size: 15px; font-weight: 700; padding: 14px; border-radius: 20px; border: none; cursor: pointer; text-align: center; box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4); margin-top: 10px; }

        /* شريط التنقل السفلي الثابت */
        .plotcraft-nav-bar {
            position: fixed;
            bottom: 0; left: 0; width: 100%;
            background-color: #0b0f19;
            padding: 10px 15px;
            display: flex; justify-content: center; align-items: center; gap: 12px;
            z-index: 999999; box-sizing: border-box; direction: rtl;
            box-shadow: 0 -4px 15px rgba(0,0,0,0.6);
            transition: transform 0.3s ease;
        }
        .plotcraft-nav-bar.hidden { transform: translateY(120%); }
        .plotcraft-nav-pill { background-color: #161b22; border: 1px solid #30363d; border-radius: 35px; display: flex; justify-content: space-around; align-items: center; padding: 8px 15px; flex-grow: 1; max-width: 380px; }
        .plotcraft-nav-item { display: flex; align-items: center; gap: 6px; color: #8b949e; font-size: 13px; text-decoration: none; cursor: pointer; white-space: nowrap; }
        .plotcraft-nav-item.active { color: #ffffff; font-weight: bold; }
        .plotcraft-nav-square { background-color: #161b22; border: 1px solid #30363d; border-radius: 16px; width: 48px; height: 48px; display: flex; justify-content: center; align-items: center; flex-shrink: 0; cursor: pointer; position: relative; }
    </style>
</head>
<body>

    <!-- الواجهة الرئيسية -->
    <div id="homeScreen" class="screen-view active">
        <div class="hero-box">
            <div class="top-header">
                <div class="brand-title">PlotCraft</div>
                <div class="upgrade-badge" onclick="switchScreen('subscriptionScreen', event)">ترقية</div>
            </div>

            <div class="welcome-section">
                <h1>مساء الخير، أيها المخرج<br>أي قصة سنصنع اليوم؟</h1>
            </div>

            <div class="cards-row">
                <div class="interactive-card" onclick="switchScreen('stepByStepScreen', event)">
                    <div class="card-header-row">
                        <div class="card-title-group-left">
                            <div class="card-title">خطوة بخطوة</div>
                            <span class="exact-bot-icon"></span>
                        </div>
                    </div>
                    <div class="card-subtitle">راجع كل خطوة</div>
                </div>

                <div class="interactive-card" id="speedCard" onclick="handleSpeedCardClick(event)">
                    <div class="pro-badge-top" id="proBadgeContainer">
                        <span id="proBadgeText">Pro only</span>
                        <span class="pro-lock-icon" id="proLockIcon"></span>
                    </div>
                    <div class="card-header-row">
                        <div class="card-title-group-left">
                            <div class="card-title">سريع</div>
                            <span class="speed-custom-icon"></span>
                        </div>
                    </div>
                    <div class="card-subtitle" id="speedCardSubtitle">إدخال واحد، فيديو كامل</div>
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

    <!-- واجهة الزر الرابع المنفصل -->
    <div id="sparkleDialogScreen" class="screen-view">
        <div style="display:flex; justify-content:space-between; align-items:center; width:100%; margin-bottom:30px; z-index:2; padding: 20px;">
            <button style="background:none; border:none; color:#fff; font-size:20px; cursor:pointer;" onclick="switchScreen('homeScreen', event)">✕</button>
            <div class="brand-title">Plotcraft</div>
            <div style="background: rgba(255,255,255,0.15); padding: 6px 16px; border-radius: 20px; color: #fff; font-size: 13px; cursor:pointer;" onclick="switchScreen('subscriptionScreen', event)">ترقية</div>
        </div>

        <div style="display:flex; flex-direction:column; align-items:center; text-align:center; padding: 0 20px; gap:20px;">
            <svg width="65" height="65" viewBox="0 0 24 24" fill="#93c5fd"><path d="M12 2C12 7.5 16.5 12 22 12C16.5 12 12 16.5 12 22C12 16.5 7.5 12 2 12C7.5 12 12 7.5 12 2Z"/></svg>
            <div style="color: #fff; font-size: 20px; font-weight: 700;">طاب مساؤك، أيها المخرج<br>أي قصة سنصنع اليوم؟</div>
            <div style="display:flex; flex-direction:column; gap:12px; width:100%; max-width:420px;">
                <div style="background: rgba(20,25,40,0.75); border: 1px solid rgba(255,255,255,0.12); border-radius: 16px; padding: 16px; display:flex; justify-content:space-between; align-items:center; cursor:pointer;" onclick="switchScreen('stepByStepScreen', event)">
                    <div style="color:#fff; font-weight:700;">خطوة بخطوة</div>
                    <div style="color:#94a3b8;">↗</div>
                </div>
                <div style="background: rgba(20,25,40,0.75); border: 1px solid rgba(255,255,255,0.12); border-radius: 16px; padding: 16px; display:flex; justify-content:space-between; align-items:center; cursor:pointer;" onclick="handleSpeedCardClick(event)">
                    <div style="color:#fff; font-weight:700;">سريع</div>
                    <div style="color:#94a3b8;" id="sparkleLockSign">🔒</div>
                </div>
            </div>
        </div>
    </div>

    <!-- واجهة صفحة "الأدوات" -->
    <div id="toolsScreen" class="screen-view">
        <div class="tools-header">
            <div class="tools-header-title">الأدوات</div>
            <div class="tools-upgrade-btn" onclick="switchScreen('subscriptionScreen', event)">ترقية</div>
        </div>
        <div class="tools-body">
            <div class="tool-card-item tool-card-1" onclick="alert('تأثيرات الفيديو')">
                <div class="tool-arrow-icon">‹</div>
                <div class="tool-info-box"><div class="tool-main-title">تأثيرات الفيديو</div><div class="tool-sub-desc">أضف لمسة سينمائية</div></div>
            </div>
            <div class="tool-card-item tool-card-2" onclick="alert('توليد الفيديو')">
                <div class="tool-arrow-icon">‹</div>
                <div class="tool-info-box"><div class="tool-main-title">توليد الفيديو</div><div class="tool-sub-desc">حول توجيهاً إلى فيديو خاص بك</div></div>
            </div>
        </div>
    </div>

    <!-- واجهة "الأعمال" -->
    <div id="worksScreen" class="screen-view">
        <div class="works-tabs-container">
            <div class="works-tab active" onclick="switchWorksTab(this)">المشاريع</div>
            <div class="works-tab" onclick="switchWorksTab(this)">مكتبة الوسائط</div>
        </div>
        <div class="works-empty-content">
            <div class="works-box-icon"></div>
            <div class="works-empty-text-sub">ستظهر هنا مشاريع القصة الخاصة بك.</div>
            <button class="works-create-btn" onclick="openSparkleDialog(event)">إنشاء قصة</button>
        </div>
    </div>

    <!-- واجهة تفاصيل "خطوة بخطوة" -->
    <div id="stepByStepScreen" class="screen-view">
        <div style="display:flex; justify-content:space-between; align-items:center; padding:20px; border-bottom:1px solid rgba(255,255,255,0.08);">
            <button style="background:rgba(255,255,255,0.1); border:none; color:#fff; width:36px; height:36px; border-radius:50%; cursor:pointer;" onclick="switchScreen('homeScreen', event)">✕</button>
            <div style="color:#fff; font-weight:700;">PlotCraft</div>
            <div style="width:36px;"></div>
        </div>

        <div class="step-container">
            <div class="ai-assistant-card">
                <div class="ai-header-row">
                    <div class="ai-title">مساعد AI بلوت كرافت</div>
                    <div class="ai-badge-circle">AI+</div>
                </div>
                <div class="ai-desc">عزيزي المخرج، استمتع بإنشاء وتخصيص تفاصيل فيلمك خطوة بخطوة بدقة احترافية عالية.</div>
            </div>

            <div class="story-setup-box">
                <div class="setup-header-row">
                    <div class="setup-main-title">إعداد القصة</div>
                    <div class="counter-badge">0/2</div>
                </div>
                <div class="setup-subtitle">أضف الشخصيات والحكاية أولاً، ثم أكمل الخطوات:</div>

                <div class="setup-row-item">
                    <div class="item-info">
                        <h4>الشخصيات</h4>
                        <p>أضف صورتين كحد أقصى لشخصيات القصة</p>
                    </div>
                    <button class="action-add-btn" onclick="openAddCharacter(event)">إضافة</button>
                </div>

                <div class="setup-row-item">
                    <div class="item-info">
                        <h4>الحكاية</h4>
                        <p>اكتب أو صف حبكة قصتك هنا</p>
                    </div>
                    <button class="action-add-btn" onclick="alert('فتح إعداد الحكاية')">إضافة</button>
                </div>
            </div>

            <div class="bottom-next-row" style="display:flex; justify-content:flex-end; margin-top:10px;">
                <button style="background:linear-gradient(135deg,#3b82f6,#8b5cf6); color:#fff; font-weight:700; padding:10px 24px; border-radius:12px; border:none; cursor:pointer;" onclick="alert('تم حفظ الخطوات بنجاح!')">التالي</button>
            </div>
        </div>
    </div>

    <!-- واجهة "إضافة شخصية" الجديدة المطابقة تماماً للصورة -->
    <div id="addCharacterScreen" class="screen-view">
        <div class="add-char-header">
            <button class="add-char-back" onclick="switchScreen('stepByStepScreen', event)">‹</button>
            <div class="add-char-title">إضافة شخصية</div>
            <div style="width: 20px;"></div>
        </div>

        <div style="padding: 0 16px 100px 16px;">
            <div class="char-main-card">
                <div class="char-section-label">الشخصية</div>
                
                <!-- المربع العلوي الكبير مع ضبط القياس لعدم قص الوجه -->
                <div class="char-big-upload-box" id="bigUploadBox" onclick="showSourceModal()">
                    <div id="bigBoxInner" style="display:flex; flex-direction:column; align-items:center; gap:8px; color:#94a3b8; font-size:13px;">
                        <div style="width:32px; height:32px; background:rgba(255,255,255,0.08); border-radius:50%; display:flex; align-items:center; justify-content:center; color:#cbd5e1;">↑</div>
                        <span>رفع صورة</span>
                    </div>
                </div>

                <!-- السرة (الشريط السفلي للصور مع زر الإضافة الدور +) -->
                <div class="char-thumbs-row" id="thumbsRow">
                    <div class="char-add-role-box" onclick="showSourceModal()">
                        <span>+</span>
                        <span class="char-add-role-text">الدور</span>
                    </div>
                    <!-- صور جاهزة افتراضية -->
                    <div class="thumb-wrapper">
                        <img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=150&auto=format&fit=crop" class="char-thumb-item" onclick="selectThumb(this)">
                        <div class="thumb-remove-badge" onclick="removeThumb(this, event)">✕</div>
                    </div>
                    <div class="thumb-wrapper">
                        <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?q=80&w=150&auto=format&fit=crop" class="char-thumb-item" onclick="selectThumb(this)">
                        <div class="thumb-remove-badge" onclick="removeThumb(this, event)">✕</div>
                    </div>
                    <div class="thumb-wrapper">
                        <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?q=80&w=150&auto=format&fit=crop" class="char-thumb-item" onclick="selectThumb(this)">
                        <div class="thumb-remove-badge" onclick="removeThumb(this, event)">✕</div>
                    </div>
                </div>
            </div>

            <div class="char-main-card">
                <div class="char-section-label">اسم الشخصية</div>
                <input type="text" class="char-name-input" placeholder="مثال: شخصية مرجعية">
            </div>
        </div>

        <div class="char-submit-btn-wrapper">
            <button class="char-submit-btn" onclick="alert('تم حفظ الشخصية بنجاح!'); switchScreen('stepByStepScreen', event);">إرسال</button>
        </div>
    </div>

    <!-- نافذة منبثقة لاختيار المصدر: كاميرا باليمين، ألبوم باليسار -->
    <div class="source-modal" id="sourceModal">
        <div class="source-modal-content">
            <div style="color:#fff; font-weight:700; font-size:15px; margin-bottom:2px;">اختر مصدر الصورة</div>
            <div class="source-buttons-row">
                <!-- كاميرا في جهة اليمين -->
                <button class="source-btn" onclick="triggerFileInput('camera')">
                    <span style="font-size:20px;">📷</span>
                    <span>كاميرا</span>
                </button>
                <!-- ألبوم الصور في جهة اليسار -->
                <button class="source-btn" onclick="triggerFileInput('album')">
                    <span style="font-size:20px;">🖼️</span>
                    <span>ألبوم الصور</span>
                </button>
            </div>
            <button style="background:none; border:none; color:#94a3b8; margin-top:4px; cursor:pointer; font-size:13px;" onclick="closeSourceModal()">إلغاء</button>
        </div>
    </div>

    <!-- عناصر رفع ملفات مخفية للكاميرا والألبوم -->
    <input type="file" id="cameraInput" accept="image/*" capture="environment" style="display:none;" onchange="handleFileSelected(event)">
    <input type="file" id="albumInput" accept="image/*" style="display:none;" onchange="handleFileSelected(event)">

    <!-- واجهة صفحة الاشتراكات الكاملة مع الخلفية والخطة الثلاثية -->
    <div id="subscriptionScreen" class="screen-view">
        <div class="animated-bg-container">
            <div class="explosion-glow glow-1"></div>
            <div class="explosion-glow glow-2"></div>
        </div>

        <div class="page-header-sub">
            <button class="back-btn-sub" onclick="switchScreen('homeScreen', event)">✕</button>
            <div class="page-title-sub">ترقية الحساب</div>
            <div style="width: 36px;"></div>
        </div>

        <div class="content-body-sub">
            <div style="text-align: center; margin-bottom: 5px;">
                <div style="color: #ffffff; font-size: 18px; font-weight: 700; margin-bottom: 4px;">حول أفكارك إلى PlotCraft</div>
                <div style="color: #94a3b8; font-size: 12px;">أنشئ كل لقطة وعدلها وأكملها بسرعة.</div>
            </div>

            <div class="plans-list">
                <div class="plan-card selected" onclick="selectPlan(this)">
                    <div class="plan-top">
                        <div class="plan-name">PlotCraft Pro Weekly</div>
                        <div class="plan-price">9.99 دولار أمريكي / أسبوع</div>
                    </div>
                    <div class="plan-desc">500 نقطة / أسبوعياً، جرب PlotCraft</div>
                </div>

                <div class="plan-card" onclick="selectPlan(this)">
                    <div class="new-tag">جديد</div>
                    <div class="plan-top">
                        <div class="plan-name">PlotCraft Pro Monthly</div>
                        <div class="plan-price">29.99 دولار أمريكي / شهر</div>
                    </div>
                    <div class="plan-desc">1800 نقطة / شهرياً، مثالي للمبدعين</div>
                </div>

                <div class="plan-card" onclick="selectPlan(this)">
                    <div class="best-value-tag">الأفضل قيمة</div>
                    <div class="plan-top">
                        <div class="plan-name">PlotCraft Pro Annual</div>
                        <div class="plan-price">69.99 دولار أمريكي / سنة</div>
                    </div>
                    <div class="plan-desc">5000 نقطة / سنوياً، إمكانيات غير محدودة للمخرجين المحترفين</div>
                </div>
            </div>

            <button class="action-main-btn" onclick="confirmSubscription()">اشتراك</button>
        </div>
    </div>

    <!-- شريط التنقل السفلي الثابت -->
    <div class="plotcraft-nav-bar" id="mainNavBar">
        <div class="plotcraft-nav-pill">
            <a href="#" class="plotcraft-nav-item active" id="navHome" onclick="switchScreen('homeScreen', event); setActiveNav('navHome')">
                <span>الرئيسية</span>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg>
            </a>
            <a href="#" class="plotcraft-nav-item" id="navTools" onclick="switchScreen('toolsScreen', event); setActiveNav('navTools')">
                <span>الأدوات</span>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"></path></svg>
            </a>
            <a href="#" class="plotcraft-nav-item" id="navWorks" onclick="switchScreen('worksScreen', event); setActiveNav('navWorks')">
                <span>الأعمال</span>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path></svg>
            </a>
        </div>

        <div class="plotcraft-nav-square" onclick="openSparkleDialog(event)" title="إنشاء سريع">
            <svg width="26" height="26" viewBox="0 0 24 24">
                <rect x="3" y="6" width="14" height="12" rx="3" fill="#94a3b8"/>
                <path d="M14 6h3c1.1 0 2 .9 2 2v8c0 1.1-.9 2-2 2h-3V6z" fill="#64748b"/>
                <polygon points="8,10 12,12 8,14" fill="#0b0f19"/>
                <path d="M8 3C8 4.65 6.65 6 5 6C6.65 6 8 7.35 8 9C8 7.35 9.35 6 11 6C9.35 6 8 4.65 8 3Z" fill="#3b82f6"/>
            </svg>
        </div>
    </div>

    <script>
        function switchScreen(screenId, event) {
            if (event) event.preventDefault();
            var screens = document.querySelectorAll('.screen-view');
            screens.forEach(s => s.classList.remove('active'));
            document.getElementById(screenId).classList.add('active');
            
            var navBar = document.getElementById('mainNavBar');
            if (screenId === 'sparkleDialogScreen' || screenId === 'addCharacterScreen') {
                navBar.classList.add('hidden');
            } else {
                navBar.classList.remove('hidden');
            }
            window.scrollTo(0, 0);
        }

        function openSparkleDialog(event) {
            switchScreen('sparkleDialogScreen', event);
            document.getElementById('mainNavBar').classList.add('hidden');
        }

        function openAddCharacter(event) {
            switchScreen('addCharacterScreen', event);
        }

        function setActiveNav(navId) {
            var items = document.querySelectorAll('.plotcraft-nav-item');
            items.forEach(i => i.classList.remove('active'));
            document.getElementById(navId).classList.add('active');
        }

        function switchWorksTab(element) {
            var tabs = document.querySelectorAll('.works-tab');
            tabs.forEach(t => t.classList.remove('active'));
            element.classList.add('active');
        }

        function selectPlan(element) {
            var cards = document.querySelectorAll('.plan-card');
            cards.forEach(c => c.classList.remove('selected'));
            element.classList.add('selected');
        }

        function showSourceModal() {
            document.getElementById('sourceModal').classList.add('show');
        }

        function closeSourceModal() {
            document.getElementById('sourceModal').classList.remove('show');
        }

        function triggerFileInput(type) {
            closeSourceModal();
            if (type === 'camera') {
                document.getElementById('cameraInput').click();
            } else {
                document.getElementById('albumInput').click();
            }
        }

        function handleFileSelected(event) {
            var file = event.target.files[0];
            if (file) {
                var reader = new FileReader();
                reader.onload = function(e) {
                    var imgSrc = e.target.result;
                    setBigBoxImage(imgSrc);
                    addThumbToRow(imgSrc);
                }
                reader.readAsDataURL(file);
            }
        }

        function setBigBoxImage(src) {
            var box = document.getElementById('bigUploadBox');
            box.innerHTML = '<button class="remove-big-img" onclick="clearBigBox(event)">✕</button><img src="' + src + '">';
        }

        function clearBigBox(event) {
            event.stopPropagation();
            var box = document.getElementById('bigUploadBox');
            box.innerHTML = '<div id="bigBoxInner" style="display:flex; flex-direction:column; align-items:center; gap:8px; color:#94a3b8; font-size:13px;"><div style="width:32px; height:32px; background:rgba(255,255,255,0.08); border-radius:50%; display:flex; align-items:center; justify-content:center; color:#cbd5e1;">↑</div><span>رفع صورة</span></div>';
        }

        function addThumbToRow(src) {
            var row = document.getElementById('thumbsRow');
            var wrapper = document.createElement('div');
            wrapper.className = 'thumb-wrapper';
            wrapper.innerHTML = '<img src="' + src + '" class="char-thumb-item" onclick="selectThumb(this)"><div class="thumb-remove-badge" onclick="removeThumb(this, event)">✕</div>';
            row.appendChild(wrapper);
        }

        function selectThumb(imgElement) {
            setBigBoxImage(imgElement.src);
        }

        function removeThumb(badgeElement, event) {
            event.stopPropagation();
            var wrapper = badgeElement.parentElement;
            var img = wrapper.querySelector('img');
            var bigBox = document.getElementById('bigUploadBox');
            var bigImg = bigBox.querySelector('img');
            
            if (bigImg && bigImg.src === img.src) {
                clearBigBox(event);
            }
            wrapper.remove();
        }

        function handleSpeedCardClick(event) {
            var isSub = localStorage.getItem('plotcraft_sub') === 'true';
            if (isSub) {
                alert('مفعل ومتاح للاستخدام الفوري.');
            } else {
                switchScreen('subscriptionScreen', event);
            }
        }

        function confirmSubscription() {
            localStorage.setItem('plotcraft_sub', 'true');
            alert('تم الاشتراك بنجاح!');
            switchScreen('homeScreen');
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=680, scrolling=True)

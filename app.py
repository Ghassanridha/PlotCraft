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
<html lang="ar" dir="rtl" id="htmlRoot">
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

        .screen-view {
            display: none;
            width: 100%;
            min-height: 100vh;
            background-color: #1f242d;
            flex-direction: column;
            padding-bottom: 90px;
        }

        .screen-view.active {
            display: flex;
        }

        #homeScreen.screen-view {
            background-color: #0b0f19;
        }

        #sparkleDialogScreen.screen-view {
            background-color: #0b0f19;
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
            margin-top: 15px;
        }
        [dir="rtl"] .welcome-section { text-align: right; }
        [dir="ltr"] .welcome-section { text-align: left; }

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
            color: #cbd5e1;
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

        .section-title { color: #ffffff; font-size: 18px; font-weight: 700; }
        .view-all { color: #cbd5e1; font-size: 13px; cursor: pointer; }

        .movies-carousel {
            display: flex;
            gap: 14px;
            overflow-x: auto;
            padding-bottom: 10px;
            scrollbar-width: none;
        }
        [dir="rtl"] .movies-carousel { flex-direction: row-reverse; }
        [dir="ltr"] .movies-carousel { flex-direction: row; }
        .movies-carousel::-webkit-scrollbar { display: none; }

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
            transition: transform 0.2s;
        }
        .movie-card:active { transform: scale(0.96); }

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

        .custom-alert-overlay {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.7);
            z-index: 99999999999;
            align-items: center;
            justify-content: center;
        }
        .custom-alert-overlay.show { display: flex; }
        .custom-alert-box {
            background: #282f3d;
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 20px;
            padding: 24px 20px;
            width: 85%;
            max-width: 280px;
            text-align: center;
            display: flex;
            flex-direction: column;
            gap: 18px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.6);
        }
        .custom-alert-msg { color: #ffffff; font-size: 16px; font-weight: 700; line-height: 1.5; }
        .custom-alert-btn {
            background: #3b82f6;
            color: #ffffff;
            border: none;
            border-radius: 12px;
            padding: 10px;
            font-size: 14px;
            font-weight: 700;
            cursor: pointer;
            transition: 0.2s;
        }
        .custom-alert-btn:active { background: #2563eb; transform: scale(0.98); }

        #worksScreen {
            display: none;
            flex-direction: column;
            min-height: 100vh;
            padding: 0;
            align-items: stretch;
        }
        #worksScreen.active { display: flex; }

        .works-top-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 20px 10px 20px;
            width: 100%;
        }

        .works-screen-title { color: #ffffff; font-size: 20px; font-weight: 700; }
        .works-header-left-group { display: flex; align-items: center; gap: 12px; }

        .works-upgrade-badge {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            padding: 6px 14px;
            border-radius: 20px;
            color: #ffffff;
            font-size: 13px;
            font-weight: 500;
            border: 1px solid rgba(255, 255, 255, 0.2);
            cursor: pointer;
        }

        .works-robot-logo {
            width: 32px;
            height: 32px;
            background: #dbeafe;
            mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 11h-1V7c0-1.1-.9-2-2-2H8c-1.1 0-2 .9-2 2v4H5c-1.1 0-2 .9-2 2v4c0 1.1.9 2 2 2h1v1c0 .55.45 1 1 1s1-.45 1-1v-1h8v1c0 .55.45 1 1 1s1-.45 1-1v-1h1c1.1 0 2-.9 2-2v-4c0-1.1-.9-2-2-2zM8 7h8v4H8V7zm3 9c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm4 0c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1 z"/></svg>') no-repeat center;
            -webkit-mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 11h-1V7c0-1.1-.9-2-2-2H8c-1.1 0-2 .9-2 2v4H5c-1.1 0-2 .9-2 2v4c0 1.1.9 2 2 2h1v1c0 .55.45 1 1 1s1-.45 1-1v-1h8v1c0 .55.45 1 1 1s1-.45 1-1v-1h1c1.1 0 2-.9 2-2v-4c0-1.1-.9-2-2-2zM8 7h8v4H8V7zm3 9c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm4 0c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1 z"/></svg>') no-repeat center;
            background-size: contain;
            cursor: pointer;
        }

        .works-body-container {
            padding: 10px 20px 20px 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            flex-grow: 1;
        }

        .works-tabs-container {
            display: flex;
            background: #282f3d;
            border-radius: 30px;
            padding: 4px;
            width: 100%;
            max-width: 360px;
            margin-top: 15px;
            margin-bottom: 60px;
            border: 1px solid rgba(255,255,255,0.08);
        }

        .works-tab {
            flex: 1;
            text-align: center;
            padding: 10px 0;
            font-size: 13px;
            font-weight: 600;
            color: #cbd5e1;
            background: transparent;
            border-radius: 25px;
            cursor: pointer;
            transition: all 0.2s ease;
            user-select: none;
        }

        .works-tab.active {
            background: #343d50 !important;
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
            margin-top: 10px;
        }

        .works-box-icon {
            width: 90px;
            height: 90px;
            margin-bottom: 24px;
            opacity: 0.8;
            background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="%23cbd5e1" stroke-width="1.5"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>') no-repeat center;
            background-size: contain;
        }

        .works-empty-text-sub { color: #cbd5e1; font-size: 13px; margin-bottom: 35px; }

        .works-create-btn {
            width: 100%;
            max-width: 220px;
            background: #ffffff;
            color: #1f242d;
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
        .works-create-btn:active { transform: scale(0.98); background: #e2e8f0; }

        /* --- شاشة الإعدادات --- */
        .settings-screen {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background-color: #1f242d;
            z-index: 999999;
            flex-direction: column;
            overflow-y: auto;
            padding: 20px;
        }
        .settings-screen.active { display: flex; }

        .settings-top-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
            margin-bottom: 25px;
        }
        .settings-title { color: #ffffff; font-size: 18px; font-weight: 700; text-align: center; flex-grow: 1; }
        
        .settings-close-btn {
            background: rgba(255, 255, 255, 0.15);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #fff;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            font-size: 18px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: 0.2s;
            outline: none;
        }
        .settings-close-btn:active { background-color: #0b0f19 !important; transform: scale(0.95); }

        .settings-upgrade-badge {
            background: rgba(255, 255, 255, 0.15);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #fff;
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 500;
            cursor: pointer;
        }

        .profile-header-card { display: flex; align-items: center; gap: 16px; margin-bottom: 20px; }
        
        .profile-avatar-box {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            overflow: hidden;
            border: 2px solid rgba(255,255,255,0.25);
            background: #111827;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.5);
        }
        .profile-avatar-box svg { width: 36px; height: 36px; fill: #60a5fa; }

        .profile-info-group { display: flex; flex-direction: column; align-items: flex-start; gap: 6px; }
        .profile-name-row { display: flex; align-items: center; gap: 10px; }
        .profile-name-text { color: #ffffff; font-size: 19px; font-weight: 700; white-space: nowrap; }
        .profile-edit-pencil {
            cursor: pointer;
            width: 26px;
            height: 26px;
            background: rgba(255, 255, 255, 0.12);
            border: 1px solid rgba(255, 255, 255, 0.25);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .profile-edit-pencil svg { width: 13px; height: 13px; fill: #ffffff; }

        .profile-id-row {
            display: flex;
            align-items: center;
            gap: 6px;
            background: #282f3d;
            border: 1px solid rgba(255,255,255,0.1);
            padding: 4px 10px;
            border-radius: 12px;
            color: #cbd5e1;
            font-size: 12px;
        }

        .pro-banner-card {
            background: linear-gradient(135deg, rgba(30, 35, 50, 0.9), rgba(15, 20, 35, 0.95));
            border: 1.5px solid rgba(255, 255, 255, 0.15);
            border-radius: 20px;
            padding: 16px;
            position: relative;
            margin-bottom: 20px;
            overflow: hidden;
            box-shadow: 0 8px 25px rgba(0,0,0,0.6);
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .pro-banner-top { display: flex; justify-content: space-between; align-items: center; }
        .pro-banner-title { color: #ffffff; font-size: 16px; font-weight: 700; }
        .pro-sparkle-icon {
            width: 45px;
            height: 45px;
            background: linear-gradient(135deg, #3b82f6, #ec4899);
            mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2C12 7.5 16.5 12 22 12C16.5 12 12 16.5 12 22C12 16.5 7.5 12 2 12C7.5 12 12 7.5 12 2Z"/></svg>') no-repeat center;
            -webkit-mask: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2C12 7.5 16.5 12 22 12C16.5 12 12 16.5 12 22C12 16.5 7.5 12 2 12C7.5 12 12 7.5 12 2Z"/></svg>') no-repeat center;
            background-size: contain;
        }
        .pro-banner-desc { color: #cbd5e1; font-size: 12px; }
        .pro-banner-btn {
            background: #3b82f6;
            color: #ffffff;
            border: none;
            padding: 8px 16px;
            border-radius: 14px;
            font-size: 13px;
            font-weight: 700;
            width: fit-content;
            cursor: pointer;
            margin-top: 4px;
        }
        .pro-banner-btn:active { background: #2563eb; }

        .settings-group-box {
            background: #282f3d;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 6px 16px;
            margin-bottom: 16px;
            display: flex;
            flex-direction: column;
        }
        .settings-item-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 14px 10px;
            margin: 0 -10px;
            border-radius: 12px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            cursor: pointer;
            transition: background-color 0.15s ease;
        }
        .settings-item-row:last-child { border-bottom: none; }
        .settings-item-row:active { background-color: #0b0f19 !important; }

        .settings-item-right {
            display: flex;
            align-items: center;
            gap: 12px;
            color: #ffffff;
            font-size: 15px;
            font-weight: 600;
        }
        .menu-icon { width: 20px; height: 20px; display: flex; align-items: center; justify-content: center; }
        .menu-icon svg { width: 18px; height: 18px; fill: #94a3b8; }
        .settings-item-left { color: #cbd5e1; font-size: 14px; display: flex; align-items: center; gap: 6px; }

        .switch-toggle { position: relative; display: inline-block; width: 44px; height: 24px; }
        .switch-toggle input { opacity: 0; width: 0; height: 0; }
        .slider-round {
            position: absolute; cursor: pointer;
            top: 0; left: 0; right: 0; bottom: 0;
            background-color: #343d50;
            transition: .3s;
            border-radius: 24px;
            border: 1px solid rgba(255,255,255,0.1);
        }
        .slider-round:before {
            position: absolute; content: "";
            height: 18px; width: 18px;
            left: 3px; bottom: 2px;
            background-color: white;
            transition: .3s;
            border-radius: 50%;
        }
        input:checked + .slider-round { background-color: #3b82f6; }
        input:checked + .slider-round:before { transform: translateX(20px); }

        /* نوافذ التطبيق */
        .language-modal-overlay, .feedback-modal-overlay, .subscription-modal-overlay, .notif-permission-overlay, .name-edit-modal-overlay {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.8);
            z-index: 999999999;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .language-modal-overlay.show, .feedback-modal-overlay.show, .subscription-modal-overlay.show, .notif-permission-overlay.show, .name-edit-modal-overlay.show { display: flex; }
        
        .modal-box {
            background: #282f3d;
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 24px;
            width: 100%;
            max-width: 340px;
            max-height: 85vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            box-shadow: 0 15px 40px rgba(0,0,0,0.8);
            padding: 22px;
            gap: 16px;
        }
        
        .lang-list-container {
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 4px;
            direction: ltr;
            text-align: left;
            max-height: 50vh;
        }
        .lang-item-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 14px;
            border-radius: 12px;
            cursor: pointer;
            color: #cbd5e1;
            font-size: 14px;
            font-weight: 600;
        }
        .lang-item-row:hover, .lang-item-row:active { background: rgba(255,255,255,0.08); color: #fff; }
        .lang-item-row.selected { background: #3b82f6; color: #fff; }

        .feedback-textarea, .name-edit-input {
            width: 100%;
            background: #1f242d;
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 12px;
            padding: 12px;
            color: #fff;
            font-size: 14px;
            outline: none;
        }
        .feedback-textarea { height: 120px; resize: none; }

        .notif-allow-btn { background: #3b82f6; color: #fff; border: none; padding: 12px; border-radius: 14px; font-size: 14px; font-weight: 700; cursor: pointer; width: 100%; text-align: center; }
        .notif-deny-btn { background: #1f242d; color: #fff; border: 1px solid rgba(255,255,255,0.2); padding: 12px; border-radius: 14px; font-size: 14px; font-weight: 700; cursor: pointer; width: 100%; text-align: center; }

        /* خطط الاشتراكات */
        .plans-list { display: flex; flex-direction: column; gap: 10px; overflow-y: auto; max-height: 50vh; }
        .plan-card { background: #1f242d; border: 1.5px solid rgba(255, 255, 255, 0.15); border-radius: 16px; padding: 14px; cursor: pointer; position: relative; }
        .plan-card.selected { border-color: #3b82f6; background: #343d50; }
        .plan-top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px; }
        .plan-name { color: #ffffff; font-size: 14px; font-weight: 700; }
        .plan-price { background: rgba(255, 255, 255, 0.12); padding: 3px 8px; border-radius: 8px; color: #ffffff; font-size: 11px; font-weight: 600; }
        .plan-desc { color: #cbd5e1; font-size: 11px; }

        .step-container { padding: 20px; display: flex; flex-direction: column; gap: 16px; max-height: calc(100vh - 90px); overflow-y: auto; }
        .ai-assistant-card { background: #282f3d; border: 1px solid #343d50; border-radius: 16px; padding: 16px; display: flex; flex-direction: column; gap: 8px; }
        .ai-header-row { display: flex; justify-content: space-between; align-items: center; }
        .ai-title { color: #ff2a85; font-size: 14px; font-weight: 700; }
        .ai-badge-circle { width: 32px; height: 32px; background: linear-gradient(135deg, #ff2a85, #7928ca); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 11px; }
        .ai-desc { color: #cbd5e1; font-size: 12px; line-height: 1.5; }

        .story-setup-box { background: #282f3d; border: 1px solid #343d50; border-radius: 16px; padding: 16px; display: flex; flex-direction: column; gap: 12px; }
        .setup-header-row { display: flex; justify-content: space-between; align-items: center; }
        .setup-main-title { color: #ffffff; font-size: 15px; font-weight: 700; }
        .counter-badge { background-color: #343d50; color: #cbd5e1; padding: 3px 10px; border-radius: 10px; font-size: 11px; font-weight: 600; }
        .setup-subtitle { color: #ffffff; font-size: 11px; font-weight: 700; }
        .setup-row-item { background: #343d50; border-radius: 12px; padding: 12px; display: flex; justify-content: space-between; align-items: center; }
        .item-info h4 { color: #ffffff; font-size: 13px; font-weight: 700; margin-bottom: 2px; }
        .item-info p { color: #cbd5e1; font-size: 11px; }
        .action-add-btn { background: rgba(255, 255, 255, 0.12); color: #ffffff; border: 1px solid rgba(255, 255, 255, 0.3); padding: 6px 14px; border-radius: 8px; font-size: 12px; font-weight: 600; cursor: pointer; }

        #toolsScreen { overflow-y: auto; }
        .tools-header { display: flex; align-items: center; justify-content: space-between; padding: 20px; background: rgba(31, 36, 45, 0.85); backdrop-filter: blur(10px); border-bottom: 1px solid rgba(255,255,255,0.08); }
        .tools-header-title { color: #ffffff; font-size: 20px; font-weight: 700; }
        .tools-upgrade-btn { background: rgba(255, 255, 255, 0.12); border: 1px solid rgba(255, 255, 255, 0.2); padding: 6px 14px; border-radius: 20px; color: #ffffff; font-size: 13px; font-weight: 500; cursor: pointer; }
        .tools-body { padding: 16px; display: flex; flex-direction: column; gap: 16px; }
        
        .tool-card-item { position: relative; width: 100%; height: 180px; border-radius: 20px; overflow: hidden; display: flex; flex-direction: column; justify-content: flex-end; padding: 18px; box-shadow: 0 6px 20px rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.1); cursor: pointer; }
        .tool-card-1 { background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), url('https://images.unsplash.com/photo-1542751371-adc38448a05e?q=80&w=600&auto=format&fit=crop') center/contain no-repeat, #1f242d; }
        .tool-card-2 { background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.85) 100%), url('https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=600&auto=format&fit=crop') center/contain no-repeat, #1f242d; }

        .tool-info-box { position: relative; z-index: 2; }
        .tool-main-title { color: #ffffff; font-size: 17px; font-weight: 700; margin-bottom: 4px; text-shadow: 0 2px 4px rgba(0,0,0,0.8); }
        .tool-sub-desc { color: #cbd5e1; font-size: 12px; text-shadow: 0 1px 3px rgba(0,0,0,0.8); }
        .tool-arrow-icon { position: absolute; top: 16px; color: #ffffff; font-size: 16px; font-weight: bold; background: rgba(0,0,0,0.4); width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; backdrop-filter: blur(5px); }
        [dir="rtl"] .tool-arrow-icon { right: 16px; }
        [dir="ltr"] .tool-arrow-icon { left: 16px; transform: scaleX(-1); }

        #sparkleDialogScreen { background-color: #0b0f19; display: none; flex-direction: column; min-height: 100vh; padding: 20px; position: relative; overflow-y: auto; }
        #sparkleDialogScreen.active { display: flex; }
        .sparkle-top-bar { display: flex; justify-content: space-between; align-items: center; width: 100%; margin-bottom: 30px; z-index: 2; }
        .sparkle-upgrade-badge { background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(10px); padding: 6px 16px; border-radius: 20px; color: #ffffff; font-size: 13px; font-weight: 500; border: 1px solid rgba(255, 255, 255, 0.2); cursor: pointer; }
        .sparkle-close-btn { background: none; border: none; color: #ffffff; font-size: 20px; cursor: pointer; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; }
        .sparkle-center-content { display: flex; flex-direction: column; align-items: center; text-align: center; z-index: 2; margin-top: 20px; gap: 20px; }
        .sparkle-icon-svg { width: 65px; height: 65px; fill: #93c5fd; filter: drop-shadow(0 0 12px rgba(147, 197, 253, 0.5)); }
        .sparkle-greeting-text { color: #ffffff; font-size: 20px; font-weight: 700; line-height: 1.5; }

        .plotcraft-nav-bar {
            position: fixed;
            bottom: 0; left: 0; width: 100%;
            background-color: #1f242d;
            padding: 10px 15px;
            display: flex; justify-content: center; align-items: center; gap: 12px;
            z-index: 999999; box-sizing: border-box;
            box-shadow: 0 -4px 15px rgba(0,0,0,0.6);
            transition: transform 0.3s ease;
        }
        .plotcraft-nav-bar.hidden { transform: translateY(120%); }
        .plotcraft-nav-pill { background-color: #282f3d; border: 1px solid #343d50; border-radius: 35px; display: flex; justify-content: space-around; align-items: center; padding: 8px 15px; flex-grow: 1; max-width: 380px; }
        .plotcraft-nav-item { display: flex; align-items: center; gap: 6px; color: #cbd5e1; font-size: 13px; text-decoration: none; cursor: pointer; white-space: nowrap; }
        .plotcraft-nav-item.active { color: #ffffff; font-weight: bold; }
        .plotcraft-nav-square { background-color: #282f3d; border: 1px solid #343d50; border-radius: 16px; width: 48px; height: 48px; display: flex; justify-content: center; align-items: center; flex-shrink: 0; cursor: pointer; position: relative; }
    </style>
</head>
<body>

    <!-- نافذة الاشتراكات -->
    <div class="subscription-modal-overlay" id="subscriptionModal">
        <div class="modal-box" onclick="event.stopPropagation()">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <div style="color:#fff; font-size:18px; font-weight:700;" data-i18n="upgradeTitle">ترقية الحساب</div>
                <button onclick="closeSubscriptionModal()" style="background:rgba(255,255,255,0.1); border:none; color:#fff; width:30px; height:30px; border-radius:50%; cursor:pointer;">✕</button>
            </div>
            <div style="text-align: center;">
                <div style="color: #ffffff; font-size: 15px; font-weight: 700; margin-bottom: 4px;" data-i18n="subSubHeading">حول أفكارك إلى PlotCraft</div>
                <div style="color: #cbd5e1; font-size: 11px;" data-i18n="subDesc">أنشئ كل لقطة وعدلها بسرعة.</div>
            </div>
            <div class="plans-list">
                <div class="plan-card selected" onclick="selectPlan(this)">
                    <div class="plan-top"><div class="plan-name">PlotCraft Weekly</div><div class="plan-price">$9.99</div></div>
                    <div class="plan-desc" data-i18n="descWeekly">500 نقطة / أسبوعياً</div>
                </div>
                <div class="plan-card" onclick="selectPlan(this)">
                    <div class="plan-top"><div class="plan-name">PlotCraft Monthly</div><div class="plan-price">$29.99</div></div>
                    <div class="plan-desc" data-i18n="descMonthly">1800 نقطة / شهرياً</div>
                </div>
            </div>
            <button class="notif-allow-btn" onclick="closeSubscriptionModal()" data-i18n="subscribeBtn">اشتراك</button>
        </div>
    </div>

    <!-- شاشة الإعدادات -->
    <div class="settings-screen" id="settingsScreen">
        <div class="settings-top-bar">
            <button class="settings-close-btn" onclick="closeSettingsScreen(event)" title="رجوع">‹</button>
            <div class="settings-title" data-i18n="settingsTitle">الإعدادات</div>
            <button class="settings-upgrade-badge" onclick="openSubscriptionModal()" data-i18n="upgradeBadge">ترقية</button>
        </div>

        <div class="profile-header-card">
            <div class="profile-avatar-box">
                <svg viewBox="0 0 24 24"><path d="M12 2a2 2 0 0 1 2 2c0 .74-.4 1.39-1 1.73V7h1a7 7 0 0 1 7 7h1a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-1v1a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-1H2a1 1 0 0 1-1-1v-3a1 1 0 0 1 1-1h1a7 7 0 0 1 7-7h1V5.73C10.4 5.39 10 4.74 10 4a2 2 0 0 1 2-2M7.5 13a1.5 1.5 0 0 0-1.5 1.5A1.5 1.5 0 0 0 7.5 16a1.5 1.5 0 0 0 1.5-1.5A1.5 1.5 0 0 0 7.5 13m9 0a1.5 1.5 0 0 0-1.5 1.5a1.5 1.5 0 0 0 1.5 1.5a1.5 1.5 0 0 0 1.5-1.5a1.5 1.5 0 0 0-1.5-1.5M10 18v2h4v-2z"/></svg>
            </div>
            <div class="profile-info-group">
                <div class="profile-name-row">
                    <span class="profile-name-text" id="displayUserName">NewUser</span>
                    <span class="profile-edit-pencil" onclick="openNameEditModal()">
                        <svg viewBox="0 0 24 24"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34a.9959.9959 0 0 0-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>
                    </span>
                </div>
                <div class="profile-id-row"><span id="displayUniqueId">4422114 ID</span></div>
            </div>
        </div>

        <div class="pro-banner-card">
            <div class="pro-banner-top">
                <div class="pro-banner-title" data-i18n="proBannerTitle">افتح PlotCraft Pro</div>
                <div class="pro-sparkle-icon"></div>
            </div>
            <div class="pro-banner-desc" data-i18n="proBannerDesc">حول كل فكرة إلى فيلم مكتمل</div>
            <button class="pro-banner-btn" onclick="openSubscriptionModal()" data-i18n="proBannerBtn">عرض خطط Pro ←</button>
        </div>

        <div class="settings-group-box">
            <div class="settings-item-row" onclick="showCustomAlert('سجل النقاط فارغ')">
                <div class="settings-item-right"><div class="menu-icon"><svg viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg></div><span data-i18n="pointsRecord">سجل النقاط</span></div>
                <div class="settings-item-left"><span>›</span></div>
            </div>
            <div class="settings-item-row" onclick="openFeedbackModal(event)">
                <div class="settings-item-right"><div class="menu-icon"><svg viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-1.99.9-1.99 2L2 22l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM6 9h12v2H6V9zm8 5H6v-2h8v2zm4-6H6V6h12v2z"/></svg></div><span data-i18n="feedbackMenu">التعليقات</span></div>
                <div class="settings-item-left"><span>›</span></div>
            </div>
        </div>

        <div class="settings-group-box">
            <div class="settings-item-row" onclick="event.stopPropagation()">
                <div class="settings-item-right"><div class="menu-icon"><svg viewBox="0 0 24 24"><path d="M12 22c1.1 0 2-.9 2-2h-4c0 1.1.9 2 2 2zm6-6v-5c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.64 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2zm-2 1H8v-6c0-2.48 1.51-4.5 4-4.5s4 2.02 4 4.5v6z"/></svg></div><span data-i18n="notificationsMenu">الإشعارات</span></div>
                <div class="settings-item-left"><label class="switch-toggle"><input type="checkbox" id="notifSwitch" onchange="handleNotifToggle(this)"><span class="slider-round"></span></label></div>
            </div>
            <div class="settings-item-row" onclick="openLanguageModal(event)">
                <div class="settings-item-right"><div class="menu-icon"><svg viewBox="0 0 24 24"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zm6.93 6h-2.95a15.65 15.65 0 0 0-1.38-3.56A8.03 8.03 0 0 1 18.92 8z"/></svg></div><span data-i18n="languageMenu">اللغة</span></div>
                <div class="settings-item-left"><span id="currentLangDisplay">العربية</span><span>›</span></div>
            </div>
            <div class="settings-item-row" onclick="openContactEmail(event)">
                <div class="settings-item-right"><div class="menu-icon"><svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg></div><span data-i18n="contactUsMenu">اتصل بنا</span></div>
                <div class="settings-item-left"><span>›</span></div>
            </div>
        </div>
    </div>

    <!-- نافذة التعليقات للمطور -->
    <div class="feedback-modal-overlay" id="feedbackModalOverlay" onclick="closeFeedbackModal(event)">
        <div class="modal-box" onclick="event.stopPropagation()">
            <div style="color:#fff; font-size:16px; font-weight:700;" data-i18n="feedbackModalTitle">أرسل مشكلتك للمطور</div>
            <textarea class="feedback-textarea" id="feedbackTextField" placeholder="اكتب مشكلتك هنا..."></textarea>
            <button class="notif-allow-btn" onclick="sendDeveloperFeedback(event)" data-i18n="sendBtn">إرسال</button>
            <button class="notif-deny-btn" onclick="closeFeedbackModal(event)" data-i18n="cancelBtn">إلغاء</button>
        </div>
    </div>

    <!-- نافذة اللغات -->
    <div class="language-modal-overlay" id="languageModalOverlay" onclick="closeLanguageModal(event)">
        <div class="modal-box" onclick="event.stopPropagation()">
            <div style="display:flex; justify-content:space-between; align-items:center; direction:ltr;">
                <div style="color:#fff; font-size:16px; font-weight:700;">Select Language</div>
                <button onclick="closeLanguageModal(event)" style="background:rgba(255,255,255,0.1); border:none; color:#fff; width:30px; height:30px; border-radius:50%; cursor:pointer;">✕</button>
            </div>
            <div class="lang-list-container">
                <div class="lang-item-row selected" onclick="changeAppLanguage('ar', 'العربية', this)">Arabic (العربية)</div>
                <div class="lang-item-row" onclick="changeAppLanguage('en', 'English', this)">English</div>
                <div class="lang-item-row" onclick="changeAppLanguage('es', 'Spanish', this)">Spanish (Español)</div>
                <div class="lang-item-row" onclick="changeAppLanguage('fr', 'French', this)">French (Français)</div>
                <div class="lang-item-row" onclick="changeAppLanguage('tr', 'Turkish', this)">Turkish (Türkçe)</div>
            </div>
        </div>
    </div>

    <!-- نافذة تعديل الاسم -->
    <div class="name-edit-modal-overlay" id="nameEditModal" onclick="event.stopPropagation()">
        <div class="modal-box">
            <div style="color:#fff; font-size:16px; font-weight:700;" data-i18n="editNameTitle">تعديل اسم المستخدم</div>
            <input type="text" class="name-edit-input" id="editNameInputField">
            <button class="notif-allow-btn" onclick="saveNewUserName(event)" data-i18n="sendBtn">إرسال</button>
            <button class="notif-deny-btn" onclick="closeNameEditModal(event)" data-i18n="cancelBtn">إلغاء</button>
        </div>
    </div>

    <!-- تنبيه الإشعارات -->
    <div class="notif-permission-overlay" id="notifPermissionModal" onclick="event.stopPropagation()">
        <div class="modal-box" style="text-align:center;">
            <div style="color:#fff; font-size:15px; font-weight:700;" data-i18n="notifAskMsg">هل تريد السماح بالإشعارات؟</div>
            <button class="notif-allow-btn" onclick="allowNotifications(event)" data-i18n="allowBtn">سماح</button>
            <button class="notif-deny-btn" onclick="denyNotifications(event)" data-i18n="denyBtn">عدم السماح</button>
        </div>
    </div>

    <!-- التنبيه العام -->
    <div class="custom-alert-overlay" id="customAlertOverlay" onclick="event.stopPropagation()">
        <div class="custom-alert-box">
            <div class="custom-alert-msg" id="customAlertMsgText">تنبيه</div>
            <button class="custom-alert-btn" onclick="closeCustomAlert(event)" data-i18n="okBtn">حسناً</button>
        </div>
    </div>

    <!-- الشاشة الرئيسية -->
    <div id="homeScreen" class="screen-view active">
        <div class="hero-box">
            <div class="top-header">
                <div class="brand-title">PlotCraft</div>
                <div class="upgrade-badge" onclick="openSubscriptionModal(event)" data-i18n="upgradeBadge">ترقية</div>
            </div>
            <div class="welcome-section">
                <h1 id="greetingHeading">مساء الخير، أيها المخرج<br>أي قصة سنصنع اليوم؟</h1>
            </div>
            <div class="cards-row">
                <div class="interactive-card" onclick="switchScreen('stepByStepScreen', event)">
                    <div class="card-header-row"><div class="card-title" data-i18n="stepByStepCard">خطوة بخطوة</div><span class="exact-bot-icon"></span></div>
                    <div class="card-subtitle" data-i18n="stepByStepSub">راجع كل خطوة</div>
                </div>
                <div class="interactive-card" onclick="openSubscriptionModal(event)">
                    <div class="pro-badge-top"><span>Pro only</span><span class="pro-lock-icon"></span></div>
                    <div class="card-header-row"><div class="card-title" data-i18n="fastCard">سريع</div><span class="speed-custom-icon"></span></div>
                    <div class="card-subtitle" data-i18n="fastSub">إدخال واحد، فيديو كامل</div>
                </div>
            </div>
        </div>
        <div class="inspiration-section">
            <div class="section-header"><div class="section-title" data-i18n="inspirationTitle">إلهام بلوت كرافت</div><div class="view-all">عرض الكل ></div></div>
            <div class="movies-carousel">
                <div class="movie-card m1" onclick="showCustomAlert('قريباً')"><div class="movie-title">THE DELIVERYMAN</div></div>
                <div class="movie-card m2" onclick="showCustomAlert('قريباً')"><div class="movie-title">SECRET BILLIONAIRE</div></div>
            </div>
        </div>
    </div>

    <!-- شاشة الأدوات -->
    <div id="toolsScreen" class="screen-view">
        <div class="tools-header">
            <div class="tools-header-title" data-i18n="toolsTitle">الأدوات</div>
            <div class="tools-upgrade-btn" onclick="openSubscriptionModal(event)" data-i18n="upgradeBadge">ترقية</div>
        </div>
        <div class="tools-body">
            <div class="tool-card-item tool-card-1" onclick="showCustomAlert('قريباً')">
                <div class="tool-arrow-icon">‹</div>
                <div class="tool-info-box"><div class="tool-main-title" data-i18n="tool1Title">تأثيرات الفيديو</div><div class="tool-sub-desc" data-i18n="tool1Sub">أضف لمسة سينمائية</div></div>
            </div>
            <div class="tool-card-item tool-card-2" onclick="showCustomAlert('قريباً')">
                <div class="tool-arrow-icon">‹</div>
                <div class="tool-info-box"><div class="tool-main-title" data-i18n="tool2Title">توليد الفيديو</div><div class="tool-sub-desc" data-i18n="tool2Sub">حول توجيهاً إلى فيديو</div></div>
            </div>
        </div>
    </div>

    <!-- شاشة الأعمال -->
    <div id="worksScreen" class="screen-view">
        <div class="works-top-header">
            <div class="works-screen-title" data-i18n="worksTitle">الأعمال</div>
            <div class="works-header-left-group">
                <div class="works-upgrade-badge" onclick="openSubscriptionModal(event)" data-i18n="upgradeBadge">ترقية</div>
                <div class="works-robot-logo" onclick="openSettingsScreen(event)" title="الإعدادات"></div>
            </div>
        </div>
        <div class="works-body-container">
            <div class="works-tabs-container">
                <div class="works-tab active" onclick="switchWorksTab(this)" data-i18n="projectsTab">المشاريع</div>
                <div class="works-tab" onclick="switchWorksTab(this)" data-i18n="mediaTab">مكتبة الوسائط</div>
            </div>
            <div class="works-empty-content">
                <div class="works-box-icon"></div>
                <div class="works-empty-text-sub" data-i18n="emptyWorksText">ستظهر هنا مشاريع القصة الخاصة بك.</div>
                <button class="works-create-btn" onclick="openSparkleDialog(event)" data-i18n="createStoryBtn">إنشاء قصة</button>
            </div>
        </div>
    </div>

    <!-- شاشة خطوة بخطوة -->
    <div id="stepByStepScreen" class="screen-view">
        <div style="display:flex; justify-content:space-between; align-items:center; padding:20px; border-bottom:1px solid rgba(255,255,255,0.08);">
            <button style="background:rgba(255,255,255,0.1); border:none; color:#fff; width:36px; height:36px; border-radius:50%; cursor:pointer;" onclick="switchScreen('homeScreen', event)">✕</button>
            <div style="color:#fff; font-weight:700;">PlotCraft</div>
            <div style="width:36px;"></div>
        </div>
        <div class="step-container">
            <div class="ai-assistant-card">
                <div class="ai-header-row"><div class="ai-title">مساعد AI</div><div class="ai-badge-circle">AI+</div></div>
                <div class="ai-desc" data-i18n="aiDescText">أنشئ تفاصيل فيلمك خطوة بخطوة بدقة عالية.</div>
            </div>
        </div>
    </div>

    <!-- شاشة الحوار الذكي (Sparkle) -->
    <div id="sparkleDialogScreen" class="screen-view">
        <div class="sparkle-top-bar">
            <button class="sparkle-close-btn" onclick="switchScreen('homeScreen', event)">✕</button>
            <div class="brand-title">Plotcraft</div>
            <div class="sparkle-upgrade-badge" onclick="openSubscriptionModal(event)" data-i18n="upgradeBadge">ترقية</div>
        </div>
        <div class="sparkle-center-content">
            <svg class="sparkle-icon-svg" viewBox="0 0 24 24"><path d="M12 2C12 7.5 16.5 12 22 12C16.5 12 12 16.5 12 22C12 16.5 7.5 12 2 12C7.5 12 12 7.5 12 2Z"/></svg>
            <div class="sparkle-greeting-text" id="sparkleGreetingText">طاب مساؤك، أيها المخرج<br>أي قصة سنصنع اليوم؟</div>
        </div>
    </div>

    <!-- شريط التنقل السفلي -->
    <div class="plotcraft-nav-bar" id="mainNavBar">
        <div class="plotcraft-nav-pill">
            <a href="#" class="plotcraft-nav-item active" id="navHome" onclick="switchScreen('homeScreen', event); setActiveNav('navHome')">
                <span data-i18n="navHome">الرئيسية</span>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg>
            </a>
            <a href="#" class="plotcraft-nav-item" id="navTools" onclick="switchScreen('toolsScreen', event); setActiveNav('navTools')">
                <span data-i18n="navTools">الأدوات</span>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"></path></svg>
            </a>
            <a href="#" class="plotcraft-nav-item" id="navWorks" onclick="switchScreen('worksScreen', event); setActiveNav('navWorks')">
                <span data-i18n="navWorks">الأعمال</span>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path></svg>
            </a>
        </div>
        <div class="plotcraft-nav-square" onclick="openSparkleDialog(event)" title="إنشاء">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="#cbd5e1"><rect x="3" y="6" width="14" height="12" rx="3"/></svg>
        </div>
    </div>

    <script>
        // قواميس الترجمة الشاملة لجميع لغات التطبيق
        const translations = {
            ar: {
                upgradeBadge: "ترقية",
                greeting: "مساء الخير، أيها المخرج<br>أي قصة سنصنع اليوم؟",
                stepByStepCard: "خطوة بخطوة",
                stepByStepSub: "راجع كل خطوة",
                fastCard: "سريع",
                fastSub: "إدخال واحد، فيديو كامل",
                inspirationTitle: "إلهام بلوت كرافت",
                toolsTitle: "الأدوات",
                worksTitle: "الأعمال",
                projectsTab: "المشاريع",
                mediaTab: "مكتبة الوسائط",
                emptyWorksText: "ستظهر هنا مشاريع القصة الخاصة بك.",
                createStoryBtn: "إنشاء قصة",
                navHome: "الرئيسية",
                navTools: "الأدوات",
                navWorks: "الأعمال",
                settingsTitle: "الإعدادات",
                proBannerTitle: "افتح PlotCraft Pro",
                proBannerDesc: "حول كل فكرة إلى فيلم مكتمل",
                proBannerBtn: "عرض خطط Pro ←",
                pointsRecord: "سجل النقاط",
                feedbackMenu: "التعليقات",
                notificationsMenu: "الإشعارات",
                languageMenu: "اللغة",
                contactUsMenu: "اتصل بنا",
                upgradeTitle: "ترقية الحساب",
                subSubHeading: "حول أفكارك إلى PlotCraft",
                subDesc: "أنشئ كل لقطة وعدلها بسرعة.",
                descWeekly: "500 نقطة / أسبوعياً",
                descMonthly: "1800 نقطة / شهرياً",
                subscribeBtn: "اشتراك",
                okBtn: "حسناً",
                cancelBtn: "إلغاء",
                sendBtn: "إرسال",
                editNameTitle: "تعديل اسم المستخدم",
                notifAskMsg: "هل تريد السماح بالإشعارات؟",
                allowBtn: "سماح",
                denyBtn: "عدم السماح",
                feedbackModalTitle: "أرسل مشكلتك للمطور",
                aiDescText: "أنشئ تفاصيل فيلمك خطوة بخطوة بدقة عالية.",
                tool1Title: "تأثيرات الفيديو",
                tool1Sub: "أضف لمسة سينمائية",
                tool2Title: "توليد الفيديو",
                tool2Sub: "حول توجيهاً إلى فيديو"
            },
            en: {
                upgradeBadge: "Upgrade",
                greeting: "Good evening, Director<br>What story shall we make today?",
                stepByStepCard: "Step-by-Step",
                stepByStepSub: "Review every step",
                fastCard: "Fast",
                fastSub: "One input, full video",
                inspirationTitle: "PlotCraft Inspiration",
                toolsTitle: "Tools",
                worksTitle: "Works",
                projectsTab: "Projects",
                mediaTab: "Media Library",
                emptyWorksText: "Your story projects will appear here.",
                createStoryBtn: "Create Story",
                navHome: "Home",
                navTools: "Tools",
                navWorks: "Works",
                settingsTitle: "Settings",
                proBannerTitle: "Unlock PlotCraft Pro",
                proBannerDesc: "Turn every idea into a complete film",
                proBannerBtn: "View Pro Plans ←",
                pointsRecord: "Points History",
                feedbackMenu: "Feedback",
                notificationsMenu: "Notifications",
                languageMenu: "Language",
                contactUsMenu: "Contact Us",
                upgradeTitle: "Account Upgrade",
                subSubHeading: "Turn your ideas into PlotCraft",
                subDesc: "Create and edit every shot quickly.",
                descWeekly: "500 points / week",
                descMonthly: "1800 points / month",
                subscribeBtn: "Subscribe",
                okBtn: "OK",
                cancelBtn: "Cancel",
                sendBtn: "Send",
                editNameTitle: "Edit Username",
                notifAskMsg: "Allow notifications?",
                allowBtn: "Allow",
                denyBtn: "Don't Allow",
                feedbackModalTitle: "Send your feedback to developer",
                aiDescText: "Create your film details step by step.",
                tool1Title: "Video Effects",
                tool1Sub: "Add a cinematic touch",
                tool2Title: "Video Generation",
                tool2Sub: "Turn a prompt into video"
            },
            es: {
                upgradeBadge: "Mejorar",
                greeting: "Buenas tardes, Director<br>¿Qué historia haremos hoy?",
                stepByStepCard: "Paso a paso",
                stepByStepSub: "Revisar cada paso",
                fastCard: "Rápido",
                fastSub: "Una entrada, video completo",
                inspirationTitle: "Inspiración PlotCraft",
                toolsTitle: "Herramientas",
                worksTitle: "Obras",
                projectsTab: "Proyectos",
                mediaTab: "Biblioteca",
                emptyWorksText: "Tus proyectos aparecerán aquí.",
                createStoryBtn: "Crear Historia",
                navHome: "Inicio",
                navTools: "Herramientas",
                navWorks: "Obras",
                settingsTitle: "Configuración",
                proBannerTitle: "PlotCraft Pro",
                proBannerDesc: "Convierte cada idea en película",
                proBannerBtn: "Ver planes Pro ←",
                pointsRecord: "Puntos",
                feedbackMenu: "Comentarios",
                notificationsMenu: "Notificaciones",
                languageMenu: "Idioma",
                contactUsMenu: "Contáctanos",
                upgradeTitle: "Mejorar Cuenta",
                subSubHeading: "Crea tus ideas",
                subDesc: "Edita rápidamente.",
                descWeekly: "500 puntos / semana",
                descMonthly: "1800 puntos / mes",
                subscribeBtn: "Suscribirse",
                okBtn: "Aceptar",
                cancelBtn: "Cancelar",
                sendBtn: "Enviar",
                editNameTitle: "Editar Nombre",
                notifAskMsg: "¿Permitir notificaciones?",
                allowBtn: "Permitir",
                denyBtn: "No permitir",
                feedbackModalTitle: "Enviar comentarios",
                aiDescText: "Crea tu película paso a paso.",
                tool1Title: "Efectos de video",
                tool1Sub: "Toque cinemático",
                tool2Title: "Generación de video",
                tool2Sub: "Convierte texto en video"
            },
            fr: {
                upgradeBadge: "Mettre à niveau",
                greeting: "Bonsoir, Réalisateur<br>Quelle histoire ferons-nous?",
                stepByStepCard: "Étape par étape",
                stepByStepSub: "Vérifier chaque étape",
                fastCard: "Rapide",
                fastSub: "Vidéo complète",
                inspirationTitle: "Inspiration PlotCraft",
                toolsTitle: "Outils",
                worksTitle: "Œuvres",
                projectsTab: "Projets",
                mediaTab: "Médiathèque",
                emptyWorksText: "Vos projets apparaîtront ici.",
                createStoryBtn: "Créer une histoire",
                navHome: "Accueil",
                navTools: "Outils",
                navWorks: "Œuvres",
                settingsTitle: "Paramètres",
                proBannerTitle: "PlotCraft Pro",
                proBannerDesc: "Transformez vos idées",
                proBannerBtn: "Voir offres Pro ←",
                pointsRecord: "Points",
                feedbackMenu: "Commentaires",
                notificationsMenu: "Notifications",
                languageMenu: "Langue",
                contactUsMenu: "Contactez-nous",
                upgradeTitle: "Mise à niveau",
                subSubHeading: "Créez vos films",
                subDesc: "Édition rapide.",
                descWeekly: "500 points / semaine",
                descMonthly: "1800 points / mois",
                subscribeBtn: "S'abonner",
                okBtn: "OK",
                cancelBtn: "Annuler",
                sendBtn: "Envoyer",
                editNameTitle: "Modifier le nom",
                notifAskMsg: "Autoriser notifications?",
                allowBtn: "Autoriser",
                denyBtn: "Refuser",
                feedbackModalTitle: "Envoyer vos commentaires",
                aiDescText: "Créez votre film étape par étape.",
                tool1Title: "Effets vidéo",
                tool1Sub: "Touche cinématique",
                tool2Title: "Génération vidéo",
                tool2Sub: "Texte en vidéo"
            },
            tr: {
                upgradeBadge: "Yükselt",
                greeting: "İyi akşamlar, Yönetmen<br>Bugün hangi hikayeyi yapacağız?",
                stepByStepCard: "Adım Adım",
                stepByStepSub: "Her adımı gözden geçir",
                fastCard: "Hızlı",
                fastSub: "Tam video",
                inspirationTitle: "PlotCraft İlhamı",
                toolsTitle: "Araçlar",
                worksTitle: "Çalışmalar",
                projectsTab: "Projeler",
                mediaTab: "Medya Kitaplığı",
                emptyWorksText: "Projeleriniz burada görünecek.",
                createStoryBtn: "Hikaye Oluştur",
                navHome: "Ana Sayfa",
                navTools: "Araçlar",
                navWorks: "Çalışmalar",
                settingsTitle: "Ayarlar",
                proBannerTitle: "PlotCraft Pro",
                proBannerDesc: "Fikirlerinizi filme dönüştürün",
                proBannerBtn: "Pro Planlar ←",
                pointsRecord: "Puanlar",
                feedbackMenu: "Geri Bildirim",
                notificationsMenu: "Bildirimler",
                languageMenu: "Dil",
                contactUsMenu: "İletişim",
                upgradeTitle: "Hesabı Yükselt",
                subSubHeading: "Fikirlerinizi hayata geçirin",
                subDesc: "Hızlıca oluşturun.",
                descWeekly: "500 puan / hafta",
                descMonthly: "1800 puan / ay",
                subscribeBtn: "Abone Ol",
                okBtn: "Tamam",
                cancelBtn: "İptal",
                sendBtn: "Gönder",
                editNameTitle: "Adı Düzenle",
                notifAskMsg: "Bildirimlere izin verilsin mi?",
                allowBtn: "İzin Ver",
                denyBtn: "İzin Verme",
                feedbackModalTitle: "Geri bildirim gönder",
                aiDescText: "Film detaylarınızı adım adım oluşturun.",
                tool1Title: "Video Efektleri",
                tool1Sub: "Sinematik dokunuş",
                tool2Title: "Video Üretimi",
                tool2Sub: "Komutu videoya dönüştür"
            }
        };

        let currentLang = 'ar';

        // تفعيل الهزاز الخفيف
        document.addEventListener('click', function(event) {
            if (event.target.closest('button') || event.target.closest('.interactive-card') || event.target.closest('.plotcraft-nav-item') || event.target.closest('.plotcraft-nav-square') || event.target.closest('.works-tab') || event.target.closest('.plan-card') || event.target.closest('.settings-item-row') || event.target.closest('.lang-item-row')) {
                if ("vibrate" in navigator) navigator.vibrate(35);
            }
        });

        // دوال التنقل بين الشاشات والنوافذ
        function switchScreen(screenId, event) {
            if (event) event.preventDefault();
            document.querySelectorAll('.screen-view').forEach(s => s.classList.remove('active'));
            document.getElementById(screenId).classList.add('active');
            
            var navBar = document.getElementById('mainNavBar');
            if (['sparkleDialogScreen', 'stepByStepScreen'].includes(screenId)) {
                navBar.classList.add('hidden');
            } else {
                navBar.classList.remove('hidden');
            }
            window.scrollTo(0, 0);
        }

        function setActiveNav(navId) {
            document.querySelectorAll('.plotcraft-nav-item').forEach(i => i.classList.remove('active'));
            document.getElementById(navId).classList.add('active');
        }

        function openSubscriptionModal(event) {
            if (event) { event.preventDefault(); event.stopPropagation(); }
            document.getElementById('subscriptionModal').classList.add('show');
        }
        function closeSubscriptionModal() {
            document.getElementById('subscriptionModal').classList.remove('show');
        }

        function openSparkleDialog(event) {
            if (event) event.stopPropagation();
            switchScreen('sparkleDialogScreen', event);
            document.getElementById('mainNavBar').classList.add('hidden');
        }

        function openSettingsScreen(event) {
            if (event) event.stopPropagation();
            document.getElementById('settingsScreen').classList.add('active');
            document.getElementById('mainNavBar').classList.add('hidden');
        }

        function closeSettingsScreen(event) {
            if (event) event.stopPropagation();
            document.getElementById('settingsScreen').classList.remove('active');
            document.getElementById('mainNavBar').classList.remove('hidden');
        }

        function openLanguageModal(event) {
            if (event) event.stopPropagation();
            document.getElementById('languageModalOverlay').classList.add('show');
        }
        function closeLanguageModal(event) {
            if (event) event.stopPropagation();
            document.getElementById('languageModalOverlay').classList.remove('show');
        }

        function openFeedbackModal(event) {
            if (event) event.stopPropagation();
            document.getElementById('feedbackTextField').value = "";
            document.getElementById('feedbackModalOverlay').classList.add('show');
        }
        function closeFeedbackModal(event) {
            if (event) event.stopPropagation();
            document.getElementById('feedbackModalOverlay').classList.remove('show');
        }

        function openNameEditModal() {
            document.getElementById('editNameInputField').value = document.getElementById('displayUserName').innerText;
            document.getElementById('nameEditModal').classList.add('show');
        }
        function closeNameEditModal(event) {
            if (event) event.stopPropagation();
            document.getElementById('nameEditModal').classList.remove('show');
        }
        function saveNewUserName(event) {
            if (event) event.stopPropagation();
            var val = document.getElementById('editNameInputField').value.trim();
            if (val !== "") document.getElementById('displayUserName').innerText = val;
            closeNameEditModal();
        }

        function sendDeveloperFeedback(event) {
            if (event) event.stopPropagation();
            var text = document.getElementById('feedbackTextField').value.trim();
            if (text === "") return;
            closeFeedbackModal();
            showCustomAlert(currentLang === 'ar' ? "تم إرسال تعليقك للمطور بنجاح!" : "Feedback sent successfully!");
        }

        // اتصل بنا المباشر لإيميلك كمطور
        function openContactEmail(event) {
            if (event) event.stopPropagation();
            window.location.href = "mailto:developer@plotcraft.app?subject=Support%20Request&body=Hello%20Developer,%20";
        }

        function showCustomAlert(msg) {
            document.getElementById('customAlertMsgText').innerText = msg;
            document.getElementById('customAlertOverlay').classList.add('show');
        }
        function closeCustomAlert(event) {
            if (event) event.stopPropagation();
            document.getElementById('customAlertOverlay').classList.remove('show');
        }

        function handleNotifToggle(checkbox) {
            if (checkbox.checked) {
                document.getElementById('notifPermissionModal').classList.add('show');
            } else {
                showCustomAlert(currentLang === 'ar' ? "تم تعطيل الإشعارات" : "Notifications disabled");
            }
        }
        function allowNotifications(event) {
            if (event) event.stopPropagation();
            document.getElementById('notifPermissionModal').classList.remove('show');
            showCustomAlert(currentLang === 'ar' ? "تم تفعيل الإشعارات بنجاح!" : "Notifications enabled!");
        }
        function denyNotifications(event) {
            if (event) event.stopPropagation();
            document.getElementById('notifPermissionModal').classList.remove('show');
            document.getElementById('notifSwitch').checked = false;
        }

        function switchWorksTab(element) {
            document.querySelectorAll('.works-tab').forEach(t => t.classList.remove('active'));
            element.classList.add('active');
        }

        function selectPlan(element) {
            document.querySelectorAll('.plan-card').forEach(c => c.classList.remove('selected'));
            element.classList.add('selected');
        }

        // تغيير اللغة الفعلي وتحديث واجهة التطبيق والاتجاه
        function changeAppLanguage(langCode, langName, element) {
            currentLang = langCode;
            document.getElementById('currentLangDisplay').innerText = langName;
            
            document.querySelectorAll('.lang-item-row').forEach(r => r.classList.remove('selected'));
            element.classList.add('selected');

            var htmlRoot = document.getElementById('htmlRoot');
            if (langCode === 'ar') {
                htmlRoot.setAttribute('dir', 'rtl');
                htmlRoot.setAttribute('lang', 'ar');
            } else {
                htmlRoot.setAttribute('dir', 'ltr');
                htmlRoot.setAttribute('lang', langCode);
            }

            const dict = translations[langCode];
            document.querySelectorAll('[data-i18n]').forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (dict[key]) el.innerText = dict[key];
            });

            if (dict['greeting']) {
                document.getElementById('greetingHeading').innerHTML = dict['greeting'];
                document.getElementById('sparkleGreetingText').innerHTML = dict['greeting'];
            }

            setTimeout(() => { closeLanguageModal(); }, 150);
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=680, scrolling=True)

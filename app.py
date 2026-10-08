import streamlit as st
import streamlit.components.v1 as components

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
<html lang="ar" dir="rtl" id="appHtmlRoot">
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
                        url('https://raw.githubusercontent.com/Ghassanridha/PlotCraft/c3d4f279f4e8d7b5e8b712b6d54dfa06a7087a30/IMG_%D9%A2%D9%A0%D9%A2%D9%A6%D9%A1%D9%A0%D9%A0%D9%A8_%D9%A1%D9%A8%D9%A3%D9%A0%D9%A4%D9%A6.jpg') left center/cover no-repeat;
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

        .section-title {
            color: #ffffff;
            font-size: 18px;
            font-weight: 700;
        }

        .view-all {
            color: #cbd5e1;
            font-size: 13px;
            cursor: pointer;
        }

        .movies-carousel {
            display: flex;
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
            transition: transform 0.2s;
        }
        .movie-card:active {
            transform: scale(0.96);
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

        .custom-alert-overlay {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.7);
            z-index: 99999999999;
            align-items: center;
            justify-content: center;
        }
        .custom-alert-overlay.show {
            display: flex;
        }
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
        .custom-alert-msg {
            color: #ffffff;
            font-size: 16px;
            font-weight: 700;
            line-height: 1.5;
        }
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
        .custom-alert-btn:active {
            background: #2563eb;
            transform: scale(0.98);
        }

        #worksScreen {
            display: none;
            flex-direction: column;
            min-height: 100vh;
            padding: 0;
            align-items: stretch;
        }
        #worksScreen.active {
            display: flex;
        }

        .works-top-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 20px 10px 20px;
            width: 100%;
        }

        .works-screen-title {
            color: #ffffff;
            font-size: 20px;
            font-weight: 700;
        }

        .works-header-left-group {
            display: flex;
            align-items: center;
            gap: 12px;
        }

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

        .works-empty-text-sub {
            color: #cbd5e1;
            font-size: 13px;
            margin-bottom: 35px;
        }

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
        .works-create-btn:active {
            transform: scale(0.98);
            background: #e2e8f0;
        }

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
        .settings-title {
            color: #ffffff;
            font-size: 18px;
            font-weight: 700;
            text-align: center;
            flex-grow: 1;
        }
        
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
        .settings-close-btn:active {
            background-color: #0b0f19 !important;
            transform: scale(0.95);
        }

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

        .profile-header-card {
            display: flex;
            justify-content: flex-start;
            align-items: center;
            gap: 16px;
            margin-bottom: 20px;
        }
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
        .profile-avatar-box svg {
            width: 36px;
            height: 36px;
            fill: #60a5fa;
            filter: drop-shadow(0 0 6px rgba(96,165,250,0.6));
        }

        .profile-info-group {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 6px;
        }
        .profile-name-row {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .profile-name-text {
            color: #ffffff;
            font-size: 19px;
            font-weight: 700;
            white-space: nowrap;
        }
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
            transition: 0.2s;
        }
        .profile-edit-pencil svg {
            width: 13px;
            height: 13px;
            fill: #ffffff;
        }
        .profile-edit-pencil:active { background: rgba(255, 255, 255, 0.25); }

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
            background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
            border-radius: 20px;
            padding: 18px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 25px;
            box-shadow: 0 8px 20px rgba(59, 130, 246, 0.3);
        }
        .pro-banner-text h3 {
            color: #ffffff;
            font-size: 16px;
            font-weight: 700;
            margin-bottom: 4px;
        }
        .pro-banner-text p {
            color: #dbeafe;
            font-size: 12px;
        }
        .pro-banner-btn {
            background: #ffffff;
            color: #1d4ed8;
            border: none;
            padding: 8px 16px;
            border-radius: 12px;
            font-size: 13px;
            font-weight: 700;
            cursor: pointer;
            transition: 0.2s;
        }
        .pro-banner-btn:active { transform: scale(0.95); background: #f8fafc; }

        .settings-section-title {
            color: #94a3b8;
            font-size: 13px;
            font-weight: 600;
            margin-bottom: 12px;
            margin-top: 10px;
        }
        .settings-menu-list {
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin-bottom: 25px;
        }
        .settings-menu-item {
            background: #282f3d;
            border: 1px solid rgba(255,255,255,0.06);
            border-radius: 16px;
            padding: 14px 16px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            cursor: pointer;
            transition: 0.2s;
        }
        .settings-menu-item:active { background: #343d50; }
        .settings-item-right {
            display: flex;
            align-items: center;
            gap: 12px;
            color: #ffffff;
            font-size: 15px;
            font-weight: 600;
        }
        .settings-item-icon {
            width: 20px;
            height: 20px;
            fill: #94a3b8;
        }
        .settings-item-left {
            color: #94a3b8;
            font-size: 14px;
        }

        /* --- شريط التنقل السفلي (Bottom Nav) --- */
        .bottom-nav {
            position: fixed;
            bottom: 0; left: 0; width: 100%;
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            display: flex;
            justify-content: space-around;
            align-items: center;
            padding: 12px 10px 22px 10px;
            z-index: 99999;
        }

        .nav-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 4px;
            background: none;
            border: none;
            cursor: pointer;
            color: #64748b;
            font-size: 11px;
            font-weight: 600;
            transition: 0.2s;
            flex: 1;
        }

        .nav-item svg {
            width: 24px;
            height: 24px;
            fill: #64748b;
            transition: 0.2s;
        }

        .nav-item.active {
            color: #ffffff;
        }

        .nav-item.active svg {
            fill: #3b82f6;
            filter: drop-shadow(0 0 8px rgba(59, 130, 246, 0.5));
        }

        .nav-item:active {
            transform: scale(0.92);
        }
    </style>
</head>
<body>
    <div class="screen-view active" id="homeScreen">
        <div class="hero-box">
            <div class="top-header">
                <div class="brand-title">PlotCraft</div>
                <div class="upgrade-badge" onclick="showCustomAlert('خاصية الترقية قريباً!')">ترقية</div>
            </div>
            <div class="welcome-section">
                <h1>اصنع قصتك بكل ابتكار</h1>
            </div>
        </div>

        <div class="inspiration-section">
            <div class="section-header">
                <div class="section-title">إلهام</div>
                <div class="view-all" onclick="showCustomAlert('عرض الكل قريباً!')">عرض الكل</div>
            </div>
            <div class="movies-carousel">
                <div class="movie-card m1" onclick="showCustomAlert('تم اختيار: عوالم خيالية')">
                    <div class="movie-title">عوالم خيالية</div>
                </div>
                <div class="movie-card m2" onclick="showCustomAlert('تم اختيار: دراما وحركة')">
                    <div class="movie-title">دراما وحركة</div>
                </div>
                <div class="movie-card m3" onclick="showCustomAlert('تم اختيار: مغامرات الفضاء')">
                    <div class="movie-title">مغامرات الفضاء</div>
                </div>
            </div>

            <div class="cards-row" style="margin-top: 24px;">
                <div class="interactive-card" onclick="switchScreen('sparkleDialogScreen')">
                    <div class="pro-badge-top">
                        <div class="pro-lock-icon"></div>
                        <span>PRO</span>
                    </div>
                    <div class="card-header-row">
                        <div class="card-title">مساعد ذكي</div>
                        <div class="exact-bot-icon"></div>
                    </div>
                    <div class="card-subtitle">توليد أفكار متقدمة</div>
                </div>
                
                <div class="interactive-card" onclick="showCustomAlert('السرعة القصوى مفعلة')">
                    <div class="card-title-group-left">
                        <div class="card-title">سرعة فائقة</div>
                        <div class="speed-custom-icon"></div>
                    </div>
                    <div class="card-subtitle" style="margin-top: 6px;">استجابة فورية</div>
                </div>
            </div>
        </div>
    </div>

    <div class="screen-view" id="worksScreen">
        <div class="works-top-header">
            <div class="works-screen-title">أعمالي</div>
            <div class="works-header-left-group">
                <div class="works-upgrade-badge" onclick="showCustomAlert('ترقية الحساب')">ترقية</div>
                <div class="works-robot-logo" onclick="switchScreen('sparkleDialogScreen')"></div>
            </div>
        </div>

        <div class="works-body-container">
            <div class="works-tabs-container">
                <div class="works-tab active" id="tabProjects" onclick="switchWorksTab('projects')">المشاريع</div>
                <div class="works-tab" id="tabCharacters" onclick="switchWorksTab('characters')">الشخصيات</div>
            </div>

            <div class="works-empty-content">
                <div class="works-box-icon"></div>
                <div class="works-empty-text-sub" id="worksEmptyText">لا توجد مشاريع حتى الآن، ابدأ بإنشاء مشروعك الأول</div>
                <button class="works-create-btn" onclick="showCustomAlert('إنشاء جديد')">إنشاء مشروع جديد</button>
            </div>
        </div>
    </div>

    <!-- شاشة المساعد الذكي -->
    <div class="screen-view" id="sparkleDialogScreen">
        <div style="padding: 20px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.08);">
            <div style="color: #fff; font-size: 18px; font-weight: 700;">المساعد الذكي</div>
            <div onclick="switchScreen('homeScreen')" style="color: #3b82f6; cursor: pointer; font-size: 14px; font-weight: 700;">إغلاق</div>
        </div>
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; flex-grow: 1; padding: 40px; text-align: center;">
            <div style="width: 70px; height: 70px; background: rgba(59,130,246,0.15); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                <div class="exact-bot-icon" style="width: 36px; height: 36px;"></div>
            </div>
            <div style="color: #fff; font-size: 18px; font-weight: 700; margin-bottom: 8px;">كيف يمكنني مساعدتك اليوم؟</div>
            <div style="color: #94a3b8; font-size: 13px; line-height: 1.5;">اسألني عن حبكة القصة، الشخصيات، أو أي أفكار إبداعية لتطوير مشروعك.</div>
        </div>
    </div>

    <!-- شاشة الإعدادات -->
    <div class="settings-screen" id="settingsScreen">
        <div class="settings-top-bar">
            <button class="settings-close-btn" onclick="closeSettingsScreen()">✕</button>
            <div class="settings-title">الإعدادات</div>
            <div class="settings-upgrade-badge" onclick="showCustomAlert('ترقية الحساب')">ترقية</div>
        </div>

        <div class="profile-header-card">
            <div class="profile-avatar-box">
                <svg viewBox="0 0 24 24"><path d="M12 2a5 5 0 1 0 5 5 5 5 0 0 0-5-5zm0 8a3 3 0 1 1 3-3 3 3 0 0 1-3 3zm9 11v-1a7 7 0 0 0-7-7h-4a7 7 0 0 0-7 7v1h2v-1a5 5 0 0 1 5-5h4a5 5 0 0 1 5 5v1z"/></svg>
            </div>
            <div class="profile-info-group">
                <div class="profile-name-row">
                    <span class="profile-name-text">غسان رضا</span>
                    <div class="profile-edit-pencil" onclick="showCustomAlert('تعديل الاسم')">
                        <svg viewBox="0 0 24 24"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04a.996.996 0 0 0 0-1.41l-2.34-2.34a.996.996 0 0 0-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>
                    </div>
                </div>
                <div class="profile-id-row">
                    <span>ID: #99482</span>
                </div>
            </div>
        </div>

        <div class="pro-banner-card">
            <div class="pro-banner-text">
                <h3>نسخة PlotCraft PRO</h3>
                <p>احصل على عدد غير محدود من الشخصيات والميزات الذكية</p>
            </div>
            <button class="pro-banner-btn" onclick="showCustomAlert('الترقية قريباً')">ترقية الآن</button>
        </div>

        <div class="settings-section-title">الحساب والتفضيلات</div>
        <div class="settings-menu-list">
            <div class="settings-menu-item" onclick="showCustomAlert('اللغة العربية مفعلة')">
                <div class="settings-item-right">
                    <svg class="settings-item-icon" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>
                    <span>لغة التطبيق</span>
                </div>
                <div class="settings-item-left">العربية</div>
            </div>
            <div class="settings-menu-item" onclick="showCustomAlert('الوضع الليلي مفعل افتراضياً')">
                <div class="settings-item-right">
                    <svg class="settings-item-icon" viewBox="0 0 24 24"><path d="M12 3c-4.97 0-9 4.03-9 9s4.03 9 9 9 9-4.03 9-9c0-.46-.04-.92-.1-1.36-.98 1.37-2.58 2.26-4.38 2.26-3.03 0-5.5-2.47-5.5-5.5 0-1.8.89-3.4 2.26-4.38-.44-.06-.9-.1-1.36-.1z"/></svg>
                    <span>المظهر</span>
                </div>
                <div class="settings-item-left">داكن</div>
            </div>
        </div>

        <div class="settings-section-title">حول التطبيق</div>
        <div class="settings-menu-list">
            <div class="settings-menu-item" onclick="showCustomAlert('PlotCraft v1.0.0')">
                <div class="settings-item-right">
                    <svg class="settings-item-icon" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>
                    <span>إصدار التطبيق</span>
                </div>
                <div class="settings-item-left">v1.0.0</div>
            </div>
        </div>
    </div>

    <!-- شريط التنقل السفلي -->
    <div class="bottom-nav">
        <button class="nav-item active" id="navHome" onclick="switchScreen('homeScreen')">
            <svg viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>
            <span>الرئيسية</span>
        </button>
        <button class="nav-item" id="navWorks" onclick="switchScreen('worksScreen')">
            <svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg>
            <span>أعمالي</span>
        </button>
        <button class="nav-item" id="navSettings" onclick="openSettingsScreen()">
            <svg viewBox="0 0 24 24"><path d="M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58c.18-.14.23-.41.12-.61l-1.92-3.32c-.12-.22-.37-.29-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54c-.04-.24-.24-.41-.48-.41h-3.84c-.24 0-.43.17-.47.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96c-.22-.08-.47 0-.59.22L2.74 8.87c-.12.21-.08.47.12.61l2.03 1.58c-.05.3-.09.63-.09.94s.02.64.07.94l-2.03 1.58c-.18.14-.23.41-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z"/></svg>
            <span>الإعدادات</span>
        </button>
    </div>

    <!-- نافذة منبثقة للتنبيهات -->
    <div class="custom-alert-overlay" id="customAlertOverlay">
        <div class="custom-alert-box">
            <div class="custom-alert-msg" id="customAlertMsg">رسالة تنبيه</div>
            <button class="custom-alert-btn" onclick="hideCustomAlert()">حسناً</button>
        </div>
    </div>

    <script>
        function switchScreen(screenId) {
            document.querySelectorAll('.screen-view').forEach(el => el.classList.remove('active'));
            document.getElementById('settingsScreen').classList.remove('active');
            document.getElementById(screenId).classList.add('active');

            document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
            if (screenId === 'homeScreen') {
                document.getElementById('navHome').classList.add('active');
            } else if (screenId === 'worksScreen') {
                document.getElementById('navWorks').classList.add('active');
            }
            window.scrollTo(0, 0);
        }

        function openSettingsScreen() {
            document.getElementById('settingsScreen').classList.add('active');
            document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
            document.getElementById('navSettings').classList.add('active');
        }

        function closeSettingsScreen() {
            document.getElementById('settingsScreen').classList.remove('active');
            document.getElementById('navSettings').classList.remove('active');
            document.getElementById('navHome').classList.add('active');
            document.getElementById('homeScreen').classList.add('active');
        }

        function switchWorksTab(tabName) {
            document.getElementById('tabProjects').classList.remove('active');
            document.getElementById('tabCharacters').classList.remove('active');
            const emptyText = document.getElementById('worksEmptyText');
            
            if (tabName === 'projects') {
                document.getElementById('tabProjects').classList.add('active');
                emptyText.innerText = 'لا توجد مشاريع حتى الآن، ابدأ بإنشاء مشروعك الأول';
            } else {
                document.getElementById('tabCharacters').classList.add('active');
                emptyText.innerText = 'لا توجد شخصيات حتى الآن، ابدأ بإنشاء شخصيتك الأولى';
            }
        }

        function showCustomAlert(msg) {
            document.getElementById('customAlertMsg').innerText = msg;
            document.getElementById('customAlertOverlay').classList.add('show');
        }

        function hideCustomAlert() {
            document.getElementById('customAlertOverlay').classList.remove('show');
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=850, scrolling=True)

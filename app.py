st.markdown(
    """
    <style>
    .bottom-nav-container {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #0b0f19;
        padding: 10px 15px;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 10px;
        z-index: 9999;
        box-shadow: 0 -4px 10px rgba(0,0,0,0.3);
    }
    .nav-btn-single {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 50%;
        width: 55px;
        height: 55px;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .nav-pill-box {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 35px;
        display: flex;
        justify-content: space-around;
        align-items: center;
        padding: 8px 15px;
        flex-grow: 1;
        max-width: 320px;
    }
    .nav-item {
        display: flex;
        align-items: center;
        gap: 6px;
        color: #8b949e;
        font-size: 13px;
        font-family: sans-serif;
        text-decoration: none;
    }
    .nav-item.active {
        color: #ffffff;
        font-weight: bold;
    }
    </style>
    <div class="bottom-nav-container">
        <div class="nav-pill-box">
            <a href="#" class="nav-item">
                <span>الأعمال</span>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
            </a>
            <a href="#" class="nav-item">
                <span>الأدوات</span>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"></path></svg>
            </a>
            <a href="#" class="nav-item active">
                <span>الصفحة الرئيسية</span>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
            </a>
        </div>
        <div class="nav-btn-single">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"></rect><line x1="7" y1="2" x2="7" y2="22"></line><line x1="17" y1="2" x2="17" y2="22"></line><line x1="2" y1="12" x2="22" y2="12"></line><line x1="2" y1="7" x2="7" y2="7"></line><line x1="2" y1="17" x2="7" y2="17"></line><line x1="17" y1="17" x2="22" y2="17"></line><line x1="17" y1="7" x2="22" y2="7"></line></svg>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

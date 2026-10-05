import streamlit.components.v1 as components

# إضافة الشريط السفلي بشكل متوافق ومضمون 100%
components.html(
    """
    <style>
        body {
            margin: 0;
            background-color: transparent;
        }
        .bottom-nav-container {
            position: fixed;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
            width: 95%;
            max-width: 450px;
            background-color: #0b0f19;
            padding: 8px 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 10px;
            z-index: 99999;
            border-radius: 40px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.6);
            border: 1px solid #30363d;
            box-sizing: border-box;
            direction: rtl;
        }
        .nav-btn-single {
            background-color: #161b22;
            border: 1px solid #30363d;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-shrink: 0;
            cursor: pointer;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }
        .nav-pill-box {
            background-color: #161b22;
            border: 1px solid #30363d;
            border-radius: 35px;
            display: flex;
            justify-content: space-around;
            align-items: center;
            padding: 8px 10px;
            flex-grow: 1;
        }
        .nav-item {
            display: flex;
            align-items: center;
            gap: 5px;
            color: #8b949e;
            font-size: 12px;
            font-family: system-ui, -apple-system, sans-serif;
            text-decoration: none;
            cursor: pointer;
            white-space: nowrap;
        }
        .nav-item.active {
            color: #ffffff;
            font-weight: bold;
        }
    </style>

    <div class="bottom-nav-container">
        <!-- الزر المنفصل اليساري -->
        <div class="nav-btn-single" title="إنشاء">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#4f46e5" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"></rect><line x1="7" y1="2" x2="7" y2="22"></line><line x1="17" y1="2" x2="17" y2="22"></line><line x1="2" y1="12" x2="22" y2="12"></line></svg>
        </div>

        <!-- المستطيل الذي يحتوي على 3 أزرار -->
        <div class="nav-pill-box">
            <!-- 1. الأعمال -->
            <a href="#" class="nav-item">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
                <span>الأعمال</span>
            </a>
            
            <!-- 2. الأدوات -->
            <a href="#" class="nav-item">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"></path></svg>
                <span>الأدوات</span>
            </a>

            <!-- 3. الصفحة الرئيسية -->
            <a href="#" class="nav-item active">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                <span>الرئيسية</span>
            </a>
        </div>
    </div>
    """,
    height=75,
)

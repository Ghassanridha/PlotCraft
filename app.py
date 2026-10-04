import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="بلوت كرافت",
    page_icon="🎬",
    layout="centered"
)

html = """
<!DOCTYPE html>

<html lang="ar" dir="rtl">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<style>

* {
    box-sizing: border-box;
}

html, body {
    margin: 0;
    padding: 0;
    background: #090a0c;
    color: white;
    font-family: Arial, Tahoma, sans-serif;
}

body {
    overflow-x: hidden;
}

.app {
    width: 100%;
    max-width: 480px;
    min-height: 100vh;
    margin: auto;
    background: #090a0c;
    overflow: hidden;
}


/* ================= HERO ================= */

.hero {

    position: relative;

    height: 650px;

    overflow: hidden;

    background:
        linear-gradient(
            to bottom,
            rgba(0,0,0,0.05),
            rgba(0,0,0,0.20) 45%,
            #090a0c 100%
        ),
        url("https://images.unsplash.com/photo-1519608487953-e999c86e7455?auto=format&fit=crop&w=900&q=80");

    background-size: cover;

    background-position: center;

}


/* ================= LOGO ================= */

.logo {

    position: absolute;

    top: 20px;
    left: 20px;

    font-size: 19px;

    font-weight: bold;

    z-index: 10;

}


/* ================= UPGRADE ================= */

.upgrade {

    position: absolute;

    top: 20px;
    right: 20px;

    padding: 9px 18px;

    border-radius: 25px;

    background: rgba(255,255,255,0.12);

    border: 1px solid rgba(255,255,255,0.08);

    backdrop-filter: blur(10px);

    font-size: 14px;

    z-index: 10;

}


/* ================= TITLE ================= */

.title {

    position: absolute;

    top: 105px;

    left: 0;
    right: 0;

    text-align: center;

    padding: 0 15px;

    z-index: 5;

}

.title h1 {

    margin: 0;

    font-size: 28px;

    line-height: 1.5;

}

.title p {

    margin: 5px 0 0;

    font-size: 24px;

    font-weight: bold;

}


/* ================= PERSON ================= */

.person {

    position: absolute;

    width: 285px;

    height: 340px;

    left: 50%;

    bottom: 150px;

    transform: translateX(-50%);

    object-fit: cover;

    object-position: top;

    border-radius: 50%;

    z-index: 3;

}


/* ================= CARDS ================= */

.cards {

    position: absolute;

    left: 0;
    right: 0;

    bottom: 20px;

    display: flex;

    gap: 12px;

    padding: 0 18px;

    z-index: 10;

}

.card {

    flex: 1;

    min-height: 125px;

    padding: 15px;

    border-radius: 23px;

    background: rgba(25,27,31,0.82);

    border: 1px solid rgba(255,255,255,0.08);

    backdrop-filter: blur(15px);

}

.card-icon {

    font-size: 27px;

    margin-bottom: 6px;

}

.card h3 {

    margin: 0;

    font-size: 17px;

}

.card p {

    margin: 5px 0;

    color: #999;

    font-size: 11px;

}

.pro {

    display: block;

    text-align: center;

    margin-top: 8px;

    color: #777;

    font-size: 9px;

}


/* ================= SECTION ================= */

.section {

    padding: 20px 18px 110px;

}

.section-title {

    display: flex;

    justify-content: space-between;

    align-items: center;

    margin-bottom: 15px;

}

.section-title h2 {

    margin: 0;

    font-size: 20px;

}

.section-title span {

    color: #888;

    font-size: 13px;

}


/* ================= MOVIES ================= */

.movies {

    display: flex;

    gap: 14px;

    overflow-x: auto;

    scrollbar-width: none;

}

.movies::-webkit-scrollbar {

    display: none;

}

.movie {

    flex: 0 0 190px;

    background: #151619;

    border-radius: 18px;

    overflow: hidden;

}

.movie img {

    width: 100%;

    height: 275px;

    display: block;

    object-fit: cover;

}

.movie-info {

    padding: 11px;

}

.movie-info h3 {

    margin: 0;

    font-size: 13px;

    line-height: 1.4;

}

.movie-info p {

    margin: 5px 0 0;

    color: #777;

    font-size: 10px;

}


/* ================= NAVIGATION ================= */

.nav {

    position: fixed;

    bottom: 15px;

    left: 50%;

    transform: translateX(-50%);

    width: calc(100% - 30px);

    max-width: 450px;

    display: flex;

    justify-content: space-around;

    align-items: center;

    padding: 8px;

    border-radius: 30px;

    background: rgba(30,31,34,0.96);

    border: 1px solid rgba(255,255,255,0.10);

    backdrop-filter: blur(15px);

    z-index: 100;

}

.nav-item {

    text-align: center;

    color: #999;

    font-size: 10px;

    padding: 8px 10px;

    border-radius: 15px;

}

.nav-item .icon {

    font-size: 19px;

    margin-bottom: 3px;

}

.nav-item.active {

    color: white;

    background: rgba(255,255,255,0.10);

}


/* ================= MOBILE ================= */

@media (max-width: 360px) {

    .title h1 {
        font-size: 23px;
    }

    .title p {
        font-size: 20px;
    }

    .person {
        width: 250px;
        height: 310px;
    }

    .card {
        padding: 12px;
    }

}

</style>

</head>


<body>


<div class="app">


    <!-- HERO -->

    <section class="hero">


        <div class="logo">
            ✦ بلوت كرافت
        </div>


        <div class="upgrade">
            👑 ترقية
        </div>


        <div class="title">

            <h1>
                مساء الخير، أيها المخرج
            </h1>

            <p>
                أي قصة سنصنع اليوم؟
            </p>

        </div>


        <img
            class="person"
            src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=600&q=90"
        >


        <div class="cards">


            <div class="card">

                <div class="card-icon">
                    ✨
                </div>

                <h3>
                    سريع
                </h3>

                <p>
                    إدخال واحد، فيديو كامل
                </p>

                <span class="pro">
                    🔒 Pro only
                </span>

            </div>


            <div class="card">

                <div class="card-icon">
                    💬
                </div>

                <h3>
                    خطوة بخطوة
                </h3>

                <p>
                    راجع كل خطوة
                </p>

            </div>


        </div>


    </section>



    <!-- INSPIRATION -->

    <section class="section">


        <div class="section-title">

            <h2>
                إلهام بلوت كرافت
            </h2>

            <span>
                عرض الكل
            </span>

        </div>


        <div class="movies">


            <div class="movie">

                <img
                    src="https://images.unsplash.com/photo-1485846234645-a62644f84728?auto=format&fit=crop&w=500&q=80"
                >

                <div class="movie-info">

                    <h3>
                        THE WRONG DOOR
                    </h3>

                    <p>
                        A mysterious story
                    </p>

                </div>

            </div>



            <div class="movie">

                <img
                    src="https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=500&q=80"
                >

                <div class="movie-info">

                    <h3>
                        THE DELIVERYMAN'S
                        SECRET BILLIONAIRE
                    </h3>

                    <p>
                        A dramatic story
                    </p>

                </div>

            </div>



            <div class="movie">

                <img
                    src="https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=500&q=80"
                >

                <div class="movie-info">

                    <h3>
                        THE INVITATION
                    </h3>

                    <p>
                        Mystery
                    </p>

                </div>

            </div>


        </div>


    </section>



    <!-- NAVIGATION -->

    <div class="nav">


        <div class="nav-item active">

            <div class="icon">
                🏠
            </div>

            الصفحة الرئيسية

        </div>


        <div class="nav-item">

            <div class="icon">
                ✦
            </div>

            الأدوات

        </div>


        <div class="nav-item">

            <div class="icon">
                🔥
            </div>

            الأعمال

        </div>


        <div class="nav-item">

            <div class="icon">
                ✎
            </div>

            إنشاء

        </div>


    </div>


</div>


</body>

</html>
"""

components.html(
    html,
    height=1000,
    scrolling=True
)

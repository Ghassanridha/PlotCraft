<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>بلوت كرافت</title>

  <script src="https://cdn.tailwindcss.com"></script>

  <style>
    body {
      font-family: Arial, "Tahoma", sans-serif;
      background: #090a0c;
    }

    .glass {
      background: rgba(25, 27, 30, 0.72);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
    }

    .hero-gradient {
      background:
        linear-gradient(
          to bottom,
          rgba(0,0,0,0.05) 0%,
          rgba(0,0,0,0.15) 45%,
          rgba(8,9,11,0.95) 100%
        );
    }

    .hide-scrollbar::-webkit-scrollbar {
      display: none;
    }

    .hide-scrollbar {
      scrollbar-width: none;
    }
  </style>
</head>

<body class="min-h-screen text-white">

  <!-- الصفحة -->
  <main class="mx-auto min-h-screen w-full max-w-[480px] overflow-hidden bg-[#0b0c0e]">

    <!-- ================= HERO ================= -->
    <section class="relative h-[620px] overflow-hidden">

      <!-- صورة الخلفية -->
      <img
        src="https://images.unsplash.com/photo-1519608487953-e999c86e7455?auto=format&fit=crop&w=900&q=80"
        class="absolute inset-0 h-full w-full object-cover"
        alt="Background"
      >

      <!-- التدرج -->
      <div class="hero-gradient absolute inset-0"></div>

      <!-- زر الترقية -->
      <button
        class="absolute right-5 top-5 z-10 rounded-full bg-white/10 px-5 py-2 text-sm font-bold backdrop-blur-md"
      >
        👑 ترقية
      </button>

      <!-- اسم الموقع -->
      <div class="absolute left-5 top-5 z-10 flex items-center gap-2">
        <div class="flex h-9 w-9 items-center justify-center rounded-full bg-white text-black">
          ✦
        </div>

        <span class="text-lg font-bold">
          بلوت كرافت
        </span>
      </div>


      <!-- المحتوى -->
      <div class="absolute inset-x-0 top-[115px] px-5 text-center">

        <h1 class="text-[29px] font-bold leading-[1.45]">
          مساء الخير، أيها المخرج
        </h1>

        <p class="mt-1 text-[25px] font-semibold">
          أي قصة سنصنع اليوم؟
        </p>

      </div>


      <!-- الوجه -->
      <div class="absolute bottom-[115px] left-1/2 w-[290px] -translate-x-1/2">

        <div class="relative overflow-hidden rounded-[50%]">

          <img
            src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=600&q=90"
            class="h-[330px] w-full object-cover object-top"
            alt="Creator"
          >

        </div>

      </div>


      <!-- بطاقات الأدوات -->
      <div class="absolute bottom-5 left-0 right-0 px-5">

        <div class="grid grid-cols-2 gap-4">

          <!-- بطاقة -->
          <div class="glass rounded-[25px] border border-white/10 p-4">

            <div class="mb-3 flex items-center gap-3">

              <div class="flex h-12 w-12 items-center justify-center rounded-2xl bg-white/10 text-2xl">
                ✨
              </div>

              <div>
                <h3 class="font-bold">
                  سريع
                </h3>

                <p class="text-xs text-gray-400">
                  إدخال واحد، فيديو كامل
                </p>
              </div>

            </div>

            <div class="text-center text-[10px] text-gray-500">
              🔒 Pro only
            </div>

          </div>


          <!-- بطاقة -->
          <div class="glass rounded-[25px] border border-white/10 p-4">

            <div class="mb-3 flex items-center gap-3">

              <div class="flex h-12 w-12 items-center justify-center rounded-2xl bg-white/10 text-2xl">
                💬
              </div>

              <div>
                <h3 class="font-bold">
                  خطوة بخطوة
                </h3>

                <p class="text-xs text-gray-400">
                  راجع كل خطوة
                </p>
              </div>

            </div>

          </div>

        </div>

      </div>

    </section>


    <!-- ================= الأعمال ================= -->

    <section class="px-5 pb-32">

      <div class="mb-5 flex items-center justify-between">

        <h2 class="text-xl font-bold">
          إلهام بلوت كرافت
        </h2>

        <button class="text-sm text-gray-400">
          عرض الكل
        </button>

      </div>


      <!-- الأعمال -->
      <div class="hide-scrollbar flex gap-4 overflow-x-auto pb-4">

        <!-- Card 1 -->
        <article class="min-w-[190px] overflow-hidden rounded-[18px] bg-[#161719]">

          <img
            src="https://images.unsplash.com/photo-1485846234645-a62644f84728?auto=format&fit=crop&w=500&q=80"
            class="h-[275px] w-full object-cover"
            alt="Movie"
          >

          <div class="p-3">

            <h3 class="truncate text-sm font-bold">
              THE WRONG DOOR
            </h3>

            <p class="mt-1 text-[10px] text-gray-500">
              A mysterious story
            </p>

          </div>

        </article>


        <!-- Card 2 -->
        <article class="min-w-[190px] overflow-hidden rounded-[18px] bg-[#161719]">

          <img
            src="https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=500&q=80"
            class="h-[275px] w-full object-cover"
            alt="Movie"
          >

          <div class="p-3">

            <h3 class="truncate text-sm font-bold">
              THE DELIVERYMAN'S
              SECRET BILLIONAIRE
            </h3>

            <p class="mt-1 text-[10px] text-gray-500">
              A dramatic story
            </p>

          </div>

        </article>


        <!-- Card 3 -->
        <article class="min-w-[190px] overflow-hidden rounded-[18px] bg-[#161719]">

          <img
            src="https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=500&q=80"
            class="h-[275px] w-full object-cover"
            alt="Movie"
          >

          <div class="p-3">

            <h3 class="truncate text-sm font-bold">
              THE INVITATION
            </h3>

            <p class="mt-1 text-[10px] text-gray-500">
              Mystery
            </p>

          </div>

        </article>

      </div>

    </section>


    <!-- ================= Bottom Navigation ================= -->

    <nav
      class="fixed bottom-4 left-1/2 z-50 flex w-[calc(100%-32px)] max-w-[450px] -translate-x-1/2 items-center justify-around rounded-[30px] border border-white/10 bg-[#202124]/90 px-3 py-3 shadow-2xl backdrop-blur-xl"
    >

      <!-- الصفحة -->
      <button class="flex flex-col items-center gap-1 rounded-2xl bg-white/10 px-5 py-2">

        <span class="text-xl">
          🏠
        </span>

        <span class="text-[10px]">
          الصفحة الرئيسية
        </span>

      </button>


      <!-- الأدوات -->
      <button class="flex flex-col items-center gap-1 px-4 py-2 text-gray-400">

        <span class="text-xl">
          ✦
        </span>

        <span class="text-[10px]">
          الأدوات
        </span>

      </button>


      <!-- الأعمال -->
      <button class="flex flex-col items-center gap-1 px-4 py-2 text-gray-400">

        <span class="text-xl">
          🔥
        </span>

        <span class="text-[10px]">
          الأعمال
        </span>

      </button>


      <!-- إنشاء -->
      <button class="flex flex-col items-center gap-1 px-4 py-2 text-gray-400">

        <span class="text-xl">
          ▣
        </span>

        <span class="text-[10px]">
          إنشاء
        </span>

      </button>

    </nav>

  </main>

</body>
</html>

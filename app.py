<!DOCTYPE html>
<html lang="ar" dir="rtl">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>بلوت كرافت</title>

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            background: #08090b;
            color: white;
            font-family: Arial, Tahoma, sans-serif;
        }

        .glass {
            background: rgba(25, 27, 31, 0.78);
            border: 1px solid rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
        }

        .hero-overlay {
            background:
                linear-gradient(
                    to bottom,
                    rgba(0, 0, 0, 0.05) 0%,
                    rgba(0, 0, 0, 0.15) 45%,
                    #08090b 100%
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


<body>

    <!-- التطبيق بالكامل -->
    <div class="mx-auto min-h-screen w-full max-w-[480px] overflow-hidden bg-[#090a0c]">


        <!-- ========================= -->
        <!-- القسم الرئيسي -->
        <!-- ========================= -->

        <section class="relative h-[650px] overflow-hidden">


            <!-- خلفية -->
            <img
                src="https://images.unsplash.com/photo-1519608487953-e999c86e7455?auto=format&fit=crop&w=900&q=80"
                alt="الخلفية"
                class="absolute inset-0 h-full w-full object-cover"
          

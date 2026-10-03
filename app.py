from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>بلوتكرافت - PlotCraft</title>
        <style>
            body { font-family: Tahoma, sans-serif; background-color: #0d1117; color: #c9d1d9; text-align: center; padding: 50px; }
            h1 { color: #58a6ff; }
            p { font-size: 18px; }
        </style>
    </head>
    <body>
        <h1>مرحباً بك في تطبيق بلوتكرافت (PlotCraft)</h1>
        <p>جاري بناء منصة تحويل القصص وصور الوجوه إلى مقاطع فيديو سينمائية عبر الذكاء الاصطناعي...</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)

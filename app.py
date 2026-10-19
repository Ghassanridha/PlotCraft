import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

INDEX_HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>الصفحة الرئيسية</title>
</head>
<body>
  <h1>أهلاً بك</h1>
  <form action="/submit" method="POST">
    <input type="text" name="username" placeholder="اكتب اسمك" required>
    <button type="submit">إرسال</button>
  </form>
</body>
</html>
"""

RESULT_HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>النتيجة</title>
</head>
<body>
  <h1>مرحباً {{ name }}!</h1>
  <a href="/">رجوع</a>
</body>
</html>
"""


@app.route('/')
def home():
    return render_template_string(INDEX_HTML)


@app.route('/submit', methods=['POST'])
def submit():
    user_name = request.form.get('username')
    return render_template_string(RESULT_HTML, name=user_name)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

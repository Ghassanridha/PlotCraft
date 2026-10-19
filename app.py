import os
from flask import Flask, render_template, request

# تحديد المسار الصحيح للمجلد الحالي ومجلد الـ templates تلقائياً
base_dir = os.path.abspath(os.path.dirname(__file__))
templates_dir = os.path.join(base_dir, 'templates')

app = Flask(__name__, template_folder=templates_dir)


@app.route('/')
def home():
  return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
  user_name = request.form.get('username')
  return render_template('result.html', name=user_name)


if __name__ == '__main__':
  app.run(debug=True)

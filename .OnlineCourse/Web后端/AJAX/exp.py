import datetime
from flask import Flask, render_template

app = Flask(__name__, static_url_path='')
app.debug = True

@app.route('/')
def home():
    return "欢迎学习 xuepy.com AJAX"

@app.route('/ajax/time/')
def current_time():
    now = str(datetime.datetime.now())
    return render_template('ajax-time.html', now=now)

def main():
    app.run()

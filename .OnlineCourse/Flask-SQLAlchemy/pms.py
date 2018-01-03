# 创建虚拟环境
# python -m venv venv_flask_orm

# pip install flask --upgrade
# pip install ipython
# pip install flask_sqlalchemy

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///.//db/personal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy
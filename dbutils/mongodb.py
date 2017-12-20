# import dbutils.sqlite

#相对导入,只能使用在from语句
from . import sqlite
from .sqlite import db_url
from .. import product

#加空格代表导入整个模块
#.一个点号代表当前'mongodb.py所在目录
#..两个点号代表向外延伸一层
#...以此类推

dbutils.sqlite.db_url

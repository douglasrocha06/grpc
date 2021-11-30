import os
import pymysql.connections

MYSQL_HOST = '127.0.0.1'
MYSQL_DB = 'dbclientes'
MYSQL_USER = 'root'
MYSQL_PASS = ''

conn = pymysql.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASS,
    db=MYSQL_DB,
    port=3306,
    cursorclass=pymysql.cursors.DictCursor
)
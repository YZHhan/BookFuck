# coding:utf-8
import pymysql


class DB_Config(object):
    def connect(self):
        conn = pymysql.connect(host="47.94.170.18", user="root", passwd="root", db="bookserver", charset="utf8")
        return conn

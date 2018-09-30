# coding = utf-8

import sys
from imp import reload
from book import db_config

'''
MySQL  工具类

'''
default_encoding = 'utf-8'


class DB_Utils(object):
    def __init__(self):
        if sys.getdefaultencoding() != default_encoding:
            reload(sys)
            sys.setdefaultencoding(default_encoding)
        self.db = db_config.DB_Config.connect()
        self.cursor = self.db.cursor()

    def insert(self, sql):
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交到数据库
            self.db.commit()
        except Exception as e:
            # 发生错误是回滚
            print('db_util_________   insert fail : ', e)
            self.db.rollback()

    def query(self, sql):
        # fetchone(): 该方法获取下一个查询的结果集，结果集是一个对象
        # fetchall(): 接受全部的返回结果行
        # rowcount(): 这是一个只读属性，并返回执行execute()方法后影响的行数
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 获取所有记录列表
            results = self.cursor.fetchall()
            for row in results:
                first_name = row[0]
                last_name = row[1]
                age = row[2]
                sex = row[3]
                income = row[4]
                # 打印结果
                print("fname=%s,lname=%s,age=%d,sex=%s,income=%d", first_name, last_name, age, sex, income)

        except:
            print("Error: unable to fecth data")

# coding = utf-8
import sys
from imp import reload
from book import url_manager, html_download, html_parser, db_utils

'''
    Date:2018.07.10
    Description:Python爬虫数据抓取
    Python Version:>3.X
'''
default_encoding = 'utf-8'


class BookMain(object):
    def __init__(self):
        if sys.getdefaultencoding() != default_encoding:
            reload(sys)
            sys.setdefaultencoding(default_encoding)
            self.db_utils = db_utils.DB_Utils

    def grab_data(self, root_url):
        print('开始抓取数据', root_url)


if __name__ == '__main__':
    root_url = "http://www.qidian.com/"
    book_main = BookMain()
    book_main.grab_data(root_url)

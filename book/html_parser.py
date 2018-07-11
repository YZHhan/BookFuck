# coding = utf-8
import re
from book import html_download,file_output
import urllib
from urllib.parse import urljoin
from bs4 import BeautifulSoup
'''
Html parser
'''


class HtmlParse(object):
    def __init__(self):
        self.download = html_download.HtmlDownLoad()
        self.output = file_output.FileOutPut()


    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        print("link==>")
        links = soup.find_all('a', href=re.compile(r"/info/"))
        for link in links:
            print("被过滤的超链接a======href=====>", link)
            new_url = link['href']
            # join 方法会按照pageurl的格式将new_url补全
            new_url_full = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_url_full)
        return new_urls



    def _get_new_data(self, page_url, data):
        res_data = set()








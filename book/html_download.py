# coding = utf-8
import requests

'''
Html 获取类
'''


class HtmlDownLoad(object):
    def download(self, url):
        if url is None:
            return
        response = requests.get(url)
        if response.status_code != 200:
            return None
        return response.content

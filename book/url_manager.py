# coding = utf-8

'''
对URL进行管理类

'''


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()  # 带爬取
        self.old_urls = set()  # 爬取过

    # add new_url
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def has_new_url(self):
        return len(self.new_urls) != 0
        pass

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def get_new_url(self):
        new_url = self.new_urls.pop()  # 获取后移除
        self.old_urls.add(new_url)
        return new_url

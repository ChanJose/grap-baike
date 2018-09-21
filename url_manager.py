# -*- coding: utf-8 -*-


class UrlManager(object):
    def __init__(self):  # 构造函数：初始化数据
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):  # 添加新的url
        if url is None:  # 如果为空
            return
        if url not in self.new_urls and url not in self.old_urls:  # 不在未爬取的urls，也不在已爬取的urls中
            self.new_urls.add(url)  # 添加到未爬取的urls集合中

    def has_new_url(self):  # 通过new_urls集合的长度，判断是否有新的url
        return len(self.new_urls) != 0

    def get_new_url(self):  # 获取新的url
        new_url = self.new_urls.pop()  # 从new_urls中取出url
        self.old_urls.add(new_url)  # 同时把取出的url添加到old_urls中
        return new_url

    def add_new_urls(self, urls):  # 添加新的批量urls
        if urls is None or len(urls) == 0:
            return
        for url in urls:  # 循环单个添加到new_urls中
            self.add_new_url(url)
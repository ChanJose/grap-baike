# -*- coding: utf-8 -*-
# 爬取1000个python相关的百度百科页面数据
import url_manager
import html_downloader
import html_parser
import html_outputer


class SpiderMain(object):  # 声明类SpiderMain
    # 初始化
    def __init__(self):
        self.urls = url_manager.UrlManager()  # url管理器
        self.downloader = html_downloader.HtmlDownloader()  # 下载器
        self.parser = html_parser.HtmlParser()  # 解释器
        self.outputer = html_outputer.HtmlOutputer()  # 输出

    # 抓取页面
    def craw(self, root_url):
        count = 1  # 计算在爬取的第几个url
        self.urls.add_new_url(root_url)  # 添加新的url
        while self.urls.has_new_url():  # 当有新的url
            try:
                new_url = self.urls.get_new_url()  # 获取新的url
                print('craw %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)  # 下载页面
                new_urls, new_data = self.parser.parse(new_url, html_cont)  # 返回新的url和数据
                self.urls.add_new_urls(new_urls)  # 添加到url管理器中
                self.outputer.collect_data(new_data)  # 收集数据

                if count == 1000:  # 爬取1000个url
                    break

                count = count + 1
            except Exception as e:  # 出现问题
                print(e)
                print('craw failed')
        self.outputer.output_html()  # 输出数据


if __name__ == "__main__":  # main函数
    root_url = "http://baike.baidu.com/item/Python"  # 入口url
    obj_spider = SpiderMain()  # 声明一个SpiderMain对象
    obj_spider.craw(root_url)  # 调用抓取页面函数

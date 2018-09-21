# -*- coding: utf-8 -*-
# import requests
import urllib.request
import ssl   # 解决报错“SSL: CERTIFICATE_VERIFY_FAILED”的问题


class HtmlDownloader(object):
    def download(self, url):
        if url is None:  # 如果url为空
            return

        context = ssl._create_unverified_context()
        response = urllib.request.urlopen(url, context=context)
        if response.getcode() != 200:  # 响应状态码
            return None
        return response.read()  # 否则，返回读取的内容
        # return response.text  # 返回响应内容


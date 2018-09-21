# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re  # 导入正则表达式库
# from urllib.parse import urljoin
import urllib.parse


class HtmlParser(object):  # 解释器
    def _get_new_urls(self, page_url, soup):  # 当前页面中新的url
        try:
            new_urls = set()  # 存结果
            # href="/item/%E9%98%BF%E5%A7%86%E6%96%AF%E7%89%B9%E4%B8%B9/2259975"
            links = soup.find_all('a', href=re.compile(r"^/item/"))  # 匹配href以/item/开头的<a>标签
            for link in links:
                new_url = link['href']
                new_full_url = urllib.parse.urljoin(page_url, new_url)
                new_urls.add(new_full_url)
            return new_urls  # 返回页面中存在的相应的urls
        except Exception as e:  # 出现错误
            print(e)

    def _get_new_data(self, page_url, soup):
        res_data = {}  # 声明为一个字典

        # url
        res_data['url'] = page_url

        # 获取标题
        # <dd class="lemmaWgt-lemmaTitle-title">
        # <h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()  # 获取结点内容

        # 获取标题的概括内容：summary
        # < div class ="lemma-summary" label-module="lemmaSummary" >
        # < div class ="para" label-module="para" > Python 是一个有条理的
        # 和强大的面向对象的程序设计语言，类似于Perl, Ruby, Scheme, 或 Java.< / div >
        # < / div >
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()  # 获取结点内容
        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data



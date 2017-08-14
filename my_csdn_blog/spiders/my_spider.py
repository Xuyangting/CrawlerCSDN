# -*- coding:utf-8 -*-
from scrapy.spider import Spider, Request
from bs4 import BeautifulSoup

class MySpider(Spider):
    name = "csdn"
    allowed_domains = ["blog.csdn.net"]
    start_urls = [
        "http://blog.csdn.net/temanm"
    ]

    # 获取blog页数 和相应的链接
    def parse(self, response):
        based_url = "http://blog.csdn.net"
        list_result = ["http://blog.csdn.net/Temanm/article/list/1"]
        soup = BeautifulSoup(response.body, 'html.parser')
        pages = soup.find("div", "list_item_new").find("div", "pagelist").find_all("a")
        for i in range(len(pages)):
            href = based_url + pages[i].get("href")
            if href not in list_result:
                list_result.append(href)
        for link in list_result:
            yield Request(link, callback=self.parse_link)

    # 获取博客链接
    def parse_link(self, response):
        based_url = "http://blog.csdn.net"
        soup = BeautifulSoup(response.body, 'html.parser')
        blog = soup.find_all("div", "list_item article_item")
        for item in blog:
            # print item.find("span", "link_title").find("a").get("href"), item.find("span", "link_title").find("a").get_text()
            href = based_url + item.find("span", "link_title").find("a").get("href")
            yield Request(href, callback=self.parse_get_blog_title)

    # 获取文章标题
    def parse_get_blog_title(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        title = soup.find("div", "details").find("div", "article_title").find("span", "link_title").find("a")
        print title.get_text()
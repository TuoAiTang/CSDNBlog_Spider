#!/usr/bin/python
# -*- coding:utf-8 -*-

# from scrapy.contrib.spiders import  CrawlSpider,Rule

from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from CSDNBlog.items import CsdnblogItem


class CSDNBlogSpider(Spider):
    """爬虫CSDNBlogSpider"""

    name = "CSDNBlog"

    # 减慢爬取速度 为1s
    # download_delay = 1
    #allowed_domains = ["blog.csdn.net"]
    start_urls = [

        # 第一篇文章地址
        "https://blog.csdn.net/u012150179/article/details/11836503"
    ]

    def parse(self, response):
        sel = Selector(response)

        # items = []
        # 获得文章url和标题
        item = CsdnblogItem()

        article_url = str(response.url)
        article_name = sel.xpath('//h1[@class="title-article"]/text()').extract_first()

        item['article_name'] = article_name
        item['article_url'] = article_url

        yield item

        # 获得下一篇文章的url
        url = response.xpath('//div[@class="tool-box"]/ul/li[last()-1]/a/@href').extract_first()
        if(url != None):
            yield Request(url, callback=self.parse)

# -*- coding:utf-8 -*-

from scrapy.item import Item, Field


class CsdnblogItem(Item):
    """存储提取信息数据结构"""

    article_name = Field()
    article_url = Field()

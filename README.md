# CSDNBlog_Spider
初试scrapy,自动爬取csdn某一博主全部文章
完整体验了item, pipeline, setting, spider的工作流程
大致了解了scrapy的使用
为了项目的实用性
实现了两种持久化方式：
  1：json本地存储（json库）
  2：存储到mysql数据库（pymysql库）
解决了关于json.dumps()的编码问题

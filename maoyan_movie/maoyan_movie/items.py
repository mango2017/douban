# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    movie_name = scrapy.Field()  #电影名字
    movie_score = scrapy.Field()  #电影评分
    movie_detail = scrapy.Field()  #电影简介
    movie_href = scrapy.Field() #跳转详情

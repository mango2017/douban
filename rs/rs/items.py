# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    rs_number = scrapy.Field()

    rs_name = scrapy.Field()

    rs_count = scrapy.Field()
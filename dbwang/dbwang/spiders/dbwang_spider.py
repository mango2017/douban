import scrapy
from scrapy.spiders import Spider
from dbwang.items import DbwangItem

class DbwangSpiderSpider(scrapy.Spider):
    name = 'dbwang_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        item = DbwangItem()
        movies = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            item['ranking'] = movie.xpath(".//div[@class='item']//em/text()").extract_first()
            item['movie_name'] = movie.xpath(".//div[@class='hd']/a/span[1]/text()").extract_first()
            item['score'] = movie.xpath(".//div[@class='star']/span[@class='rating_num']/text()").extract_first()
            item['score_num'] = movie.xpath(".//div[@class='star']/span[4]/text()").extract_first()
            yield item
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250" + next_link, callback=self.parse)

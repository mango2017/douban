import scrapy
from maoyan_movie.items import MaoyanMovieItem

class MaoyanSpiderSpider(scrapy.Spider):
    name = 'maoyan_spider'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/?utm_source=meituanweb']

    def parse(self, response):
        movie_list = response.xpath("//div[@class='movie-grid']/div[1]//dl[@class='movie-list']/dd")
        print(movie_list)
        for m_item in movie_list:
            movie_item = MaoyanMovieItem()
            movie_item['movie_name'] = m_item.xpath(".//div[contains(@class,'movie-title')]/text()").extract_first()
            score_1 = m_item.xpath(".//div[@class='movie-score']/i[1]/text()").extract_first()
            score_2 = m_item.xpath(".//div[@class='movie-score']/i[2]/text()").extract_first()
            movie_item['movie_score'] = score_1+score_2
            movie_item['movie_href'] = "https://maoyan.com" + m_item.xpath(".//div[@class='movie-item']/a/@href").extract_first()

            yield scrapy.Request(
                movie_item['movie_href'],
                callback=self.parse_detail,
                meta={"movie_item":movie_item}
            )


    def parse_detail(self,response):
        movie_item = response.meta['movie_item']
        movie_item['movie_detail'] = response.xpath("//div[@class='mod-content']/span/text()").extract_first()
        yield  movie_item







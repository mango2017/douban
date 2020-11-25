import scrapy
from rs.items import RsItem

class RsSpiderSpider(scrapy.Spider):
    name = 'rs_spider'
    allowed_domains = ['baidu.com']
    # start_urls = ['https://www.baidu.com/s?wd=xpath&rsv_spt=1&rsv_iqid=0x9057622600031126&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=88093251_56_hao_pg&rsv_enter=1&rsv_dl=tb&oq=scrapy%2520%25E7%2588%25AC%25E8%2599%25AB%25E7%2599%25BE%25E5%25BA%25A6%25E7%2583%25AD%25E6%2590%259C&rsv_btype=t&inputT=2207&rsv_t=de88ER8GoD6avs2hmvh8EfNrrmGqPVrR48vpIajhRXm%2FqLxZWZNHHpf03fgV6%2Fuhr412QTzu92ES&rsv_pq=c8dd316300034634&rsv_sug2=0&rsv_sug4=2207']
    start_urls = ['https://www.baidu.com/s?wd=php&rsv_spt=1&rsv_iqid=0x9057622600031126&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=88093251_56_hao_pg&rsv_enter=1&rsv_dl=tb&oq=xpath&rsv_btype=t&inputT=724&rsv_t=1319pUuL70aYjuG1v7PA1m93QRM%2Bu0Oo68Xu8rBMhkvJcGVGsOmBM8brnq%2BYwP2JTj9HrKN%2BuWVj&rsv_pq=97e71ff300050893&rsv_sug2=0&rsv_sug4=724']

    def parse(self, response):
        # print(response.xpath("//div[@class='opr-recommends-merge-content']//div[contains(@class,'opr-recommends-merge-item-new')]/div[@class='opr-recommends-merge-img-titleline-height']/a/text()").extract())
        # print(response.body)
        rs_list = response.xpath("//table[contains(@class,'opr-toplist1-table')]/tbody/tr")

        for i_item in rs_list:
            rs_item = RsItem()
            rs_item['rs_name'] = i_item.xpath("./td[1]/a/text()").extract()
            rs_item['rs_name'] = rs_item['rs_name'][0].replace("\xa0", "").strip()  #去掉\n\r

            rs_item['rs_number'] = i_item.xpath('./td[1]/span[1]/text()').extract()
            rs_item['rs_number'] = rs_item['rs_number'][0].replace("\xa0", "").strip() #去掉\n\r

            rs_item['rs_count'] = i_item.xpath('./td[2]/text()').extract_first()
            yield rs_item
            print(rs_item)


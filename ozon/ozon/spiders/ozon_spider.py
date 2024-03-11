import scrapy


class OzonSpiderSpider(scrapy.Spider):
    name = "ozon_spider"
    allowed_domains = ["ozon.ru"]
    start_urls = ["https://ozon.ru"]

    def parse(self, response):
        pass

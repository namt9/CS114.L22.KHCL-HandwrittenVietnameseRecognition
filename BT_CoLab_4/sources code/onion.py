import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'onion'
    def start_requests(self):
        urls = [
        ]
        for i in range(0, 1001, 20):
            urls.append('https://www.theonion.com/breaking-news/news-in-brief?startIndex=' + str(i))
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        for products in  response.css('a'):
            yield {
                'title' : products.css('h2::text').get(),
            }
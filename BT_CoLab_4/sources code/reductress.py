import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'reductress'
    def start_requests(self):
        urls = [
            'https://reductress.com/news/page/1/'
        ]
        for i in range(2, 61):
            urls.append('https://reductress.com/news/page/' + str(i) + '/')
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        for products in response.css('div.container').css('div.content').css('div.row'):
            yield {
                'title' : products.css('h1::text').get(),
            }
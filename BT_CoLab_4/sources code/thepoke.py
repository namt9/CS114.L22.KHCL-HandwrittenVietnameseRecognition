import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'thepoke'
    def start_requests(self):
        urls = [
            'https://www.thepoke.co.uk'
        ]
        for i in range(2, 701):
            urls.append('https://www.thepoke.co.uk/page/' + str(i) + '/')
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        for products in response.css('div.boxframe').css('div.txt'):
            yield {
                'title' : products.css('p::text').getall(),
            }
            
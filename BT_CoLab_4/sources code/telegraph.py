import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'telegraph'
    def start_requests(self):
        urls = [
            'https://www.telegraph.co.uk/news/',
            'https://www.telegraph.co.uk/politics/',


        ]
        for i in range(2, 301):
            urls.append('https://www.telegraph.co.uk/news/page-' + str(i) + '/')
            urls.append('https://www.telegraph.co.uk/politics/page-' + str(i) + '/')
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        for products in response.css('section.article-list').css('div.card__content').css('h3').css('a'):
            yield {
                'title' : products.css('span::text').getall(),
            }
            
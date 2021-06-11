import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'bestinau'
    def start_requests(self):
        urls = [
        ]
        for i in range(1, 16):
            urls.append('https://bestinau.com.au/category/news/page'+ str(i) + '/')
        for i in range(1,19):
            urls.append('https://bestinau.com.au/category/digital-world/page/' + str(i) + '/')
        for i in range(1,23):
            urls.append('https://bestinau.com.au/category/entertainment/page' + str(i) + '/')
        for i in range(1, 17):
            urls.append('https://bestinau.com.au/category/sport/page/' + str(i) + '/')
        for i in range(1,15):
            urls.append('https://bestinau.com.au/category/politics/page/' + str(i) + '/')
        for i in range(1,5):
            urls.append('https://bestinau.com.au/category/business/school-education/page/' + str(i) + '/')
        for i in range(1,14):
            urls.append('https://bestinau.com.au/category/technology/page/' + str(i) + '/')

        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        for products in response.css('div.td-container').css('h3'):
            yield {
                'title' : products.css('a::text').get(),
            }
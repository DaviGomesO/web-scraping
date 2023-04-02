import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    def parse(self, response):
        id = 1
        for filmes in response.css('.titleColumn'):
            yield{
                'id': id,
                'titulo': filmes.css('.titleColumn a ::text').get(),
                'ano': filmes.css('.secondaryInfo ::text').get(),
                'nota': response.css('strong ::text').get()
            }
            id = id + 1

        pass

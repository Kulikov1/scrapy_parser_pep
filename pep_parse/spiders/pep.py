import scrapy

from pep_parse.constants import PATERN
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """ Основной паук проекта

    Парсит данные по каждому PEP с сайта https://peps.python.org/
    Сохраняет в .csv файле номер, название и статус по каждому PEP
    Так же сохраняет в отдельный файл общее количество PEP по каждоуму статусу
    """

    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """Парсинг основного урл"""

        tab = response.css('table.pep-zero-table')
        all_peps = tab.css('tbody a::attr(href)')
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Парсинг каждого PEP"""

        title = response.css('h1.page-title::text').get()
        data = {
            'number': PATERN.search(title).group(1),
            'name': PATERN.search(title).group(2),
            'status': response.css(
                'dt:contains("Status") + dd').css('abbr::text').get()
        }
        yield PepParseItem(data)

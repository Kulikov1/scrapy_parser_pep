import scrapy

from pep_parse.constants import ALLOWED_DOMAINS, PATERN, START_URLS
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """ Основной паук проекта

    Парсит данные по каждому PEP с сайта https://peps.python.org/
    Сохраняет в .csv файле номер, название и статус по каждому PEP
    Так же сохраняет в отдельный файл общее количество PEP по каждоуму статусу
    """

    name = 'pep'
    allowed_domains = [ALLOWED_DOMAINS]
    start_urls = [START_URLS]

    def parse(self, response):
        """Парсинг основного урл"""

        tab = response.css('table.pep-zero-table')
        all_peps = tab.css('tbody tr')
        for pep in all_peps:
            pep_link = pep.css('a::attr(href)').extract_first()
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response) -> object:
        """Парсинг каждого PEP"""

        title = response.css('h1.page-title::text').get()
        data = {
            'number': PATERN.search(title).group(1),
            'name': PATERN.search(title).group(2),
            'status': response.css(
                'dt:contains("Status") + dd').css('abbr::text').get()
        }
        yield PepParseItem(data)

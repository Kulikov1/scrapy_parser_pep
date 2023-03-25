import scrapy


class PepParseItem(scrapy.Item):
    """Основная модель парсера"""

    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()

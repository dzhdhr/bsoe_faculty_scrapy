# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BsoeFacultyScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    email_address = scrapy.Field()
    title = scrapy.Field()
    department = scrapy.Field()
    research_areas = scrapy.Field()
    selected_publications = scrapy.Field()
    web_page = scrapy.Field()
    student = scrapy.Field()
    biography = scrapy.Field()
    degree = scrapy.Field()
    pass

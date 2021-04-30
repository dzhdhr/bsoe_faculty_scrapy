import scrapy
import base64

from bsoe_faculty_scrapy.items import BsoeFacultyScrapyItem


class FacultySpider(scrapy.Spider):
    name = 'faculty'
    allowed_domains = ['www.soe.ucsc.edu']
    start_urls = ['https://www.soe.ucsc.edu/people/faculty']

    def parse(self, response):
        urls = response.xpath("//div[@id='middle-wrapper']//li[not (@class)]/a/@href").extract()

        for url in urls:
            u = 'https://www.soe.ucsc.edu%s' % url
            yield response.follow(u, self.get_info)
            # yield {"url": u}

    def get_info(self, response):

        keys = response.xpath('//div/label//text()').extract()
        contains = {'name': response.xpath("//div[@id='body-wrapper']/h1/text()").extract_first()}
        contain = response.xpath("//div[@id='body-wrapper']//ul")
        for i, c in enumerate(contain):
            if c.xpath('.//script'):
                bs64 = c.xpath('.//script/text()').extract_first()
                bs64 = bs64.split('\'')[1]
                email = str(base64.standard_b64decode(bs64))
                email = email.split('>')[1]
                email = email.split('<')[0]

                contains[keys[i]] = email

            elif c.xpath('.//a'):

                url = c.xpath('.//a/@href').extract()
                u = ','.join(url)
                contains[keys[i]] = u
                # print(c.xpath('.//a/@href'))
            else:
                contains[keys[i]] = c.xpath('./li//text()').extract_first()
        item = BsoeFacultyScrapyItem()
        item['name'] = contains.get('name')
        item['email_address'] = contains.get('E-Mail Address ')
        item['title'] = contains.get('Title ')
        item['department'] = contains.get('Department ')
        item['research_areas'] =  contains.get('Research Areas ')
        item['selected_publications'] = contains.get('Selected Publications ')
        item['web_page'] = contains.get('Web Page ')
        item['student'] = contains.get('Student ')
        item['biography'] = contains.get('Biography ')
        item['degree'] = contains.get('Degree ')

        yield item

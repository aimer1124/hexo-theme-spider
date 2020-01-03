import scrapy


class ThemeSpider(scrapy.Spider):
    name = "themes"

    def start_requests(self):
        urls = [
            'https://hexo.io/themes/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.log('------Saved theme---------')
        # self.log('%s' % response.body)
        for theme in response.css(".plugin"):
            self.log(theme.css(".plugin-name::text").get())
            self.log(theme.css(".plugin-name::attr(href)").get())

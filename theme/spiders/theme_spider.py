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
        for theme in response.css(".plugin.on"):
            theme_name = theme.css(".plugin-name::text").get()
            theme_url = theme.css(".plugin-name::attr(href)").get()
            yield scrapy.Request(url=theme_url, callback=self.parse_github, cb_kwargs={
                'name': theme_name,
                'url': theme_url})

    def parse_github(self, response, name, url):
        data = response.css(".social-count::attr(aria-label)").getall()
        watch = data[0].split(' ')[0]
        star = data[1].split(' ')[0]
        folk = data[2].split(' ')[0]
        self.log("The theme's name is %s , watch is %s, star is %s , fold is %s, the url is %s." % (name, watch, star, folk, url))

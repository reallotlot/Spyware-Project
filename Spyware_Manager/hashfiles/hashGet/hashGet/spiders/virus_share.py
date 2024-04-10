import scrapy


class VirusShareSpider(scrapy.Spider):
    name = "virus_share"
    start_urls = [f"https://virusshare.com/hashfiles/VirusShare_00005.md5"]
    def parse(self, response):
        content = list(response.text.split('\n'))
        with open("..\Spyware_Manager\hashfiles\md5.txt", 'a') as md5:
            for i in content: 
                md5.write(i + '\n')
            md5.write(f"########################################################## FILE 5 END")
        
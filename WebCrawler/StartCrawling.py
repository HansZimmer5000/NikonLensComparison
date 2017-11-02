# Start the LensSpider and let it crawl.
# start_urls and name is set in LensSpider class.

from LensSpider import LensSpider
from scrapy.crawler import CrawlerProcess
import RawData

def start_spider_within_python():
    custom_settings = {
        'DOWNLOAD_DELAY': 7,
		'RANDOMIZE_DOWNLOAD_DELAY': False, #from 0.5*DELAY till 1.5*DELAY
		'COOKIES_ENABLED': False
    }
    process = CrawlerProcess(custom_settings)
    process.crawl(LensSpider)
    process.start() 

if __name__ == "__main__":
	RawData.clean_rawdata_file_and_write_titles()
	start_spider_within_python()
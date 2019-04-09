import scrapy
import base64
from bs4 import BeautifulSoup
from Pchome.items import PchomeItem

class PchomeCrawler(scrapy.Spider):
    
    name = 'pchome'
    key = input("請輸入你想要搜尋的關鍵字 :")
    base64_key = base64.b64encode(key.encode('utf-8'))
    #print(str(base64_key, 'utf-8'))
    start_urls = ['https://www.pcstore.com.tw/adm/psearch.htm?store_k_word='+ str(base64_key, 'utf-8') +'=&slt_k_option=1']
    print("網址為 : "+ start_urls[0])
    
    def parse(self, response):
        #print("測試")
        res = BeautifulSoup(response.body)
        
        for products in res.select('div.pic2')[2:]:
            print('title :'+ products.select('a')[0].text)
            print('shop :'+ products.select('a')[-1].text)
            print('money :'+ products.select('.pic3')[0].text)
            pchomeItem = PchomeItem()
            pchomeItem['title'] = products.select('a')[0].text
            pchomeItem['shop'] = products.select('a')[-1].text
            pchomeItem['money'] = products.select('.pic3')[0].text
            yield pchomeItem

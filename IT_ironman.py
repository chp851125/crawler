import requests
from bs4 import BeautifulSoup
import re

def get_info(articles):
    for article in articles:
        try:
            print(article.select('div.qa-list__info a.qa-list__info-time')[0].text, article.select('div.qa-list__series a')[0].text, "：", article.select('h3.qa-list__title a')[0].text, article.select('h3.qa-list__title a')[0]['href'])
        except Exception as err:
            print(article.select('div.qa-list__info a.qa-list__info-time')[0].text, article.select('h3.qa-list__title a')[0].text, article.select('h3.qa-list__title a')[0]['href'])

def crawler():
    url = "https://ithelp.ithome.com.tw/tags/articles/%E9%90%B5%E4%BA%BA%E8%B3%BD?tab=hot"
    for i in range(1):
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        articles = soup.select('div.qa-list')
        paging = soup.select("ul.pagination li a")
        next_url = paging[len(paging) - 1]['href']  # 每頁paging陣列個數可能不同，但一定是最後一個
        url = next_url
        get_info(articles)
        
crawler()

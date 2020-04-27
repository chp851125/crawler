import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def get_info(articles):
    for article in articles:
        array = [
            article.select('div.qa-list__info a.qa-list__info-time')[0].text,
            article.select('div.qa-list__series a')[0].text,
            article.select('h3.qa-list__title a')[0].text,
            article.select('h3.qa-list__title a')[0]['href']
        ]
        try:
            print(array[0], array[1], ":", array[2], array[3])
        except Exception as err:
            print(array[0], array[2], array[3])
'''
def excel():
    # 將數據寫入Excel 
    wb = Workbook() 
    # 設置Excel文件名 
    dest_filename = 'UserInfoFile.xlsx' 
    # 新建一個表 
    ws1 = wb.active 
    # 設置表頭 
    titleList = ['時間', '網址', '招聘企業', '學校', '地址'] for row in range(len(titleList)): c = row + 1 ws1.cell(row=1, column=c, value=titleList[row]) 
    # 填寫表內容 
    for listIndex in range(len(setSQLData)): 
        ws1.append(setSQLData[listIndex]) 
    wb.save(filename=dest_filename)
'''

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

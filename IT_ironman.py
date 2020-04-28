#此爬蟲網頁為 iT邦 與鐵人賽相關文章 熱門文章
#將輸出結果建立至excel.xls

import requests
from bs4 import BeautifulSoup
import re
import xlwt

#使用全域變數儲存爬蟲結果資訊，需再優化
result = []
column = 4
def get_info(articles):
    global result
    for article in articles:
        array = [
            article.select('div.qa-list__info a.qa-list__info-time')[0].text,
            #article.select('div.qa-list__series a')[0].text,
            '',
            article.select('h3.qa-list__title a')[0].text,
            article.select('h3.qa-list__title a')[0]['href']
        ]
        try:
            #print(array[0], array[1], ":", array[2], array[3])
            array[1] = article.select('div.qa-list__series a')[0].text
            #count += 1
            #print(array)
            result.append(array)

        except Exception as err:
            #print(array[0], array[2], array[3])
            #count += 1
            result.append(array)

def save_excel(information):
    global column
    print("輸出中")
    wb = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = wb.add_sheet('sheet1', cell_overwrite_ok=True)
    # 按位置添加數據，前面兩個參數是位置，後面一個是單元格內容 sheet.write(0, 0, '123')
    for i in range(len(information)):
        for k in range(column):
            sheet.write(i, k, information[i][k])
    wb.save('C:/Users/user/Desktop/test.xls')
    print("已完成")

def crawler(page):
    url = "https://ithelp.ithome.com.tw/tags/articles/%E9%90%B5%E4%BA%BA%E8%B3%BD?tab=hot"
    for i in range(page):
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        articles = soup.select('div.qa-list')
        paging = soup.select("ul.pagination li a")
        next_url = paging[len(paging) - 1]['href']  # 每頁paging陣列個數可能不同，但一定是最後一個
        url = next_url
        get_info(articles)
        print("爬蟲第"+str(i+1)+"頁")

#crawler()內輸入要爬蟲的頁數
crawler(4)
save_excel(result)

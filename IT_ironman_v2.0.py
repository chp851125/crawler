#此爬蟲網頁為 iT邦 與鐵人賽相關文章 熱門文章
#將輸出結果建立至excel.xls

import requests
from bs4 import BeautifulSoup
import re
import xlwt

#輸入要儲存的路徑檔名 例：'C:/Users/user/Desktop/test.xls'
filename = 'C:/Users/user/Desktop/test.xls'

def save_excel(result, column):
    global filename
    print("輸出中")
    wb = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = wb.add_sheet('sheet1', cell_overwrite_ok=True)
    # 按位置添加數據，前面兩個參數是位置，後面一個是單元格內容 sheet.write(0, 0, '123')
    for i in range(len(result)):
        for k in range(column):
            sheet.write(i, k, result[i][k])
    #設定excel欄寬
    sheet.col(0).width = 256 * 12
    sheet.col(1).width = 256 * 50
    sheet.col(2).width = 256 * 60
    sheet.col(3).width = 256 * 45
    wb.save(filename)
    print("已完成")

def crawler(page):
    url = "https://ithelp.ithome.com.tw/tags/articles/%E9%90%B5%E4%BA%BA%E8%B3%BD?tab=hot"
    result = []
    for i in range(page):
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        articles = soup.select('div.qa-list')
        paging = soup.select("ul.pagination li a")
        next_url = paging[len(paging) - 1]['href']  # 每頁paging陣列個數可能不同，但一定是最後一個
        url = next_url
        print("爬蟲第"+str(i+1)+"頁")

        #擷取每一頁的欄位
        for article in articles:
            array = [
                article.select('div.qa-list__info a.qa-list__info-time')[0].text,
                # article.select('div.qa-list__series a')[0].text, #非所有文章都有系列小標題
                '',
                article.select('h3.qa-list__title a')[0].text,
                article.select('h3.qa-list__title a')[0]['href']
            ]

            column = len(array)
            try:
                # print(array[0], array[1], array[2], array[3])
                array[1] = article.select('div.qa-list__series a')[0].text
                result.append(array)

            except Exception as err:
                # print(array[0], array[2], array[3])
                result.append(array)

    save_excel(result, column)

#crawler()內輸入要爬蟲的頁數
crawler(2)

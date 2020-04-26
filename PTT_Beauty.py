import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlretrieve
import os

payload={
    'from':'/bbs/Beauty/index.html',
    'yes':'yes'
}

rs = requests.session()
res = rs.post('https://www.ptt.cc/ask/over18', verify=False, data=payload)
reg_imgur_file  = re.compile('http[s]?://[i.]*imgur.com/\w+\.(?:jpg|png|gif)')


def download_images(articles):
    for article in articles:
        print(article.text, article['href'])
        if not os.path.isdir(os.path.join('download', article.text)):
            os.mkdir(os.path.join('download', article.text))
        res = rs.get("https://www.ptt.cc"+article['href'])
        images = reg_imgur_file.findall(res.text)
        print(images)

        for image in set(images):
            ID = re.search('http[s]?://[i.]*imgur.com/(\w+\.(?:jpg|png|gif))', image).group(1)
            print(ID)
            urlretrieve(image, os.path.join('download', article.text, ID))

def crawler():
    if not os.path.isdir('download'):
        os.mkdir('download')

    url = "https://www.ptt.cc/bbs/Beauty/index.html"

    for i in range(3):
        res = rs.get(url, verify=False)
        soup = BeautifulSoup(res.text, "html.parser")
        articles = soup.select("div.title a")
        paging = soup.select("div.btn-group-paging a")
        next_url = 'https://www.ptt.cc'+paging[1]['href']
        url = next_url
        download_images(articles)

crawler()

# 引入套件
import csv

import requests
from bs4 import BeautifulSoup

# 設定網路請求 headers 讓網站覺得是正常人瀏覽
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
}

# 發出網路請求 GET
resp = requests.get('https://www.ptt.cc/bbs/Baseball/index.html', headers=headers)
# 使用 BeautifulSoup 解析內容為 BeautifulSoup 物件
soup = BeautifulSoup(resp.text, 'html.parser')
items = soup.select('.r-ent')
# 解析抓取 class name 為 r-ent 區塊（list 列表）
# 宣告一個暫存列表 list
row_list = []

# 一一取出 r-ent 區塊，注意網路爬蟲往往需要額外處理例外的格式避免程式錯誤
for item in items:
    # 為了避免抓取到刪除文章產生 list index out of range 錯誤，先判斷若文章作者若為 - 則跳過該列
    print('author', item.select('.author'))
    # 取得作者
    author = item.select('.author')[0].text
    if author == '-':
        print('continue')
        continue
    # 取得 class name title 內的 a 超連結（由於 select 回傳會是 list 所以 index 0 取第一個，text 為元素內容）
    title = item.select('.title a')[0].text

    # 將資料整理成一個 dict
    data = {}
    data['title'] = title
    data['author'] = author
    # 存入 row_list 方便之後寫入 csv 檔案使用
    row_list.append(data)
    print(data)
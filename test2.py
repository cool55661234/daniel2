# 引入套件
import csv

import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
}

resp = requests.get('https://movies.yahoo.com.tw/movie_comingsoon.html',
                    headers=headers)
soup = BeautifulSoup(resp.text, 'html.parser')
items = soup.select('.release_info')

row_list = []
for item in items:

    title = item.select('.release_movie_name a')[0].text

    time = item.select('.release_movie_time')[0].text
    data = {}
    data['title'] = title
    data['time'] = time
    row_list.append(data)
    print(data)

headers = ['title', 'time']

with open('yahoo_movie3.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, headers)
    dict_writer.writeheader()
    dict_writer.writerows(row_list)

with open('yahoo_movie3.csv', 'r') as input_file:
    rows = csv.reader(input_file)


    for row in rows:
        print(row)
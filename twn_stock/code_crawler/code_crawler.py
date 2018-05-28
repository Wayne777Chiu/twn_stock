
import requests
import urllib.request
from lxml import etree
import csv

# TWSE
TWSE_REQ_URL = 'http://isin.twse.com.tw/isin/C_public.jsp?strMode=2'
TPEX_REQ_URL = 'http://isin.twse.com.tw/isin/C_public.jsp?strMode=4'


def get_data_from_url(url):
    contents = requests.get(url)
    root = etree.HTML(contents.text)
    trs = root.xpath('//tr')[0:]
    i = 0
    for child in trs:
        tr = list(map(lambda x: x.text, child.iter()))
        if i <= 20:
            print(tr)
        i += 1



if __name__ == '__main__':
    get_data_from_url(TWSE_REQ_URL)
    print('ok')

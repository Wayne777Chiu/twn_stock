
import requests
from collections import namedtuple
from lxml import etree
import csv

# Securities Code Reference:
# http://www.twse.com.tw/zh/page/products/stock-code2.html
# TWSE
TWSE_REQ_URL = 'http://isin.twse.com.tw/isin/C_public.jsp?strMode=2'
# TPEX
TPEX_REQ_URL = 'http://isin.twse.com.tw/isin/C_public.jsp?strMode=4'


class CrawlerCoder:

    def __init__(self):
        self.ROW = namedtuple('row', ['type', 'id', 'name', 'ISIN_code', 'start_date', 'market', 'industry', 'CFI_code'])

    def make_row_data(self, type_data, row):
        id_number, name = row[1].split('\u3000')
        return self.ROW(type_data, id_number, name, *row[2:-1])

    def get_data_from_url(self, url):
        contents = requests.get(url)
        root = etree.HTML(contents.text)
        trs = root.xpath('//tr')[1:]
        result = []
        type_name = ''
        for tr in trs:
            tr = list(map(lambda x: x.text, tr.iter()))
            if len(tr) == 4:
                type_name = tr[2].strip(' ')
            else:
                result.append(self.make_row_data(type_name, tr))

        def to_csv(filename):
            with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(result[0]._fields)
                for d in result:
                    writer.writerow([_ for _ in d])
        return to_csv


if __name__ == '__main__':
    coder = CrawlerCoder()
    coder.get_data_from_url(TWSE_REQ_URL)('twse_equities.csv')
    coder.get_data_from_url(TPEX_REQ_URL)('tpex_equities.csv')
    print('ok')

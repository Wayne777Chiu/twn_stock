
import requests
# import urllib.request
from collections import namedtuple
from lxml import etree
import csv

# TWSE
TWSE_REQ_URL = 'http://isin.twse.com.tw/isin/C_public.jsp?strMode=2'
TPEX_REQ_URL = 'http://isin.twse.com.tw/isin/C_public.jsp?strMode=4'

ROW = namedtuple('row',['type','id','name','ISIN_code','start_date','market','industry','CFI_code'])

def make_row_data(type_data,row):
    id,name = row[1].split('\u3000')
    return ROW(type_data,id,name,*row[2:-1])

def get_data_from_url(url):
    contents = requests.get(url)
    root = etree.HTML(contents.text)
    trs = root.xpath('//tr')[1:]
    result=[]
    type_name=''
    for tr in trs:
        tr = list(map(lambda x: x.text, tr.iter()))
        if len(tr) == 4:
            type_name = tr[2].strip(' ')
        else:
            result.append(make_row_data(type_name,tr))
    return result

def to_csv(url,filename):
    data = get_data_from_url(url)
    '''with open(filename,'w',newline='',encoding='utf-8') as file:
        for item_name in data[0]._fields:
            file.write(item_name)
            file.write(',')
        file.write('\n')
        for line in data:
            for single in line:
                #print(i)
                if single is None:
                    file.write('')
                else:
                    file.write(single)
                file.write(',')
            file.write('\n')
        file.close()'''

    with open(filename, 'w', newline='',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile,
                            delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        writer.writerow(data[0]._fields)
        for d in data:
            #writer.writerow(d)
            writer.writerow([_ for _ in d])

if __name__ == '__main__':
    to_csv(TWSE_REQ_URL,'twse_equities.csv')
    to_csv(TPEX_REQ_URL,'tpex_equities.csv')
    print('ok')

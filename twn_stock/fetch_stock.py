
import urllib.parse
import requests

TWSE_BASE_URL = 'http://www.twse.com.tw/'
TPEX_BASE_URL = 'http://www.tpex.org.tw/'

class stock_source:

    def __init__(self):
        self.twse_base_url= TWSE_BASE_URL
        self.tpex_base_url= TWSE_BASE_URL


    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year_data:  int):
        if year_data < 81:
            raise ValueError('Year is less than 81')
        if year_data < 127:
            self._year = ''.join('{:}'.format(str(year_data+1911)))
        elif year_data < 1992:
            raise ValueError('Year is less than 81')
        else:
            self._year = ''.join('{:}'.format(str(year_data)))


def dataparser():
    REPORT_URL = urllib.parse.urljoin(TWSE_BASE_URL, 'exchangeReport/STOCK_DAY')
    year = 2018
    month = 5
    sid = 1101
    params = {'date': '%d%02d01' % (year, month), 'stockNo': sid}
    r = requests.get(REPORT_URL, params=params)
    print(r.content)

if __name__ == '__main__':
    # dataparser()
    source = stock_source()
    source.year = 83
    print(source.year)
    source.year = 2008
    print(source.year)
    #stock_id
    #date
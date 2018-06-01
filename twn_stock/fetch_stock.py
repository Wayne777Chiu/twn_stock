
import urllib.parse
import requests

TWSE_BASE_URL = 'http://www.twse.com.tw/'
TPEX_BASE_URL = 'http://www.tpex.org.tw/'


class StockSource:

    def __init__(self):
        self.twse_base_url = TWSE_BASE_URL
        self.tpex_base_url = TWSE_BASE_URL
        self._year = ''
        self._month = ''
        self._day = ''
        self._date = '19920104'

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self,  date_data: str):
        split_symbol = ''
        if len(date_data.split('/')) is 3:
            split_symbol = '/'
            error = False
        elif len(date_data.split('\\')) is 3:
            split_symbol = '\\'
            error = False
        elif len(date_data.split('-')) is 3:
            split_symbol = '-'
            error = False

        if error is False:
            date_list = date_data.split(split_symbol)
            print(date_list)
            self.year = int(date_list[0])
            self.month = int(date_list[1])
            self.day = int(date_list[2])
            self._date = self._year + self._month + self._day
            print(self._date)
        if error is True:
            raise ValueError('Date not recognize')

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year_data:  int):
        if year_data < 81:
            raise ValueError('Year must bigger than 80')
        if year_data < 127:
            self._year = ''.join('{}'.format(str(year_data+1911)))
        elif year_data < 1992:
            raise ValueError('Year must bigger than 1991')
        else:
            self._year = ''.join('{}'.format(str(year_data)))

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, month_data: int):
        if month_data > 12:
            raise ValueError('Month must be between 1 ~ 12')
        else:
            self._month = ''.join('{:02}'.format(x) for x in int.to_bytes(month_data, length=1, byteorder='big'))

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day_data: int):
        if day_data > 31:
            raise ValueError('Day must be between 1 ~ 31')
        else:
            self._day = ''.join('{:02}'.format(x) for x in int.to_bytes(day_data, length=1, byteorder='big'))


def dataparser():
    report_url = urllib.parse.urljoin(TWSE_BASE_URL, 'exchangeReport/STOCK_DAY')
    year = 2018
    month = 5
    sid = 1101
    params = {'date': '%d%02d01' % (year, month), 'stockNo': sid}
    r = requests.get(report_url, params=params)
    print(r.url)
    # print(r.content)


if __name__ == '__main__':
    # dataparser()
    string_input = input('please input:')
    source = StockSource()
    source.date = string_input

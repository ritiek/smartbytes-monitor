#!/usr/bin/env python

from bs4 import BeautifulSoup

try:
    import urllib2
except ImportError:
    import urllib.request as urllib2


class _ExtractInformation:
    def __init__(self, soup):
        table = soup.find('table')
        info = [span.get_text()
                for span in table.find_all('span')]

        self.data_total = info[0]
        self.data_left= info[1]
        self.days_left= info[2]
        self.dsl_number= info[3]


def smartbytes():
    soup = _parse_url('http://122.160.230.125:8080/planupdate/')
    smartbytes  = _ExtractInformation(soup)
    return smartbytes


def _parse_url(url):
    response = urllib2.urlopen(url)
    soup = BeautifulSoup(response.read(), 'html.parser')
    response.close()
    return soup


def _command_line():
    smartbytes = smartbytes()
    print('=============================')
    print('Total data : ' + smartbytes.data_total)
    print('Data left  : ' + smartbytes.data_left)
    print('Days left  : ' + smartbytes.days_left)
    print('DSL number : ' + smartbytes.dsl_number)
    print('=============================')


if __name__ == '__main__':

    _command_line()

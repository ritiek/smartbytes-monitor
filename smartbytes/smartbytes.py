#!/usr/bin/env python

from bs4 import BeautifulSoup

try:
    import urllib2
except ImportError:
    import urllib.request as urllib2


def parse_url(url):
    response = urllib2.urlopen(url)
    soup = BeautifulSoup(response.read(), 'html.parser')
    response.close()
    return soup


def extract_info(soup):
    table = soup.find('table')
    info = [span.get_text()
            for span in table.find_all('span')]
    return info


def command_line():
    soup = parse_url('http://122.160.230.125:8080/planupdate/')
    data_total, data_left, days_left, dsl_number  = extract_info(soup)

    print('Total data : ' + data_total)
    print('Data left  : ' + data_left)
    print('Days left  : ' + days_left)
    print('DSL number : ' + dsl_number)


if __name__ == '__main__':

    command_line()

"""
 a .py file for tickers module. use python3 tickers.py number_of_tickers
 ticker_filename to execute
"""

import requests
import re
link = "http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQrender=download"

d = requests.get(link)
#print(d.text
html_file = open('html.txt', 'w')
html_file.write(d.text)
html_file = open('html.txt')

# print(html_file)
tickerbaselink = "https://www.nasdaq.com/symbol/"
i = 1
for line in html_file.readlines():
    x = re.search(tickerbaselink, line)
    if x is not None:
    #really ratchet counter, but it works :) 
        if i is 1:
            print(x.string)
        if i is 3:
            i = 0
        i = i + 1

# fetches the first n valid tickers from the following URL and write tickes in
# file tickers.txt
# def save_tickers():
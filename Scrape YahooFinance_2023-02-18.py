import cv2
import csv
import time
import yfinance as yf
import re
import os


with open(r'C:\Users\abyssinianHornbill\Dropbox\GME Script\companyList\company_list_2022-12-16.csv', newline='') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    header = next(csvReader)
    for row in csvReader:
        ticker = row[0]
        print(ticker)

        tickerDF = yf.download(ticker, start="2019-01-02", end="2023-02-18")
        directory = r'C:\Users\abyssinianHornbill\Dropbox\GME Script\shortPercentAnalysis\pricedta'
        outfile = os.path.join(directory, ticker+'.dta')
        tickerDF.to_stata(outfile)  

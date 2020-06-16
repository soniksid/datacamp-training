# Importing files from web

# importing required packages
import pandas as pd
import requests
from urllib.request import urlretrieve, Request, urlopen
from bs4 import BeautifulSoup

# getting files using urlretrieve() function
url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
urlretrieve(url, 'corona.csv')
df = pd.read_csv('corona.csv')
print(df.head())


# getting HTML files from web using requests package
url = "https://siddharth.engineer"
request = Request(url)
response = urlopen(request)
html = response.read()
print(html)
response.close()


# getting HTML text files from webpage using requests package 
url = "https://siddharth.engineer"
r = requests.get(url)
text = r.text
print(text)


# getting HTML structured data from webpage using BeautifulSoup package
url = "https://siddharth.engineer"
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html)
print(soup.prettify)
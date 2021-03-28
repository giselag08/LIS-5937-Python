# Convert Excel to CSV
pip3 install openpyxl
pip3 install pandas
import openpyxl
import pandas as pd
read_file = pd.read_excel (r'/Users/giselagonzale/desktop/COVID19_032420_ByCounty.xlsl', sheet_name='COVID19_032420_ByCounty')
read_file.to_csv(r'/Users/giselagonzale/desktop/COVID19_032420_ByCounty.csv', index = None, header = TRUE)
print(read_file.to_csv)

# Webscrapping
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# URL I want to webscrape from
url = 'https://jump.fandom.com/wiki/Jump_Database'

# Connect to URL
response = requests.get(url)

# Parse HTML and save BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

line_count = 1 #variable to track what line I am on
for one_a_tag in soup.findAll('img'):
    if line_count >= 1:  # code for text files starts at line
    link = one_a_tag['img']
    download_url = 'https://jump.fandom.com/wiki/One_Piece' + link
    urllib.request.urlretrieve(download_url, './' + link[link.find('/Jump_Database') + 1:])
    time.sleep(1)  # pause the code for a sec
# add 1 for next line
line_count += 1
# Imported Libraries 
import requests 
from bs4 import BeautifulSoup 
import random 
import pandas as pd
from io import StringIO
import re
import seaborn as sns 
import matplotlib.pyplot as plt


user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        # Add more user agents as needed
    ]

header = random.choice(user_agents)

url = 'https://en.wikipedia.org/wiki/Human_body_weight'

response = requests.get(url, headers = {'User-Agent':'header'})
# print(response)
# print(response.text)

# Use BeautifulSoup to convert plain text to html
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

# To extract data from the html format data 
data = soup.find_all('table', {'class':'wikitable'})
data[0]
# print(data[0])

# To read_html (convert to DF), soup obj must be converted to a str
a = pd.read_html(StringIO(str(data[0])))
# print(a[0])

df = a[0]


# Data cleaning
# Check data for info/ variables
# df.info()
# print(df.info())


# Remove Ref col as it is not needed
df.drop(columns='Ref', inplace=True)
# print(df)


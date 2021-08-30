#https://oxylabs.io/blog/python-web-scraping
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

#driver.get('https://your.url/here?yes=brilliant')
driver.get('https://oxylabs.io')

results = []
other_results = []

# Add the page source to the variable `content`.
content = driver.page_source
# Load the contents of the page, its source, into BeautifulSoup
# class, which analyzes the HTML as a nested data structure and allows to select
# its elements by using various selectors.
soup = BeautifulSoup(content)

for element in soup.findAll(attrs={'class': 'title'}):
    name = element.find('a')
    #results.append(name.text)
    if name not in results:
        results.append(name.text)

#for x in results:
#    print(x)

for b in soup.findAll(attrs={'class': 'otherclass'}):
    name2 = b.find('span')
    other_results.append(name.text)
series1 = pd.Series(results, name='Names')
series2 = pd.Series(other_results, name='Categories')
df = pd.DataFrame({'Names': series1, 'Categories': series2})
df.to_csv('names.csv', index=False, encoding='utf-8')

# ===== INSTALL REQUIREMENTS =====
# pip install requests
# pip install html5lib
# pip install bs4

from bs4.element import NavigableString
import requests
from bs4 import BeautifulSoup
url = "https://cses.fi/problemset/"

# ======== Request the html content ==========

r = requests.get(url)
htmlContent = r.content

# ========= Parsing the HTML ===========

soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)


# ========= Commonly used types of objects ==========
# 1. Tag
# 2. NavigableString
# 3. BeautifulSoup
# 4. Comment
title = soup.title
print(title)
# Tag
print(type(title)) 
# NavigableString
print(type(title.string)) 
# BeautifulSoup
print(type(soup)) 
# Comment
markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string)) 


# ========= HTML Tree Traversal ==========

# Selecting all para tags
paras = soup.find_all('p')
# Selecting first li tag
lists = soup.find('li') 
print(paras)
# gives class of first div
div = soup.find('div')['class']  
print(lists)
print(div)
# gives inner HTML
print(soup.find('li').get_text())
print(soup.get_text())

# Parsing all links on the website
links = soup.find_all('a')

for l in links:
    print(l.get_text())

print("=========================")
# Get the classes of the first div
firstDiv = soup.find('div')['class']
print(firstDiv)
# Find elements with a particular class name
print(soup.find_all("div", class_="header"))

# ========= Children and content ==========
# .contents - A tag's children are available as a list
# .children - A tag's children are available as a generator

divs = soup.find('li')

for item in divs.strings:
    print(item)

for item in divs.stripped_strings:
    print(item)

for elem in divs.contents:
    print(elem)

# Immediate parent
print(divs.parent)

# All parents in a heirarchial manner
for p in divs.parents:
    print(p.name)

# All children in a heirarchial manner
for c in divs.children:
    print(c.name)

# Printing contents of the element
for elem in divs.contents:
    print(elem.name)

# ========== CSS Selectors ===========

# Selecting a class
item = soup.select('.logo')
print(item)
# Selecting an id
item2 = soup.select('#darkmode-enabled')
print(item2)
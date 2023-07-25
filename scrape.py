import requests
from bs4 import BeautifulSoup

link = "https://www.creatibly.com/blogs/learn/70-web-design-and-development-terms-to-learn-today"

title = []
defination = []

response = requests.get(link).text
soup = BeautifulSoup(response, 'html.parser')

for text in soup.find_all(name="h4", attrs={'class': 'p1'}):
    title.append(text.get_text())

for text in soup.find_all(name='p', attrs={'class': 'p1'}):
    defination.append(text.get_text())

newDefList = defination[9:77]
newTitleList = title[0:68]

from bs4 import BeautifulSoup

html = open('sample.html', 'r').read()
soup = BeautifulSoup(html, features="lxml")

for element in soup.find_all('a', href=True):
    print (element['href'])

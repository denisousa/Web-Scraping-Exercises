import requests
from bs4 import BeautifulSoup

wiki = "https://pt.wikipedia.org/wiki/Lista_de_capitais_do_Brasil"
page = requests.get(wiki)
soup = BeautifulSoup(page.text, features="html.parser")
list_item = soup.find("li", attrs={"class": "toclevel-2 tocsection-26"})
name = list_item.text.strip()

"""print(name)
print(soup.prettify())
print(soup.title)
print(soup.title.string)
print(soup.find_all('a'))"""

all_links = soup.find_all("a")
for link in all_links:
    print(link.get("href"))

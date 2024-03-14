import requests
from bs4 import BeautifulSoup

# Making a GET request
r = requests.get("https://www.accountingmatch.com/major-markets/0CMGK9ZC")
soup = BeautifulSoup(r.content, "html.parser")
s = soup.find("div", class_="listing")

name = s.find_all("a")
for link in soup.find_all("a"):
    print(link.get("href"))
name_number = soup.get_text()
print(name_number)

"""for content in name:
    
    print(content.text)"""

from bs4 import BeautifulSoup
import requests

headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Max-Age": "3600",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
}

url = "https://arstechnica.com/gadgets/"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, "html.parser")
excerpts = soup.find_all("p", class_="excerpt")
for excerpt in excerpts:
    print(excerpt.text)

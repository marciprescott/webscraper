import httpx
from selectolax.parser import HTMLParser

url = "https://www.rei.com/c/snow-clothing/f/scd-deals"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}
response = httpx.get(url, headers=headers)
print(response.text)
html = HTMLParser(response.text)
# print(html.css_first("title").text)
products = html.css("VcGDfKKy_dvNbxUqm29K")
print(products)
for product in products:
    print(products)

import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get("https://pythonjobs.github.io//")
soup = BeautifulSoup(r.content, "html.parser")
s = soup.find("section", class_="job_list")
contents = s.find_all("p")
for content in contents:

    print(content.text)

soup_2 = BeautifulSoup(r.content, "html.parser")

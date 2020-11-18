import requests
from bs4 import BeautifulSoup
import json

url = "https://en.wikipedia.org/wiki/List_of_Harry_Potter_characters"
names = []
page = requests.get(url)
soup = BeautifulSoup(page.content, "lxml")
uls = soup.find_all("li")
for ul in uls:
    line = str(ul.text)
    if "–" in line or "–" in line:
        name = line.split("–")[0].strip()
        if "The Deathly Hallows" in name:
            break
        else:
            if "/" in name:
                two_names = name.split("/")
                for item in two_names:
                    item = item.strip()
                    names.append(item)
            else:
                names.append(name)
print (names)
with open ("data/hp_characters.json", "w", encoding="utf-8") as f:
    json.dump(names, f, indent=4)

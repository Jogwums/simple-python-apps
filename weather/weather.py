import requests
from bs4 import BeautifulSoup


search = "weather in jalna"
url = f"https://www.google.com/search?&q={search}"

r = requests.get(url)

if r.status_code == 429:
    raise 'Too Many requests'
else:
    print(r)

    s = BeautifulSoup(r.text, "html.parser")

# update = s.find("div", class_="BNEawe").text
# update = s.find("span", id_="wob_tm").text

# print(update)

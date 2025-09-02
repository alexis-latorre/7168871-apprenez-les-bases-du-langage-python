import requests
from bs4 import BeautifulSoup

with open("index.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file.read(), "html.parser")

produits = []

for li in soup.find_all("li"):
    li = BeautifulSoup(str(li), "html.parser")
    euros = int(li.select('p.price')[0].string.split(" ")[1].split("€")[0])
    p_list = li.find_all("p")
    for p in p_list:
        if str(p).find("Description") != -1:
            description = str(p).split("Description : ")[1]
    dollars = round(euros * 1.2, 2)
    produits.append({li.h2.string: {"euros": euros, "dollars": dollars, "description": description}})

print(produits)
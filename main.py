from requests import get
from bs4 import BeautifulSoup
from statistics import mean


url = 'https://www.portalinmobiliario.com/venta/departamento/vitacura-metropolitana'
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser', from_encoding="utf-8")
props_containers = html_soup.find_all('div', class_ = 'rowItem item highlighted item--stack item--has-row-logo new ')
count = 1
results = []

for apt in props_containers:
    try:
        
        price = float(apt.find("span", class_="price__fraction").text)
        items = str(apt.find("div", class_="item__attrs").text.encode("utf-8"))[3:].replace(" m\\xc2\\xb2 \\xc3\\xbatiles", "").replace("dormitorios \\xc2\\xa0", "").split(" | ")
        print(items)
    except AttributeError:
        pass
"""
count += 50
while len(props_containers) == 50:
    url = 'https://www.portalinmobiliario.com/venta/departamento/vitacura-metropolitana/_Desde_'+str(count)
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    props_containers = html_soup.find_all('div', class_ = 'rowItem item highlighted item--stack item--has-row-logo new ')
    for apt in props_containers:
        try:
            numb = float(apt.find("span", class_="price__fraction").text)
            results.append(numb*1000)
        except AttributeError:
            pass
        except ValueError:
            pass

    count += 50

print(mean(results))
"""
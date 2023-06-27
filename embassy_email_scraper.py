from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://embassies.net/united-kingdom').text
soup = BeautifulSoup(html_text, 'lxml')
groups = soup.find_all('div', class_="s4_c")
for group in groups:
    temp = []
    name = group.find('h5', class_="s4_ct").text
    represent = group.find('ul', class_="s4_cn")
    office = represent.find_all('li')
    for x in office:
        if x.text[:7] == "Embassy":
            print(x.text)
        else:
            temp.append(x.text)
    if len(temp) > 0:
        print(temp[0])

#so far able to country name, all their representatives and their offices 
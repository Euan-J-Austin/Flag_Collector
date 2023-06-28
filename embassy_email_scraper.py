from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://embassies.net/united-kingdom').text
soup = BeautifulSoup(html_text, 'lxml')
# groups = soup.find_all('div', class_="s4_c")
group = soup.find('div', class_="s4_c")
name = group.find('h5', class_="s4_ct")
represent = group.find('ul', class_="s4_cn")
office = represent.find('li')
link = office.find('a')['href']

mail_html_text = requests.get("https://embassies.net/" + link).text
mail_soup = BeautifulSoup(mail_html_text, 'lxml')
table = mail_soup.find('table', class_='tb5')
rows = table.find_all('tr')

for row in rows:
    subrow = row.find_all('td')
    string = str(subrow[1].text)
    if "@" in string:
        print(string)

# string = "info@algerianembassy.org.uk"

# if "@" in string:
#     print(string)





# for group in groups:
#     temp = []
#     name = group.find('h5', class_="s4_ct").text
#     represent = group.find('ul', class_="s4_cn")
#     office = represent.find_all('li')
#     link = office.find_all(href=True)
#     for x in office:
#         if x.text[:7] == "Embassy":
#             print(x.text)
#         else:
#             temp.append(x.text)
#     if len(temp) > 0:
#         print(temp[0])

#so far able to country name, all their representatives and their offices 
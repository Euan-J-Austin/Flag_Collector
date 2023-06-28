from bs4 import BeautifulSoup
import requests

rolodex = []
html_text = requests.get('https://embassies.net/united-kingdom').text
soup = BeautifulSoup(html_text, 'lxml')
groups = soup.find_all('div', class_="s4_c")

def get_email(rows):
    for row in rows:
        subrow = row.find_all('td')
        string = str(subrow[1].text)
        if "@" in string:
            return string

def rolodex_adder(name, represent):
    offices = represent.find_all('li')
    for office in offices:
        office_name = office.find('a')
        link = office.find('a')['href']
        mail_html_text = requests.get("https://embassies.net/" + link).text
        mail_soup = BeautifulSoup(mail_html_text, 'lxml')
        table = mail_soup.find('table', class_='tb5')
        rows = table.find_all('tr')
        rolodex.append([name.text, office_name.text, get_email(rows)])

for group in groups:
    name = group.find('h5', class_="s4_ct")
    represent = group.find('ul', class_="s4_cn")
    rolodex_adder(name, represent)

print(rolodex)
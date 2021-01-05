from bs4 import BeautifulSoup
import requests

url = 'https://www.livefpl.net/prices'          # Price Changes
header = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'})
html_text = requests.get(url, headers=header).text
soup = BeautifulSoup(html_text, 'lxml')

tables = soup.find_all('table')

table_head_contents = soup.find('table').thead.tr.th.text.split()
date_for_the_day = table_head_contents[2]
print(f'\nDate: {date_for_the_day}')

table_body = soup.find('table').tbody
players = table_body.find_all('tr')

for i in range(len(players)):
    data = players[i].find_all('td')
    name = data[0].text
    team = data[1].text
    price = data[3].text
    if data[3].text > data[2].text:
        change = "Increase"
    else:
        change = "Decrease"
    print(f'\nPlayer: {name}')
    print(f'Team: {team}')
    print(f'Price: {price}')
    print(f'Status: {change}')

import requests
from bs4 import BeautifulSoup

# get list of links/days
baseurl = 'https://webshop.meyerskantiner.dk'
r = requests.get(baseurl + '/shop/2240/take-away/g/23332') 
soup = BeautifulSoup(r.content, 'html.parser') 
soup_navbar_dates = soup.find(id='navbar-dates')

links_list = []
dates_list = []
for a in soup_navbar_dates.find_all('a', href=True): 
    if a.text: 
        dates_list.append(a.text)
        links_list.append(a['href'])

# for each day get the menu (if there is any)
for date, link in zip(dates_list, links_list):
    url = baseurl + link
    r = requests.get(url) 
    soup = BeautifulSoup(r.content, 'html.parser') 
    table = soup.findAll('div', attrs = {'class':'name'})
    if table: 
        print('\n')
        print(date)
        for row in table:
            print(row.text.strip())
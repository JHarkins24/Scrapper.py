import requests
website_url =  requests.get('http://www.ohranger.com/channel-islands/animals').text

from bs4 import BeautifulSoup
soup = BeautifulSoup(website_url,'lxml')
# print(soup.prettify())
My_table = soup.find('div', { 'class': 'content'})
# print(My_table)
animals = My_table.findAll('p')
print(animals)
# Common_Names = []
# for animal in animals:
#     Common_Names.append(animal.get(''))
#
# print(Common_Names)
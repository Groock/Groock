#python 3.7.9
#This program uses the library Beautiful soup and prints the headings from a random Wikipedia article in the python shell. 


import requests
from bs4 import BeautifulSoup
import time

time.sleep(1.25)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0",
}

url = 'https://en.wikipedia.org/wiki/Special:Random'

result = requests.get(url)

doc = BeautifulSoup(requests.get(url, headers=headers).text, 'html.parser')

#prices = doc.find_all(text="£")

#parent = prices[0].parent

heading_object=doc.find_all( 'h1' )
subheading_object=doc.find_all( 'h2' )

for info in heading_object:
    print(info.getText())
    print("------")

for info in subheading_object:
    print(info.getText())
    print("------")

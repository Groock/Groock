#python 3.7.9
#This program scrapes images from ebays homepage, first checks for images, then you can press enter to download them to the containing folder.

import requests
from bs4 import BeautifulSoup
import time

time.sleep(1.25)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0",
}

url = 'https://www.ebay.co.uk/'

page = requests.get(url)

content = page.text

#print(page.content)

#doc = BeautifulSoup(requests.get(url, headers=headers).text, 'html.parser')

#prices = doc.find_all(text="£")

#parent = prices[0].parent

#print(doc.prettify())

#find the image source link

soup = BeautifulSoup(content, 'html.parser')

filecount = 1

#video is .mp4 and same method... tutorial https://www.youtube.com/watch?v=u7ssFX3fJvk

image_list = []

#scrape image url's and put them into python list

for img in soup.find_all('img', src=True):
    
    print ("Found the URL:", img['src'])

    if '.gif' in img['src']:
        print ('error gif')

    else:
        image_list.append(img['src'])

print('amount of images is:',len(image_list))

input('Continue? Press Enter.')

#cycle through list of url's and download images to file

for item in image_list:
    
    img_url = item

    image = requests.get(img_url)

    if '.jpg' in img_url:
        extension = '.jpg'

    elif '.png' in img_url:
        extension = '.png'

    elif '.gif' in img_url:
        extension = '.gif'

    filecount = filecount+1

    print (filecount)
    
    with open('image'+str(filecount)+extension, 'wb') as file:
        for chunk in image.iter_content(chunk_size=1024):
            file.write(chunk)


#as yet unused function.

def SingleImage():
    img_tag = soup.find('img')

    print(img_tag)

    print (img_tag['src'])

    img_url = img_tag['src']

    #download image from URL

    image = requests.get(img_url)

    #store the image in file

    with open('image.png', 'wb') as file:
        for chunk in image.iter_content(chunk_size=1024):
            file.write(chunk)

import datetime
from bs4 import BeautifulSoup

#python 3.7.9

#This program needs to have your .html bookmarks file from chrome in the same folder.
#This program gets the date time of when you bookmarked a bookmark to chrome, because chrome doesn't let you do this currently.
#This program combines some code found on stackoverflow with Beautiful Soup 4 https://stackoverflow.com/questions/19074423/how-to-parse-the-date-added-field-in-chrome-bookmarks-file/20306973#20306973

#You will need to change the title to match below
with open('bookmarks_1_31_25.html', 'r', encoding="utf8") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, "html.parser")

    #[tag['ADD_DATE'] for tag in soup.css.iselect("a")]
    
    #for tags in soup.find_all(tags):
    
    for tags in soup.find_all('a', class_="ADD_DATE"):
        print(tags)
        #.text.strip()


def getFiletime(dtms):
    dtms = dtms*1000000
    #read total amount of seconds from chrome bookmark timestamp
    seconds, micros = divmod(dtms, 1000000)
    days, seconds = divmod(seconds, 86400)

    return datetime.datetime(1970, 1, 1) + datetime.timedelta(days, seconds, micros)

print("Source", getFiletime(1619803324).strftime( '%a, %d %B %Y %H:%M:%S %Z' ) )

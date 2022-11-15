import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

#enables code to choose a random chapter from John to load
urlNum = str(random.randint(1,21))

webpage = 'https://biblehub.com/asv/john/' + '1' + '.htm'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(webpage, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

chapter = soup.findAll("div", class_='padleft')

#for verse in chapter:
#    print(verse.text)

for verse in chapter:
   verse_list = verse.text.split('.')



myVerse = random.choice()
message = 'Chapter: ' + urlNum + '  Verse: ' + myVerse
print(message)



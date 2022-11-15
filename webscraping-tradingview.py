from urllib.request import urlopen, Request
from bs4 import BeautifulSoup




##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"


#url = 'https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/'
url = 'https://www.webull.com/quote/us/gainers'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}


req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

print(title.text)






#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

tablecells = soup.findAll("div", attrs={'class':'table-cell'})

print('Spot:', tablecells[0].text)
print('Company Name:', tablecells[1].text)
print('Percent Change:', tablecells[3].text)
print('High:', tablecells[5].text)
print('Low:', tablecells[6].text)
#value = int(tablecells[5].text) - int(tablecells[6].text)
#print('% Change:', (value / int(tablecells[6].text)*100) )
print()

#tables = soup.findAll('div', attrs={'class':'table-row table-row-hover'})

index = 0
for x in range(5):
    print('Spot:', tablecells[index+0].text)
    print('Company Name:', tablecells[index+1].text)
    print('Percent Change:', tablecells[index+3].text)
    print('High:', tablecells[index+5].text)
    print('Low:', tablecells[index+6].text)
    print()
    index+=11



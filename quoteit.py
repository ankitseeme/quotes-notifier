from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import sys
from urllib.error import HTTPError
from win10toast import ToastNotifier
limit=20
minMinute = 1
duration= minMinute * 60
def getquote():  
    try:
        url="http://quotes.toscrape.com/random"
        html=urlopen(url)
    except HTTPError as e:
        print(e)
    try:
        bsObj=BeautifulSoup(html.read(),'html.parser')
        quote = bsObj.find('span',{'class':'text'}).text
        author = bsObj.find('small',{'class':'author'}).text
    except AttributeError as e:
        print(e)
    return quote,author
    
def callit(cnt):
    try:
        quote,author = getquote()
        while len(quote) not in range(140):
            quote,author = getquote()
            #print("too long")
        if cnt != 1:
            time.sleep(duration)
        print(str(count) + "." + quote + " by " + author + " at " + time.strftime('%H:%M:%S'))
    except:
        print("Exiting")
        exit()
    try:
        toaster = ToastNotifier()
        toaster.show_toast(author, quote[1:-1], duration=20)
    except:
        print("ToastError")
    return quote,author

if __name__ == '__main__':
    """ Get Motivated with quotes.
    Usage: quoteit.py [duration]
    duration is in minutes. Minimum is 1 """
    if (len(sys.argv)) == 2:
        minMinute = sys.argv[1]
        duration= int(minMinute) * 60
    if (len(sys.argv)) == 3:
        limit = int(sys.argv[2])
    count=1
    while count <= limit:
        quote,author = callit(count)
        count+=1
    print("bye")
    
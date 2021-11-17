import requests
from bs4 import BeautifulSoup
import tweepy
import time
import datetime


#doesn't work anymore try using an API

#web scraper
url = 'https://coinmarketcap.com/'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')


price = soup.find('a', attrs={'href': '/currencies/bitcoin/markets/'})
convertedPrice = price.text.strip()

print(convertedPrice)





#details removed, obviously fill with your own twitter bot account details
consumer_key =''
consumer_secret = ''
access_key = ''
access_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

now = datetime.datetime.now()
print (now.strftime('%H:%M %d/%m/%Y'))

api.update_status('the current bitcoin value in USD is ' + convertedPrice)
print('tweet sent')
print("the current bitcoin value in USD is" + convertedPrice)
time.sleep(300)


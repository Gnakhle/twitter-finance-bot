# theStockBot

import tweepy as tp
import time
import quandl
import numpy as np
from datetime import date
from config import *


# Log-in twitter account
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

#Pull stock price from Quandl
quandl.ApiConfig.api_key = quandl_api_key

while True: 
    today = str(date.today()) # get date in format 'YYYY-MM-DD'
    stock = quandl.get("ASX/APQ2018", start_date="2018-05-10", end_date=today) # Pull data from Quandl API
    priceArray = str(np.array(stock.tail(1)['Previous Settlement'])) # Get latest price
    price = priceArray.replace("[", "").replace(".]","") #Removes brackets from np array print


    #Post price to twitter
    priceString = "Todays ASX SPI 200 Index Futures (August 2018) price is" + price + " as of " + today
    api.update_status(priceString) #tweet price to twitter

    time.sleep(86400)


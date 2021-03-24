import tweepy
import os 
import yfinance as yf 

from secrets import user_key, user_secret_key, user_token, user_secret_token


auth = tweepy.OAuthHandler(user_key, user_secret_key)
auth.set_access_token(user_token, user_secret_token)

api = tweepy.API(auth)
# api.update_status("HELLLLOOOO IS THIS WORKING?")

data = yf.download("AMC", period= "1d", interval= "1d")
print(data)

row = data.iloc[0]

status = "The price of AMC's stock is %s. The close price of AMC's stock is %s. Volume is currently %s" %(
    str(round(row["Open"],2)), str(round(row["Close"],2)), str(int(row["Volume"]))
)
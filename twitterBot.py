import tweepy

from secrets import user_key, user_secret_key, user_token, user_secret_token


auth = tweepy.OAuthHandler(user_key, user_secret_key)
auth.set_access_token(user_token, user_secret_token)

api = tweepy.API(auth)

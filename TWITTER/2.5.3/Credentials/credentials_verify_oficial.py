"""
Philosopher Bot
---------------
Created by Caio Madeira
Co-worker: Rodrigo Carmo

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!

"""
from Credentials.acess_tokens_oficial import *
import tweepy.api


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACESS_TOKEN, ACESS_TOKEN_SECRET)


try:
    api_oficial = tweepy.API(auth, wait_on_rate_limit = False, wait_on_rate_limit_notify = True)

except tweepy.TweepError:
    print('Error! Falha ao pegar o Token de acesso!')

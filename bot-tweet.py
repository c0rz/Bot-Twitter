import tweepy
import time

consumer_key = 'XXX' # masukan key aplikasi kalian 
consumer_secret = 'XXXX' # masukan secret aplikasi kalian
access_token = 'XXXXX' # akses token dari aplikasi untuk akun kita
access_token_secret = 'XXXXXX' # akses token secret yang diberikan untuk kita

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

data_tweet = open("tweet.txt", "r", encoding="mbcs").readlines()
for status in data_tweet:
    tweet = status.split('\n')[0]
    update = api.update_status(tweet)
    print("Update Tweet :",tweet)
    print("Jeda mencenggah limit twitter.\n")
    time.sleep(60) # delay 60 detik = 1 Menit
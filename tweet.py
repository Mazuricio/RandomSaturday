import tweepy
import senhas
# Keys
consumer_key =  senhas.consumer_key 
consumer_secret = senhas.consumer_secret
access_token = senhas.access_token
access_token_secret = senhas.access_token_secret
# autenticar

#mensagem e imagem
tweet =" " # toDo 
image_path ="new_post.jpg" # toDo 
  
# to attach the media file 
def postar_twiiter():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    auth.set_access_token(access_token, access_token_secret) 
    api = tweepy.API(auth) 
    #status = api.update_with_media(image_path, tweet)
    api.update_status_with_media(tweet, image_path)  

#api.update_status(status = tweet) 
#postar_twiiter()

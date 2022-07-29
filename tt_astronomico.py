import tweepy 
import time 
import os

KEY_1 = os.environ{'KEY_1'}
KEY_2 = os.environ{'KEY_2'}
KEY_3 = os.environ{'KEY_3'}
KEY_4 = os.environ{'KEY_4'}

#tweepy
auth = tweepy.OAuthHandler('{}'.format(KEY_1),'{}'.format(KEY_2))
auth.set_access_token('{}'.format(KEY_3),'{}'.format(KEY_4))
api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()

print("\n")
print ('pai on')
semnada = 'não tem nd hoje'



#POSTAGEM
def sites():
        while True:
            with open( 'datasCalendar.txt', 'r',encoding = 'utf8') as x:
                data = time.localtime()
                for y in x:
                    if data[3] == 13:
                        oi = y.split('.')
                        poeo = oi[2]
                        if int (oi[0]) == int(data[1]) and int (oi [1]) == int(data[2]):
                            print (poeo)
                            api.update_status((poeo))
                            print ('tudo ok parceiro')

            time.sleep(3600)
            print ("again")      
            



def local ():  
    with open( 'datasCalendar.txt', 'r', encoding = 'utf8') as x:
        for y in x: 
            data = time.localtime()
            oi = y.split('.')
            if int (oi[0]) == int(data[1]) and int (oi [1]) == int(data[2]):  
                print('entrou') 
                poeo = oi[2]
                print (poeo)
                api.update_status((poeo))
                print ('tudo ok parceiro') 

local()


'''
GetRedditAccessToken
by Naim Kabir

FUNCTION:
Will get you an access token to allow a bot to interface with Reddit.
Reddit recently has done away with password authentification and now
exclusively uses OAuth, so this should be handy.


DEPENDENCIES:
To run something like this, you will need to download PRAW here:
https://praw.readthedocs.org/en/stable/index.html

They have excellent documentation, and the below workflow is pretty easily
extracted from their manual! Good people.
'''

#Import important libraries
import praw
import webbrowser

#Setting a unique user_agent to identify my script to Reddit. Change this!
user_agent = 'Application Tester 1.0 by Naim Kabir'
r = praw.Reddit(user_agent=user_agent)

#Setting up OAuth
#Uses client_id from the reddit app I created. 
#Create another for another ID. Do this by joining Reddit and going to: 
#https://ssl.reddit.com/prefs/apps/
#They will provide you with an ID and 'secret'
r.set_oauth_app_info(client_id= #Insert your ID from Reddit here,
                     client_secret= #Insert your 'secret' from reddit here,
                     redirect_uri='http://127.0.0.1:65010/authorize_callback')

url = r.get_authorize_url('uniqueKey', 'read', True) #middle argument is scope
webbrowser.open(url)

#Click allow on the open webbrowser to get access key, in the URL of the next page
#This is the access key that you'll use to have your bot log into reddit.

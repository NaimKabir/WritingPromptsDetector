'''
Writing Prompts Hot Prompts Early Detector
by Naim Kabir

Learned much of the text sending from OccultBioinformatics:
https://github.com/OccultBioinformatics/Assembler/blob/master/sendMessage.py

FUNCTION:
This script will detect hot prompts posted to /r/WritingPrompts before they 
are seen under the Hot Tab. It will text the prompt titles directly to your
phone so you can jump online and get writing on what'll probably be a 
popular post.

DEPENDENCIES:
You must download PRAW here: https://praw.readthedocs.org/en/stable/index.html
You must have a valid Gmail account.
You need a cellphone number.
You must first run the 'GetRedditAccessToken' script to receive an access code!
'''
#Import libraries
import time
import praw
import pprint
import smtplib

# This access code will need to change every time you run the script. Get it
#by first running 'GetRedditAccessToken.py'
access_code = 'Insert Code Here'

# Credentials for e-mail address/number
# Check what your phone's email address is here: 
# http://www.sensiblesoftware.com/weblog/2011/02/28/cell-phone-email-addresses/
username = 'Your Gmail username'
password = 'Your Gmail password'
fromaddr = 'Your Gmail email address'
toaddrs  = 'The e-mail address of your phone number'

def TextSend(msg) :
    '''
    function takes in an error name (as a string), and sends
    a text message alerting the user of the error
    '''
    msg = str(msg)

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()


#Setting a unique user_agent to identify my script to Reddit. Change this!
user_agent = 'Prompt Analyzer 1.4 by Naim Kabir'
r = praw.Reddit(user_agent=user_agent)

#Setting up OAuth
#Uses client_id from the reddit app I created. 
#Create another app for another ID. Do this by joining Reddit and going to: 
#https://ssl.reddit.com/prefs/apps/
#They will provide you with an ID and 'secret'
r.set_oauth_app_info(client_id= 'Insert your ID from Reddit here',
                     client_secret= 'Insert your secret from Reddit here',
                     redirect_uri='http://127.0.0.1:65010/authorize_callback')

#Setting access information from Key I got from Setting Up OAuth
#This key is for /u/Shehwa. You have to get key on every bot start.
access_information = r.get_access_information(access_code)
r.set_access_credentials(**access_information)

#START OF WRITING PROMPTS DETECTION

#Setting list of already caught prompt IDs so you don't get repeat texts
already_done = []

#start main loop
counter = 1

while True:
    subreddit = r.get_subreddit('WritingPrompts')
    for submission in subreddit.get_new(limit = 30): #only look at 'New' tab's top 30

        score  = submission.score
        score_threshold = 6

        
        post_time = submission.created_utc
        post_time = time.time() - post_time
        time_threshold = 1500 #Around twenty-five minutes

        #Setting a 'velocity' variable for each prompt
        if post_time < 300:
            velocity = float(score/300.00)
        else:
            velocity = float(score/post_time)

        print(score)
        print(post_time)
        print(velocity)
        print(' ')
        
        #Setting a velocity threshold below which we won't text your phone
        velocity_threshold = 10.00/(1800)
        
        is_hot = velocity > velocity_threshold
        
        if is_hot and submission.id not in already_done:
            #sending text
            msg = 'Hot thread in New: ' + str(submission.title)
            print(msg)

            TextSend(str(submission.title))
            already_done.append(submission.id)

    #This will just tell you how many sweeps have occurred. The loop is set
    #to sleep for twenty minutes before waking and sweeping again.
    print('Sweep ' + str(counter))
    counter = counter + 1
    time.sleep(1200)
    
    #This will refresh the OAuth token and make sure the bot can run indefinitely
    r.refresh_access_information(access_information['refresh_token'])

from time import sleep
from turtle import pos
from bot2 import Insta_Bot
from selenium import webdriver
import sqlite3
import datetime as dt

statrt = dt.datetime.now()
browser = webdriver.Firefox(executable_path="geckodriver")
browser.get('https://www.instagram.com/')
browser.add_cookie({"name" : "sessionid" ,"domain" : ".instagram.com", "value" : "17129991155%3ALfzxCcWImYn9rz%3A16","httponly" : True ,"secure" : True})

bot_insta = Insta_Bot(browser)

# 17129991155
pkfollowings = bot_insta.get_followings_pks(17129991155)


def get_like_word():
    conn = sqlite3.connect('AlphA.db')
    c = conn.cursor()
    c.execute("SELECT username,pk FROM User Where (bio like '%photo%' or  bio like '%عکاس%' or username like '%photo%' or work like '%photo%') and following > 500 and followers < 1500")
    b = set(c.fetchall())
    x = []
    for i in b:
        x.append([i[0],i[1]])    
    # c.execute("SELECT username FROM User Where bio like '%%'")
    print(len(x))
    return x

# print(get_like_word())


users2 = []
users = get_like_word()

for i in users:
    if i[1]  in pkfollowings:
        print('l')
        continue
    users2.append(i[0])


lenusers = len(users2)
j = 0 
for i in users2:
    sleep(5)
    try:
        username = i[0]
        bot_insta.follow_user(username)
        # sleep(18)
        posts = bot_insta.get_all_post(username)
        postlen = len(posts)
        sleep(10)
        jj = 0
        for i in posts:
            try:
                bot_insta.like_post(i)
            except:
                pass
            print(f"like posts of {username} : {jj}/{postlen}")
            jj += 1
            sleep(10)
    
    except:
        pass
    
    print(f"users : {j}/{lenusers}")
    j += 1
    fin0 = dt.datetime.now()
    print(f"time : {fin0 - statrt}")

    sleep(180)


finish = dt.datetime.now()
print(f"full time = {finish - statrt}")




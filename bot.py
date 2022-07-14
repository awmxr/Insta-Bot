from logging import exception
import random
from turtle import pos
from matplotlib.style import use
from numpy import number
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from sympy import E, true
import setting
from time import sleep
from Database.databaseinsta import insert_like, select_current_userid_by_usrname, insert_user , insert_follows , insert_Comments , insert_user_for_first_one_with_out_info
from Database.Models import Follows, Likes , User , Comments
import datetime as dt
from functions import text_to_dec
import os

from getfolloings import get_followings




browser = webdriver.Firefox(executable_path="geckodriver")

# browser.add_cookie({"name" : "csrftoken" , "value" : "5fC95wFeq3XfScyImI0dUSi162fWg48i" , "domain" : "https://www.instagram.com/" })
# browser.add_cookie({"name" : "ds_user_id" , "value" : "52659641865" , "domain" : "https://www.instagram.com/" })
# browser.add_cookie({"name" : "ig_did" , "value" : "4985B645-EE37-41E0-AEF6-BF896E84D764" , "domain" : "https://www.instagram.com/" })
# browser.add_cookie({"name" : "mid" , "value" : "YkQzmwALAAHnG2-x3g_-W7ZqjOeY" , "domain" : "https://www.instagram.com/" })
# browser.add_cookie({"name" : "rur" , "value" : '"ASH\05452659641865\0541680262914:01f794826135ce711a773271a9556cc795a33b1774fef168d3732790884b043f6f47f9b2"' , "domain" : "https://www.instagram.com/" })
# browser.add_cookie({"name" : "sessionid" , "value" : "52659641865%3ARP3ounZ2nhPiZj%3A18" , "domain" : "https://www.instagram.com/" })
browser.get('https://www.instagram.com/')



# browser.add_cookie({"name" : "csrftoken" , "value" : "5fC95wFeq3XfScyImI0dUSi162fWg48i" , "httponly" : False ,"secure" : True })
# browser.add_cookie({"name" : "ds_user_id" , "value" : "52659641865","httponly" : False ,"secure" : True })
# browser.add_cookie({"name" : "ig_did" , "value" : "4985B645-EE37-41E0-AEF6-BF896E84D764","httponly" : True ,"secure" : True })

# browser.add_cookie({"name" : "ig_nrcb" , "value" : '1' ,"httponly": False,"secure" : True})
# browser.add_cookie({"name" : "mid" , "value" : "YkQzmwALAAHnG2-x3g_-W7ZqjOeY","httponly" : False ,"secure" : True})

# browser.add_cookie({"name" : "rur" , "value" : '"RVA\05452659641865\0541680272856:01f7512d9fb8eee996399b6e9d7a5f16874f336570d9650b8ac1f539b586fa8af6f5b583"',"httponly" : False,"secure" : True})
browser.add_cookie({"name" : "sessionid" ,"domain" : ".instagram.com", "value" : "52659641865%3ARP3ounZ2nhPiZj%3A18","httponly" : True ,"secure" : True})
# sleep(3)






browser.implicitly_wait(5)


class Insta_Bot :
    def __init__(self, username , password , browser):

        self.username = username
        self.password = password
        self.browser = browser
    

    def test_login_page(self):
        self.browser.get('https://www.instagram.com/')
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()

        # errors = browser.find_elements_by_css_selector('#error_message')
        # assert len(errors) == 0
    
    def access_to_my_profile(self):
        # sleep(5)

        self.browser.get(f'https://www.instagram.com/{setting.username}/')

        



        
        # self.browser.find_element_by_xpath("//a[contains(@href, '/{}')]".format(self.username)).click()

    def follow_user(self,followuser):
        

        self.browser.get(f'https://www.instagram.com/{followuser}/')
        follow_button = browser.find_element_by_xpath("//button[normalize-space()='Follow']")
        follow_button.click()

    def unfollow_user(self , unfollowuser):
        # unfollow_buttons = driver.find_elements_by_css_selector('.sqdOP.L3NKy._8A5w5')
        self.browser.get(f'https://www.instagram.com/{unfollowuser}/')
        buttons = browser.find_elements_by_css_selector('._5f5mN.-fzfL._6VtSN.yZn4P')
        print(buttons)
        print("len :       ",len(buttons))
        unfollow_button = buttons[0]
        unfollow_button.click()
        sleep(2)
        unfollow_button2 = browser.find_element_by_xpath("//button[normalize-space()='Unfollow']")
        unfollow_button2.click()

    def get_followers(self , username):
        # unfollow_buttons = driver.find_elements_by_css_selector('.sqdOP.L3NKy._8A5w5')
        self.browser.get(f'https://www.instagram.com/{username}/')
        sleep(4)
        buttons = browser.find_elements_by_css_selector('._7UhW9.vy6Bb.MMzan.KV-D4.uL8Hv.T0kll')
        # print(buttons)
        print("len :       ",len(buttons))
        unfollow_button = buttons[1]
        numbers = browser.find_elements_by_css_selector('.g47SY')
        
        unfollow_button.click()
        sleep(4)
        xt = True
        while xt == True:
            try :
                pop_up_window = WebDriverWait(
                self.browser, 2).until(EC.element_to_be_clickable(
                    (By.XPATH, "//div[@class='isgrP']")))
                xt = False
            except:
                pass


        # pop_up_window = browser.find_elements_by_css_selector(".isgrP")
        lasti = 0
        lastword = ''

        start = dt.datetime.now()

        
        
        for i in range(0 , int(numbers[1].text)):

            print(i)
            self.browser.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',pop_up_window)
            sleep(0.1)
            self.browser.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop - arguments[0].offsetHeight/2;',pop_up_window)
            sleep(0.1)
            self.browser.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',pop_up_window)
            sleep(0.1)

            last = browser.find_elements_by_css_selector("._7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll")[-1]
            if last == lastword:
                lasti += 1
                lastword = last
            else:
                lasti = 0
                lastword = last
            if lasti == 10:
                # lasti = 0
                loadinginsta = None
                try:
                    loadinginsta = browser.find_elements_by_css_selector(".By4nA")[-1]
                except:
                    pass
                if loadinginsta == None:
                    lasti = 0

                    break
                else:
                    lasti -= 5
            
            sleep(0.1)
        

        finish = dt.datetime.now()
        time = finish - start

        print(time)

        
        


      
        

        









         
        
        usernames = browser.find_elements_by_css_selector('._7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll')
        usernames2 = []
        print(f"followers : {int(numbers[1].text)}")
        # print(f"followers2 : {len(usernames)}")
        pageid = select_current_userid_by_usrname(username)
        print(pageid)
        os.system("cls")
        print("\twait please ...")
        try:
            for i in range(0 , int(numbers[1].text)):
                
                

                user = User(usernames[i].text.lower())

                curent_userid = insert_user_for_first_one_with_out_info(user)


                follow = Follows(curent_userid, pageid)
                print("userid : " ,follow.userid)
                print("pageid : " ,follow.pageid)
                

                insert_follows(follow)





                print(i + 1)
                # print(usernames[i].text)
                usernames2.append(usernames[i].text)
        except IndexError:
            pass
        
        print(f"\n\tget followers of {username} done")
        return usernames2

    def get_followings(self , username):
        # unfollow_buttons = driver.find_elements_by_css_selector('.sqdOP.L3NKy._8A5w5')
        self.browser.get(f'https://www.instagram.com/{username}/')
        sleep(4)
        buttons = browser.find_elements_by_css_selector('._7UhW9.vy6Bb.MMzan.KV-D4.uL8Hv.T0kll')
        print(buttons)
        print("len :       ",len(buttons))
        unfollow_button = buttons[2]
        numbers = browser.find_elements_by_css_selector('.g47SY')
        
        unfollow_button.click()
        sleep(4)
        xt = True
        while xt == True:
            try :
                pop_up_window = WebDriverWait(
                self.browser, 2).until(EC.element_to_be_clickable(
                    (By.XPATH, "//div[@class='isgrP']")))
                xt = False
            except:
                pass


        # pop_up_window = browser.find_elements_by_css_selector(".isgrP")
        lasti = 0
        lastword = ''

        start = dt.datetime.now()

        usernames3 = set([])
        zzzzz = 0
        for i in range(0 , int(numbers[2].text.replace(",",""))):
            if zzzzz == 5:
                break
            zzzzz += 1
            print(i)
            self.browser.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',pop_up_window)
            sleep(0.1)
            self.browser.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop - arguments[0].offsetHeight/2;',pop_up_window)
            sleep(0.1)
            self.browser.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',pop_up_window)
            sleep(0.1)

            last = browser.find_elements_by_css_selector("._7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll")[-1]
            if last == lastword:
                lasti += 1
                lastword = last
            else:
                lasti = 0
                lastword = last
            if lasti == 10:
                # lasti = 0
                loadinginsta = None
                try:
                    loadinginsta = browser.find_elements_by_css_selector(".By4nA")[-1]
                except:
                    pass
                if loadinginsta == None:
                    lasti = 0

                    break
                else:
                    lasti -= 5
            
            sleep(0.1)
            usernames = browser.find_elements_by_css_selector('._7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll')[-20:]
            for i in usernames:
                usernames3.add(i.text)
            
        

        finish = dt.datetime.now()
        time = finish - start

        print(time)

        
        


      
        

        









         
        
        # usernames = browser.find_elements_by_css_selector('._7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll')
        usernames2 = []
        print(f"followigs : {numbers[2].text}")
        # print(f"followers2 : {len(usernames)}")
        curent_userid = select_current_userid_by_usrname(username)
        print(curent_userid)
        # os.system("cls")
        print("\twait please ...")
        try:
            for i in range(0 , int(numbers[2].text.replace(",",""))):
                
                
                usernames3 = list(usernames3)
                user = User(usernames3[i].lower())

                pageid = insert_user_for_first_one_with_out_info(user)


                follow = Follows(curent_userid, pageid)
                print("userid : " ,follow.userid)
                print("pageid : " ,follow.pageid)
                

                insert_follows(follow)





                print(i + 1)
                # print(usernames[i].text)
                # usernames2.append(usernames3[i].text)
        except IndexError:
            pass
        
        print(f"\n\tget followings of {username} done")
        return usernames3
    
    def get_post_info(self , post ):

        self.browser.get(f'https://www.instagram.com/p/{post}/')
        view_mores = browser.find_elements_by_css_selector('._7UhW9.xLCgt.qyrsm.KV-D4.fDxYl.T0kll')
        i = 0
        more = browser.find_elements_by_css_selector(".qF0y9.Igw0E.IwRSH.YBx95._4EzTm.NUiEW")

        while i < 4 and len(more) == 1:
            try:
                more = browser.find_elements_by_css_selector(".qF0y9.Igw0E.IwRSH.YBx95._4EzTm.NUiEW")
                more[0].click()
                sleep(1)
            except:
                break
            i += 1
        
        
        comments = browser.find_elements_by_css_selector('.sqdOP.yWX7d._8A5w5.ZIAjV')
        comments2 = []
        username = comments[0].text
        for i in comments:
            if i.text == username:
                pass
            else:
                comments2.append(i.text)
        

        # print(set(comments2))

        comments = list(set(comments2))
        pageid = select_current_userid_by_usrname(username)
        for i in comments:
            user = User(i)
            userid = insert_user_for_first_one_with_out_info(user)
            # userid = select_current_userid_by_usrname(i)
            if userid == None:
                continue
            comm = Comments(userid,post,pageid)
            insert_Comments(comm)

        usernames_who_liked = set([])
        try:
            like_link = browser.find_elements_by_css_selector('._7UhW9.xLCgt.qyrsm.KV-D4.fDxYl.T0kll')[0]
            like_link.click()
            print("\n\n\n\n\n\n")
            print(like_link.text)
            print("\n\n\n\n\n\n")

            likes = like_link.text.replace(" likes" , '')
            likes = likes.replace(",",'')

            print("likes : " , likes)
            print("\n\n\n\n\n\n")

            

            
            # pop_up_window = WebDriverWait(
            # self.browser, 2).until(EC.element_to_be_clickable(
            #     (By.XPATH, "//div[@class='qF0y9.Igw0E.IwRSH.eGOV_.vwCYk.i0EQd']")))
            xt = True
            while xt == True:
                try :
                    pop_up_window = WebDriverWait(
                    self.browser, 2).until(EC.element_to_be_clickable(
                        (By.XPATH, "/html/body/div[5]/div/div/div[2]/div")))
                    xt = False
                except:
                    pass

            print(pop_up_window)
            lasti = 0
            lastword = ''

            
            print("debug1")
            for i in range(0 , int(likes)):
                print("debug2")
                print(i)
                print("debug3")
                # browser.execute_script("return arguments[0].scrollIntoView();", elements[-1])
                self.browser.execute_script(
                    'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',pop_up_window)
                sleep(0.1)
                self.browser.execute_script(
                    'arguments[0].scrollTop = arguments[0].scrollTop - arguments[0].offsetHeight/2;',pop_up_window)
                sleep(0.1)
                self.browser.execute_script(
                    'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',pop_up_window)
                sleep(0.1)
                print("debug4")
                last = browser.find_elements_by_css_selector("._7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll")[-1]
                if last == lastword:
                    lasti += 1
                    lastword = last
                else:
                    lasti = 0
                    lastword = last
                if lasti == 10:
                    lasti = 0
                    break
                print("debug5")
                usernames_who_liked2 = browser.find_elements_by_css_selector("._7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll")
                print("debug6")
                print(len(usernames_who_liked2))
                print("debug7")
                # usernames_who_liked = []
                # pageid = select_current_userid_by_usrname(username)
                for i in usernames_who_liked2:
                    # userid = select_current_userid_by_usrname(i.text)
                    usernames_who_liked.add(i.text)
                    # like = Likes(userid,pageid , post)
                print("debug8")
            
        except:
            print("exept")
            pass






        

        # usernames_who_liked = browser.find_elements_by_css_selector("._7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll")
        # print(len(usernames_who_liked))
        # # usernames_who_liked = []
        pageid = select_current_userid_by_usrname(username)
        usernames_who_liked = list(usernames_who_liked)
        for i in usernames_who_liked:
            user = User(i)
            x = insert_user_for_first_one_with_out_info(user)

            
            like = Likes(x,pageid , post)
            insert_like(like)
            
        

        


        



            
            




            




        
        








        # likes_link = browser.find_elements_by_css_selector('._7UhW9.xLCgt.qyrsm.KV-D4.fDxYl.T0kll')[0]

        # likes_link.click()
    
    def like_post(self , post):
        
        self.browser.get(f'https://www.instagram.com/p/{post}/')
        sleep(6)
        like = browser.find_elements_by_css_selector('.QBdPU.rrUvL')[0]
        like.click()
    

    def get_info(self , username):
        # start = dt.datetime.now()
        self.browser.get(f'https://www.instagram.com/{username}/')
        sleep(4)
        all = browser.find_elements_by_css_selector('.g47SY')
        posts = None
        followers = None
        following = None
        name = None
        bio = None
        website = None
        work = None
        phone = None




        posts = text_to_dec(all[0].text)
        followers = text_to_dec(all[1].text)
        following = text_to_dec(all[2].text)
        
        try:
            name = browser.find_element(By.XPATH,value='/html/body/div[1]/section/main/div/header/section/div[2]/span').text
        except:
            pass
        
        try:
            bio = browser.find_element(By.XPATH, value = '/html/body/div[1]/section/main/div/header/section/div[2]/div[2]').text
        
        except:
            pass
        
        try:
            website = browser.find_element(By.XPATH , value = "/html/body/div[1]/section/main/div/header/section/div[2]/a[1]/div").text
        except:
            pass
        
        try:
            work = browser.find_element(By.XPATH , value = "/html/body/div[1]/section/main/div/header/section/div[2]/div[1]/div").text
        except:
            pass
        
        user = User(username , name , followers , following , posts, bio ,website , phone , work )

        print(user)

        insert_user(user)
        print(f"info of {username} has been geted")


        # finish = dt.datetime.now()


        # time = finish - start

        # print(f"time : {time}")


    def get_all_post(self,username):

        self.browser.get(f'https://www.instagram.com/{username}/')
        

        # xt = True
        # while xt == True:
        #     try :
        #         pop_up_window = WebDriverWait(
        #         self.browser, 2).until(EC.element_to_be_clickable(
        #             (By.XPATH, "/html/body/div[1]/section/main")))
        #         xt = False
        #     except:
        #         pass

        # print(pop_up_window)
        lasti = 0
        lastword = ''

        posts = set([])
        posts2 = set([])
        
        for i in range(0 , 1000):

            print(i)
            
            # browser.execute_script("return arguments[0].scrollIntoView();", elements[-1])
            browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            sleep(0.1)

            last = browser.find_elements_by_css_selector(".v1Nh3.kIKUG._bz0w")[-1]
            if last == lastword:
                lasti += 1
                lastword = last
            else:
                lasti = 0
                lastword = last
            if lasti == 10:
                # lasti = 0
                loadinginsta = None
                try:
                    loadinginsta = browser.find_elements_by_css_selector(".By4nA")[-1]
                except:
                    pass
                if loadinginsta == None:
                    lasti = 0

                    break
                else:
                    lasti -= 5
        
            elems = browser.find_elements_by_xpath("//a[@href]")
            

            

            for i in elems:
                z = i.get_attribute("href")

                if "/p/" in z:
                    posts.add(z)
                else:
                    pass
            sleep(0.3)


        print(posts)

        print("len : ", len(posts))

        posts3 = []

        for i in posts:
            z = i.replace("https://www.instagram.com/p/" , "")
            z = z.replace("/" , "")
            posts3.append(z)

        return posts3

    

    


        
         






        




        






        # unfollow_button2 = browser.find_element_by_xpath("//button[normalize-space()='Unfollow']")
        # unfollow_button2.click()


test_bot = Insta_Bot(setting.username,setting.password , browser)

# test_bot.test_login_page()
# sleep(5)
# test_bot.like_post("CakdujJNdYqsmBSvZkTfbee4xczK1Lhefp0wyM0")
# test_bot.get_likes()
# test_bot.access_to_my_profile()

start = dt.datetime.now()


test_bot.get_info("artbeton.co")
sleep(1)

# usernames = test_bot.get_followings("artbeton.co")
usernames = get_followings()[-10:]
pageid = select_current_userid_by_usrname("artbeton.co")
for i in usernames:
    user = User(i)
    userid = insert_user_for_first_one_with_out_info(user)

    follow = Follows(userid,pageid)

    insert_follows(follow)


    

lenusers = len(usernames)
j = 0
for i in usernames:
    # sleep(1)
    j += 1
    print(f'done info users {j}/{lenusers}')
    test_bot.get_info(i)

finish1 = dt.datetime.now()
time1 = finish1 - start
print("time1 : " , time1)


# test_bot.get_info("artbeton.co")

posts = test_bot.get_all_post("artbeton.co")
lenpost = len(posts)
ji = 0
for i in posts:
    ji += 1
    print(f"posts : {ji}/{lenpost}")
    test_bot.get_post_info(i)
    



finish2 = dt.datetime.now()
time2 = finish2 - finish1
print("time2 : " , time2)
print("all : " , finish2 - start)




# test_bot.get_post_info("CbaPlJfNTTq")

# test_bot.follow_user("alpha.photogrphy")
# test_bot.unfollow_user("alpha.photogrphy")
# test_bot.get_all_post("the.great_amir")

#   By4nA
import email
from operator import pos
from time import sleep
from numpy import full_like
import requests
from requests.structures import CaseInsensitiveDict
from sympy import true
from Database.Models import Follows, User,Comments,Likes
from Database.databaseinsta import get_all_pks_who_follow_page, insert_follows, insert_user_for_first_one_with_out_info,select_current_userid_by_usrname,insert_Comments,insert_like
import datetime as dt
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
import queue 





# browser = webdriver.Firefox(executable_path="geckodriver")
# browser.get('https://www.instagram.com/')
# browser.add_cookie({"name" : "sessionid" ,"domain" : ".instagram.com", "value" : "52659641865%3ARP3ounZ2nhPiZj%3A18","httponly" : True ,"secure" : True})
q = queue.Queue()
q2 = queue.Queue()
class Insta_Bot:

    def __init__(self , browser):

        # self.username = username
        # self.password = password
        self.browser = browser
        self.headers = CaseInsensitiveDict()
        self.headers["authority"] = "i.instagram.com"
        self.headers["accept"] = "*/*"
        self.headers["accept-language"] = "en-US,en;q=0.9"
        # self.headers["cookie"] = 'mid=YkQXhQALAAG7ckBUry-I_Spw6ANO; ig_did=0CD208E8-A5C7-4872-A438-BE024BC4C1D8; fbm_124024574287414=base_domain=.instagram.com; ds_user_id=52659641865; ds_user_id=52659641865; shbid="13705\05452659641865\0541680473556:01f7c8b609fa6e96c251fcd9ea6ebbc8543e8aa157d6405a883971a7efa2794b7932cc2e"; shbts="1648937556\05452659641865\0541680473556:01f74679012b215b51999c01e5b944d0f2de5c3e7592b4b4584bf0ca5ea5351ef77047c1"; csrftoken=eAh2bjLZ0HxycMUT2wdHrO5mox1iN0NP; sessionid=52659641865%3ABFDzzhUQNbWD89%3A1; csrftoken=eAh2bjLZ0HxycMUT2wdHrO5mox1iN0NP; rur="ASH\05452659641865\0541680512353:01f7d8a37f3f5c73d5804195b3f042715880af71da007178aa93b362bea38a8c8585fe58"; rur="ASH\05452659641865\0541680512354:01f73a542b7643ae91db773f6c315ee0289c282edf7239e1ca1681afe0c6b7d1d6a2d3c6"'
        self.headers["cookie"] = 'mid=YkQXhQALAAG7ckBUry-I_Spw6ANO; ig_did=0CD208E8-A5C7-4872-A438-BE024BC4C1D8; fbm_124024574287414=base_domain=.instagram.com; shbid="19455\05452449758078\0541680738848:01f7e90b5167ae78c8c89158d5b25aab6c9748ba77933e4636172378ec2bd08f19bc3d14"; shbts="1649202848\05452449758078\0541680738848:01f7ca452919d6dc76d6fd7b76b9368bc1bb43078eb32701f179000eaa1857c68e414007"; csrftoken=1AzKE1Kv8UTVM2vmBftRSBIAnGXYoDfe; ds_user_id=52659641865; sessionid=52659641865%3A0fG8n3xk3zXjnC%3A18; csrftoken=1AzKE1Kv8UTVM2vmBftRSBIAnGXYoDfe; ds_user_id=52659641865; rur="RVA\05452659641865\0541680802025:01f791387c0e00c04471bca9175b9f9c1b77e7244fb9c166fbaee5d4445ad3931e830e7c"; rur="RVA\05452659641865\0541680802026:01f7de13781047a0e881cd4d21dd0f566d5bde9ebf14328c8adb7d109e31af001bb869c8"'

        

        self.headers["origin"] = "https://www.instagram.com"
        self.headers["referer"] = "https://www.instagram.com/"
        self.headers["sec-ch-ua"] = '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"'
        self.headers["sec-ch-ua-mobile"] = "?0"
        self.headers["sec-ch-ua-platform"] = '"Windows"'
        self.headers["sec-fetch-dest"] = "empty"
        self.headers["sec-fetch-mode"] = "cors"
        self.headers["sec-fetch-site"] = "same-site"
        self.headers["user-agent"] = "Instagram 9.0.2 (iPhone7,2; iPhone OS 9_3_3; en_US; en-US; scale=2.00; 750x1334) AppleWebKit/420+"
        self.headers["x-asbd-id"] = "198387"
        self.headers["x-ig-app-id"] = "936619743392459"

        self.headers["x-ig-capabilities"] = "3w=="
        # self.headers["x-ig-www-claim"] = "hmac.AR35GEXqVqFYY3oPEe8mx89e5dcif5fawVCm5xnksaalU4fC"
        self.headers["x-ig-www-claim"] = "hmac.AR35GEXqVqFYY3oPEe8mx89e5dcif5fawVCm5xnksaalU4KY"
    

    def get_followings_pks(self,pk):
        url = f"https://i.instagram.com/api/v1/friendships/{pk}/following/?count=7000"
        resp = requests.get(url, headers=self.headers)
        sleep(3)
        x = resp.json()

        print(x)
        users = x['users']
        users2 = []
        for i in users:
            users2.append(i['pk'])

        return users2   

    def get_info_of_user(self,pk):
        url = f"https://i.instagram.com/api/v1/users/{pk}/info/"
        
        resp = requests.get(url, headers=self.headers)
        respjson = resp.json()

        try:
            username = respjson['user']['username']
        
        except:
            username = None

        try:
            name = respjson['user']['full_name']
        
        except:
            name = None
        
        try:
            followers = respjson['user']['follower_count']
        
        except:
            followers = None
        
        try:
            followings = respjson['user']['following_count']
        
        except:
            followings = None
        
        try:
            posts =respjson['user']['media_count']

        except:
            posts =None

        try:
            bio = respjson['user']['biography']

        except:
            bio = None
        
        try:
            site = respjson['user']['external_url']

        except:
            site = None
        
        try:
            public_phone_number = respjson['user']['public_phone_number']

        except:
            public_phone_number = None
        

        try:
            public_phone_country_code = respjson['user']['public_phone_country_code']
        
        except:
            public_phone_country_code = None
        
        try:
            work = respjson['user']['category']
        
        except:
            work = None


        try:
            address = respjson['user']['address_street']
        
        except:
            address = None
        

        try:
            public_email = respjson['user']['public_email']
        
        except:
            public_email = None
        

        try:
            city_name = respjson['user']['city_name']
        
        except:
            city_name = None

        

        
        

        user = User(pk,username,name,followers,followings,posts,bio,site,public_phone_number,work,address,public_email,city_name,public_phone_country_code)

        insert_user_for_first_one_with_out_info(user)
    
    # def get_posts(self,pk):
    #     num = 1
    #     # url = f'https://www.instagram.com/graphql/query/?query_hash=8c2a529969ee035a5063f2fc8602a0fd&variables=%7B%22id%22%3A%22{pk}%22%2C%22first%22%3A12%2C%22after%22%3A%22QVFDbWdmb1ZUZi1VdUE0Vk9YNmRodndjTUsycFBRZ09kbGdhZXI3T3lRRHJtMnFDbFcxeG42N2ZHbm1mX09oR2Q5Z05neWdKeFFqUF85aXQtYzl2QzB4UA%3D%3D%22%7D'
    #     url = f'https://www.instagram.com/graphql/query/?query_hash=8c2a529969ee035a5063f2fc8602a0fd&variables=%7B%22id%22%3A%22{pk}%22%2C%22first%22%3A{num}%2C%22after%22%3A%22QVFBTjh0cDNRdGEweTBhYzdsZk5nV0NDdF95Z19pMkJqUWN2UzAweUVZc05scm5QX2Z4ekZaVHMyQ0J4MDk1bnVMaVpBd1lhUDZZeHFVcVJZMkJydnN3bw%3D%3D%22%7D'
    #     resp = requests.get(url, headers=self.headers)
    #     respjson = resp.json()

    #     x = respjson['data']['user']['edge_owner_to_timeline_media']['edges'][0]['node']['shortcode']
    #     json_formatted_str = json.dumps(x, indent=4)
    #     print(json_formatted_str)


    
    # def get_likes(self,postid , likes):
    #     # likes = 1000
    #     url = f'https://www.instagram.com/graphql/query/?query_hash=d5d763b1e2acf209d62d22d184488e57&variables=%7B%22shortcode%22%3A%22{postid}%22%2C%22include_reel%22%3Atrue%2C%22first%22%3A{likes}%7D'
    #     resp = requests.get(url, headers=self.headers)
    #     respjson = resp.json()

    #     print('count : ',respjson['data']['shortcode_media']['edge_liked_by']['count'])
    #     print('count2 : ',len(respjson['data']['shortcode_media']['edge_liked_by']['edges']))

    def get_pk_from_username(self,username):
        url = f'https://www.instagram.com/{username}/?__a=1'
        resp = requests.get(url, headers=self.headers)
        respjson = resp.json()
        return respjson['graphql']['user']['id']
    

    def get_likes(self,post,pageid):
        url = f'https://www.instagram.com/graphql/query/?query_hash=d5d763b1e2acf209d62d22d184488e57&variables=%7B%22shortcode%22%3A%22{post}%22%2C%22include_reel%22%3Atrue%2C%22first%22%3A50%7D'
        test_set = set([])
        while True:
            try:
                resp = requests.get(url, headers=self.headers)
                respjson = resp.json()
        
        
                x = respjson['data']['shortcode_media']['edge_liked_by']['edges']
                break
            except KeyError:
                print("key error exept 213")
                sleep(2)
                pass

            except json.decoder.JSONDecodeError:
                print("exept json 218")
                sleep(2)
                pass

        
        for i in x:
            test_set.add(i['node']['id'])



        
        hash2 = respjson['data']['shortcode_media']['edge_liked_by']['page_info']['end_cursor'].replace("==",'')
        while True:
            try:
                print(len(test_set))
                url2 = f'https://www.instagram.com/graphql/query/?query_hash=d5d763b1e2acf209d62d22d184488e57&variables=%7B%22shortcode%22%3A%22{post}%22%2C%22include_reel%22%3Atrue%2C%22first%22%3A50%2C%22after%22%3A%22{hash2}%3D%3D%22%7D'
                while True:
                    try:
                        resp = requests.get(url2, headers=self.headers)
                        respjson = resp.json()
                        # print(respjson)
                        x = respjson['data']['shortcode_media']['edge_liked_by']['edges']
                        break

                    # except TypeError:
                    #     break
                    except json.decoder.JSONDecodeError:
                        print("exept json 245")
                        sleep(2)
                        pass
                    except KeyError:
                        print("key error 250")
                        sleep(2)
                        pass

                    


                for i in x:
                    test_set.add(i['node']['id'])
                hash2 = respjson['data']['shortcode_media']['edge_liked_by']['page_info']['end_cursor'].replace("==",'')
            except TypeError:
                break

        j22 = 0
        j33 = 0
        lentest_set = len(test_set)
        for i in test_set:
            j33 += 1
            q.put(i)
            # t1 = threading.Thread(target=self.get_info_of_user, args=(i,))
            # t1.start()
            
            
            like = Likes(i,pageid,post)
            q2.put(like)
            # t2 = threading.Thread(target=insert_like , args=(like,))
            # t2.start()
            # insert_like(like)
            # if j33 == 30:
            #     print(f"\n\tlike aded {j22 + 1}/{lentest_set}")
            #     j33 = 0
            j22 +=1 

    def put_users(self):
        i = 0
        while True:
            i += 1
            try:

                x = q.get()
                self.get_info_of_user(x)
                # print(f"user {x} aded")

            except:
                # print("exept users")
                pass
            
            if i == 30:
                print(f"len q(users) in q : {queue.Queue.qsize(q)}")
                
                i = 0


    def put_likes(self):
        i = 0
        while True:
            i += 1
            try:
                x = q2.get()
                insert_like(x)
                # print(f"len q2 like : {queue.Queue.qsize(q2)}")

            except:
                # print("exept likes")
                pass
            if i == 30:
                print(f"len q2(like) in q2: {queue.Queue.qsize(q2)}")
                i = 0

    def follow_user(self,followuser):
        

        self.browser.get(f'https://www.instagram.com/{followuser}/')
        follow_button = self.browser.find_element_by_xpath("//button[normalize-space()='Follow']")
        follow_button.click()

    def unfollow_user(self , unfollowuser):
        # unfollow_buttons = driver.find_elements_by_css_selector('.sqdOP.L3NKy._8A5w5')
        self.browser.get(f'https://www.instagram.com/{unfollowuser}/')
        buttons = self.browser.find_elements_by_css_selector('._5f5mN.-fzfL._6VtSN.yZn4P')
        print(buttons)
        print("len :       ",len(buttons))
        unfollow_button = buttons[0]
        unfollow_button.click()
        sleep(2)
        unfollow_button2 = self.browser.find_element_by_xpath("//button[normalize-space()='Unfollow']")
        unfollow_button2.click()
    
    def like_post(self , post):
        
        self.browser.get(f'https://www.instagram.com/p/{post}/')
        sleep(6)
        like = self.browser.find_elements_by_css_selector('.QBdPU.rrUvL')[0]
        like.click()
    # def get_post_info(self , post ):

    #     self.browser.get(f'https://www.instagram.com/p/{post}/')
    #     view_mores = browser.find_elements_by_css_selector('._7UhW9.xLCgt.qyrsm.KV-D4.fDxYl.T0kll')
    #     i = 0
    #     more = browser.find_elements_by_css_selector(".qF0y9.Igw0E.IwRSH.YBx95._4EzTm.NUiEW")

    #     while i < 4 and len(more) == 1:
    #         try:
    #             more = browser.find_elements_by_css_selector(".qF0y9.Igw0E.IwRSH.YBx95._4EzTm.NUiEW")
    #             more[0].click()
    #             sleep(1)
    #         except:
    #             break
    #         i += 1
        
        
    #     comments = browser.find_elements_by_css_selector('.sqdOP.yWX7d._8A5w5.ZIAjV')
    #     comments2 = []
    #     username = comments[0].text
    #     for i in comments:
    #         if i.text == username:
    #             pass
    #         else:
    #             comments2.append(i.text)
        

    #     # print(set(comments2))

    #     comments = list(set(comments2))
    #     pageid = select_current_userid_by_usrname(username)
    #     for i in comments:
    #         pk = self.get_pk_from_username(i)
    #         self.get_info_of_user(pk)
    #         # user = User(i)
    #         # userid = insert_user_for_first_one_with_out_info(user)
    #         # userid = select_current_userid_by_usrname(i)
    #         # if userid == None:
    #         #     continue
    #         comm = Comments(pk,post,pageid)
    #         insert_Comments(comm)

    #     usernames_who_liked = set([])
    #     try:
    #         like_link = browser.find_elements_by_css_selector('._7UhW9.xLCgt.qyrsm.KV-D4.fDxYl.T0kll')[0]
    #         like_link.click()
    #         # print("\n\n\n\n\n\n")
    #         # print(like_link.text)
    #         # print("\n\n\n\n\n\n")

    #         likes = like_link.text.replace(" likes" , '')
    #         likes = likes.replace(",",'')

    #         # print("likes : " , likes)
    #         # print("\n\n\n\n\n\n")

            

            
    #         # pop_up_window = WebDriverWait(
    #         # self.browser, 2).until(EC.element_to_be_clickable(
    #         #     (By.XPATH, "//div[@class='qF0y9.Igw0E.IwRSH.eGOV_.vwCYk.i0EQd']")))
    #         xt = True
    #         while xt == True:
    #             try :
    #                 pop_up_window = WebDriverWait(
    #                 self.browser, 2).until(EC.element_to_be_clickable(
    #                     (By.XPATH, "/html/body/div[5]/div/div/div[2]/div")))
    #                 xt = False
    #             except:
    #                 pass

    #         # print(pop_up_window)
    #         lasti = 0
    #         lastword = ''

            
    #         print("debug1")
    #         for i in range(0 , int(likes)):
    #             # print("debug2")
    #             # print(i)
    #             # print("debug3")
    #             # browser.execute_script("return arguments[0].scrollIntoView();", elements[-1])
    #             self.browser.execute_script(
    #                 'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',pop_up_window)
    #             sleep(0.1)
    #             self.browser.execute_script(
    #                 'arguments[0].scrollTop = arguments[0].scrollTop - arguments[0].offsetHeight/2;',pop_up_window)
    #             sleep(0.1)
    #             self.browser.execute_script(
    #                 'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',pop_up_window)
    #             sleep(0.1)
    #             # print("debug4")
    #             last = browser.find_elements_by_css_selector("._7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll")[-1]
    #             if last == lastword:
    #                 lasti += 1
    #                 lastword = last
    #             else:
    #                 lasti = 0
    #                 lastword = last
    #             if lasti == 10:
    #                 lasti = 0
    #                 break
    #             # print("debug5")
    #             usernames_who_liked2 = browser.find_elements_by_css_selector("._7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll")
    #             # print("debug6")
    #             # print(len(usernames_who_liked2))
    #             # print("debug7")
    #             # usernames_who_liked = []
    #             # pageid = select_current_userid_by_usrname(username)
    #             for i in usernames_who_liked2:
    #                 # userid = select_current_userid_by_usrname(i.text)
    #                 usernames_who_liked.add(i.text)
    #                 # like = Likes(userid,pageid , post)
    #             # print("debug8")
            
    #     except:
    #         print("exept")
    #         pass






        

    #     # usernames_who_liked = browser.find_elements_by_css_selector("._7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll")
    #     # print(len(usernames_who_liked))
    #     # # usernames_who_liked = []
    #     pageid = select_current_userid_by_usrname(username)
    #     usernames_who_liked = list(usernames_who_liked)
    #     for i in usernames_who_liked:
    #         # user = User(i)
    #         # x = insert_user_for_first_one_with_out_info(user)
    #         pk = self.get_pk_from_username(i)
    #         self.get_info_of_user(pk)

            
    #         like = Likes(pk,pageid , post)
    #         insert_like(like)
    
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
        # posts2 = set([])
        
        for i in range(0 , 1000):

            # print(i)
            
            # browser.execute_script("return arguments[0].scrollIntoView();", elements[-1])
            self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            sleep(0.1)

            last = self.browser.find_elements_by_css_selector(".v1Nh3.kIKUG._bz0w")[-1]
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
                    loadinginsta = self.browser.find_elements_by_css_selector(".By4nA")[-1]
                except:
                    pass
                if loadinginsta == None:
                    lasti = 0

                    break
                else:
                    lasti -= 5
        
            elems = self.browser.find_elements_by_xpath("//a[@href]")
            

            

            for i in elems:
                z = i.get_attribute("href")

                if "/p/" in z:
                    posts.add(z)
                    
                else:
                    pass
            if len(posts) >= 7:
                break
            sleep(0.3)


        # print(posts)

        print("\n\tlen post : ", len(posts))

        posts3 = []

        for i in posts:
            z = i.replace("https://www.instagram.com/p/" , "")
            z = z.replace("/" , "")
            posts3.append(z)

        return posts3


# start = dt.datetime.now()

# bot_insta = Insta_Bot()

# filewww = open('posts.txt','r')

# ppp = filewww.read()


# filewww.close()


# posts = ppp.split("\n")

# lenposts= len(posts)
# pageid = select_current_userid_by_usrname('artbeton.co')
# t1 = threading.Thread(target=bot_insta.put_users)
# t1.start()

# t2 = threading.Thread(target=bot_insta.put_likes)
# t2.start()
# j = 0
# for i in posts:
    
#     bot_insta.get_likes(i,pageid)
#     j += 1 
#     print(f"\n\tposts :  {j}/{lenposts}\n")
#     time2 = dt.datetime.now()

#     full_time1 = time2 - start
#     # print(f"len q(users) in q : {queue.Queue.qsize(q)}")
#     # print(f"len q2(like) in q2: {queue.Queue.qsize(q2)}")
#     print( "\n\n\ttime : ",full_time1)


# posts = bot_insta.get_all_post('artbeton.co')

# lenposts= len(posts)

# j = 0
# for i in posts:
#     bot_insta.get_post_info(i)
#     j += 1 
#     print(f"\n\t{j}/{lenposts}\n")

# bot_insta.get_posts('3517615623')

# bot_insta.get_likes("CZq-C-qt7Jd",'255')



# pks = bot_insta.get_followings_pks('3517615623')

# who_follows = get_all_pks_who_follow_page('3517615623')

# pks = list(set(pks)^set(who_follows))

# lenpks = len(pks)
# j = 0
# while True:
    
#     if j == lenpks:
#         break

#     try:
#         follow = Follows(pks[j],'3517615623')
#         insert_follows(follow)
#         bot_insta.get_info_of_user(pks[j])

#         print(f"{j + 1}/{lenpks}")
#         j += 1
#     except json.decoder.JSONDecodeError:
#         pass

#     except:
#         j += 1
    

#

# finish = dt.datetime.now()

# full_time = finish - start

# print( "\n\n\t full time : ",full_time)









        

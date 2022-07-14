# from matplotlib.style import use
import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
import urllib.request as rq






def get_followings():
    url = "https://i.instagram.com/api/v1/friendships/3517615623/following/?count=3"

    headers = CaseInsensitiveDict()
    headers["authority"] = "i.instagram.com"
    headers["accept"] = "*/*"
    headers["accept-language"] = "en-US,en;q=0.9"
    headers["cookie"] = 'mid=YkQXhQALAAG7ckBUry-I_Spw6ANO; ig_did=0CD208E8-A5C7-4872-A438-BE024BC4C1D8; fbm_124024574287414=base_domain=.instagram.com; csrftoken=kVQSFHMVpnQd2ufTp4vyI58IY2cE7Iif; ds_user_id=52659641865; sessionid=52659641865%3AruqQVv7zm5k8Cz%3A27; csrftoken=kVQSFHMVpnQd2ufTp4vyI58IY2cE7Iif; ds_user_id=52659641865; rur="RVA\05452659641865\0541680459976:01f761d3ee267cb50cf1c785853239e5f6f9b8ec53c673f6c7dce1d00bcc819cc9aca616"; rur="RVA\05452659641865\0541680459981:01f7d42bcd91b029262248897ac37a14fde1b8f8b1678b2f2817df41e8577bbebcd274f3"'

    headers["origin"] = "https://www.instagram.com"
    headers["referer"] = "https://www.instagram.com/"
    headers["sec-ch-ua"] = '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"'
    headers["sec-ch-ua-mobile"] = "?0"
    headers["sec-ch-ua-platform"] = '"Windows"'
    headers["sec-fetch-dest"] = "empty"
    headers["sec-fetch-mode"] = "cors"
    headers["sec-fetch-site"] = "same-site"
    headers["user-agent"] = "Instagram 9.0.2 (iPhone7,2; iPhone OS 9_3_3; en_US; en-US; scale=2.00; 750x1334) AppleWebKit/420+"
    headers["x-asbd-id"] = "198387"
    headers["x-ig-app-id"] = "936619743392459"

    headers["x-ig-capabilities"] = "3w=="
    headers["x-ig-www-claim"] = "hmac.AR35GEXqVqFYY3oPEe8mx89e5dcif5fawVCm5xnksaalU_T5"
    # headers["authority"] = "i.instagram.com"
    # headers["authority"] = "i.instagram.com"



    resp = requests.get(url, headers=headers)
    x = resp.json()

    # print(x)
    users = x['users']
    users2 = []
    for i in users:
        users2.append(i['pk'])



    # print(users2)
    # print(len(users2))
    print(users2)

    return users2

def get_info():
    url = "https://i.instagram.com/api/v1/users/3517615623/info/"
    headers = CaseInsensitiveDict()
    headers["authority"] = "i.instagram.com"
    headers["accept"] = "*/*"
    headers["accept-language"] = "en-US,en;q=0.9"
    headers["cookie"] = 'mid=YkQXhQALAAG7ckBUry-I_Spw6ANO; ig_did=0CD208E8-A5C7-4872-A438-BE024BC4C1D8; fbm_124024574287414=base_domain=.instagram.com; csrftoken=kVQSFHMVpnQd2ufTp4vyI58IY2cE7Iif; ds_user_id=52659641865; sessionid=52659641865%3AruqQVv7zm5k8Cz%3A27; csrftoken=kVQSFHMVpnQd2ufTp4vyI58IY2cE7Iif; ds_user_id=52659641865; rur="RVA\05452659641865\0541680459976:01f761d3ee267cb50cf1c785853239e5f6f9b8ec53c673f6c7dce1d00bcc819cc9aca616"; rur="RVA\05452659641865\0541680459981:01f7d42bcd91b029262248897ac37a14fde1b8f8b1678b2f2817df41e8577bbebcd274f3"'

    headers["origin"] = "https://www.instagram.com"
    headers["referer"] = "https://www.instagram.com/"
    headers["sec-ch-ua"] = '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"'
    headers["sec-ch-ua-mobile"] = "?0"
    headers["sec-ch-ua-platform"] = '"Windows"'
    headers["sec-fetch-dest"] = "empty"
    headers["sec-fetch-mode"] = "cors"
    headers["sec-fetch-site"] = "same-site"
    headers["user-agent"] = "Instagram 9.0.2 (iPhone7,2; iPhone OS 9_3_3; en_US; en-US; scale=2.00; 750x1334) AppleWebKit/420+"
    headers["x-asbd-id"] = "198387"
    headers["x-ig-app-id"] = "936619743392459"

    headers["x-ig-capabilities"] = "3w=="
    headers["x-ig-www-claim"] = "hmac.AR35GEXqVqFYY3oPEe8mx89e5dcif5fawVCm5xnksaalU_T5"

    

    resp = requests.get(url, headers=headers)
    respjson = resp.json()
    username = respjson['user']['username']
    name = respjson['user']['full_name']
    followers = respjson['user']['follower_count']
    followings = respjson['user']['following_count']
    bio = respjson['user']['biography']
    
    work = respjson['user']['category']
    
    
    



    address = respjson['user']['address_street']
    public_phone_number = respjson['user']['public_phone_number']
    public_phone_country_code = respjson['user']['public_phone_country_code']
    public_email = respjson['user']['public_email']
    city_name = respjson['user']['city_name']
    site = respjson['user']['external_url']
    posts =respjson['user']['media_count']
    
    

    # print(work ,"    " ,name)

    print(public_phone_number)

    

    # x = open("12.txt" , "w")
    # x.write(respjson)

def get_test():
    url = 'https://www.instagram.com/artbeton.fdfdfdfdfdfco/?__a=1'
    headers = CaseInsensitiveDict()
    headers["authority"] = "i.instagram.com"
    headers["accept"] = "*/*"
    headers["accept-language"] = "en-US,en;q=0.9"
    headers["cookie"] = 'mid=YkQXhQALAAG7ckBUry-I_Spw6ANO; ig_did=0CD208E8-A5C7-4872-A438-BE024BC4C1D8; fbm_124024574287414=base_domain=.instagram.com; shbid="13705\05452659641865\0541680473556:01f7c8b609fa6e96c251fcd9ea6ebbc8543e8aa157d6405a883971a7efa2794b7932cc2e"; shbts="1648937556\05452659641865\0541680473556:01f74679012b215b51999c01e5b944d0f2de5c3e7592b4b4584bf0ca5ea5351ef77047c1"; csrftoken=9p0xdR6O1ONJ3ZsVELYrAee2VD7ntu50; ds_user_id=52659641865; sessionid=52659641865%3AKBfz2pp7n6r4fy%3A19; rur="RVA\05452659641865\0541680630482:01f7b91dd1f0b707b2850f14b8697332e690f2dbc3bc58cf63469a160970dab17052e176"'

    headers["origin"] = "https://www.instagram.com"
    headers["referer"] = "https://www.instagram.com/"
    headers["sec-ch-ua"] = '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"'
    headers["sec-ch-ua-mobile"] = "?0"
    headers["sec-ch-ua-platform"] = '"Windows"'
    headers["sec-fetch-dest"] = "empty"
    headers["sec-fetch-mode"] = "cors"
    headers["sec-fetch-site"] = "same-site"
    headers["user-agent"] = "Instagram 9.0.2 (iPhone7,2; iPhone OS 9_3_3; en_US; en-US; scale=2.00; 750x1334) AppleWebKit/420+"
    headers["x-asbd-id"] = "198387"
    headers["x-ig-app-id"] = "936619743392459"

    headers["x-ig-capabilities"] = "3w=="
    headers["x-ig-www-claim"] = "hmac.AR35GEXqVqFYY3oPEe8mx89e5dcif5fawVCm5xnksaalU0PU"

    

    resp = requests.get(url, headers=headers)
    respjson = resp.json()
    print(respjson['graphql']['user']['id'])

def get_likes(post):
    url = f'https://www.instagram.com/graphql/query/?query_hash=d5d763b1e2acf209d62d22d184488e57&variables=%7B%22shortcode%22%3A%22{post}%22%2C%22include_reel%22%3Atrue%2C%22first%22%3A50%7D'
    headers = CaseInsensitiveDict()
    headers["authority"] = "i.instagram.com"
    headers["accept"] = "*/*"
    headers["accept-language"] = "en-US,en;q=0.9"
    headers["cookie"] = 'mid=YkQXhQALAAG7ckBUry-I_Spw6ANO; ig_did=0CD208E8-A5C7-4872-A438-BE024BC4C1D8; fbm_124024574287414=base_domain=.instagram.com; shbid="13705\05452659641865\0541680473556:01f7c8b609fa6e96c251fcd9ea6ebbc8543e8aa157d6405a883971a7efa2794b7932cc2e"; shbts="1648937556\05452659641865\0541680473556:01f74679012b215b51999c01e5b944d0f2de5c3e7592b4b4584bf0ca5ea5351ef77047c1"; csrftoken=9p0xdR6O1ONJ3ZsVELYrAee2VD7ntu50; ds_user_id=52659641865; sessionid=52659641865%3AKBfz2pp7n6r4fy%3A19; rur="RVA\05452659641865\0541680630482:01f7b91dd1f0b707b2850f14b8697332e690f2dbc3bc58cf63469a160970dab17052e176"'

    headers["origin"] = "https://www.instagram.com"
    headers["referer"] = "https://www.instagram.com/"
    headers["sec-ch-ua"] = '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"'
    headers["sec-ch-ua-mobile"] = "?0"
    headers["sec-ch-ua-platform"] = '"Windows"'
    headers["sec-fetch-dest"] = "empty"
    headers["sec-fetch-mode"] = "cors"
    headers["sec-fetch-site"] = "same-site"
    headers["user-agent"] = "Instagram 9.0.2 (iPhone7,2; iPhone OS 9_3_3; en_US; en-US; scale=2.00; 750x1334) AppleWebKit/420+"
    headers["x-asbd-id"] = "198387"
    headers["x-ig-app-id"] = "936619743392459"

    headers["x-ig-capabilities"] = "3w=="
    headers["x-ig-www-claim"] = "hmac.AR35GEXqVqFYY3oPEe8mx89e5dcif5fawVCm5xnksaalU0PU"
    resp = requests.get(url, headers=headers)
    respjson = resp.json()
    print(respjson)
    # test_set = set([])
    # x = respjson['data']['shortcode_media']['edge_liked_by']['edges']
    # for i in x:
    #     test_set.add(i['node']['id'])



    
    # hash2 = respjson['data']['shortcode_media']['edge_liked_by']['page_info']['end_cursor'].replace("==",'')
    # while True:
    #     try:
    #         print(len(test_set))
    #         url2 = f'https://www.instagram.com/graphql/query/?query_hash=d5d763b1e2acf209d62d22d184488e57&variables=%7B%22shortcode%22%3A%22{post}%22%2C%22include_reel%22%3Atrue%2C%22first%22%3A50%2C%22after%22%3A%22{hash2}%3D%3D%22%7D'
    #         resp = requests.get(url2, headers=headers)
    #         respjson = resp.json()
    #         x = respjson['data']['shortcode_media']['edge_liked_by']['edges']
    #         for i in x:
    #             test_set.add(i['node']['id'])
    #         hash2 = respjson['data']['shortcode_media']['edge_liked_by']['page_info']['end_cursor'].replace("==",'')
    #     except TypeError:
    #         break

    
    # for i in test_set:
    #     print(i)
        
    
    # for i in x:
    #     print(i['node']['id'])

    # print(respjson['data']['shortcode_media']['edge_liked_by']['page_info']['end_cursor'].replace("==",''))


get_likes('CbaPlJfNTTq')




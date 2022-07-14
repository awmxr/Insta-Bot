


from ctypes import addressof
from turtle import pos


class User:
    def __init__(self , pk,username = None , name = None , followers = None , followings = None,posts = None ,  bio = None, website = None , phone = None , work = None,address = None , email = None , city = None , country_code = None):
        self.pk = pk
        self.username = username
        self.name = name
        self.followers = followers
        self.followings = followings
        self.posts = posts
        self.bio = bio
        self.website = website
        self.phone = phone
        self.work = work
        self.address = address
        self.country_code = country_code
        self.email = email
        self.city = city
    

    def __str__(self):

        x = f"name : {self.name}\nusername : {self.username}\nfollowers : {self.followers}\nfollowing : {self.followings}\n posts : {self.posts}\nbio : {self.bio}\nwebsite : {self.website}\nphone : {self.phone}\nwork : {self.work}"
        return x
        
        


class Likes :
    def __init__(self , userid , pageid , post):
        self.userid = userid
        self.pageid = pageid
        self.post = post


class Follows:
    def __init__(self, userid , pageid):
        self.userid = userid
        self.pageid = pageid


class Comments:
    def __init__(self , userid , post , pageid):
        self.userid = userid
        self.pageid = pageid
        self.post = post






        

        

        


        
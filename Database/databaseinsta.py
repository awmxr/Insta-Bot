import sqlite3

from matplotlib.style import use
from sqlalchemy import false, true
conn = sqlite3.connect('AlphA.db')
import datetime as dt

# from Models import User, Likes , Follows , Comments

# c = conn.cursor()
# c.execute("""CREATE TABLE User (
#     pk integer,
#     username text,
#     name text,
#     followers integer,
#     following integer,
#     posts integer,
#     website text,
#     phone text,
#     work text,
#     bio text,
#     address text,
#     country_code text,
#     email text,
#     city text
#     )""")


# c.execute("""CREATE TABLE Likes (
    
#     userid integer,
#     post text,
#     pageid integer
#     )""")


# # conn.commit()
# c.execute("""CREATE TABLE Follows (
    
#     userid integer,
#     pageid integer
    
#     )""")


# c.execute("""CREATE TABLE Comments (
    
#     userid integer,
#     pageid integer,
#     post text
#     )""")



# conn.commit()






# ////////////////////////////////////////////////////////////////////////


def insert_user(user):

    
    conn = sqlite3.connect('AlphA.db')
    c = conn.cursor()
    # print(admin)


    # with conn:
    #     c.execute("Select * From User WHERE username = :username", {"username" : user.username})

    # x = c.fetchall()

    # if len(x) > 0:
    c.execute("DELETE From User WHERE pk = :pk" , {"pk" : user.pk})
    conn.commit()
        


    with conn:
        c.execute("INSERT INTO User ( pk ,username , name , followers , following , posts , website , phone, work, bio,address ,country_code,email ,city ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
                 user.pk,user.username , user.name , user.followers ,  user.followings , user.posts , user.website , user.phone , user.work , user.bio , user.address , user.country_code,user.email , user.city))

    rowid = c.lastrowid
    with conn:
        c.execute("Select pk From User WHERE rowid = :rowid", {"rowid" : rowid})

    return c.fetchone()[0]



def insert_user_for_first_one_with_out_info(user):

    
    conn = sqlite3.connect('AlphA.db')
    c = conn.cursor()
    # print(admin)


    with conn:
        c.execute("Select pk From User WHERE pk = :pk", {"pk" : user.pk})

    x = c.fetchone()

    if x != None:
        return x[0]
    else:


        with conn:
            c.execute("INSERT INTO User ( pk ,username , name , followers , following , posts , website , phone, work, bio,address ,country_code,email ,city ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
                 user.pk,user.username , user.name , user.followers ,  user.followings , user.posts , user.website , user.phone , user.work , user.bio , user.address , user.country_code,user.email , user.city))
    

        rowid = c.lastrowid
        with conn:
            c.execute("Select pk From User WHERE rowid = :rowid", {"rowid" : rowid})

        return c.fetchone()[0]



def insert_like(like):

    
    conn = sqlite3.connect('AlphA.db')
    c = conn.cursor()
    with conn:
        c.execute("Select * From Likes WHERE userid =:userid and post = :post ", { "userid" : like.userid,"post" : like.post })
    
    x = c.fetchone()

    if x != None:
        pass
    else:

    # print(admin)
        with conn:
            c.execute("INSERT INTO Likes ( userid , post , pageid ) VALUES (?,?,?)", (
                    like.userid , like.post , like.pageid ))



def insert_follows(follows):

    
    conn = sqlite3.connect('AlphA.db')
    c = conn.cursor()
    # print(admin)
    with conn:
        c.execute("Select * From Follows WHERE userid =:userid  and pageid =:pageid", { "userid" : follows.userid, "pageid":follows.pageid})
    
    x = c.fetchone()

    if x != None:
        pass
    else:


        with conn:
            c.execute("INSERT INTO Follows ( userid , pageid ) VALUES (?,?)", (
                    follows.userid , follows.pageid ))


def insert_Comments(comment):

    
    conn = sqlite3.connect('AlphA.db')
    c = conn.cursor()


    with conn:
        c.execute("Select * From Comments WHERE userid =:userid and post = :post ", { "userid" : comment.userid,"post" : comment.post })
    
    x = c.fetchone()

    if x != None:
        pass
    else:
    # print(admin)
        with conn:
            c.execute("INSERT INTO Comments ( userid , pageid , post ) VALUES (?,?,?)", (
                    comment.userid , comment.pageid , comment.post ))




def select_current_userid_by_usrname(username):

    conn = sqlite3.connect('AlphA.db')
    c = conn.cursor()
    c.execute("SELECT pk FROM User  WHERE  username=:username ",{"username":username})
    b = c.fetchone()

    conn.close()
    if b == None:
        return None
    else:

        return b[0]


def get_all_pks_who_follow_page(page_pk):
    conn = sqlite3.connect('AlphA.db')
    c = conn.cursor()
    c.execute("SELECT userid FROM Follows  WHERE  pageid=:page_pk ",{"page_pk":page_pk})
    b = c.fetchall()
    conn.close()
    if b == None:
        return None
    


    
    else:
        bb = []
        for i in b:
            bb.append(i[0])
        return bb
    



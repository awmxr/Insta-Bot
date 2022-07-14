import sqlite3

from sympy import true

def select_posts_from_likes():
    conn = sqlite3.connect('AlphA.db')
    c = conn.cursor()
    c.execute("SELECT post FROM likes")
    b = set(c.fetchall())
    x = []
    for i in b:
        x.append(i[0])    
    print(len(x))
    return x

def keytt(e):
    return e[1]

def select_user():
    conn = sqlite3.connect('AlphA.db')
    c = conn.cursor()
    c.execute("SELECT pk FROM User")
    b = set(c.fetchall())
    x = []
    for i in b:
        x.append(i[0])    
    lenx = len(x)
    final_list = []
    z = ''
    j = 0
    for i in x:
        c.execute("SELECT count(*) FROM Likes where userid =:pk",{"pk":i})
        likes = c.fetchone()
        
        final_list.append([i,likes[0]])
        print(f'\n\t {j}/{lenx}')
        j += 1

    final_list.sort(reverse=True , key=keytt)


    for i in final_list:
        z += f'{i[0]} : {i[1]}\n'

    f= open("gozaresh.txt",'w')
    f.write(z)
    f.close()

    # print(final_list)
    





        

    # return x


# print(select_posts_from_likes())
    # f = open('ff.txt','w')

    # f.write(x)
    # f.close()

# select_user()
select_posts_from_likes()






    

# get_all_pks_who_follow_page()
# import datetime as dt
# from time import sleep
# start = dt.datetime.now()
# sleep(2)
# finish = dt.datetime.now()
# time = finish - start


# print(time)
for i in range(10):
    f = open('x.txt','a')
    f.write(str(i) + '\n')
    f.close()
import time
import random

lyrics = ("I just wanna be yours")

abc = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")
printt = ""
f = 0

while printt!=lyrics:
    x = random.randint(0,52)
    if(abc[x] == lyrics[f]):
        printt += lyrics[f]
        f += 1
        print(printt)
    else:
        time.sleep(0.01)
        print(printt + abc[x])


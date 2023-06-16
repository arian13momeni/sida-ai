from imdb import Cinemagoer
from wikipedia import *


print("welcome to sida ai ")
print("-" * 50)
print("1.film and animation ")
print("2. qustion")


menu = input("import number :  ")



if menu == "1":

    # film 
    im = Cinemagoer()
    inp = input("sarch an film or animation : ")
    movies = im.search_movie(inp)
    print(movies)
if menu == "2":
    q = input("enter your qustion : ")
    wikipedia.set_lang("en")
    print(wikipedia.summary(q))



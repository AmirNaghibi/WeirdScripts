import time
import random
import urllib.request
import re
from random_word import RandomWords
import requests


for k in range(10):
    
    r = RandomWords()
    str = r.get_random_word()
    if str == None: str = "None"
    str_list = list(str.split(" "))
    str = '-'.join(str_list)
    
    print("search term = " + str)
    
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+str)
    video_ids = re.findall(r'watch\?v=(\S{11})', html.read().decode())
    
    link = 'https://www.youtube.com/watch?v=' + video_ids[random.randint(0,5)]
    
    r = requests.get(link)
    print(link)
    time.sleep(3)

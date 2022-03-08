import scraper
import numpy as np
import matplotlib.pyplot as plot

def createMap():
    list = scraper.scrapeQuery("Wordle 262", 100)
    map = { "1" : 0,
            "2" : 0,
            "3" : 0,
            "4" : 0,
            "5" : 0,
            "6" : 0,
            "X" : 0}
    for i in list:
        if ("/6" in i):
            location = i[i.index("/6") - 1]
            if(location in map):
                map[location] = map.get(location, 0) + 1
    
    return map

    
map = createMap()

keys = map.keys()
values = map.values()

plot.bar(keys, values)
plot.ylabel("Number of users")
plot.title("Wordle guesses Wordle #262")
plot.show()
import scraper
import numpy as np
import matplotlib.pyplot as plot

def createMap():
    list = scraper.scrapeQuery("Wordle 262", 100)
    average = 0
    length = 0
    
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
            
            if (i[i.index("/6") - 1] is not "X"):
                average += int(i[i.index("/6") - 1])                
                length = length + 1
    
    return map, round((average / float(length)), 1)
    
map, mean = createMap()

keys = map.keys()
values = map.values()

plot.bar(keys, values)
plot.ylabel("Number of users")
plot.title("Wordle guesses Wordle #262")

print("Mean value: " + str(mean))
plot.show()
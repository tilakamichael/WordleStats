import scraper
import numpy as np
import matplotlib.pyplot as plot

def createMap():
    list = scraper.scrapeQuery("Wordle 262", 100)
    mean = 0
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
            
            if (i[i.index("/6") - 1] != "X"):
                mean += int(i[i.index("/6") - 1])                
                length = length + 1
    
    return map, round((mean / float(length)), 1)
    
map, mean = createMap()

print("Mean value: " + str(mean))   

mean = round(mean)

keys = map.keys()
values = map.values()

barlist = plot.bar(keys, values)
barlist[mean - 1].set_color('y')


plot.ylabel("Number of users")
plot.title("Wordle guesses Wordle #262")

plot.show()
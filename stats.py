from tracemalloc import start
import scraper
import numpy as np
import matplotlib.pyplot as plot
from datetime import date, datetime

def createMap():
    list = scraper.scrapeQuery(todayWordle(), 100)
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

def todayWordle():
    today = datetime.today().strftime("%Y-%m-%d")
    startDate = "2022-03-08"
    
    difference = datetime.strptime(today, "%Y-%m-%d") - datetime.strptime(startDate, "%Y-%m-%d")
    
    return "Wordle " + str(262 + abs(difference.days))


def main():
    map, mean = createMap()

    print("Mean value: " + str(mean))   

    roundedMean = round(mean)

    keys = map.keys()
    values = map.values()

    barlist = plot.bar(keys, values)
    barlist[roundedMean - 1].set_color('y')


    plot.ylabel("Number of users")
    plot.xlabel("Average: " + str(mean))
    plot.title("Wordle guesses for " + todayWordle())

    plot.show()

main()
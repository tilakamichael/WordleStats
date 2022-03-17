from tracemalloc import start
import scraper
import matplotlib.pyplot as plot
from datetime import datetime 
import time

def createMap():
    #Collect tweets
    list = scraper.scrapeQuery(todayWordle())
    mean = 0
    numlength = 0
    
    #Set up dictionary for results and number of users per result
    map = { "1" : 0,
            "2" : 0,
            "3" : 0,
            "4" : 0,
            "5" : 0,
            "6" : 0,
            "X" : 0}
    
    #Iterate through the list
    for i in list:
        #If it contains a Wordle result and it is a valid result, increment the map value
        if ("/6" in i):
            location = i[i.index("/6") - 1]
            
            if(location in map):
                map[location] = map.get(location, 0) + 1
            
            #Calculate running mean for all successful guesses 
            if (ord(i[i.index("/6") - 1]) >= 49 and ord(i[i.index("/6") - 1]) <= 54):
                mean += int(i[i.index("/6") - 1])                
                numlength = numlength + 1
                
            #Include unsuccessful results in the calculation as 7
            elif ((i[i.index("/6") - 1]).upper() == 'X'):
                mean += 7
                numlength = numlength + 1
    
    #Return the dictionary and the mean rounded to one decimal place
    return map, round((mean / float(numlength)), 1), numlength

def todayWordle():
    #Set up today and start date
    today = datetime.today().strftime("%Y-%m-%d")
    startDate = "2022-03-08"
    
    #Bases what the wordle number is on the difference between current date, and march 8th (262, when I started)
    difference = datetime.strptime(today, "%Y-%m-%d") - datetime.strptime(startDate, "%Y-%m-%d")
    
    return "Wordle " + str(262 + abs(difference.days))


def main():
    #start of runtime
    startTime = time.time()    
    map, mean, length = createMap()
    
    print("Mean value: " + str(mean))   

    #Rounds to nearest integer
    roundedMean = round(mean)

    keys = map.keys()
    values = map.values()

    #Keys (results) on x, values (users) on y
    barlist = plot.bar(keys, values)
    barlist[roundedMean - 1].set_color('y')

    #Sets up bar graph labels
    plot.ylabel("Number of users")
    plot.xlabel("Average: " + str(mean))
    plot.title("Wordle guesses for " + todayWordle() + " per " + str(length) + " users")

    #end of runtime
    print("Runtime: %s seconds" % (time.time() - startTime))
    plot.show()

main()
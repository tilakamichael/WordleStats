import scraper
import matplotlib.pyplot as plot
from datetime import datetime 
from datetime import timedelta
import time

def createMap():
    #Collect tweets
    response = ''
    print ("Would you like to grab a previous wordle or today's wordle? ('t' for today and 'p' for previous):")
    response = input()
    
    #Making sure the user enters a valid resopnse on whether they want a prev wordle or today's wordle
    while (response  != 'p' and response != 't'):
        print ("Please enter 'p' or 't':")
        response = input()
    
    whatWordle = todayWordle()
    
    date = ''
    
    #If they want previous wordle
    if (response == 'p'):
        #Grabs what wordle number they want
        print ("Enter what wordle number you would like to grab, today's is " + todayWordle())
        wordleNum = int(input())
        
        #Grabs today's wordle number
        currWordleNum = int(whatWordle[7:])
        
        #Makes sure the user enters a wordle number less or equal to today's
        while(wordleNum > currWordleNum):
            print ("Please enter a number less than " + str(currWordleNum))
            wordleNum = int(input())
            
        #Grab the date of that wordle
        difference = currWordleNum - wordleNum
        date = datetime.strptime(datetime.today(), "%Y-%m-%d") - timedelta(difference)
    
    list = scraper.scrapeQuery(whatWordle, date, date)
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
#the purpose of the program is to take a file and parse
#the data to create candlestick timeframes. candle times will
#be specified by the user (ie. 1min, 3min, 30min, 1hr...)

#in order to practice with python this will be done two ways. 
#1. take a csv file and parse the info 
#2. use pandas or some other http client to store info in some
#dataframe

import csv
from datetime import datetime
from CandleMakerLib1Min import *
from CandleMakerLib2Min import *
from CandleMakerLib4Min import *
from CandleMakerLib8Min import *
from CandleMakerLib16Min import *
from CandleMakerLib32Min import *
from CandleMakerLib1Hour import *
from CandleMakerLib2Hour import *
from CandleMakerLib4Hour import *
from CandleMakerLib8Hour import *
from CandleMakerLib12Hour import *
from CandleMakerLib24Hour import *

#boolean values for 1min, 3min, ...4hr, 1day etc is
#initialized to false and set to true when a row 
#with the respective time is found. this way no more
#rows are added which have the correct minute but
#who's second has changed. once  a new minute is 
#found reset the 

#create file storing each new minutes row so you don't
#need to worry about seconds

with open('EUR_USD_Week1.csv') as f:
    readCSV = csv.reader(f, delimiter=',')
    firstRow = next(readCSV)

    initMinOne(firstRow)
    initMinTwo(firstRow)
    initMinFour(firstRow)
    initMinEight(firstRow)
    initMinSixteen(firstRow)
    initMinThirtyTwo(firstRow)
    initHourOne(firstRow)
    initHourTwo(firstRow)
    initHourFour(firstRow)
    initHourEight(firstRow)
    initHourTwelve(firstRow)
    initHourTwentyFour(firstRow)

    holdRow = {}

    for row in readCSV:
        
        #checkMinOne(row)
        #checkMinTwo(row)
        #checkMinFour(row)
        #checkMinEight(row)
        checkMinSixteen(row)
        checkMinThirtyTwo(row)

        checkHourOne(row)
        checkHourTwo(row)
        checkHourFour(row)
        checkHourEight(row)
        checkHourTwelve(row)
        checkMinTwentyFour(row, 0)

        holdRow = row

        print ("minOneCount == ", minOneCount) 
        print ("minTwoCount == ", minTwoCount) 
        print ("minFourCount == ", minFourCount) 
        print ("minEightCount == ", minEightCount) 
        print ("minSixteenCount == ", minSixteenCount) 
        print ("minThirtyTwoCount == ", minThirtyTwoCount) 
        print ("hourOneCount == ", hourOneCount) 
        print ("hourTwoCount == ", HourTwoCount) 
        print ("hourFourCount == ", hourFourCount) 
        print ("hourEightCount == ", hourEightCount) 
        print ("hourTwelveCount == ", hourTwelveCount) 
        print ("hourTwentyFourCount == ", hourTwentyFourCount) 

    checkHourTwentyFour(holdRow, 1)
    """
        time = row[2]
        kick = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
        if kick.hour != butt.hour:
            with open('hour.csv', 'a') as w:
                w.write(','.join([str(x) for x in row]))
                w.write("\n")
                count += 1
            butt = kick
            
    print ((60*24*7)+ (60*9))
    print (count)
    """
    #    if time_object.hour == 0:
   #         print (row)
            #if time_object.hour == 0:
                #print (row)
        #if time[17] == 0 & time[18] == 0:
        #        print(time)
        #print(row[2])





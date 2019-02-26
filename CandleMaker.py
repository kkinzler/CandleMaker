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
    initHourTwelve(firstRow)
    initHourTwentyFour(firstRow)

    holdRow = [] 

    for row in readCSV:
        
        
        checkMinOne(row)
        checkMinTwo(row)
        checkMinFour(row)
        checkMinEight(row)
        checkMinSixteen(row)
        checkMinThirtyTwo(row)

        checkHourOne(row, 0)
        checkHourTwo(row, 0)
        checkHourFour(row, 0)
        checkHourTwelve(row, 0)
        
        checkHourTwentyFour(row, 0)
        

        holdRow = row


    checkHourOne(holdRow, 1)
    checkHourTwo(holdRow, 1)
    checkHourFour(holdRow, 1)
    checkHourTwelve(holdRow, 1)
    checkHourTwentyFour(holdRow, 1)

    #print out how many candles were created for each timeframe

    minOneCount = getMinOne()
    minTwoCount = getMinTwo()
    minFourCount = getMinFour()
    minEightCount = getMinEight()
    minSixteenCount = getMinSixteen()
    minThirtyTwoCount = getMinThirtyTwo()
    hourOneCount = getHourOne()
    hourTwoCount = getHourTwo()
    hourFourCount = getHourFour()
    hourTwelveCount = getHourTwelve()
    hourTwentyFourCount = getHourTwentyFour()

    print ("minOneCount == ", minOneCount) 
    print ("minTwoCount == ", minTwoCount) 
    print ("minFourCount == ", minFourCount) 
    print ("minEightCount == ", minEightCount) 
    print ("minSixteenCount == ", minSixteenCount) 
    print ("minThirtyTwoCount == ", minThirtyTwoCount) 
    print ("hourOneCount == ", hourOneCount) 
    print ("hourTwoCount == ", hourTwoCount) 
    print ("hourFourCount == ", hourFourCount) 
    print ("hourTwelveCount == ", hourTwelveCount) 
    print ("hourTwentyFourCount == ", hourTwentyFourCount) 

    print ("minOneCount/2 = ", minOneCount/2, " /4 = ", minOneCount/4, " /8 = ", minOneCount/8)
    print ("minOneCount/16 = ", minOneCount/16, " /32 = ", minOneCount/32, " /60 = ", minOneCount/60)
    print ("minOneCount/120 = ", minOneCount/120, " /240 = ", minOneCount/240, " /720 = ", minOneCount/720)
    
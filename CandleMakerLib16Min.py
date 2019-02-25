#functions for gain capital parser
from datetime import datetime
import math

minSixteenCount = 0
minSixteenCount = 0
minSixteenOpen = 0.0
minSixteenClose = 0.0
minSixteenHigh = 0.0
minSixteenLow = 0.0
minSixteen = 0

#getPrice() takes as args, row: where the 4th element in the row is the ask price
#                    returns: ask price rounded to the 5th decimal (pipette)
def getPrice(row):
    ask = row[4]
    price = round(float(ask), 5)
    return price


#getPrice() takes as args, row: where the 3rd element is the bid and the 
#                               4th element in the row is the ask price
#                    returns: ask - bid rounded to the 5th decimal (pipette)
def getSpread(row):
    bid = row[3]
    ask = row[4]
    spread = float(ask)-float(bid)
    return round(spread, 5)


#getPrice() takes as args, row: used to grab price and int representing minute or hour
#                    returns: 1 for success or 0 for fail
def initMinSixteen(row):
    global minSixteenOpen
    global minSixteenClose
    global minSixteenHigh
    global minSixteenLow
    global minSixteen

    if row == 0:
        "row empty could not initiate minSixteen data"
        return 0

    #set price for open, high and low.
    #set current minute or hour 
    price = getPrice(row)
    minSixteenOpen = price
    minSixteenClose = 0.0
    minSixteenHigh = price
    minSixteenLow = price
    minSixteen = getTime(row, 1, 0)

    return 1



#getPrice() takes as args, row: containing a list of 6 elements. [0] number, [1] currency pair, 
#                               [2] time, [3] bid, [4] ask, [5] the letter 'D'
#                    returns: 1 for success or 0 for fail
def checkMinSixteen(row):

    if row == 0:
        print ("row empty could not check mon one data")
        return 0

    global minSixteenOpen
    if minSixteenOpen == 0.0:
        minSixteenOpen = getPrice(row)

    setBounds(row)
    

    currentTime = getTime(row, 1, 0)    
    if (currentTime >= minSixteen + 16 or (minSixteen >= 47 and currentTime < minSixteen)):

        #simple check to see how many gaps there are in the data. 
        #probably need to come back and create more thorough checks
        #if (minSixteen >= 50 and currentTime < minSixteen):
        #    print ("minuteSixteen data had a ten minute gap in data") 
        #    print ("minSixteen: ", minSixteen, "    currentTime: ", currentTime)

        writeMinSixteenBar(row)

        global minSixteenCount
        minSixteenCount += 1
        initMinSixteen(row)
        minSixteenOpen = 0.0

    return 1
    
#writeMinSixteenBar takes args row: for row in data to analyze
#                      returns: 1 for success and 0 for failure
def writeMinSixteenBar(row):
    global minSixteenClose 
    minSixteenClose = getPrice(row)
    #writes list to one minute timeframe. 
    #list = [0] Time, [1] Open, [2] Close, [3] High, [4] Low, [5] Spread 
    with open('EURUSD-MinSixteen.csv', 'a') as w:
            barData = [row[2], minSixteenOpen, minSixteenClose, minSixteenHigh, minSixteenLow, getSpread(row)]
            w.write(','.join([str(x) for x in barData]))
            w.write("\n")
        

#getTime takes args row: for row in data to analyze
#                   min: Boolean True if returning minute
#                   hr: Boolean True if returning hour
#              returns: current minute(0-59) or current hour(0-23)
def getTime(row, min, hr):
    
    kick = row[2]
    butt = datetime.strptime(kick, "%Y-%m-%d %H:%M:%S")

    if min == True:
        return butt.minute
    if hr == True:
        return butt.hour


#getTime takes args row: for row in data to analyze
#if current price is above or below high/low price respecively
#replace high or low with current price
def setBounds(row):
    global minSixteenHigh
    global minSixteenLow
    price = getPrice(row)
    if minSixteenLow > price:
        minSixteenLow = price
    if minSixteenHigh < price:
        minSixteenHigh = price
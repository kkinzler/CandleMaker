#functions for gain capital parser
from datetime import datetime
import math

minFourCount = 0
minFourOpen = 0.0
minFourClose = 0.0
minFourHigh = 0.0
minFourLow = 0.0
minFour = 0

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
def initMinFour(row):
    global minFourOpen
    global minFourClose
    global minFourHigh
    global minFourLow
    global minFour

    if row == 0:
        "row empty could not initiate minFour data"
        return 0

    #set price for open, high and low.
    #set current minute or hour 
    price = getPrice(row)
    minFourOpen = price
    minFourClose = 0.0
    minFourHigh = price
    minFourLow = price
    minFour = getTime(row, 1, 0)

    return 1



#getPrice() takes as args, row: containing a list of 6 elements. [0] number, [1] currency pair, 
#                               [2] time, [3] bid, [4] ask, [5] the letter 'D'
#                    returns: 1 for success or 0 for fail
def checkMinFour(row):

    if row == 0:
        print ("row empty could not check mon one data")
        return 0

    global minFourOpen
    if minFourOpen == 0.0:
        minFourOpen = getPrice(row)

    setBounds(row)
    

    currentTime = getTime(row, 1, 0)    
    if (currentTime >= minFour + 4 or (minFour >= 55 and currentTime < minFour)):

        #simple check to see how many gaps there are in the data. 
        #probably need to come back and create more thorough checks
        #if (minFour >= 50 and currentTime < minFour):
        #    print ("minuteFour data had a ten minute gap in data") 
        #    print ("minFour: ", minFour, "    currentTime: ", currentTime)

        writeMinFourBar(row)

        global minFourCount
        minFourCount += 1
        initMinFour(row)
        minFourOpen = 0.0

    return 1
    
#writeMinFourBar takes args row: for row in data to analyze
#                      returns: 1 for success and 0 for failure
def writeMinFourBar(row):
    global minFourClose 
    minFourClose = getPrice(row)
    #writes list to one minute timeframe. 
    #list = [0] Time, [1] Open, [2] Close, [3] High, [4] Low, [5] Spread 
    with open('EURUSD-MinFour.csv', 'a') as w:
            barData = [row[2], minFourOpen, minFourClose, minFourHigh, minFourLow, getSpread(row)]
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
    global minFourHigh
    global minFourLow
    price = getPrice(row)
    if minFourLow > price:
        minFourLow = price
    if minFourHigh < price:
        minFourHigh = price

def getMinFour():
    return minFourCount
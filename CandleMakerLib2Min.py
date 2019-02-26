#functions for gain capital parser
from datetime import datetime
import math

minTwoCount = 0

minTwoOpen = 0.0
minTwoClose = 0.0
minTwoHigh = 0.0
minTwoLow = 0.0
minTwo = 0

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
def initMinTwo(row):
    global minTwoOpen
    global minTwoClose
    global minTwoHigh
    global minTwoLow
    global minTwo

    if row == 0:
        "row empty could not initiate minTwo data"
        return 0

    #set price for open, high and low.
    #set current minute or hour 
    price = getPrice(row)
    minTwoOpen = price
    minTwoClose = 0.0
    minTwoHigh = price
    minTwoLow = price
    minTwo = getTime(row, 1, 0)

    return 1



#getPrice() takes as args, row: containing a list of 6 elements. [0] number, [1] currency pair, 
#                               [2] time, [3] bid, [4] ask, [5] the letter 'D'
#                      returns: minTwoCount which is the number of entries created 
def checkMinTwo(row):

    if row == 0:
        print ("row empty could not check mon one data")
        return 0

    global minTwoOpen
    if minTwoOpen == 0.0:
        minTwoOpen = getPrice(row)

    setBounds(row)
    

    currentTime = getTime(row, 1, 0)    
    if (currentTime >= minTwo + 2 or (minTwo >= 55 and currentTime < minTwo)):

        #simple check to see how many gaps there are in the data. 
        #probably need to come back and create more thorough checks
        #if (minTwo >= 50 and currentTime < minTwo):
        #    print ("minuteTwo data had a ten minute gap in data") 
        #    print ("minTwo: ", minTwo, "    currentTime: ", currentTime)

        writeMinTwoBar(row)

        global minTwoCount
        minTwoCount += 1
        initMinTwo(row)
        minTwoOpen = 0.0

    return 1
    
#writeMinTwoBar takes args row: for row in data to analyze
#                      returns: 1 for success and 0 for failure
def writeMinTwoBar(row):
    global minTwoClose 
    minTwoClose = getPrice(row)
    #writes list to one minute timeframe. 
    #list = [0] Time, [1] Open, [2] Close, [3] High, [4] Low, [5] Spread 
    with open('EURUSD-MinTwo.csv', 'a') as w:
            barData = [row[2], minTwoOpen, minTwoClose, minTwoHigh, minTwoLow, getSpread(row)]
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
    global minTwoHigh
    global minTwoLow
    price = getPrice(row)
    if minTwoLow > price:
        minTwoLow = price
    if minTwoHigh < price:
        minTwoHigh = price

def getMinTwo():
    return minTwoCount
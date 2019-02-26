Candle Maker

Comment out whichever timeframes you aren't interested in and generate candles out 
of files downloaded from Gain Capital's historical forex rates at:
              http://ratedata.gaincapital.com/
              
For your consideration:

  You will need to change the name of the file you're reading from as you grab data
  from the website to match what's in candleMaker.py or change the name of the file
  in candleMaker.py
  
  Sometimes the files from Gain Capital are zipped and sometimes they aren't.
  
  Some of the files have fields before the data and some don't. This program doesn't
  account for fields so you'll just need to delete those before extracting candles.
  
  Some files represent seconds with higher resolution (micro). The function that turns 
  the date-time (which is a STRING when read from the file) into a date-time object,
  reads second with %S. To read as a microsecond change %S to %f. 
  
  
  

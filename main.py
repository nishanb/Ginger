from helper.ApiClient import ApiClient
from helper.Notifer import Notifer
import time
import os
from dotenv import load_dotenv, find_dotenv

if __name__ == "__main__":
    
    #setup env 
    load_dotenv(find_dotenv())

    #setup helpers
    TappiClient =  ApiClient(os.environ.get("TAAP_SECRET"),os.environ.get("MARKET"),os.environ.get("CURRENCY"),os.environ.get("TRADE_INTERVAL"))
    Notifer = Notifer(os.environ.get("TLEGRAM_BOT_TOKEN"),os.environ.get("TELEGRAM_NOTIFIER_ID"))

    #Trading logic
    while True:
        
        #Start looking for the signal
        currentRSIValue = TappiClient.getRSIValue()
        
        #signal for trading 
        upSingal = False
        downSignal = False
        
        print("Current RSI Value: " + str(currentRSIValue))
        
        #Step 1: Check if RSI is above 70
        if currentRSIValue > 70 :
            
            #Step2 : Check EMA200 is above cuurent candle high
            if TappiClient.getCandleUpValue() <= TappiClient.getEMA200():
                
                #got signal down trend
                downSignal = True
                
                print("Entered OverBought position")
                
                #Step3: Wait for RSI to Fall Down
                previousRSIValue = currentRSIValue
                
                #check 3 times before exiting for down trend
                for i in range(3):
                    
                    while previousRSIValue  <=  currentRSIValue :
                        print("Current RSI Value: " + str(currentRSIValue))
                        print("Previous RSI Value: " + str(previousRSIValue))
                    
                        previousRSIValue = currentRSIValue
                        currentRSIValue = TappiClient.getRSIValue()

        elif currentRSIValue < 30:
            
            #Step2 : heck if EMA200 is below current candle low
            if TappiClient.getCandleDownValue() >= TappiClient.getEMA200():
            
                #Step3: Wait for RSI to Rise Up
                previousRSIValue= currentRSIValue
                
                #got signal down trend
                upSingal = True
                
                print("Entered Undersold position")
                
                #check 3 times before exiting for up trend
                for _ in range(3):
                    while previousRSIValue  >=  currentRSIValue :
                        print("Current RSI Value: " + str(currentRSIValue))
                        print("Previous RSI Value: " + str(previousRSIValue))
                        
                        previousRSIValue = currentRSIValue
                        currentRSIValue = TappiClient.getRSIValue()
        
        if upSingal or downSignal :

            if upSingal:
                Notifer.notify("RSI is at {} , Opted a Up Trend".format(currentRSIValue))
            else:
                Notifer.notify("RSI is at {} , Opted for Down Trend".format(currentRSIValue))        

            #TODO : Send notification to WS for trend change
            
            #TODO : wait for price change to start next trade
            time.sleep(60*3)
            
            #Restart Trading
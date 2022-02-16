import requests
import time
class ApiClient:
    
    def __init__(self,secret,exchange,symbol,interval = "1m", optInTimePeriod = 200,chart = "candles"):
        
        self.secret = secret
        self.exchange = exchange
        self.symbol = symbol
        self.interval = interval
        self.chart = chart
        self.BASE_URL = "https://api.taapi.io"
        self.sleep = 3
    
    def getRSIValue(self) -> float:
        time.sleep(self.sleep )
        try:
            url = self.BASE_URL+"/rsi?secret="+self.secret+"&exchange="+self.exchange+"&symbol="+self.symbol+"&interval="+self.interval+"&chart="+self.chart
            return float(requests.get(url).json()["value"])
        except:
            return 50
    
    def getEMA200(self) -> float:
        time.sleep(3)
        try:
            url = self.BASE_URL+"/ema?secret="+self.secret+"&exchange="+self.exchange+"&symbol="+self.symbol+"&interval="+self.interval+"&optInTimePeriod=200"+"&chart="+self.chart
            return float(requests.get(url).json()["value"])
        except:
            return -1
    
    def getCandleUpValue(self) -> float:
        time.sleep(self.sleep )
        try:
            url = self.BASE_URL+"/candle?secret="+self.secret+"&exchange="+self.exchange+"&symbol="+self.symbol+"&interval="+self.interval+"&chart="+self.chart
            return float(requests.get(url).json()["high"])
        except:
            return -1
    
    def getCandleDownValue(self) -> float:
        time.sleep(self.sleep )
        try:
            url = self.BASE_URL+"/candle?secret="+self.secret+"&exchange="+self.exchange+"&symbol="+self.symbol+"&interval="+self.interval+"&chart="+self.chart
            return float(requests.get(url).json()["low"])
        except:
            return -1
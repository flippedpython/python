def main():
    appName = 'Shares Application'
    print(appName)

    deal = Deal()
    deal.shareTicker = getTicker()
    deal.sharePrice = getTickerPrice(deal.shareTicker);
    deal.quantity = getQuantity()

    print('Ticker ',deal.shareTicker)
    print('Quantity Pay ',deal.quantity)
    print('Share Price',deal.sharePrice)
    print('Deal Cost ',deal.quantity*deal.sharePrice/100.0)
    print('Commission ',getCommission(deal))

def getCommission(d):
    if (d.quantity*d.sharePrice/100*0.01 < 10):
        return 10
    else:
        return 10 + (d.quantity*d.sharePrice/100-1000)*0.005
        

def getTickerPrice(ticker):
    tickers = ['BAR', 'VOD', 'SHE','ORG','APP','ARM','INT','ZZZ']
    livePrices = [180.92, 172.45,451.78,328.11,4861.1,609.5,3291.0,100.0]
    tickerIndex  = 0;
    
    for t in tickers:
        if t == ticker:
            return livePrices[tickerIndex]
            
        tickerIndex = tickerIndex +1
    
        
def getQuantity():
    qt = 0
    while (qt < 1 or qt > 2000):
        qt = int(input("enter quantity? "))
        if (qt < 1 or qt > 2000):
            print ('Enter Quanity BETWEEN 1 and 2000')
            
    return qt

def getTicker():
    ticker = input("enter ticker? ")
    return ticker

class Deal:
    def __init__(self):
        self.quantity = 0
        self.shareTicker = "NULL"
        self.sharePrice = 0
        
if __name__ == '__main__':
    main()


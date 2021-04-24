import yfinance as yf
from datetime import datetime

def api():
    print("Input:\n")
    print('Please enter a symbol:\n')
    stockName = input()

    try:
        stockDetails = yf.Ticker(stockName)
        stockInfo = stockDetails.info

        if stockInfo['logo_url'] == '':
            raise ValueError('Stock name '+stockName+' is not valid')
        print("\nOutput:")
        now = datetime.now()
        time = now.strftime('%a %b %d  %H:%M:%S %Y')
        print(f"\n{time}")
        print("\n"+stockDetails.info['longName']+"\n")

        closeData = stockDetails.history(period='2d')
        close1 = closeData['Close'][1]
        close2 = closeData['Close'][0]

        valChange = round(close1-close2,2)
        valChangePer = round((valChange/close1)*100,2)

        valChangeStr = '+'+str(valChange) if valChange>=0 else '-'+str(valChange)
        valChangePerStr = '+'+str(valChangePer) if valChangePer>=0 else '-'+str(valChangePer)
        print(str(close1)+" "+valChangeStr+" ("+valChangePerStr+"%)")
       
    except Exception as e:
        print("[ERROR] Failed to execute stock api.",e)



if __name__ == "__main__":
    enter_again = "y"
    while enter_again == "y":
        api()
        print("\nEnter 'y' to check stock details again, any other key to exit")
        enter_again = input()
        if enter_again != "y":
            break

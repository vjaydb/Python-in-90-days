stocks = ["Reliance", "HPCL", "Suzlon", "AartiDrugs", "DLF","AtherEnergy"]
for stock in stocks:
    print(stock)
    
    ##Loops
stocks = ["Ather Energy", "Suzlon", "AdaniPower"]
for stock in stocks:
    print(f"processing:{stock}")
for i in range(5):
    print(i)
for m in range(2,10,2):
    print(m)
    
    ##Stocks Review Sheet
stocks1 = ["Ather Energy", "Suzlon", "Dlf", "AdaniGreen"]
buy_price = [830, 78, 900, 2400]
curent_price = [950, 40, 700, 400]
for n in range(len(stocks1)):
    profit_percent = ((curent_price[n]-buy_price[n])/buy_price[n])*100
    if profit_percent >0:
        print(f"{stocks1[n]}:+{profit_percent:.2f}%:-Hold")
    else:
        print(f"{stocks1[n]}:{profit_percent:.2f}%:Review")
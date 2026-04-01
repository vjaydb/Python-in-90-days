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

##Loan EMI Outstanding Balance basic
outstanding_balance =108000
emi = 12000
month =1 
while outstanding_balance>0:
    outstanding_balance -= emi
    print (f"Outstanding loan amount is {outstanding_balance} for the month {month}")
    month += 1

##Break Loop
stocks2 = ["Suzlon", "Amazon", "Dlf"]
for stock in stocks2:
    if stock == "Dlf":
        print("Found DLf - Hence stopping search")
        break
    print (stock)
for stock in stocks2:
    if stock == "Amazon":
        continue
    print(stock)
for i, stock in enumerate(stocks2,1):
    print(f"{i}. {stock}")
    
           
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
#continue Loop
for stock in stocks2:
    if stock == "Amazon":
        continue
    print(stock)
# Enumerate Loop
for i, stock in enumerate(stocks2,1):
    print(f"{i}. {stock}")

#Enumurate loop "Exercise 1"
stocks3 = ["Ather Energy", "Sesagoa", "Hindalco", "Suzlon", "Sunpharma"]
for i, stock in enumerate(stocks3, 1):
    print(f"{i}. {stock}")

#Loan EMI,  Excercise 2

outstanding_loan_amount = 500000
emi = 12500
month= 1
while outstanding_loan_amount >12500:
    outstanding_loan_amount -= emi
    print(f"Outstanding Loan amount is INR.{outstanding_loan_amount} for the end of the month {month}st/nd/rd/th")
    month += 1

##challenge BMI and category print

bmi_values = [14.5, 17.2, 22.1, 27.4, 32.8, 37.1, 41.5]
for i, bmi in enumerate(bmi_values,1):
    if bmi <16:
        print(f"{i}: Severely Underweight")
    if bmi >=16 and bmi <= 18.4:
        print(f"{i}: Underweight")
    if bmi >=18.5 and bmi <=24.9:
        print (f"{i}: Normal")
    if bmi >=25 and bmi <=29.9:
        print (f"{i}: Overweight")
    if bmi >=30 and bmi <=34.9:
        print (f"{i}: Obsese Class 1")
    if bmi >=35 and bmi <=39.9:
        print (f"{i}: Obese Class 2")
    if bmi >=40:
        print (f"{i}: Severely Obese")

           
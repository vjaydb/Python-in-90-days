#Loan EMI,  Excercise 2, Retaken from day4 for st/nd/rd/th logic
##########Taken From line 132 ####Prefix at number like 1st
def cordinal(n):
    remainder=n % 10
    if n == 1:
        return(f"{n}st")
    elif n==2:
        return(f"{n}nd")
    elif n==3:
        return (f"{n}rd")
    elif n==4 and 5 and 6 and 7 and 8 and 9 and 10 and 11 and 12 and 13:
        return(f"{n}th")
    elif remainder == 4 and 5 and 6 and 7 and 8 and 9 and 0:
        return(f"{n}th")
    elif remainder == 1:
        return(f"{n}st")
    elif remainder == 2:
        return(f"{n}nd")
    elif remainder == 3:
        return(f"{n}rd")
    else:
        return(f"{n}th")

outstanding_loan_amount = 500000
emi = 12500
month= 1
while outstanding_loan_amount >12500:
    outstanding_loan_amount -= emi
    month_1=cordinal(month)
    print(f"Outstanding Loan amount is INR.{outstanding_loan_amount} for the end of the month {month_1}")
    month += 1
    

## Creating Functions
def greet():
    print(f"Hello Vivan")

greet()

## Use case of Def With Parameteres

def greet(name):
    print(f"Hello {name}")
greet("shivani")
greet("shiv")

## Use case of Def with variable, Math Functions
def calculate_bmi(weight, height):
    bmi = weight/(height/100)**2
    return bmi
my_bmi = calculate_bmi(68,175)
print(f"My BMI is {my_bmi:.2f}")
shivani_bmi = calculate_bmi(44,154)
print(f"Shivani's BMI is {shivani_bmi:.2f}")

## Loan Case, counting EMI by Making function
def calculate_emi(principal, rate=10, tenure=12):
    monthly_rate= rate/1200
    emi=principal*monthly_rate*(1+monthly_rate)**tenure
    emi= emi/(1+monthly_rate)**tenure-1
    return emi 

Loan1= calculate_emi(100000,10,12)
print(f"Your Emi for Loan1 is INR.{Loan1:.2f} ")

##Task by Chatgpt

def calculate_emi_1(principal, rate=10, tenure=12, debug=False):
    monthly_rate=rate/1200
    emi=numerator=principal*monthly_rate*(1+monthly_rate)**tenure
    denominator=(1+monthly_rate)**tenure-1
    emi=numerator/denominator
    if debug == True:
        print(f"monthly_rate : {monthly_rate:.2f}%, numerator : {numerator:.2f}, denominator {denominator:.2f}")
    else:
        return emi 

emi2=calculate_emi_1(500000,8.5,12)

##EMi calculation with total interest and total payment

def calculate_emi3(principle, rate=8.5, tenure=12, debug=False):
    monthly_rate=rate/1200
    numerator_emi=principle*monthly_rate*(1+monthly_rate)**tenure
    denominator_emi=(1+monthly_rate)**tenure-1
    emi=numerator_emi/denominator_emi
    
    if debug:
        print(f"Monthly Rate of interest {monthly_rate:.2f}%, Numerator of EMI {numerator_emi:.2f}, denominator of emi {denominator_emi:.2f}")
    return emi

emi_loan3=calculate_emi3(210000, 10, 12)
principle=210000
total_payment= emi_loan3*12
interest=total_payment-principle
print(f"EMI will be INR.{emi_loan3:.2f}, Total Payment made by borrower will be {total_payment:.2f}, and interest will be {interest:.2f}")
    
##EMi calculation with total interest and total payment: way 2

def calculate_emi3(principle, rate=8.5, tenure=12, debug=False):
    monthly_rate=rate/1200
    numerator_emi=principle*monthly_rate*(1+monthly_rate)**tenure
    denominator_emi=(1+monthly_rate)**tenure-1
    emi=numerator_emi/denominator_emi
    total_payment= emi*tenure 
    interest=total_payment-principle
    
    if debug:
        print(f"Monthly Rate of interest {monthly_rate:.2f}%, Numerator of EMI {numerator_emi:.2f}, denominator of emi {denominator_emi:.2f}")
    return emi, total_payment, interest

variables_loan3=calculate_emi3(210000, 10, 12)
print(f"EMI will be in INR., Total Payment made by borrower will be in INR. and interest will be in INR in sequence as follows: {variables_loan3}")
    
#def oridinal(n):
#    if n ends with 1 
    
##Trade Analyzer
def review_trade(stock, buy_price, current_price):
    change_prc=(current_price-buy_price)/buy_price*100
    if change_prc>0:
        print(f"{stock}:+{change_prc:.2f}%:Hold")
    else:
        print(f"{stock}: {change_prc:.2f}%: Review")
    #return change_prc
stock1=review_trade("Ather Energy", 750, 730)
#print(stock1)
stock2=review_trade("Suzlon", 90, 34)
stock3=review_trade("SanseraTech", 2300, 2200)
stock4= review_trade("Waree Energy", 2700, 3700)

## BMI Report with Function creation by DEF
def bmi_calculation3(name, weight, height):
    bmi= weight/(height/100)**2
    if bmi<18.5:
        weight_staus = "Underweight"        
    elif bmi <24.9:
        weight_staus = "Normal"
    elif bmi <29.9:
        weight_staus = "Overweight"
    elif bmi <34.9:
        weight_staus = "Obese class 1"
    elif bmi<39.9:
        weight_staus = "Obese class 2"
    else:
        weight_staus = "Severely Overweight"
    print(f"Mr/Mrs/Ms.{name}, Your Weight class falls in {weight_staus} category")
bmi1=bmi_calculation3("Shivani", 45, 155)
bmi2=bmi_calculation3("Vivan",78, 175)
bmi3=bmi_calculation3("Shiv",60,155)
bmi4=bmi_calculation3("VivanBeast",90,175)
bmi5=bmi_calculation3("ShivGoluMolu",85, 155)

##Prefix at number like 1st
def cordinal(n):
    remainder=n % 10
    if n == 1:
        return(f"{n}st")
    elif n==2:
        return(f"{n}nd")
    elif n==3:
        return(f"{n}rd")
    elif n==4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13:
        return(f"{n}th")
    elif remainder == 4 or 5 or 6 or 7 or 8 or 9 or 0:
        return(f"{n}th")
    elif remainder == 1:
        return(f"{n}st")
    elif remainder == 2:
        return(f"{n}nd")
    elif remainder == 3:
        return(f"{n}rd")
    else:
        return(f"{n}th")
number1=cordinal(225)

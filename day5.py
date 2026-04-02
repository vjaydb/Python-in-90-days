#Loan EMI,  Excercise 2, Retaken from day4 for st/nd/rd/th logic

outstanding_loan_amount = 500000
emi = 12500
month= 1
while outstanding_loan_amount >12500:
    outstanding_loan_amount -= emi
    print(f"Outstanding Loan amount is INR.{outstanding_loan_amount} for the end of the month {month}st/nd/rd/th")
    month += 1

## Creating Functions
def greet():
    print(f"Hello Vivan")

greet()

## Use case of Def With Parameteres

def greet(name):
    print(f"Hello {name}")
greet("shabana")
greet("sahiba")

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



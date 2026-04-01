# Trade Info
buy_price =775
current_price = 4503
stoploss = buy_price*.95
target = buy_price*1.25
loss = ((buy_price - current_price)/buy_price)*100
profit = ((current_price -buy_price) / buy_price ) *100 
if current_price  > buy_price and current_price < target:
    print(f"Trade is in profit-Hold it. Profit:{profit:.2f}%")
elif current_price < buy_price and current_price> stoploss:
    print(f"Trade is in Loss, but Stoploss is not triggered, Hold it, Loss{loss:.2f}%")
elif current_price == stoploss:
    print(f"Stoploss has breached stoploss, Exit Immidietely, Loss {loss:.2f}%")
elif current_price == target:
    print(f"Target is hit, Book Profit Immidietely, Profit{profit:.2f}%")
elif current_price > buy_price and current_price > target :
    print(f"Target is breached, Profit is {profit:.2f}%")
elif current_price < buy_price and current_price < stoploss:
    print(f"Stoploss is breached, Exit Immidietely, Loss is {loss:.2f}%")
   
   
    #BMI excercise for if else functionalityn
name = "Vivan"
height = 175
weight = 90 
bmi = (weight/(height/100)**2)
if bmi <= 16:
    print(f"Vivan, You are Severierly Underweight, eat something man")
elif bmi >=16 and bmi <18.4:
    print(f"Vivan, You are underweight, eat something buddy")
elif bmi >=18.4 and bmi <24.9:
    print(f"Vivan, You have normal weight, keep eating quantity same")
elif bmi >=24.9 and bmi < 29.9:
    print(f"Vivan, you are overweight, keep some food for others too, man")
elif bmi >=29.9 and bmi <34.9:
    print(f"Vivan, you fall into obese class 1, you should be reducing diet")
elif bmi >=34.9 and bmi <39.9:
    print(f"Vivan, You fall to obese class 2, Drop a hell of quantity of food from your diet man")
elif bmi >=40:
    print(f"Vivan, you are severely obese, tera kuch nahi ho sakta dost or skip some lunches or dinners")    


##Loan Eligibility Checker
name ="Vivan"
age=60
salary=17000
existing_loan=4
if age>=21 and age <=58 and salary >25000 and existing_loan<2:
    print(f"Mr.{name}, You are eligible to get our LOAN facility")
elif age<21:
    print(f"Mr.{name}, you are not eligible to get our loan facility, Reason for rejection: You are not 21 years old ")
elif age>58:
    print(f"Mr.{name}, you are not eligible to get our loan facility, Reason for rejection: You are older than 58 years")
elif salary<=25000:
    print(f"Mr.{name}, you are not eligible to get our loan facility, Reason for rejection: Your salary is not beyond threshold mark of 25000 ")
elif existing_loan>=2:
    print(f"Mr.{name}, you are not eligible to get our loan facility, Reason for rejection: You are already having 2 or more exisitng Loan")
elif age<=21 or age >=58 & salary <25000 & existing_loan>=2:
    print(f"Mr.{name}, you are not eligible to get our loan facility, Reason for rejection: You are not qualifying in more than one of our criteria such as 1.age might be lower than 21 years or higher than 58 years 2. Salary might be equal or lower than to 25000 3. You might already be having lons more than 1")
    
    ##Improvised version of Loan Eligibility Checker
reason =[]
if age <21:
    reason.append(f"Your Age {age} is below minimum requirement of 21")
if age >58:
    reason.append(f"Your Age {age} is above maximum requirement of 58")
if salary<=25000:
    reason.append(f"Your Salary {salary} is below threshold of 25001")
if existing_loan >1:
    reason.append(f"Your Existing loans count {existing_loan} is above maximum threshold of 1")
if len(reason) == 0:
    print(f"Mr/Mrs/Ms{name}, you are eligible for our loan facility.")
else:
    print(f"Mr/Mrs/Ms {name}, your loan applications has been rejected for {len(reason)}reason(s):")
    for i, reason in enumerate(reason, 1):
        print(f"{i}. {reason}")        
    
    
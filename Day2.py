Name ="Vivan"
Age= 30
City = "Bhavnagar"
Weight= 68
Height= 175
BMI = Weight/ (Height/100)**2
print("My Name is",Name)
print("I am", Age, "years old")
print("I live in", City, "City")
print(f"My Name is {Name} and my age is {Age}")
print(f"I live in {City} city")
#controlling Decimal Point
print(f"My BMI is {BMI:.2f}")
print(f"My BMI is {BMI:.0f}")
print(f"My BMI is {BMI:.4f}")
Salary = 37000
print(f"My Salary is {Salary:,}")
print(f"My Salary is {Salary:,.2f}")
#padding-useful for tables/alignment
print(f"{'Name':<15} {'Age':<5} {'City':<15}") #left Alligned
print (f"{Name:<15} {Age:<5} {City:<15}")
#Stock Sell data excercise
Stock_Name = "Ather Energy" 
buy_price = 618
Sell_price = 720 
Quantity = 501
Total_Profit = (Sell_price - buy_price) * Quantity
print(f"Total Profit:{Total_Profit:,.2f}")
# Trade Report 
trade_1 = "Reliance"
trade_2 = "HPCL"
trade_3 = "Sesagoa"
price_1 = 1500
price_2 = 250
price_3 = 950
quantity_1=10
quantity_2=25
quantity_3=43
print(f"{'SerielNo':<10}{'Stock':<10}{'Price':<10}{'Quantity':<10}{'Date & Time':<15}")
print(f"{1:<10}{trade_1:<10}{price_1:<10}{quantity_1:<10}{"25/03/2026 17:40":<15}")
print(f"{2:<10}{trade_2:<10}{price_2:<10}{quantity_2:<10}{"25/03/2026 17:40":<15}")
print(f"{3:<10}{trade_3:<10}{price_3:<10}{quantity_3:<10}{"25/03/2026 17:40":<15}")
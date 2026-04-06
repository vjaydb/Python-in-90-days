#List beyond Basic
stocks = ["Ather Energy", "Reliance", "Suzlon", "Swiggy","Dmart"]
stocks.append("Aarti Drugs")
stocks.insert(0, "ONGC")
stocks.remove("ONGC")
stocks.pop()
stocks.pop(3)
print("Ather Energy" in stocks)
print(stocks.index("Ather Energy"))
print(stocks.index("Suzlon"))

stocks.sort()
stocks.sort(reverse=True)
sorted_stocks=sorted(stocks)
print(sorted_stocks)
print(len(stocks))
print(stocks[0])
print(stocks[-1])
print(stocks[0:1])

print(stocks)
prices= [211,342,543,232,543,321,324,453,343]
high_prices=[]
for p in prices:
    if p>300:
        high_prices.append(p)
print(high_prices)                  

high_prices1=[p for p in prices if p >300]
print(high_prices1)

#with transformation
double=[p*2 for p in prices]
formatted=[f"INR.{p:,}" for p in prices]
print(formatted)
print(double)

## Database and Analyser
portfolio=[
    {"name":"Ather Energy", "buy_price":618, "current_price":790, "quantity":501},
    {"name":"Reliance", "buy_price":2300, "current_price":2600, "quantity":20},
    {"name":"Suzlon", "buy_price":80, "current_price":40, "quantity":5000},
    {"name":"Waaree Energy", "buy_price":2300, "current_price":3000, "quantity":120},
    ]
for stock in portfolio:
    change_prc= ((stock["current_price"] - stock["buy_price"])/stock["buy_price"])*100
    value= stock["current_price"]*stock["quantity"]
    status= "Hold" if change_prc>0 else "Review"
    print(f"{stock['name']:<15}{change_prc:+.2f}% INR.{value:<7,.0f} {status}")


#excercise 1 Portfolio
portfolio_1 = [
    {"name" : "Sula Wine Yards", "buy_price":180, "current_price":120, "quantity":3500},
    {"name": "Ashok Leyland", "buy_price":1500, "current_price":1410, "quantity":124},
    {"name": "Laxmi Organics", "buy_price":2400, "current_price":1200, "quantity":310},
    {"name": "Abbot India", "buy_price":9500, "current_price":11500, "quantity":45},
    {"name" : "Ahmednagar Forging", "buy_price":145, "current_price":25, "quantity":1254}
]

for stock in portfolio_1:
    change_prc1= ((stock["current_price"]-stock["buy_price"])/(stock["buy_price"]))*100
    value= stock["current_price"]*stock["quantity"]
    status=  "Hold" if change_prc1>0 else "Review"
    print(f"{stock['name']:<20} {change_prc1:+.2f}% INR.{value:<10}{status:<10}")

##Excercise 2 

profitable_trade=[
     stock["name"] for stock in portfolio_1 
     if (stock["current_price"]-stock["buy_price"] ) > 0 
]
print(f"The profitable trade is {profitable_trade}")

stock_list =[
    stock["name"] for stock in portfolio_1]
print(f"Here is the stock list from portfolio: {stock_list}")

current_values_list = [
    stock ["current_price"] * stock["quantity"]  for stock in portfolio_1 
    
]
print(f"The values of different segments of the portfolio are as follows : {current_values_list}")

##Excercise 3

trader1 = {
    "name" : "vivan",
    "portfolio" : {
       "equity" : 145000,
        "gold" : 15000,
        "mutual fund" : 140000,
        "FD" : 200000,
    }
}

portfolio_2 =  trader1["portfolio"]
portfolio_values = sum(portfolio_2.values())
print(f"Total Investment INR.{portfolio_values:,}")

def portfolio_summary(trader1):
    portfolio_3 = trader1["portfolio"]
    portfolio_values_1 = sum(portfolio_3.values())
    equity_prc= (trader1 ["portfolio"] ["equity"]/portfolio_values_1 )*100
    for category, amount in portfolio_3.items():
        share= (amount/portfolio_values_1)*100
        print(f"{category:<15} INR.{amount:,} ({share:.2f}%)")
    if equity_prc >60:
        print(f"Recommendation: Too Agressive")
    elif equity_prc <30:
        print(f"Recommendation: Too Conservative")
    else:
        print(f"Recommendation: Balanced")
portfolio_summary(trader1)
        
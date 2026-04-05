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
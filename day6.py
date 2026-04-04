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
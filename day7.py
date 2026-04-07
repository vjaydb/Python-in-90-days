# Strings
raw_tickers = [
    "  nse:reliance  ",
    "BSE:HPCL ",
    " nse:ather energy ",
    "  BSE:suzlon  ",
    "NSE:INFY  ",
    " bse:WIPRO",
    "  NSE:hal  ",
    "BSE:IRFC ",
]

#print(raw_tickers.strip[])
#print(raw_tickers.upper[])
#for exchange, stock in raw_tickers:
#    print(exchange_list)


# Excersise 2, Write a function def parse_trade(trade_string) that takes a string like "Ather,750,830,50" and returns a dictionary with name, buy_price, current_price, quantity. Handle the case where the string is malformed (wrong number of parts).
trades = [
    "Ather,750,830,50",
    "TataPower,240,265,100",
    "Infosys,1450,1520,10",
    "Reliance,2500,2480,5",
    "InvalidData",
    "HDFC,1600,1700",
    "Zomato,90,110,abc",
    "IRCTC,720,800,20"
]

for stock, buy_price, current_price, quantity in trades:
    print(stock)
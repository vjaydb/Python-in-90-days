#File handling
def parse_trade_info(tradex):
    parts=tradex.split(",")
    if len(parts) !=4:
        return "Invalid Format"
    name, bp, sp, qty = parts
    try:
        return {
        "stock_name" : name,
        "buy_price" : float(bp),
        "sell_price":float(sp),
        "quantity":int(qty)
    }
    except:
        return "Invalid numbers"

with open("text.txt","w") as f:
    f.write("Ather Energy, 609, 810, 501\n")
    f.write("Suzlon, 86, 45,6000\n")
    f.write("Ahmednagar Forging, 150, 20, 500\n")
    f.write("RVNL, 400,300, 5000\n")
    f.write("AshokLeyland, 30, 500, 50000\n")
    f.write("Lodha Devlopers, 500, 1200, 435\n")
    
with open("text.txt", "r") as f:
    for line in f:
        trade=line.strip()
        #print(trade)
        print(parse_trade_info(trade))

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
        trade_info=parse_trade_info(trade)
#Profit Loss counting per trade 
  
        if isinstance(trade_info, dict):
            change_prc=(trade_info["sell_price"]-trade_info["buy_price"])*trade_info["quantity"]
            if change_prc>0:
                msg=(f"Trade in {trade_info["stock_name"]} has occured profit of +INR.{change_prc:,.0f}/-")
            else:
                msg=(f"Trade in {trade_info["stock_name"]} has occured Loss of -INR.{change_prc:,.0f}/-")
            
        else:
            msg(trade_info)
        #print(msg)
         #   with open ("Trade_Report.txt", "w") as f:
         #       f.write(msg + "\n")
         #   with open ("Trade_Report.txt" "r") as f:
         #       f.read()
       # report.write(msg + "\n")
    
##CSV file
import csv
with open("file.csv","w", newline="")as f:
    writer=csv.writer(f)
    writer.writerow(["stock","buy price", "sell price", "quantity"])
    writer.writerow(["Ather Energy", 618, 958, 501])
    writer.writerow(["DLF", 550, 650, 85])

with open("file.csv", "r")as f:
    reader=csv.DictReader(f)
    for row in reader:
        print(row["stock"], row["buy price"])


#File handling
with open("text.txt","w") as f:
    f.write("Ather Energy, 609, 810/n")
    f.write("Suzlon, 86, 45,6000/n")
    f.write("Ahmednagar Forging, 150, 20, 500/n")
    f.write("RVNL, 400,300, 5000/n")
    f.write("AshokLeyland, 30, 500, 50000")
    f.write("Lodha Devlopers, 500, 1200, 435")
    
with open("text.txt", "r") as f:
    for line in f:
        trade=line.strip()
print(trade)
    
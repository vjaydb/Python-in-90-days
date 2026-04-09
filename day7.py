# Strings
#Excercise 1 : formatting from strings of data
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
for trade in raw_tickers:
    #print(trade.strip())
    #print(trade.strip().upper())
    a=(trade.strip().split(":"))
    print(a[:1])
    #b=(a[:1])
    #print(b.strip().upper)
    #for exchange, stock in a:
       # print(exchange.upper().strip())

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

def parse_trade_info(trade):
    parts=trade.split(",")

    if len(parts) !=4:
        return "Invalid Format"
    name, buy, sell, qty = parts 

    try: 
        return {
            "stock_name":name,
            "buy_price": float(buy),
            "sell_price": float(sell),
            "quantity": int(qty),

        }
    except:
        return "Invalid Number"
    
for trade in trades:
    result=parse_trade_info(trade)
    print(result)        
         
#print(trades.strip().split("-"))

#Exercise 3 :Exercise 3: Write a function that takes any text and returns a word frequency count as a dictionary — how many times each word appears. Test it with a paragraph of your choice.

paragraph = ("Why does it matter for India specifically? India has limited uranium resources but one of the world's largest deposits of thorium. Physicist Homi Bhabha designed a three-stage nuclear programme: Stage 1 uses uranium to generate power and produce plutonium; Stage 2 uses plutonium in breeder reactors like the PFBR; Stage 3 will use thorium to generate uranium-233 for long-term, self-sustaining energy. Gulf News The PFBR project was built indigenously with contributions from over 200 Indian industries, including several MSMEs, aligning with the government's Aatmanirbhar Bharat (self-reliance) initiative. Channeliam")

def word_enlister(text):
    text=text.lower()
    for ch in ".,;/?!':[]{}()":
        text=text.replace(ch, " ")
    return text.split()
def word_counter(words):
    freq={}
    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    return freq
word_list=word_enlister(paragraph)
print(word_counter(word_list))

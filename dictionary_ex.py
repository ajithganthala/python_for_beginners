shopping=["Iphone","Samsung","Nokia"]
stock={"Iphone":10,"Samsung":15,"Nokia":12,"Oppo":20}
prices={"Iphone":60000,"Samsung":12000,"Nokia":25000,"Oppo":6000}
Total=0
for i in shopping:
    p=prices[i]
    if stock[i]>0:
        Total=Total+p
        stock[i]=stock[i]-1
print(Total)
print(stock)

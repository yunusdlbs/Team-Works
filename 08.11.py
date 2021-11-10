prices = list(map(float,input("Enter your prices: ").split()))
discount_amount = len(prices)//3
newprices = []
counter = 0
total_price = 0
total_discount = 0
mylist = []
if len(prices) > 2:
    for i in prices:
        total_price += i 
    for i in range(discount_amount):
        total_discount += sorted(prices)[i]
    for i in prices:
        a = float("{:.2f}".format(prices[counter]-(prices[counter]*total_discount/total_price)))
        newprices.append(a)
        counter +=1
    for i in range(discount_amount):
        mylist.append(prices.index(min(prices)))
        prices.remove(min(prices))
    mylist = set(mylist)
    print(f"For {discount_amount} product, there'll be discount.")
    print("For the",mylist,"numbered products,discount'll be applied.")
    print(newprices)
else:
    print(f"Because your product amount is {len(prices)}, no discount'll be applied.")
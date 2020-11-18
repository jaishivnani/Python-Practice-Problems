'''In Python, list is implemented as dynamic array'''

'''Array declaration using lists'''
stock_prices = [298,305,320,301,292,301]

# print(stock_prices[0])

'''on what day was price 301?'''

for i in range(len(stock_prices)):
    if stock_prices[i]==301:
        print(i)


#Time Complexity = O(n)

for price in stock_prices:
    print(price)

#Time Complexity = O(n)

stock_prices.insert(1,305)
print(stock_prices)
stock_prices.remove(305)
print(stock_prices)

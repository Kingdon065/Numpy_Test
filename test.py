from random import random, randint
import csv

def get_price():
    f = random()
    i = randint(330, 365)
    num = i + f
    return f'{num:.2f}'


with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(20):
        temp = [get_price() for i in range(4)]
        max_price = max(temp)
        temp.remove(max_price)
        min_price = min(temp)
        temp.remove(min_price)
        
        prices = []
        index = randint(0, 1)
        prices.append(temp[index])
        prices.append(max_price)
        prices.append(min_price)
        if index:
            prices.append(temp[0])
        else:
            prices.append(temp[1])
        print(prices)
        
        row = ['AAPL', f'{8+i:02}-01-2011', ' '] + prices
        row.append(randint(20000000, 25000000))
        writer.writerow(row)

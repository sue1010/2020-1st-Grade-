prices = [90,86,75,50,98,64]
maximum = prices[0]
i = 1
while i < len(prices):
    if prices[i] > maximum:
        maximum = prices[i]
    else:
        i += 1
print(maximum)

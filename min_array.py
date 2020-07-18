prices = [90,86,75,50,98,64]
minimum = prices[0]
i = 1
while i < len(prices):
    if prices[i] < minimum:
        minimum = prices[i]
    else:
        i += 1
print(minimum)

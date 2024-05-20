# Input: prices = [7, 5, 3, 6, 4,1]
# Output: 5


# prices = [7,6,4,3,1]
prices = [1,2,3,4,5]
# min_price = prices[0]
# max_price = prices[1]

# for i in range(len(prices)):
#     if prices[i] < min_price:
#         min_price=prices[i]
# print(min_price)

# # max_price = min_price


# for j in range(min_price , len(prices)):
#     if prices[j] > max_price:
#         max_price = prices[j]
# print(max_price)

# print(max_price - min_price)






# prices = [99,7,63,3]
# minbuy = float('inf')
minbuy = prices[0]
maxsell=0

for i in range (len(prices)):
            
            minbuy=min(minbuy,prices[i])
            maxsell=max(maxsell,prices[i]-minbuy)
print(maxsell)
    

# def maxProfits( prices):
#     profit = 0
#     for i in range(1, len(prices)):
#         profit += max(prices[i]-prices[i-1], 0)
#     return profit

#***************************
# best time to buy and sell stocks 
# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

def maxProfit( prices) -> int:
    return sum(max(prices[i]-prices[i-1], 0) for i in range(1,len(prices)))



print(maxProfit([7,1,5,3,6,4]))
 
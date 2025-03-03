"""
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # given int array prices
        # choose day to buy
        # choose different day to sell

        # return max profit
        # if no profit, return 0

        lowest_price = 1000
        max_profit = 0

        # iterate through prices
        for price in prices:
            # check if current price is lower than our big number
            # updated lowest_price = our buy day
            if price < lowest_price:
                lowest_price = price
            # for each price, we calculate the profit with our lowest
            profit = price - lowest_price

            # update max_profit when biggest
            if profit > max_profit:
                max_profit = profit

        return max_profit


# two pointers methodclass Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initiate two pointers, one will determine lowest day and then
        # move right to get highest day (buy and sell)
        left = 0
        right = 1

        # initiate profit
        max_profit = 0
        
        # iterate through while right is still in bounds of arr
        while right < len(prices):
            # make sure left stays less than right
            if prices[left] < prices[right]:
                # formula for finding current profit
                profit = prices[right] - prices[left]

                # update maxprofit if new max profit found
                max_profit = max(max_profit, profit)
            
        # if no max profit found, update pointers
            else:
                # means we found a lower buy price
                left = right
            right += 1
        return max_profit


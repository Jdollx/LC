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
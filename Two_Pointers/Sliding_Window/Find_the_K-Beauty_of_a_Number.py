"""
The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that meet the following conditions:

It has a length of k.
It is a divisor of num.
Given integers num and k, return the k-beauty of num.

Note:

Leading zeros are allowed.
0 is not a divisor of any value.
A substring is a contiguous sequence of characters in a string.
"""

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        # k beauty -
        # length = k
        #  num \ k-beauty 
        # leading 0s allowed
        # 0 is not a divisor

        # so i need to move length of k across the num and see if the contents of
        # k can divide num

        # convert num to string
        n = str(num)

        # initiate count
        count = 0

        # iterate from the start to the end, allowing for k elements in final
        for i in range(len(n) - k + 1):
            # for each window of k, see if it is divisible and not 0
            k_int = int(n[i:i+k])
            if k_int != 0 and num % k_int == 0:
                # if its divisible, its good
                count += 1
        return count



        

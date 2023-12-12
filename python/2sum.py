
import pandas as pd
from pandas import DataFrame as df

'''

MOST POPULAR LEETCODE PROBLEM
2SUM

given an array of ints, return indices of 2 numbers that add to a number

theres always 1 solution
check every combination of 2 values and see if they sum to the target

brute force algorithm
time complexity O(n^2)
n*n

implement a hashmap or a dictionary
assigning the difference of target - index to the index


'''

class Solution:
    def two_sum(self, input:list[int], target:int) -> list[int]:
        prevMap = df({})
        
        for i, n in enumerate(input):
            #NOTE: enumerate returns the val and its index
            # i is index, n is the number in that index
            # if only 1 arg itll return a list of both
            diff = target- n
            if diff in prevMap.columns: #if the difference exists in columns
                return [prevMap.columns.get_loc(diff), i]
            prevMap[n] = i

            

print(Solution.two_sum(Solution, [1,4,7,2], 6))





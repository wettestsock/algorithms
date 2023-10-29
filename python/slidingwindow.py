'''
SLIDING WINDOW TECHNIQUE
useful for when theres overlapping subarrays 

start with initial subarray, 
sum it up

move up a value
substart previous and add the last value in subarray

1st sum = sum
2nd sum = sum + element that went in - element that went out

    
'''


class Solution:
    def fixed_sliding_window(self, arr:list[int], k:int)-> list[int]:
        curr = sum(arr[:k])
        output = [curr]

        for i in range(1, len(arr)-k+1):
            curr = curr - arr[i-1]
            curr = curr + arr[i+k-1]
            output.append(curr)
        
        #returns the sum of all subarrays given the length of k
        return output



print(Solution.fixed_sliding_window(Solution, [3,5,3,4,5,2], 2))


# O(n) CONSTANT TIMEj
def slide_window(arr:list[int], k:int) -> list[int]:
    curr = sum(arr[:k]) # first sum
    out = [curr] #puts the first sum in the output list

    for i in range(len(arr)-k):
        # i until start index of the last group (to not overflow)

        #basically calculates the sum for the next window (starting from after current)
        curr -= arr[i]
        curr += arr[i+k]
        out.append(curr)
    return out

print(slide_window([3,5,3,4,5,2], 2))
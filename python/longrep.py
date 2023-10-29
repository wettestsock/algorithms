

'''
LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
substring has to be continguous


basically have 1 substr, 
if theres a duplicate remove it and all chars on the left from the substr

make the substr longer

SLIDING WINDOW TECHNIQUE <- very common
O(n) space time complexity
O(n) memory complexity

maintain longest substring

    
'''

class Solution:
    def sub_str_len(self, s:str) -> int:
        char_set = set()
        result = 0


        #sliding window - > left and right ptr
        left = 0 # index of leftmox char, starts at 0 and increases by 1
        for right in range(len(s)):
            while s[right] in char_set: #while the duplicate is within the character set
                char_set.remove(s[left]) # removes every left and duplicate
                left +=1
            char_set.add(s[right])
            result = max(result, right-left +1) #checks if the current is bigger than the result
            # if so, assigns it to result
        return result


print(Solution.sub_str_len(Solution, 'abcdabcdc'))

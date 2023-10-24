

'''
VALID PALINDROME 

given a string, determine if its a palidrome
only alphanumeric and ignoring cases


take values left to right and right to left and evaluate if they're equal
121 % 10 = 1
121 /100 = 1 True, 1 = 1

-----------

division (/) moves zeros amount to the right (/10 moves to the right once)
modulus (%) removes every number after the given zeros amount (%10 removes everything after the ones place)

ex:
int(253 / 100) = 2
253 % 100 = 53

-----------

# to find 2 
121 % 100 = 21
21 / 10 = 2 (rounded down)

'''


class solution:
    def isPalindrome(self, x:int) -> bool:
        return False



print(solution.isPalindrome(solution, 121))
print(solution.isPalindrome(solution, -121))
print(solution.isPalindrome(solution, 10))
print(solution.isPalindrome(solution, 0))
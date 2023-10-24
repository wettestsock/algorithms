

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
        if x<0: return False #exception
        
        divider = 1 #initially 1, value to divide by
        while x >= divider*10: #gets the divider to the biggest possible divider given the num
            divider *= 10
        
        while x: #while x is not 0 
            right = x%10
            left = x // divider  #int division divide
            
            if left != right: return False
            
            x = (x%divider) // 10 
            '''
            x%divider chops off the left
            ex: 
            1243 % 1000 = 243 , chopped off 1
            
            243 // 10 = 24, chopped off 3
            
            x is 24 for next iteration
            
            24 % 10 = 4
            
            4 // 10 = 0
            algorithm ends 
            
            '''
            
            divider /= 100
            
        return True



print(solution.isPalindrome(solution, 121))
print(solution.isPalindrome(solution, -121))
print(solution.isPalindrome(solution, 10))
print(solution.isPalindrome(solution, 0))
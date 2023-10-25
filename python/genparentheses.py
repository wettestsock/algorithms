
'''
GENERATE PARENTHESES 
generates every combination

given n pairs of parentheses,
returns a list of strings with every combination of parentheses


need n open and n closing parentheses
can start with open parenthese but NOT with closed 
can start with multiple parentheses

open and close count
close count cant be bigger than open count
only allowed closing parenthese when open is bigger than close count

when both open and close are n then it's valid

always start with open parenthese
->              '('
->          '((' or '()'
->      '(((' '(()'     or '()(' (open > close = false, have to put open)
-> '((()' or '(()(' '(())' or etc/////



'''

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
       #only add open p if open < n 
        # only add close p if closed < open
        # valid IIF open == closed == n 

        # doing this recursively
        stack = []
        output = []
        
        def backtrack(openN, closeN):
            if openN == closeN == n: #occurs for each string
                output.append(''.join(stack)) # ''.join() makes a list into a string
                return
            
            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closeN)
                stack.pop()
            
            if closeN < openN:
                stack.append(')')
                backtrack(openN, closeN +1)
                stack.pop()
        
        backtrack(0,0)
        return output
            
def other_sol(n:int) -> list[str]:
    output = []
    
    def recurs(openN, closeN, temp=''): #temp is output string to be put into output
        if not openN and not closeN: #if both are 0, then appends the string to output
            output.append(temp) 
        
        if openN > 0:
            recurs(openN -1, closeN, temp+'(')
        if openN < closeN:
            recurs(openN, closeN-1, temp+')')
    
    recurs(n,n)
    return output
        

print(Solution.generateParenthesis(Solution, 3))
print(Solution.generateParenthesis(Solution, 2))
print(Solution.generateParenthesis(Solution, 1))
print(other_sol(3))
print(other_sol(2))
print(other_sol(1))

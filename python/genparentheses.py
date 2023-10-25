
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
                output.append(''.join(stack))
                
            



print(Solution.generateParenthesis(Solution, 3))
print(Solution.generateParenthesis(Solution, 2))
print(Solution.generateParenthesis(Solution, 1))
print(Solution.generateParenthesis(Solution, 10))
print(Solution.generateParenthesis(Solution, 22))
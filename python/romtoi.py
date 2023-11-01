
'''
ROMAN TO INTEGER

roman numerals normally written left to right, largest to smallest order
7 symbols - I V X L C D M

if adding smaller value after the larger -
then substracting it
cant put multiple smaller values before larger


ex IM <- -1 and 1000 = 999


ex 2 :

CMXCVIII

is there a bigger value after it? then it's negative
C < M then -100
M > X then +1000
X < C then -10
C > V then +100
V > I then +5
I = I then +1
I = I then +1
I = I then +1

 = 998

'''
#if i+1 < boundary    #checks if there's a num after the current

class Solution:
    def romanToInt(self, s:str) -> int:
        # next is bigger then add
        # next is smaller than substract
        ROMAN = {'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        output = 0
        for i in range(len(s)):
            if i + 1 < len(s) and ROMAN[s[i]] < ROMAN[s[i+1]]: 
                output -= ROMAN[s[i]] # if next is bigger and if there's even a num after the num
            else:
                output += ROMAN[s[i]]
        return output
print(Solution.romanToInt(Solution, 'CMXCVIII'))
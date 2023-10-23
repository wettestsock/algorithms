


'''
ADD 2 NUMS

2 NON EMPTY LINKED LISTS
represent non negative ints
stored in REVERSE ORDER, each node with 1 digit
add the nums and return sum as linked list


imagine adding numbers manually.

    342
   +465
   ----
    807  # 4 + 6 = 10, 0 stays and 1 gets carried over to the next numbers
'''

class node:  #linked list in python
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




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
    
    
#note: != and is not are not same
# != compares values while is not checks for pointers
def list_print(list_head: node):
    c = list_head
    while (c.next is not None):
        print(c.val, '-> ', end ='')
        c = c.next 
    print(c.val, '\n')

d = node(4)       
c = node(2, d)       
b = node(32, c)       
a = node(4, b)        

list_print(a)

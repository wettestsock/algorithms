


'''
ADD 2 NUMS

2 NON EMPTY LINKED LISTS
represent non negative ints
stored in REVERSE ORDER, each node with 1 digit
add the nums and return sum as linked list

reverse order makes it easier

imagine adding numbers manually.

    342
   +465
   ----
    807  # 4 + 6 = 10, 0 stays and 1 gets carried over to the next numbers

edge cases: 
if one num is bigger than the other (ex 53 and 253), assume the missing num is a zero when adding

if both nums are same but the carry carries over both of them,
make sure to include that at the end

'''

class node:  #linked list in python
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def print(self):
        c = self
        while (c.next is not None):
            print(c.val, '<- ', end ='')
            c = c.next 
        print(c.val, '\n')
    
    
#note: != and is not are not same
# != compares values while is not checks for pointers

    


class solution:
    def add_two_nums(self, l1: node, l2: node) -> node:
        dummy = node() # to not deal with edge cases
        cur = dummy # position to insert the new node into

        carry = 0 # carry over num
        #carries over to the next iteration


        #iterate while either has a digit
        while l1 or l2 or carry: #while either is non-null
            # will iterate for the carry edge case

            val1 = l1.val if l1 else 0 # if its null then set to 0
            val2 = l2.val if l2 else 0
        
            #new digit
            val = val1+val2+carry # finds the new value

            #get the carry value (tenth location num)
            carry = val // 10 #double divide is floor divide 

            #value after the carry (ones location num)
            val = val %10

            #makes next node with the value
            cur.next = node(val)

            #iterates to the next nodes
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
    

        return dummy.next


a3 = node(9)       
a2 = node(2, a3)       
a1 = node(4, a2)  

b3 = node(4)       
b2 = node(6, b3)       
b1 = node(2, b2)  

a1.print()
b1.print()

solution.add_two_nums(solution, a1, b1).print()





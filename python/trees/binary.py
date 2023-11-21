import numpy as npy 
import pandas as pd

'''
INTRO TO BINARY TREES 
TODO: implement in c / cpp

always a root node 
every left node gets smaller whereas every right node gets bigger than their parent


makes sure the bianry tree is sorted
left is smaller
right is bigger

BINARY SEARCH TREE 
TODO: implement a binary search tree (BST algorithm)


4 ways to traverse a binary tree:

1- depth first aproach of DFS
    a. inorder traversal
    b. preorder traversal
    c. postorder traversal
2- level order traversal or breadth first search of BFS
3- boundary traversal
4- diagonal traversal
'''

# node itself
class node:
    #init the head node
    def __init__(self, data):

        self.data = None
        self.left = None  # default
        self.right = None # default none
        #basically linked list
        if isinstance(data,str): # if the data is a string
            for c in data:
                self.insert(c)
        else:
            self.data = data # must have data

    def insert(self,data):
        if(self.data is None): # if node itself is null
            self.data = data 
            
        else:
            if data < self.data: #inser to the left
                if self.left is None: # if theres nothing then put it
                    self.left = node(data) #new node using the data
                    #NOTE: tutorial implements as if and else statements
                else:
                    #if theres something there then recursively insert it there
                    self.left.insert(data) #gonna keep recursing until the condition becomes false

            elif data > self.data:
                # same as left but to right
                if self.right is None:
                    self.right = node(data)
                
                self.right.insert(data) #recursiveee

        

# printing all nodes InOrder

'''
lets say a tree like this

        b (root)
       / \
(left)a   c  (right)
       \
        e

starts at root, prints left, then prints the current, then prints the right
in ex - prints a e b c 


'''
def in_order_print(curr:node):
    if curr is None:
        return

    in_order_print(curr.left)
    print(curr.data, end = ' ')
    in_order_print(curr.right)

# makes sure that the python file is NOT imported
if __name__ == '__main__':

    #can do each individual
    #but implemented pseudo constructor overloading
    root = node('gcbaedfihjk')

    in_order_print(root)
import numpy as npy 
import pandas as pd

'''
INTRO TO BINARY TREES 
TODO: implement in c / cpp

always a root node 
every left node gets smaller whereas every right node gets bigger than their parent

left is smaller
right is bigger

BINARY SEARCH TREE 
TODO: implement a binary search tree (BST algorithm)
'''

# node itself
class node:
    #init the head node
    def __init__(self, data):
        self.data = data # must have data
        self.left = None  # default
        self.right = None # default none
        #basically linked list

    def insert(self,data):
        if(self.data is None): # if node itself is null
            self.data = data 
            return
        
        #insert to the left 
        if data < self.data:
            if self.left is not None: # if theres nothing then put it
                #if theres something there then recursively insert it there
                self.left.insert(data) #gonna keep recursing until the condition becomes false

            self.left = node(data) #new node using the data

            #NOTE: tutorial implements as if and else statements
            
                    


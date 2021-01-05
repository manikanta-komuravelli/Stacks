# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 06:36:07 2021

@author: manik
"""


class Node:
    
    def __init__(self,value):
        self.value= value
        self.next= None
        
class Stack:
    
    def __init__(self):
        self.head= None
        self.num_elements= 0
        
    def push(self,value):
        new_node= Node(value)
        new_node.next= self.head
        self.head= new_node
        self.num_elements+= 1
        
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0
    
    def pop(self):
        old_head= self.head
        new_node= self.head.next
        
        self.head= new_node
        
        self.num_elements-= 1
        return old_head.value

sta= Stack()
#print(sta.head.value)
sta.push(1)
print(sta.head.value)
sta.push(2)
print(sta.head.value)
print(sta.size())
print(sta.is_empty())
print(sta.pop().value)
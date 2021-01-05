# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 07:22:14 2021

@author: manik
"""


class Stack:
    
    def __init__(self):
        self.arr=[]
        self.new_elements=0
        
    def push(self,value):
        self.arr.append(value)
        self.new_elements+=1
    
    def pop(self):
        
        if self.arr:
            self.new_elements-= 1
            return self.arr.pop()
        else:
            return None
        
    def size(self):
        return self.num_elements
    
    
MyStack = Stack()

MyStack.push("Web Page 1")
MyStack.push("Web Page 2")
MyStack.push("Web Page 3")

print (MyStack.arr)
        
MyStack.pop()
MyStack.pop()

print ("Pass" if (MyStack.arr[0] == 'Web Page 1') else "Fail")            

MyStack.pop()

print ("Pass" if (MyStack.pop() == None) else "Fail")
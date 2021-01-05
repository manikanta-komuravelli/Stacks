# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 07:31:14 2021

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
        return len(self.arr)
    

def equation_checker(equation):
    
    stack= Stack()
    
    for char in equation:
        if char == '(':
            stack.push('(')
        elif char == ')':
            val= stack.pop()
            if val == None:
                return False
    if stack.size()== 0:
        return True
    else:
        return False
    
    
print ("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
print ("Pass" if not (equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 06:07:36 2021

@author: manik
"""


class stack:
    def __init__(self,init_size=10):
        self.arr= [0 for _ in range(init_size)]
        self.next_index=0
        self.num_elements = 0
        
    def push(self,data):
        
        if self.next_index == len(self.arr):
            print("Stack is full, hold on creating some space for you")
            self._handle_stack_capacity_full()
            
        self.arr[self.next_index]= data
        self.next_index+= 1
        self.num_elements+= 1
        
    def pop(self):
        
        if self.is_empty():
            self.next_index= 0
            return None
        self.next_index-= 1
        self.num_elements-= 1
        return self.arr[self.next_index]
    
    def size(self):
        #return len(self.arr)
        size_val= 0
        for i in range(len(self.arr)):
            if self.arr[i] !=0:
                size_val+= 1
        return size_val
    
    def is_empty(self):
        ret_val=False
        
        ret_val= all(val==0 for val in self.arr)
        
        return ret_val
    
    def _handle_stack_capacity_full(self):
        old_arr= self.arr
        self.arr=[0 for _ in range(2*(len(old_arr)))]
        
        for i, val in enumerate(old_arr):
            self.arr[i]= val


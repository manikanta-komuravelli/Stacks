# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 22:07:16 2021

@author: manik
"""


class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0



def count_bracket_reversals(input):
    
    if len(input)%2 !=0:
        return -1
    
    my_stack= Stack()
    count= 0
    for val in input:
        if my_stack.is_empty():
            my_stack.push(val)
        else:
            top= my_stack.top()
            if top != val:
                if val == '}':
                    my_stack.pop()
                    continue
            my_stack.push(val)
    
    while not my_stack.is_empty():
        first= my_stack.pop()
        second= my_stack.pop()
        if first == '{' and second == '{':
            count+= 1
        elif first == '}' and second == '{':
            count+= 2
        elif first == '}' and second == '}':
            count+= 1
    
    return count
        


    

input_string= "}}}}"

print(count_bracket_reversals(input_string))
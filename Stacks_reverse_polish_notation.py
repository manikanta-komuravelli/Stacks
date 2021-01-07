# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 21:28:31 2021

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


def polish_math(input_list):
    
    my_stack= Stack()
    for val in input_list:
        if val == "*":
            second_val= my_stack.pop()
            first_val= my_stack.pop()
            multiplication= second_val*first_val
            my_stack.push(multiplication)
        elif val == "/":
            second_val= my_stack.pop()
            first_val= my_stack.pop()
            division= int(first_val/second_val)
            my_stack.push(division)
        elif val == "+":
            second_val= my_stack.pop()
            first_val= my_stack.pop()
            addition= second_val+first_val
            my_stack.push(addition)
        elif val == "-":
            second_val= my_stack.pop()
            first_val= my_stack.pop()
            subtraction= first_val-second_val
            my_stack.push(subtraction)
        else:
            my_stack.push(int(val))
    return my_stack.pop()




input_list= ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

print(polish_math(input_list))

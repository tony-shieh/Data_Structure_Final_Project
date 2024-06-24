# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 16:32:10 2022

@author: User
"""
from tree import Dish

class Node:
    def __init__(self):
        self.meal = None
        self.quantity = 0
        self.link = None
    

class LinkedList:
    
    def __init__(self):
        self.head = Node()
        self.last = self.head
    
    def insert(self, meal: Dish, num: int):
        target = self.search(meal.name)
        
        if target == None:
            new = Node()
            new.meal = meal
            new.quantity = num
        
            self.last.link = new
            self.last = new
        else:
            target.quantity += num
        print()
        print("  Order successfully!")
    
    @staticmethod
    def display(head: Node):
        
        ptr = head.link
        total = 0 #to store total price of the bill
        
        if ptr == None:
            print("  You haven't ordered yet.")
            return
        while ptr != None:
            p = ptr.meal.price*ptr.quantity
            total += p
            print("Dish Name: %-15s Quantity: %-3d Price: %-3d" %(ptr.meal.name, ptr.quantity, p))
            ptr = ptr.link
        print()
        print("%-18s: %-3d"%("Total Price", total))
    
    #delete all meal of that item(quantity to 0)
    def delete(self, dish_name: str):
        target = self.search(dish_name)
        ptr = self.head.link
        prev = self.head
        
        if target == None:
            print("  You don't order this meal.")
        else:
            while ptr != None and ptr.meal.name != dish_name:
                prev = ptr
                ptr = ptr.link
            prev.link = ptr.link
            ptr = None
            print("  Delete successfully")
            
    
    #modify the quantity of that item
    def modify(self, dish_name: str, quantity: int):
        target = self.search(dish_name)
        
        if target == None:
            print("  You don't order this meal.")
        else:
            target.quantity = quantity
            print("  Modify successfully!")
    
    def search(self, dish_name: str) -> Node:
        ptr = self.head.link
        
        while ptr != None:
            if ptr.meal.name == dish_name:
                return ptr
            ptr = ptr.link
        return None

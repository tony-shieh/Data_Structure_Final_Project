# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 21:53:31 2022

@author: User
"""
from LinkedList import LinkedList

class Restaurant():
    def __init__(self):
        self.order_queue = []
        self.ptr = 0
        self.profit = 0
    
    address = 1
    
    def build_order(self, bill):
        self.order_queue.append(bill)
        print()
        print("  You ordered successfully!")
        print()
        print("****************Here's your order****************")
        print()
        LinkedList.display(bill.order_data.head)
        print()
        print("*************************************************")
    
    def cancel_order(self, name, phone, address):
        for i in self.order_queue:
            if i.c_name == name and i.phone == phone and i.address == address:
                self.order_queue.remove(i)
                print()
                print("  Your order has been canceled.")
                return
        else:
            print()
            print("  Wrong infomation for the order!")
    
    def check_order(self, name, phone, address):
        for i in self.order_queue:
            if i.c_name == name and i.phone == phone and i.address == address:
                i.check_order(address)
                return
        else:
            print()
            print(" Wrong infomation for the order!")
    
    def order_out(self):
        if self.ptr >= len(self.order_queue):
            print("  There's no order to deal with.")
        else:
            target = self.order_queue[self.ptr]
            target.order_status = True
            self.profit += target.total_price()
            self.ptr += 1
            print("  " + target.c_name + "'s Order has been dished out!")
    
    #to check if there are still order to deal with
    def is_no_order(self):
        if self.ptr >= len(self.order_queue):
            return True
        return False
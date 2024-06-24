# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 15:43:36 2022

@author: User
"""
import tree
from LinkedList import LinkedList
from Customer import Bill
from restaurant import Restaurant

r = Restaurant()

def order():
    global r
    
    print("What do you want to eat today?")
    order = LinkedList()
    done = False
    
    while done == False:
        meal = input("> Input your order(one meal at one time): ")
        print()
        num = 0
            
        target = tree.search(meal)
        if  target != None:
            try:
                num = int(input("> How many of %s do you want to eat: "%meal))
                order.insert(target, num)
            except ValueError:
                print()
                print("  Invalid quantity.")
        else:
            print("  The meal you ordered is not in the menu.")
        
        #to check if the customer's order is done
        while True:
            choose = input("> Do you want to finish your order('Y' for yes, 'M' for modify, others for keep ordering): ")
            if choose.upper() == "Y": #upper() to capital the cnhoice, which is covience to customers
                print()
                done = True
                break
            elif choose.upper == "M":
                modify(order)
            else:
                break
    
    name, phone, address = Bill.cusInfo()
    cus = Bill(name, phone, address, order)
    r.build_order(cus)

def modify(order):
    name = input("> Please enter the dish name to modify: ")
    print()
    node = order.search(name)
    if node == None:
        print("  You didn't order this meal.")
    else:
        new_quantity = None
        
        print("  The current quantity: %d" %node.quantity)
        while new_quantity == None:
            try:
                new_quantity = int(input("> Plaese enter the new quantity: "))
            except ValueError:
                print()
                print("  invalid input for the price!")
                print("  Please re-enter.")
                print()
        
        if new_quantity == 0:
            order.delete(name)
        else:
            node.quantity = new_quantity
        print()
        print("  The quantity of Dish %s has been modified to %d" %(name, node.quantity))
    print()

def cancel():
    name, phone, address = Bill.cusInfo()
    r.cancel_order(name, phone, address)
    
    
def check():
    name, phone, address = Bill.cusInfo()
    r.check_order(name, phone, address)

def main():
    option = 0
    
    tree.main()
    
    while True:
        
        print()
        print("--------------Welcome--------------")
        print("1. Order")
        print("2. See Menu")
        print("3. Cancel Order")
        print("4. Check Order")
        print("5. Order Out(for restaurant)")
        print("6. Exit")
        print("-----------------------------------")
        print()
        
        try:
            option = int(input("> Please choose an option choice: "))
        except ValueError:
            print()
            print("  This is not a correct number \n")
            print("  Please try again")
            continue
            
        print()
            
        if option == 1:
            order()
        elif option == 2:
            tree.display()
        elif option == 3:
            cancel()
        elif option == 4:
            check()
        elif option == 5:
            r.order_out()
        elif option == 6:
            if r.is_no_order() == True:
                break
            else:
                print("  There are still orders to deal with.")
        elif option == 0:
            continue
        else:
            print("  Wrong option \n")
            print("  Please try again")
    
    print()
    print()
    print()
    print("**********Here's the total profit today**********")
    print()
    print("Total Profit: ", r.profit)
    print()
    print("*************************************************")

if __name__ == "__main__":
    main()
    
from LinkedList import LinkedList
import shortest_path
import re

class Bill:
    def __init__(self, name, phone, address: int, order_data):
        self.c_name = name
        self.phone = phone
        self.address = address
        self.order_data = order_data
        self.order_status = False
        
    @staticmethod
    def cusInfo():#enter customer data and return
        print("======== customer data ========")
        c_name, phone, address = None, None, None
        
        try:
            c_name = input("> Please enter your name: ")
            phone = input("> Please enter your phone number(09xx-xxxxxx): ")
            address = int(input("> Please enter your address:(number: 2-7) "))
            print()
       
        except ValueError:
            print("  Wrong address.")   
        except Exception:
            print("  Wrong enter.")
        
        #to check the format of customer's info
        if re.search("[0-9]{4}-[0-9]{6}", phone) and len(phone) == 11 and address > 1 and address <= 7:
            pass
        elif address <= 1 or address > 7:
            print("  Wrong address.")
            print()
            return Bill.cusInfo()
        else:
            print("  Wrong phone number.")
            print()
            return Bill.cusInfo()
            
        return c_name, phone, address
        
    def check_order(self, address):
            
        print("****************Here's your order****************")
        LinkedList.display(self.order_data.head)
        print()
        if self.order_status == True:
            print("  your order has been dished out.")
            shortest_path.main(address)
        else:
            print("  your order is prepared now.")
        print("*************************************************")
    
    def total_price(self):
        head = self.order_data.head.link
        total = 0
        
        while head != None:
            total += head.quantity*head.meal.price    
            head = head.link
        return total
    
    def cal_dis(self):
        shortest_path.main()
            
    
    
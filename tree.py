class Dish:
    def __init__(self):
        self.name = ""
        self.price = 0
        self.llink = None
        self.rlink = None
        
root = None

def insert():#enter dish name and price
    print("======== Insert ========")
    
    name = input("> Plaese enter a dish name: ")
    price = None
    
    while price == None:
        try:
            price = int(input("> Plaese enter the price of the dish: "))
        except ValueError:
            print()
            print("  invalid input for the price!")
            print("  Please re-enter.")
            print()
        
    access(name, price)
    
    print("========================")    
    
def access(name, price):
    global root
    node = None
    prev = None
    
    if search(name) != None:#dish name cannot be the same
        print("  Dish %s has been existed" %name)
        return
    
    ptr = Dish()
    ptr.name = name
    ptr.price = price
    
    if root == None:
        root = ptr
    else:
        node = root
        while node != None:
            prev = node
            if ptr.name < node.name:
                node = node.llink
            else:
                node = node.rlink
        if ptr.name < prev.name:
            prev.llink = ptr
        else:
            prev.rlink = ptr        
    print()
    print("  Insert successfully! \n")
    
#use dish name to store the menu in the tree
def search(target):
    global root
    
    node = root
    while node != None:
        if target == node.name:
            return node
        elif target < node.name:
            node = node.llink
        else:
            node = node.rlink
    return node

#print menu
def display():
    global root
    
    if root == None:
        print("  no dish record")
        return
    print("============= Menu =============")
    inorder(root)
    print("============= Menu =============")
    print()
 
#以中序法輸出，採遞迴方式
def inorder(node):
        if node != None:
            inorder(node.llink)
            print("Dish Name: %-15s Price: %-3d" %(node.name, node.price))
            inorder(node.rlink)
            
def delete():
    global root            
    
    print("======== Delelte ========")
    if root == None:
        print()
        print("  There's no dish can be deleted.")
        return
    else:
        name = input("> Please enter a dish name to delete: ")
        removing(name)
        
    
    print("=========================")
    print()
        
def removing(name):
    global root
    
    del_node = search(name)
    if del_node == None:
        print()
        print("  Dish %s is not found" %name)
        print()
        return
    
    if del_node.llink != None or del_node.rlink != None:
        del_node = replace(del_node)
    else:
        if del_node == root:
            root = None
        else:
            connect(del_node, "n")
    del_node = None
    print()
    print("  Dish %s has been deleted" %name)
    print()
        
def replace(node):
    re_node = None
    re_node = search_re_r(node.rlink)
    if re_node == None:
        re_node = search_re_l(node.llink)
    if re_node.rlink != None:
        connect(re_node, "r")
    elif re_node.llink != None:
        connect(re_node, "l")
    else:
        connect(re_node,"n")
    
    node.name = re_node.name
    node.price = re_node.price
    return re_node
    
def connect(node, link):
    parent = search_p(node)   
    if node.name < parent.name:
        if link == "r":
            parent.llink = node.rlink
        elif link == "l":
            parent.llink = node.llink
        else:
            parent.llink = None            
    else: 
        if link == "r":
            parent.rlink = node.rlink
        elif link == "l":
            parent.rlink = node.llink
        else:
            parent.rlink = None
            
def search_p(node):
    global root
    parent = root
    while parent != None:
        if node.name < parent.name:
          if node.name == parent.llink.name:
              return parent
          else:
              parent = parent.llink
        else:
            if node.name == parent.rlink.name:
                return parent
            else:
                parent = parent.rlink
    return None     
                
def search_re_r(node):
    re_node = node
    while re_node != None and re_node.llink != None:
        re_node = re_node.llink
    return re_node

def search_re_l(node):
    re_node = node    
    while re_node != None and re_node.rlink != None:
        re_node = re_node.rlink
    return re_node

def modify():
    global root

    print("======== Modify ========")
    if root == None:
        print()
        print("  There's no dish can be modified.")
        return
    
    name = input("> Please enter the dish name to modify: ")
    print()
    node = search(name)
    if node == None:
        print("  Dish %s is not found" %name)
    else:
        new_price = None
        
        print("  The current price: %d" %node.price)
        while new_price == None:
            try:
                new_price = int(input("> Plaese enter the new price: "))
            except ValueError:
                print()
                print("  invalid input for the price!")
                print("  Please re-enter.")
                print()
                
        node.price = new_price
        print()
        print("  The price of Dish %s has been modified to %d" %(name, node.price))
    print()
    print("========================")
    print()
        

def main():
    option = 0
    
    while True:
        print()
        print("**********ACCESSING MENU**********")
        print("1. Insert")
        print("2. Display")
        print("3. Delete")
        print("4. Modify")
        print("5. Finish the menu setting")
        #print("5. Exit")
        print("**********************************")
        print()
        
        try:
            option = int(input("> Please choose an option choice: "))
        except ValueError:
            print()
            print("  This is not a correct number \n")
            print("  Please try again")
            
        print()
            
        if option == 1:
            insert()
        elif option == 2:
            display()
        elif option == 3:
            delete()
        elif option == 4:
            modify()
        elif option == 5:
            break
            #sys.exit(0)
        elif option == 0:
            continue
        else:
            print("  wrong option \n")
            print("  please try again")

if __name__ == "__main__":
    main()
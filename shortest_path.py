import sys
from restaurant import Restaurant

MAX = 100
visited = 1
novisited = 0
infinite = 1073741823 #python's largest number

A = [[0]*(MAX+1) for row in range(MAX+1)] #adjacency matrix
D = [0] *(MAX+1) #儲存某起始點到i點的最短路徑
S = [0] *(MAX+1) #紀錄頂點是否拜訪過
P = [0] *(MAX+1) #紀錄已過的最短路徑

#用堆疊的方式，stack
source = 0 #起點
destination = 0 #終點
n = 0
top = -1
step = 1 #記錄走了多少步

stack = [0] *(MAX+1)

def init(des):
    global visited 
    global novisited 
    global infinite 
    global A 
    global D 
    global S 
    global P 
    global source 
    global destination
    global n 
    
    weight = 0
    done = False #還未全部讀完，若讀完變True
    
    try:
        input_stream = open("shortest_path.dat", "r")
    except FileNotFoundError:
        print("file not found")
        sys.exit(1)
        
    try:
        n = eval(input_stream.readline().strip("\n"))
    except Exception:
        pass
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            A[i][j] = infinite#初始先把設每個點到點無限大
            
    while done == False:
        try:
            temp = input_stream.readline().strip("\n").split(" ")
            i = eval(temp[0])
            j = eval(temp[1])
            weight = eval(temp[2])
        except Exception:
            done = True
        
        A[i][j] = weight
            
    input_stream.close()
    
    source = Restaurant.address
    
    destination = des
    
    for i in range(1, n+1):
        S[i] = False
        D[i] = A[source][i]
        P[i] = source
        
    S[source] = visited 
    D[source] = 0
    
"""def output_step():
    global D
    global P
    global infinite
    global n
    
    print("step: ", step)
    print("D: ")
    for i in range(1, n+1):
        if D[i] == infinite:
            print("----", end = "")
        else:
            print("%4d" %D[i], end ="")
    print()
    
    print("P: ")
    for i in range(1, n+1):
        print("%4d" %P[i], end = "")
    print()"""
        
def access():
    global A 
    global D
    global S
    global P
    global step
    global novisited
    global visited
    global n
    
    for step in range(2, n+1):#因為地一步已經做了，所以從第2開始
        t = minD()
        S[t] = visited
        
        for i in range(1,n+1):
            if S[i] == novisited and D[t] + A[t][i] <= D[i]:#不確定是小於還是小於等於< D[i]
                D[i] = D[t] + A[t][i]
                P[i] = t
                
       # output_step()
         
def minD():
    global infinite
    global S
    global N
    global novisited
    
    t = 0
    minimum = infinite 
    
    for i in range(1, n+1):
        if S[i] == novisited and D[i] < minimum:
            minimum = D[i]
            t = i
            
    return t
 
def output_path():
    global D
    global P
    global source
    global destination
    global infinite
    global A
    
    #node = sink 
    
    if destination == source or D[destination] == infinite:
        print("\n  address %d has no path to address %d" %(source, destination), end ="")
        return
    
    #print("v%d" %source, end = "")
    
    """while node != source:
        push(node)
        node = P[node]"""
        
    """while node != sink:
        node = pop()
        print("-- %d--> " %A[P[node]][node], end = "")
        print("v%d" %node, end = "")"""
    
    print()
    print("total length: %d Km" %D[destination])#the unit ofthe distance is Km
    print("Your meal will arrive in : %d mimnutes" %((D[destination] / 50) *60))#Suppose the delivery person rides its motorcycle with 50Km/Hr
    
def pop():
    global top 
    global stack
    
    if top < 0:
        print("stack is empty")
        sys.exit(1)
    
    temp = stack[top]
    top -= 1
    return temp

def push(value):
    global MAX
    global top 
    global stack
   
    if top >= MAX:
        print("stack is full")
        sys.exit(1)
    else:
        top += 1
        stack[top] = value
        
def main(des):
    init(des)
    #output_step()
    access()
    output_path()

if __name__ == "__main__":
    main()
            
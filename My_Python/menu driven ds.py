class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next

   #Adding elements to queue at the rear end
def enqueue(data):
    queue.insert(0,data)

#Removing the front element from the queue
def dequeue():
    if len(queue)>0:
      return queue.pop()
    return ("Queue Empty!")

def display():
    print("Elements on queue are:");
    for i in range(len(queue)):
       print(queue[i])

def isEmpty(stk): # checks whether the stack is empty or not
    if stk==[]:
      return True
    else:
      return False

def Push(stk,item): 
    stk.append(item)
    top=len(stk)-1

def Pop(stk):
    if isEmpty(stk): # verifies whether the stack is empty or not
      print("Underflow")
    else:
        item=stk.pop()
        if len(stk)==0:
            top=None
        else:
            top=len(stk)
            print("Popped item is "+str(item))

def Display(stk):
    if isEmpty(stk):
      print("Stack is empty")
    else:
       top=len(stk)-1
       print("Elements in the stack are: ")
       for i in range(top,-1,-1):
          print (str(stk[i]))


if __name__ == "__main__":
    print("Stack operations:")
    stk=[]
    top = None
    n = int(input('How many elements would you like to add? '))
    for i in range(n):
        data = int(input('Enter data item: '))
        Push(stk,data)
    
    Pop(stk)
    Display(stk)
    print("\nQueue Operations:")
    queue=[]
    n = int(input('How many elements would you like to add? '))
    for i in range(n):
        data = int(input('Enter data item: '))
        enqueue(data)
    print("Popped Element is: "+str(dequeue()))
    display()
    
    a_llist = LinkedList()
    n = int(input('How many elements would you like to add? '))
    for i in range(n):
        data = int(input('Enter data item: '))
        a_llist.append(data)
    print('The linked list: ', end = '')
    a_llist.display()
   





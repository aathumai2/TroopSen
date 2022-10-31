class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp =self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def insertAfter(self, prev_node, new_data):
        if prev_node ==None:
            print("Given prev node must be in linked list")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next=new_node

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head

        while(last.next):
            last=last.next
        
        last.next = new_node

    def deleteNode(self, key):
        temp = self.head

        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

        while (temp is not None):
            if temp.data == key:
                break
            prev=temp
            temp= temp.next

        if (temp == None):
            print("key not found")
            return

        prev.next=temp.next
        temp = None

        


#Code excecution starts here

if __name__=='__main__':
  
    # Start with the empty list
    llist = LinkedList()
  
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    # Driver program
    llist = LinkedList()
    llist.push(7)
    llist.push(1)
    llist.push(3)
    llist.push(2)
    
    print ("Created Linked List: ")
    llist.printList()
    llist.deleteNode(1)
    print ("\nLinked List after Deletion of 1:")
    llist.printList()
    
    # This code is contributed by Nikhil Kumar Singh (nickzuck_007)
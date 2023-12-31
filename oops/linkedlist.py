####################single linklist 
class node:
      def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
      def __init__(self):
       self.start=None
      def viewlist(self):
          if self.start==None:
              print("list is empty")
          else:
              temp=self.start
              while temp!=None:
                  print(temp.data,end = " ")
                  temp=temp.next
      def reverse(self):
          prev=None
          current=self.start
          while current != None:
              next=current.next
              current.next=prev
              prev=current
              current=next
          self.start=prev 
      def detectLoop(self):
        slow_p = self.head
        fast_p = self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return 1
        return 0    
      def length(self): 
          temp=self.start
          count=0
          while (temp):
               count +=1
               temp=temp.next
          return count
      def deletefirst(self):
          if self.start == None:
              print("linked list is empty")
          else:
              self.start=self.start.next 
      def insertlast(self,value):
          newnode=node(value)
          if(self.start==None):
              self.start=newnode
          else:
               temp=self.start
               while temp.next != None:
                  temp=temp.next
               temp.next=newnode
mylist=linkedlist()
mylist.insertlast(10)         
mylist.insertlast(20)
mylist.insertlast(30)
mylist.insertlast(40)
mylist.viewlist()
print()
print(mylist.length())
mylist.detectLoop()
mylist.viewlist()





        
#class Node:
#    def __init__(self, data):
#        self.item = data
#        self.next = None
#        self.prev = None
## Class for doubly Linked List
#class doublyLinkedList:
#    def __init__(self):
#        self.start_node = None
#    # Insert Element to Empty list
#    def InsertToEmptyList(self, data):
#        if self.start_node is None:
#            new_node = Node(data)
#            self.start_node = new_node
#        else:
#            print("The list is empty")
#    # Insert element at the end
#    def InsertToEnd(self, data):
#        # Check if the list is empty
#        if self.start_node is None:
#            new_node = Node(data)
#            self.start_node = new_node
#            return
#        n = self.start_node
#        # Iterate till the next reaches NULL
#        while n.next is not None:
#            n = n.next
#        new_node = Node(data)
#        n.next = new_node
#        new_node.prev = n
#    # Delete the elements from the start
#    def DeleteAtStart(self):
#        if self.start_node is None:
#            print("The Linked list is empty, no element to delete")
#            return 
#        if self.start_node.next is None:
#            self.start_node = None
#            return
#        self.start_node = self.start_node.next
#        self.start_prev = None;
#    # Delete the elements from the end
#    def delete_at_end(self):
#        # Check if the List is empty
#        if self.start_node is None:
#            print("The Linked list is empty, no element to delete")
#            return 
#        if self.start_node.next is None:
#            self.start_node = None
#            return
#        n = self.start_node
#        while n.next is not None:
#            n = n.next
#        n.prev.next = None
#    # Traversing and Displaying each element of the list
#    def Display(self):
#        if self.start_node is None:
#            print("The list is empty")
#            return
#        else:
#            n = self.start_node
#            while n is not None:
#                print("Element is: ", n.item)
#                n = n.next
#        print("\n")
## Create a new Doubly Linked List
#NewDoublyLinkedList = doublyLinkedList()
## Insert the element to empty list
#NewDoublyLinkedList.InsertToEmptyList(10)
## Insert the element at the end
#NewDoublyLinkedList.InsertToEnd(20)
#NewDoublyLinkedList.InsertToEnd(30)
#NewDoublyLinkedList.InsertToEnd(40)
#NewDoublyLinkedList.InsertToEnd(50)
#NewDoublyLinkedList.InsertToEnd(60)
## Display Data
#NewDoublyLinkedList.Display()
## Delete elements from start
#NewDoublyLinkedList.DeleteAtStart()
## Delete elements from end
#NewDoublyLinkedList.DeleteAtStart()
## Display Data
#NewDoublyLinkedList.Display()





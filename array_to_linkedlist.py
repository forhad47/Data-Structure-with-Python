class Node:
    def __init__(self,elem,next):
        self.elem = elem
        self.next = next
class LinkedList:
    def __init__(self, arr1):
        self.head = Node(arr1[0], None)
        temp = self.head
        for i in range(1,len(arr1),1):
            new_node = Node(arr1[i],None)
            temp.next = new_node
            temp = temp.next

    def remove_elem(self):
        current = self.head
        while current:
            runner = current
            while runner.next:
                if runner.next.elem == current.elem :
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next
    def printList(self):
        temp = self.head
        while temp!= None:
            print(temp.elem,end="-->")
            temp = temp.next
        print("None")


h1=LinkedList([12,10,12,5,7,10,5,8,9,12])
print("Before removing elem: ")
h1.printList()
h1.remove_elem()
print("After removing elem : ")
h1.printList()
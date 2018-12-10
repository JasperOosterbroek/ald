class ListNode:
    def __init__(self,data,next_node):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return str(self.data)

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        s = ''
        current = self.head
        if current != None:
            s = s + str(current)
            current = current.next
        while current != None:
            s = s + " -> " + str(current)
            current = current.next
        if not s: # s == '':
            s = 'empty list'
        return s

    def addLast(self, e):
        if not self.head: # self.head == None:
            self.head = ListNode(e,None)
            self.tail = self.head
        else:
            n = ListNode(e,None)
            self.tail.next = n
            self.tail = self.tail.next

    def delete(self,e):
        if self.head: # self.head != None:
            if self.head.data == e:
                self.head = self.head.next
                if self.head == None:
                    self.tail = None
            else:
                current = self.head
                while current.next != None and current.next.data != e:
                    current = current.next
                if current.next != None:
                    current.next = current.next.next
                if current.next == None:
                    self.tail = current

class MyCircularLinkedList:
    def __init__(self):
        self.tail = None

    def __repr__(self):
        s = ''
        current = self.tail
        head = self.tail
        if current != None:
            current = current.next
            s = s + str(current)
        while current != None and current != head:
            current = current.next
            s = s + " -> " + str(current)
        if not s:  # s == '':
            s = 'empty list'
        return s

    def addLast(self, e):
        if not self.tail:
            self.tail = ListNode(e, None)
            self.tail.next = self.tail
        else:
            n = ListNode(e, self.tail.next)
            self.tail.next = n
            self.tail = self.tail.next

    def delete(self,e):
        if self.tail: # self.head != None:
            if self.tail.data == e:
                if self.tail.next is self.tail:
                    self.tail = None
                else:
                    self.tail = self.tail.next
                    self.tail.next = self.tail
            else:
                current = self.tail
                start = current
                while current.next != None and current.next.data != e and current != start:
                    current = current.next
                    if current.next != None:
                        current.next = current.next.next
                    if current.next == None:
                        self.tail = current
            return False




mylist = MyCircularLinkedList()
# print(mylist) # empty list
# # mylist.addLast(1)
# # mylist.addLast(2)
# # mylist.addLast(3)
# # print(mylist) # 1 -> 2 -> 3
# # mylist.delete(2)
# # print(mylist) # 1 -> 3
# # mylist.delete(1)
# # print(mylist) # 3
# # mylist.delete(3)
# # print(mylist) # empty list
# #
# # print(mylist) # empty list
# # mylist.addLast(1)
# # mylist.addLast(2)
# # mylist.addLast(3)
# # print(mylist) # 1 -> 2 -> 3
# # mylist.delete(2)
# # print(mylist) # 1 -> 3
# # mylist.delete(3) # hier loopt hij nu stuk
# # print(mylist) # 1
# # mylist.delete(1)
# # print(mylist) # empty list
# # mylist.delete(3)
# # print(mylist) #empty list
# #
# # mylist.addLast(1)
# # mylist.addLast(2)
# # mylist.addLast(3)
# # print(mylist)
# # mylist.delete(3)
# # print(mylist)
# # mylist.delete(1)
# # print(mylist)
# # mylist.delete(2)
# # print(mylist)
mylist = MyCircularLinkedList()
print(mylist) # empty list
mylist.addLast(1)
mylist.addLast(2)
print(mylist.delete(99))
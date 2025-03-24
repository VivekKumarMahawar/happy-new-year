class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def printLL(head):
    cur=head
    while cur!=None:
        print(cur.data,end="->")
        cur=cur.next
    print("None")

def insert_at_the_beginning(head,data):
    temp=Node(data)
    temp.next=head
    head=temp
    return head

def insert_at_last(head, data):
    temp = Node(data)
    cur = head
    while cur.next is not None:
        cur = cur.next
    cur.next = temp 
    return head

def insert_in_middle(head,data,pos):
    if pos==1:
        head=insert_at_the_beginning(head,data)
        return head
    cur=head
    count=1
    while count<pos-1 and cur!=None:
        cur=cur.next
        count+=1
    temp=Node(data)
    temp.next=cur.next
    cur.next=temp
    return head

def del_at_the_begin(head):
    head=head.next
    return head

def del_end(head):
    temp=head
    while temp.next.next!=None:
        temp=temp.next
    temp.next=None
    return head

def del_mid(head, pos):
    temp = head
    for i in range(1, pos - 1):
        if temp is None or temp.next is None:
            print("Position out of range.")
            return head
        temp = temp.next

    if temp.next is None:
        print("Position out of range.")
        return head

    temp.next = temp.next.next
    return head

def sum(head):
    temp=head
    sum=0
    while temp is not None:
        sum+=temp.data
        temp=temp.next
    print(sum)





def reverseLinkedList(head):
    arr = []
    current = head
    while current != None:
        arr.append(current.data)
        current = current.next

    arr.reverse()

    cur = head
    i = 0
    while cur != None:
        cur.data = arr[i]
        cur = cur.next
        i += 1
    
    return head

def reverse_using_space(head):
    arr=[]
    cur=head
    while cur!=None:
        arr.append(cur.data)
        cur=cur.next
    cur=head
    for i in reversed(arr):
        cur.data=i
        cur=cur.next
    return head

def rev(head):
    prev = None
    cur = head
    while cur is not None:
        nextNode = cur.next
        cur.next = prev
        prev = cur
        cur = nextNode
    return prev 

def mid_of_the_node(head):
    count = 0
    cur = head
    while cur:
        count += 1
        cur = cur.next
    mid_index = count // 2  
    cur = head
    for _ in range(mid_index):
        cur = cur.next
    print(cur.data)




node1=Node(10)
node2=Node(20)
node3=Node(30)
node1.next=node2
node2.next=node3
head=node1
printLL(head)
head = insert_at_the_beginning(head, 5)
printLL(head)
head=insert_at_last(head,40)
printLL(head)
head=insert_in_middle(head,25,4)
printLL(head)
head=del_at_the_begin(head)
printLL(head) 
head=del_end(head)
printLL(head)
head=del_mid(head,2)
printLL(head)
sum(head)
head=reverseLinkedList(head)
printLL(head)
head=reverse_using_space(head)
printLL(head)
head=rev(head)
printLL(head)
mid_of_the_node(head)
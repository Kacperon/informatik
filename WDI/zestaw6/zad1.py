class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def __str__(self):
        return "{} -> {}".format(self.data,self.next)
T=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,11,11]
print(T[10::-1])
head=Node(None)
def is_in(head,value):
    # zakladam ze head istnieje 
    while head.next != None:
        if head.data==value:
            return True
        head=head.next
    return head.data==value
def add(head,value):
    head_copy=head
    if not is_in(head,value):
        while head.next != None:
            head=head.next
        head.next=Node(value)
    return head_copy
        
def remove(head,value):
    head_copy=head
    if is_in(head,value):
        while head.next.data!=value:
            head=head.next
        head.next=head.next.next

    return head_copy

for x in T:
    add(head,x)
print(head)
for x in T[:5]:
    remove(head,x)
print(head)
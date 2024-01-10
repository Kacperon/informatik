a=[1,0,0,0,0,0,0,0,0,2,0,0,0,0,0,1,0,0,30,0,0,0,0,0]
class Node:
    def __init__(self,value,index):
        self.value=value
        self.index=index
        self.next=None
    def __str__(self):
        return "({},{}) -> {}".format(self.value,self.index,self.next)
def init_list(list):
    head=Node("dł",len(list))
    head_copy=head
    for i,x in enumerate(list):
        if x!=0:
            head.next=Node(x,i)
            head=head.next
    return head_copy
głowa=init_list(a)
def drukarka(head):
    t=[0 for _ in range(head.index)]
    head=head.next
    while head!=None:
        t[head.index]=head.value
        head=head.next
    return t
print(drukarka(głowa))

a=Node()
        

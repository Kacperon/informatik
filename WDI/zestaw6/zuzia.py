class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __str__(self):
        return "{}->{}".format(self.data,self.next)
    def __ge__(self,other):
        return self.data>=other.data
    def __gt__(self,other):
        return self.data>other.data
    def __eq__(self,other):
        return self.data == other.data
    def __hash__(self):
        return hash(hash(self.value),hash(self.index))

a=Node(14)
a.next=a
print(a)
b=Node(14)
print(a>b)
num=a.data
# print(num)
# a=[[1]*10]*10
# a[0][0]=0
print(a == b)

#a,b,c=1.5,True,[1,23,4]

#print(a,b,c)
#print("a: {}, b: {}, c: {}".format(a,b,c))

for i in range(10):
    i+=10
    print(i)
for x in [a,b]:
    x.data+=10
    print(x)
print(a,b)


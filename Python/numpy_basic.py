import numpy as np

a= np.array([1,2,3,4,5])
b= np.zeros((2,3))
c= np.ones((3,3))
d= np.empty((3,3))
e= np.full((2,3),3)
f= np.full_like(a, 99)
g= np.full(b.shape,10)
h= np.random.randint(100,size=(3,3,3))
i= np.identity(3)
j= np.eye(3,4)
k= np.arange(12)  # 0...11
k= k.reshape(3,4)
l= np.arange(3,14,2).reshape(3,2)


a=np.array([[12,13,14,15],[3,24,13,6],[10,18,1,2]])
#to search the value
print(a[a%6==0])
print(a>5)# this will return values in bool : true or false 
print(np.any(a>10,axis=0) )# this will return true if any value in col(axis=0) is greater than 10
print(np.all(a>10,axis=1) )#this will return true only if all values in row(axis=1) is greater than 10
print(a[a>5]) # this will return actual values

print((a>5) & (a<10))

#to search the position
print(np.where(a%2==0))
#all row values
lst=list(np.where(a%2==0)[0].data)
#all column values
lst1=list(np.where(a%2==0)[1].data)
for pos in zip(lst,lst1):
    print(pos)
    
print(np.sum(a,axis=0)) #column wise
print(np.sum(a,axis=1)) #row wise

x=np.array([10,20,30])
y=np.array([11,12,13])
z=np.array([21,22,23])

#to arrange data horizontally
print(np.hstack((x,y,z)))

# d=np.vstack((x,y,z))
print(np.vstack((x,y,z)))

print(np.flip(k))
print(np.flip(k,axis=1))
print(np.flip(k,axis=0))


n= np.full((2,3),2)
o= np.arange(3,10).reshape(3,2) # this arange in sorted manner
p= np.matmul(o,n)
print(np.min(p))#print(np.max(p)), sum(p) , mean(p) 
print(np.min(p,axis=1)) # print(np.max(p,axis=1))
print(np.min(p,axis=0)) # print(np.max(p,axis=0))



a1= np.random.randint(size=(3,5))
a2= np.random.randint(20,size=(5,3))

a3= np.arange(15).reshape(3,5)

a1.matmul(a2)
a1.dot(a2)


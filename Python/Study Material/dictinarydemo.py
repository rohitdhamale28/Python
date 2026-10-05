d1={'a':100,'b':234,'c':200}
d2={'x':20,'y':23,'b':345}
d1.update(d2)
d3={**d1,**d2}
print(d3)
d1['d']=56   #add a key
print(d1)
d1['a']=1000 #overwrite the key

v=d1.get('a',-1)
if v!=-1:
    d1['a']=300
else:
    print("Key exists")
    
v=d1.setdefault('a',567)

lst=['Pune','Mumbai','Delhi']
d3=dict.fromkeys(lst,100)

#delete the last key, value pair
d1.popitem()

#to delete given key,value pair
d1.pop('a',-1)

c={"java":100,"python":200,"linux":150}
#find all courses with capacity < 180
for k in c.keys():
    print(f"{k}--->{c[k]}")

for k,v in c.items():
    if v<180:
        print(f"{k}--->{v}")















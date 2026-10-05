s={"Python","Perl","python","java","Python"}
print(s)

s.add(12)
print(s)
#s.add([12,34,56]) #error

s.add("test")

s.update([23,56,78,89])
print(s)

s.update("test")

s.pop()

if 23 in s:
   s.remove(23)
   
s.discard(23)

print(s)







s1={1,2,3,4,5}
s2={4,5,11,12}
print("union",s1.union(s2),s1|s2)
print("Intersection ",s1.intersection(s2),s1&s2)
print("difference ",s1.difference(s2),s1-s2)
print("symmetric difference ",s1.symmetric_difference(s2),s1^s2)

s1.symmtric_difference_update(s2)
print(s1)
#s1=s1^s2
#print(s1)

s1.difference_update(s2)
print(s1)
#s1=s1-s2
#print(s1)
















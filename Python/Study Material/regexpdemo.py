import re

# re.search() looks for a match anywhere in the string.
s="Something is there somewhere"
ob=re.search("s.*?e",s,re.I|re.M)
if ob!=None:
    print(ob.group())
    print(ob.span())
else:
    print("not found")

# re.match() checks for a match only at the beginning of the string.
s="Something is there somewhere"
ob=re.match("s.*?e",s,re.I|re.M)
if ob!=None:
    print(ob.group())
    print(ob.span())
else:
    print("not found")

# search() can find a match even when the pattern starts later in the string.
s="Something is there somewhere"
ob=re.search("t.*?e",s,re.I|re.M)
if ob!=None:
    print(ob.group())
    print(ob.span())
else:
    print("not found")


# match() returns no match when the pattern does not start at position zero.
s="Something is there somewhere"
ob=re.match("t.*?e",s,re.I|re.M)
if ob!=None:
    print(ob.group())
    print(ob.span())
else:
    print("not found")
    
# findall() returns all matching parts as a list.
s="Something is there somewhere"
lst=re.findall("s.*?e",s,re.I|re.M)
if lst!=None:
    print(lst)
else:
    print("not found")

# finditer() returns match objects one at a time.
s="Something is there somewhere"
lst=re.finditer("s.*?e",s,re.I|re.M)
if lst!=None:
    for ob in lst:
        print(ob.group())
        print(ob.span())
else:
    print("not found")

    
# sub() replaces matching text with the replacement string.
s="Something is there somewhere"
newstr=re.sub("s.*?e","XXXXXXXX",s,flags=re.I|re.M,count=1)
print(newstr)

# compile() creates a reusable regular-expression pattern object.
myreg=re.compile("s.*?e",re.I|re.M)
m=myreg.search(s)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("not found")


# Groups in parentheses capture separate parts of a matching pattern.
s="This is string"
m=re.search("^(\w+)\s\w+\s$(\w+)",s)
if m!=None:
    print(m.group())
    print(m.group(1))
    print(m.group(2))

acno="XXXXXXXX1234XXXX"
m=re.search("^X{8}(\d{4})X{4}$")
if m!=None:
    print(m.group(1))
    
s="what is status of #1234 "
s="is flight #454567 is on time"








    
    
    
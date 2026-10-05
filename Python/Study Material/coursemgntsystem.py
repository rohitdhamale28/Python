#https://codeshare.io/alV70y
lst=[("Java",200,150),("cpp",180,200)]
def addnewcourse():
    nm=input("enetr name")
    duration=int(input("enetr duration"))
    capacity=int(input("enter capacity"))
    lst.append((nm,duration,capacity))
    return True

def displayAll(clst=lst):
    for c,d,cap in clst:
        print(f"{c}---->{d}---->{cap}")
        
def displayByCapacity(c):
    clist=[]
    for course in lst:
        if course[2]>c:
           clist.append(course)
    if len(clist)>0:
        return clist
    else:
        return None
    
def searchByName(nm):
    for pos,course in enumerate(lst):
        if course[0]==nm:
            return pos,course
    return -1,None


    
def deleteByName(nm):
    pos,course=searchByName(nm)
    if course!=None:
        lst.remove(course)
        return True
    return False
            
def modifyByName(cname,c,d):
    pos,course=searchByName(cname)
    if pos!=-1:
      ans=input(f"do you want to modify {course}") 
      if ans=="y":
          #overwrite old tuple with new tuple
          lst[pos]=cname,d,c 
          return 1
      else: 
          return 2
    else:
        return 3
def sortByDuration(ch):
    lst1=lst.copy()
    if ch==1:
        lst1.sort(key=lambda x:x[1])
    else:
        lst1.sort(key=lambda x:x[1],reverse=True)
    return lst1
           
choice=0
while choice!=9:
    choice=int(input("""
                     1. add new course
                     2. delete course by name
                     3. display all
                     4. display by capacity
                     5. display by duration
                     6. sort on duration
                     7.sort on capacity
                     8. modify course duration and capacity
                     9.exit"""))
    match choice:
        case 1:
            status=addnewcourse()
            if status:
                print("course added successfully")
            else:
                print("Error occured")
        case 2:
            nm=input("enetr name to delete")
            status=deleteByName(nm)
            if status:
                print("Deleted successfully")
            else:
                print("Not found")
                
        case 3:
            displayAll()
            
        case 4:
            c=int(input("enter capacity"))
            lstcap=displayByCapacity(c)
            if lstcap!=None:
                displayAll(lstcap)
            
            pass
        case 5:
            pass
        case 6:
            ch=int(input("1. Ascending 2.Descending"))
            
            sort_duration=sortByDuration(ch)
            displayAll(sort_duration)
            pass
        case 7:
            pass
        case 8:
            cname=input("enetr course name to modify")
            c=int(input("enetr new capacity"))
            d=int(input("Enter duration"))
            status=modifyByName(cname,c,d)
            if status==1:
                print("found and modification done")
            elif status==2:
                print("found and modification not done")
            else:
                print(f"{cname} not found")
           
        case 9:
            print("Thank you for visiting......")
            
        case _:
            print("wrong choice")
                
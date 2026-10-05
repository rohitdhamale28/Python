# File Handling :
    
    
fh=open("employeeinfo.txt")
fh1=open("employeedata.txt","w")
for line in fh:
    print(line)
    lst=line.split(",")
    print(lst[0],lst[1])
    ln=":".join(lst)
    fh1.write(ln)
fh.close()
fh1.close()

#========================================================================================


try: 
    fh=open("employeeinfo111.txt")
    fh1=open("employeedata.txt","w")
    for line in fh:
        print(line)
        lst=line.split(",")
        print(lst[0],lst[1])
        if lst[3]=='Admin': #to filter employee who have admin = 3
            ln=":".join(lst)
            fh1.write(ln)   
except FileNotFoundError as e:
    print(e)
finally:
    fh.close()
    fh1.close()

# alternative to fh=open("employeeinfo111.txt")
with open("employeeinfo.txt") as fh:
    with open("empcopy.txt","w") as fh1:
        for line in fh:
            print(line)
            fh1.write(line)



#create employeedata.txt with this data
#123,Rohit,Manager,Admin,45678
#124,Sameer,Clerk,Admin,34567
#125,Hrishikesh,Analyst,It,45679
#126,Deepali,Analyst,HR,34567  
# import math
# print(math.sqrt(16))

# F2 : change the name of the function or variable at all the places in the file
# r = 10
# y = 20

# def addF(r,y):
#     print(r + y)


# def subtractF(r,y):
#     print(r - y)    

# for i in range(1, 11):
#     print(i)


class MyClass:
    def __init__(self, name="",age=0,id=0,no=0):
        self.name = name
        self.age  = age
        self.id   = id
        self.no   = no


    def greet(self):
        print(f"Hello, {self.name}!")

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    def __str__(self):
        print(f"MyClass(name={self.name})")



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
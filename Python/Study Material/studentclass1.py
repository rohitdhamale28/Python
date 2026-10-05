class Student:
    #static variable
    count=0
    
    #static method can acees only static members
    #it cannot access instance varibles
    @staticmethod  #static method
    def __generateId(name):
        Student.count=Student.count+1
        return name[0:3]+str(Student.count)
       
        
    def __init__(self,sname="",m1=0,m2=0,m3=0):
        print("Student constructor called")
        
        self.__sid=Student.__generateId(sname)
        self.__sname=sname
        self.__m1=m1
        self.__m2=m2
        self.__m3=m3
        
    #def set_sid(self,sid):
     #   self.__sid=sid
    def set_sname(self,nm):
        self.__sname=nm
    def set_m1(self,m1):
        self.__m1=m1
    def set_m2(self,m2):
        self.__m2=m2
    def set_m3(self,m3):
        self.__m3=m3

    def get_sid(self):
        return self.__sid
    def get_sname(self):
        return self.__sname
    def get_m1(self):
        return self.__m1
    def get_m2(self):
        return self.__m2  
    def get_m3(self):
        return self.__m3
        
    @staticmethod
    def myfunction(x):
        print("test my function",)
        
    def __str__(self):
        return f"Sid: {self.__sid} sname:{self.__sname} m1:{self.__m1} m2: {self.__m2} m3: {self.__m3}"


s1=Student(sname="Rohit",m1=88,m3=87)
s2=Student("Sameer",85,86,89)
print(s1)
print(s2)
print(s1.get_sname())
s1.set_sname("Sameer")
print(s1)

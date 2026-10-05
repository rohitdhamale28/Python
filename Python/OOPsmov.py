class A:
    def __init__(self,a1=0,a2=2):
        print("In A constructor")
        self.__a1 = a1
        self.__a2 = a2
    def __str__(self):
        return f"A1:{self.__a1}  A2: {self.__a2}"
    
    
class B(A):
    def __init__(self,a1=0,a2=2,b1=0):
        print("In B constructor")
        A.__init__(self,a1,a2)
        self.__b1 = b1
    def __str__(self):
        return A.__str__(self) + f" B1: {self.__b1}"

class C(A):
    def __init__(self,c1=0,c2=0,**kwargs):
        print("In C constructor")
        A.__init__(self,**kwargs)
        self.__c1 = c1
        self.__c2 = c2
    def __str__(self):
        return A.__str__(self) + f" C1: {self.__c1}  C2: {self.__c2}"
    

class D(B,C):
    def __init__(self,d1=0,d2=0,**kwarg):
        print("In D constructor")
        #  B.__init__(self,a1,a2,b1)
        # C.__init__(self,a1,a2,c1,c2)
        super
        self.__d1 = d1
        self.__d2 = d2
        
    def __str__(self):
        return B.__str__(self) + C.__str__(self) + f" D1: {self.__d1} D2: {self.__d2}"
    

ob = D(a1=1,a2=2,b1=11,c1=21,c2=22,d1=31,d2=32)
print(ob)


#=======================================================================================



class A:
    def __init__(self,a1=0,a2=2):
        print("In A constructor")
        self.__a1 = a1
        self.__a2 = a2
    def __str__(self):
        return f"A1:{self.__a1}  A2: {self.__a2}"
    
    
class B(A):
    def __init__(self,b1=0,**kwargs):
        print("In B constructor")
        #A.__init__(self,a1,a2)
        super().__init__(**kwargs)
        self.__b1 = b1
    def __str__(self):
        #return A.__str__(self) + f" B1: {self.__b1}"
        return super().__str__() + f" B1: {self.__b1}"

    
class C(A):
    def __init__(self,c1=0,c2=0,**kwargs):
        print("In C constructor")
        super().__init__(**kwargs)
        #A.__init__(self,**kwargs)
        self.__c1 = c1
        self.__c2 = c2
    def __str__(self):
        #return A.__str__(self) + f" C1: {self.__c1}  C2: {self.__c2}"
        return super().__str__() + f" C1: {self.__c1}  C2: {self.__c2}"
    

class D(B,C):
    def __init__(self,d1=0,d2=0,**kwargs):
        print("In D constructor")
        # B.__init__(self,a1,a2,b1)
        # C.__init__(self,a1,a2,c1,c2)
        super().__init__(**kwargs)
        self.__d1 = d1
        self.__d2 = d2
        
    def __str__(self):
        #return B.__str__(self) +C.__str__(self) + f" D1: {self.__d1} D2: {self.__d2}"
        return  super().__str__() + f" D1: {self.__d1} D2: {self.__d2}"
    
ob = D(a1=1,a2=2,b1=11,c1=21,c2=22,d1=31,d2=32)
print(ob)
print(D.mro())   # prints the order in which the classes are called n parameters are initialised when u try to create a object using hybrid inheritance 

# if we have not used super n used the (B.__str__(self),B.__init__(self)), it initialise the parameter of parent Class A 2 times and also prints  parameter of parent Class A(a1,a2) 2 times :
# return B.__str__(self) +C.__str__(self) + f" D1: {self.__d1} D2: {self.__d2}"

#    D constructor -->  B constructor -->  A constructor --> C constructor --> A constructor
# Ouput : A1:1  A2: 2 B1: 11 A1:1  A2: 2 C1: 21  C2: 22 D1: 31 D2: 32

# If we use [ super().__init__(**kwargs) ]  then the class are called in following way , initiallising the parameters of each class  only once 

# return  super().__str__() + f" D1: {self.__d1} D2: {self.__d2}"

# class D(B,C): when D constructor is called , super() checks for parentclass  [class D('B',C)] , 
# and call B as its the first parent , then again in B constructor we have super(), 
# then it check for next parent C [class D(B,'C')], so B->C ,
# then again in C we have super(), so now C calls its parent class A , D->B->C->A


#   D constructor -->  B constructor -->  C constructor --> A constructor
# Ouput : A1:1  A2: 2 C1: 21  C2: 22 B1: 11 D1: 31 D2: 32
#  



class Friend :
    def __init__(self,id=0,name="",lastname="",hobbies="",mobno="",email="",bdate="",address=""):
        self.__id=id 
        self.__name=name
        self.__lastname=lastname
        self.__hobbies=hobbies
        self.__mobno=mobno
        self.__email=email
        self.__bdate=bdate
        self.__address=address


    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
    
    def get_lastname(self):
        return self.__lastname
    
    def get_hobbies(self):
        return self.__hobbies

    def get_mobno(self):
        return self.__mobno

    def get_email(self):
        return self.__email
    
    def get_bdate(self):
        return self.__bdate
    
    def get_address(self):
        return self.__address


    def set_id(self,id):
           self.__id=id 
                  
    def set_name(self,name):
        self.__name=name
                          
    def set_lastname(self,lastname):
        self.__lastname=lastname
                               
    def set_hobbies(self,hobbies):
        self.__hobbies=hobbies

    def set_mobno(self,mobno):
        self.__mobno=mobno                         

    def set_email(self,email):
            self.__email=email
                                                           
    def set_bdate(self,bdate):          
       self.__bdate=bdate
                                                          
    def set_address(self,address):
              self.__address=address 
              
    def __str__(self):
        return f"Friend :- ID: {self.__id}, Name: {self.__name}, Lastname:{self.__lastname}, Hobbies:{self.__hobbies} "
    
    
    
class ObjectNotFound(Exception):
    def __int__(self,msg="") :
        self.__msg=msg
    def __str__(self):
        return f"{self.__msg}"
    
    
    
        

   
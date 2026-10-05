from abc import abstractmethod,ABC
class Account(ABC):
    def __init__(self,aid=0,nm="",bal=0,pin="",sque="",sans=""):
        self.__aid=aid
        self.__name=nm
        self._balance=bal
        self.__pin=pin
        self.__sque=sque
        self.__sans=sans
    def set_aid(self,aid):
        self.__aid=aid
    def set_name(self,nm):
        self.__name=nm
    def set_balance(self,bal):
        self._balance=bal
    def set_pin(self,pin):
        self.__pin=pin
    def set_sque(self,sque):
        self.__sque=sque
    def set_sans(self,sans):
        self.__sans=sans
    #getter methods
    def get_aid(self):
         return self.__aid
    def get_name(self):
         return self.__name
    def get_balance(self):
         return self._balance
    def get_pin(self):
         return self.__pin
    def get_sque(self):
         return self.__sque    
    def get_sans(self):
         return self.__sans
    def withdraw(self,amount):
        self._balance-=amount
    def deposit(self,amount):
        self._balance+=amount
    @abstractmethod
    def calculatecharges(self):
        pass
    def __str__(self):
        return f"Aid :{self.__aid} name: {self.__name} balance: {self._balance} pin: {self.__pin} que: {self.__sque} Ans: {self.__sans}"

class DematAccount(Account):
    def __init__(self,aid=0,nm="",bal=0,pin="",sque="",sans="",comm=0):
        super().__init__(aid,nm,bal,pin,sque,sans)
        self.__comm=comm
    def set_comm(self,num):
        self.__comm=num
    def get_comm(self):
        return self.__comm
    def calculatecharges(self):
        return self._balance*self.__comm
    def __str__(self):
        return super().__str__()+f" commission {self.__comm}"
    
class SavingAccount(Account):
    def __init__(self,aid=0,nm="",bal=0,pin="",sque="",sans="",chnum=0):
        super().__init__(aid,nm,bal,pin,sque,sans)
        self.__chequebknum=chnum
    def set_chequebknum(self,num):
        self.__chequebknum=num
    def calculatecharges(self):
        return self._balance*0.02
    def get_chequebknum(self):
        return self.__chequebknum
    def __str__(self):
        return super().__str__()+f" cheque bk num {self.__chequebknum}"

if __name__=="__main__":    
    #ac1=Account(12,"Sameer",23456,1111,"favorite color","Red")
    #ac2=Account(13,"Rohit",33456,2222,"favorite color","Red")
    sac1=SavingAccount(12,"Sameer",23456,1111,"favorite color","Red",11111111)
    sac2=SavingAccount(13,"Rohit",33456,2222,"favorite color","Red",22333)
    print(sac1)
    print(sac2)
def divide(a,b):
    return a/b
for i in range(3): 
    # if user is giving wrong input n we wanna give only 3 chances to the user
  try:
    a=int(input("a :"))
    b=int(input("b :"))
    c=a+b
    print("addition :",c)
    result=divide(a,b)
    print("Result : ",result)
    break
  except ValueError:
    print("please enter a no. not string ! ")
  except ZeroDivisionError as e:
    print(e)   #this is exception given by the system
    print("please don't enter 0 ! ")
  except:
    print("Error occured")
#except Exeption as e:
#   print("Error occured",e)     both of the above are same used to handle all the rest of excptions which we have not defined    
  finally:
    print("inside finally block")
   
else:
    print("3 Chances done ")



#========================================================================================

# maybe sometime the input by user is not n erro for system , but its a logic error as per us , for this situation we can raise our user defined custom excepption

class WrongNumberExcepetion(Exception):
    def __init__(self,msg):
        self.__msg = msg
    def __str__(self):
        return self.__msg

num =31

while True :
    
    try :
        n=int(input("Guess the no. :"))
        if n!=num:
            raise WrongNumberExcepetion("OOPs, Wrong Number")
        else:
            print("correct number ! ")
            break
    except (WrongNumberExcepetion,ValueError) as e:
        print(e)
    except : 
        print("Error")
        
        

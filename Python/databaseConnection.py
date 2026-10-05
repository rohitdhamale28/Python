#database connection 
import pymysql

# pip install pymysql
def DisplayStudents():
    sql="select * from student"
    cursor.execute(sql)
    print("\nStudent Details")
    print("-"*60)
    print(f"{'SID':<10}{'NAME':<20}{'AGE':<10}{'MOBILE':<20}")
    print("-"*60)
    
    for row in cursor.fetchall():
        print(
            f"{row[0]:<10}"
            f"{row[1]:<10}"
            f"{row[2]:<10}"
            f"{row[3]:<20}"
            )

    
    
def addStudent():
    try:
        sid=int(input("Enter Sid: "))
        name=input("Enter Name: ")
        mobile=int(input("Enter Mobile: "))
        age=int(input("Enter Age: "))
        
        sql="insert into student values(%s,%s,%s,%s)"
        cursor.execute(sql,(sid,name,mobile,age))
        conn.commit()
        return True
    except ValueError as e :
        print("id and age has to be numeric",e)
    # except pymysql.MySQLError as e :    OR
    except pymysql.IntegrityError as e :
        if e.args[0]==1062:
            print("Error : Student Id or mobile No are same",e)
        else:
            print("database integrity error",e)
    except pymysql.MySQLError as e :
        print("database error: ",e)
        
        
def searchById(sid):
    sql="select * from student where sid=%s"
    cursor.execute(sql,(sid,))
    student= cursor.fetchone()
    if student:
        print("Student Info : ")
        print("SID    :",student[0])
        print("Name   :",student[1])
        print("Mobile :",student[2])
        print("Age    :",student[3])
    else:
        print("Student Id not found")

def searchByName(name):
    sql="select * from student where sname=%s"
    cursor.execute(sql,(name,))
    student= cursor.fetchone()
    if student:
        print("Student Info : ")
        print("SID    :",student[0])
        print("Name   :",student[1])
        print("Mobile :",student[2])
        print("Age    :",student[3])
    else:
        print("Student name not found")

def updateStudent(sid,mobile,age):
    sql="update student set mobile=%s,age=%s where sid=%s"
    cursor.execute(sql,(mobile,age,sid))
    if cursor.rowcount == 0:
        print("Error: Student ID not found")
    else:
        conn.commit()
        print("student updated successfully")


def deleteById(sid):
    sql="delete from student where sid = %s"
    cursor.execute(sql,(sid,))
    if cursor.rowcount == 0:
        print("Error: Student Id not found")
    else:
        conn.commit()
        print("Student deleted successfully")
        
        
        
def getStudentByAge(age):
    result=cursor.callproc("getstudentcount",(age,0))
    #getstudentcount this is the procedure in mysql given below
    print(result)
    
        
try:
    conn=pymysql.connect(host="localhost",user="root",password="root1234",database="test")
    if conn != None :               
        print("Connected to mysql!")
        cursor=conn.cursor()
    choice=-1
    while choice!=8:
        choice= int(input('''
                          1. Add Student 
                          2. Display Students 
                          3. search by Id 
                          4. Search by name 
                          5. update Student 
                          6. Delete Student 
                          7. find student count
                          8. EXIT 
                         '''))
        match choice:
            case 1: 
                status=addStudent()
                print("Student Added !") if status else print("Error")
            case 2: 
                DisplayStudents()
            case 3: 
                sid=int(input("Enter Id : "))
                searchById(sid)
            case 4: 
                name=input("Enter Name: ")
                searchByName(name)
            case 5: 
                sid=int(input("Enter Id : "))
                mobile=int(input("Enter New Mobile: "))
                age=int(input("Enter New Age: "))
                updateStudent(sid,mobile,age)
            case 6: 
                sid = int(input("Enter id: "))
                deleteById(sid)
            case 7: # For this we have created a procedure in mysql given below
                age=int(input("Enter Age : "))
                getStudentByAge(age)
            case 8: 
                pass
            case _: 
                pass
            
except pymysql.MySQLError as e :
    print("DataBase connection failed :",e)
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    
    
    
# procedure to count student 
#delimiter //
#create procedure getstudentcount(page int ,out cnt int)
#begin
#    select count(*) into cnt
#    from student
#    where age>page;
#end //

#delimiter ;
    

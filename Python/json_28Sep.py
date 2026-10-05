# Pickling 

# Libary to use json file
import json 



#--------------------------------------------------------------------------------------
# json.load

# function to load data from json file 
with open ("/home/pgcp-esd/Downloads/PYTHON/Notes2/students.json","r") as file:
    data=json.load(file)

# making a list of data from json file
students=data["students"]

for student in students:
    print(student["sid"],student["name"],student["marks"])
    
for student in students:
    if student["marks"] >80 :
        print(student["sid"],student["name"],student["marks"])

top_student = max(students, key=lambda s:s["marks"])

print("Top Student: ",top_student)

students.append({"sid":104,"name":"rohit","marks":99})


#--------------------------------------------------------------------------------------
# json.dump


# write ( "w" ) : use 'w' while opening the file
# the below function will overwite the json file removing the old data , n wrting data1 in it ! 
data1={"students":students}

with open("/home/pgcp-esd/Downloads/PYTHON/Notes2/student2.json", "w") as file:
    json.dump(data1, file, indent=4)
    
    
# append ( "a" ) : use 'a' while opening the file 
# the below function will add/append a new object at the end of the json file 
a={"new_student":[{"sid":104,"name":"rohit","marks":99}]}
   
with open("/home/pgcp-esd/Downloads/PYTHON/Notes2/students.json", "a") as file:
    json.dump(a, file, indent=4)
    
    
    
#--------------------------------------------------------------------------------------
# json.loads && json.dumps    
    

#to convert data from string to python object use loads, and dumps for student in students:
#convert python object to String use dumps


import json

json_string = '{"name": "Amit", "age": 21, "marks": 85}'

student = json.loads(json_string)

print(student["name"])
print(student["marks"])
print(student["name"], student["age"], student["marks"])



# import pickly as pck

# similar to json libary , google it (if data is not in json format it is used )

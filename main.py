import os
from pathlib import Path
import random

filename = Path("students.txt")
with open(filename, "x"):
    pass

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def showInfo(self):
        return f"{self.name} {self.age}"


class Student(Person):
    def __init__(self, name,age, major,gpa):
        super().__init__(name,age)
        self.major = major
        self.id = random.randint(100000000,1999999999)
        self.courses = {}
        self.__gpa = gpa
    
    def showInfo(self):
        return f"{super().showInfo()} {self.id} {self.major}"
    
    def addCourse(self,name,degree):
        self.courses[name] = degree if degree < 100 else 0
    
    def showMarks(self):
        if len(self.courses.keys()) > 0:
         print(self.courses)
        else:
            print("Sorry add course first")
    def getgpa(self):
        return self.__gpa
    
    def updateCourse(self):
       print("1-Modify\n2-Delete")
       value = int(input("What operation you want to perform: "))
       match value:
           case 1:
               name = input("What is the name of the course: ")
               for value in list( self.courses.keys()):
                   if value == name:
                    newName = input("new Course name: ")
                    newGrade = int(input("New grade: "))
                    del self.courses[name]
                    self.courses[newName] = newGrade if newGrade < 100 else 0
           case 2:
               name = input("Enter hte name of the course: ")
               for value in list(self.courses):
                   if value == name:
                       del self.courses[name]
    def exportInfo(self):
        with open(filename, "a+") as f:
            f.write(f"{self.showInfo()}\n")
        


flag = True
while flag:
    print("1-Add student\n2-Update\n3-Remove\n4-Show\n5-quit")
    operation = int(input("Enter type of operation you want to perform:"))
    if operation == 5:
        flag = False
    else:
        match operation:
            case 1:
              try:
                name = input("Enter name: ")
                age = int (input("Enter age: "))
                major = input("Enter major: ")
                gpa = float(input("Enter gpa: "))
                sNew = Student(name, age, major, gpa)
                sNew.exportInfo()
              except:
                  print("Invalid Data")
                  print("Follow this rule:\n name is string\n age and GPA are numbers")
                  

            case 2:
                with open(filename,"r") as f: 
                    lines = f.readlines()
                
                print("".join(lines))
                target_id = int(input("Enter the ID of the student: "))
                updated = False
                for i, line in enumerate(lines):
                    sep = line.strip().split(" ")
                    if len(sep) > 4 and target_id == int(sep[3]):
                        print("1-Name\n2-Age\n3-Major\n")
                        value = int(input("What value to be udpated: "))
                        match value:
                            case 1:
                                new_name = input("Enter new Name: ").split(" ")
                                sep[0] = new_name[0]
                                sep[1] = new_name[1] if len(new_name) > 1 else sep[1]
                            case 2:
                                new_age = int(input("Enter new age: "))
                                sep[2] = new_age if new_age > 0 else sep[2]
                            case 3:
                                new_major = input("new major: ")
                                sep = sep[:4] + new_major
                            case _:
                                break
                        lines[i] = " ".join(sep) + "\n"
                        print(lines[i])
                        updated = True
                    if updated:
                        with open(filename, "w") as f:
                            f.writelines(lines)
                            print("updated")
                    else:
                        print("ID not found")
            case 3:
                target_id = int(input("Enter the ID of student you want to remove: "))    
                if filename.exists():
                    with open(filename,"r") as f:
                        lines = f.readlines()
                        print(" ".join(lines))
                    
                    for i,line in enumerate(lines):
                        sep = line.strip().split(" ")
                        if int(sep[3]) == target_id:
                            del lines[i]
                    
                   
                    with open(filename, "w") as f:
                        f.writelines(lines)
                else:
                    print("ID not found")
                
                     
                
            case 4:
             if filename.exists():
                with open(filename,"r") as f:
                    content = f.read().strip()
                    if content:
                        print(content)
                    else:
                        print("No students exist")                    
             else:
                 print("Please add student")
            
            case 5:
                break;
            

os.remove(filename)


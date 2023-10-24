from validation import *
from datetime import datetime
class employee:
    def __init__(self,id1,name,sal,age,gender,add,city,dob,doj,dname,designation,pan,adh):
        self.id1=id1
        self.name=name
        self.sal=sal
        self.age=age
        self.gender=gender
        self.add=add
        self.city=city
        self.dob=dob
        self.doj=doj
        self.dname=dname
        self.designation=designation
        self.pan=pan
        self.adh=adh
    def display(self):
        print(self.id1,self.name,self.sal,self.age,self.gender,self.add,self.city,self.dob,self.doj,self.dname,self.designation,self.pan,self.adh)
emp=[]
while True:
    print("1:Add a record of Employee.")
    print("2:Display the record of Employee.")
    print("3:Delete the record of Employee.")
    print("4:Update Employee details.")
    print("5:Search details of Employee.")
    print("6:Display the details of Employee with highest salary.")
    print("7:Display the details of Employee with lowest salary.")
    print("8:Exit")

    choice=int(input("Enter your choice."))
    if choice ==1:
        id1=input("Enter the Employee_Id.")
        while True:
            name=input("Enter the Name.")
            if valid_Empname(name):
                break
            else:
                print("Invalid name Please Enter Again")
        while True:
            sal=int(input("Enter salary "))
            if valid_Salary(sal):
                break
            else:
                print("Invalid Salary Please Enter Again")

        while True:
            gender=input("Enter gender(M/F/T).")
            if valid_Gender(gender):
                break
            else:
                print("Invalid gender Please Enter Again")

        add=input("Enter Address.")

        while True:
            state=input("Enter the state.")
            city=input("Enter city.")
            if valid_City(state.title(),city.title()):
                break
            else:
                print("Invalid city Please Enter Again")
        while True:
            dob=input("Enter dob(YYYY-MM-DD).")
            year,month,date=map(int,dob.split('-'))
            if valid_DOB(year,month,date):
                current_year=datetime.now().year
                age=current_year-year
                print(f"the year is.{year,month,date},the  age is.{age}")
                break
            else:
                print("Invalid dob Please Enter Again")
        while True:
            doj=input("Enter doj(YYYY-MM-DD).")
            year,month,date=map(int,dob.split('-'))
            if valid_DOJ(year,month,date):
                break
            else:
                print("Invalid date Please Enter Again")

        while True:
            dname=input("Enter Department name.")
            if valid_Depname(dname):
                break
            else:
                print("Invalid Department name Please Enter Again")
        while True:
            designation=input("Enter designation.")
            if valid_Designation(designation):
                break
            else:
                print("Invalid designation Please Enter Again")

        while True:
            pan=input("Enter Pan no(XXXXX0000X).")
            if valid_Pan(pan):
                break
            else:
                print("Invalid Pan no Please Enter Again")
        while True:
            adh=input("Enter Aadhar no(eg. 123412341234).")
            if valid_Aadhar(adh):
                break
            else:
                print("Invalid Aadhar no Please Enter Again")
        e=employee(id1,name,sal,age,gender,add,city,dob,doj,dname,designation,pan,adh)
        emp.append(e)

        for i in emp:
            i.display()

    elif choice==3:
        for i in emp:
            i.display()

    elif choice==2:
        eid=input("Enter the Employee id to delete the record.")
        flag = True
        for i in emp:
            if i.id1==eid:
                flag = False
                emp.remove(i)
        if flag==True:
            print("Employee id Not Found")
    

    elif choice==4:
        eid=input("Enter the Employee id.")
        for i in emp:
            if i.id1==eid:
                print("Press a to update the name of the employee.")
                print("Press b to update the address of the employee.")
                print("Press c to update the dob of the employee.")
                print("Press d to update the salary of the employee.")
                ch=input("Enter ur choice.")
                if ch=="a":
                    nm=input("Enter the updated name.")
                    i.name=nm
                elif ch=="b":
                    a=int(input("Enter the updated address."))
                    i.add=a
                elif ch=="c":
                    d=input("Enter the updated DOB.")
                    i.dob=d
                elif ch=="d":
                        eid=input("Enter the Employee_id to update the salary: ")
                        flag = True
                        for i in emp:
                            if i.id1==eid:
                                flag = False
                                new_sal = int(input("Enter new Salary: "))
                                i.sal = new_sal
                                print(f"Salary updated of the gievn Employee_id:{eid} ")
                                print(f"New Salary is : {new_sal}")
                        if flag==True:
                            print("Employee_id Not Found")

    elif choice==5:
        print("Press a to search by Employee_id.")
        print("Press b to search by Employee_name.")
        print("Press c to search by Department_name.")
        ch=input("Enter Your choice.")
        if ch=="a":
            eid=input("Enter the Employee_id to be searched.")
            for i in emp:
                if i.id1==eid:
                    i.display()
        elif ch=="b":
            nm=input("Enter the Employee_name to be searched.")
            for i in emp:
                if i.name==nm:
                    i.display()
        elif ch=="c":
            dn=input("Enter the Department_name to be searched.")
            for i in emp:
                if i.dname==dn:
                    i.display()
        else:
            print("Invalid choice")

    elif choice==6:
        sal=emp[0].sal
        for i in emp:
            if i.sal>sal:
                sal=i.sal
        for i in emp:
            if i.sal==sal:
                i.display()

    elif choice==7:
        sal=emp[0].sal
        for i in emp:
            if i.sal<sal:
                sal=i.sal
        for i in emp:
            if i.sal==sal:
                i.display()

    elif choice==8:
        break
    else:
        print("Enter valid choice")

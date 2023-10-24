from datetime import datetime


def valid_Empname(name):
    l=name.split()
    if len(l)==2 or len(l)==3:
        if len(l)==3:
            if (l[0].isalpha() and l[1].isalpha() and l[2].isalpha()):
                return True
        else:
            if (l[0].isalpha() and l[1].isalpha()):
                return True
    return False


def valid_Salary(sal):
    s=str(sal)
    if sal>=0 and s.isdigit():
        return True
    else:
        return False
#print (valid_Salary(30000))



def valid_Gender(g):
    gender=('M','F','T')
    if g.title() in gender:
        return True
    else:
        return False


def valid_City(state,city):
    sc={"Maha":["Mumbai","Pune","Nashik"],
         "MP":["Indore","Ujjain"],
         "Bihar":["Patna","Gaya","Nawada"],
         "UP":["Agra","Kanpur"]}
    v=sc[state]
    if city in v:
        return True
    else:
        return False
#print (valid_City("Maha","Nashik"))


def valid_DOB(year,month,date):
    if year<0:
        return False
    if month<1 or month>12:
        return False
    if month in {1,3,5,7,8,10,12} and (date<1 or date>31):
        return False
    elif month in {4,6,9,11} and (date<1 or date>30):
        return False
    elif month==2:
        if(year%4==0 and year%100==0) or (year%400==0):
            if date<1 or date>29:
                return False
        else:
            if date<1 or date>28:
                return False
    return True

def valid_DOB(year, month, date):
    try:
        dob_date = datetime(year, month, date)
        current_date = datetime.now()

        # Check if the DOB is not in the future and not too far in the past
        if dob_date <= current_date and current_date.year - year <= 100:
            return True
        else:
            return False
    except ValueError:
        return False


def valid_DOJ(year,month,date):
    if year<0:
        return False
    if month<1 or month>12:
        return False
    if month in {1,3,5,7,8,10,12} and (date<1 or date>31):
        return False
    elif month in {4,6,9,11} and (date<1 or date>30):
        return False
    elif month==2:
        if(year%4==0 and year%100==0) or (year%400==0):
            if date<1 or date>29:
                return False
        else:
            if date<1 or date>28:
                return False
    return True


def valid_Depname(dname):
    d={"It","Hr","Finance","Marketing","Sales"}
    if dname.title() in d:
        return True
    else:
        return False
#print (valid_Depname("HR"))

def valid_Designation(designation):
    de={"Manager","Software Developer","Accountant","Customer Service",
         "Marketing Coordinator","IT Support","Data Analyst"}
    if designation.title() in de:
        return True
    else:
        return False


def valid_Pan(pan):
    if pan.isalnum() and pan.isupper() and len(pan)==10 and pan[0:5].isalpha() and pan[5:9].isdigit() and pan[9].isalpha():
        return True
    else:
        return False
#print (valid_Pan("AAAAA0000A"))

def valid_Aadhar(adhno):
    if len(adhno)==12 and adhno.isdigit():
        return True
    else:
        return False
#print(valid_Aadhar("123412341234"))

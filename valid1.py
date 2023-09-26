def isGender(gender):
    if gender in('male','female','transgender'):
        return True

    return False


def isAge(age):
    if(len(age)==2 or len(age)==1):
        if(age.isdigit()):
            a=int(age)
            if a>1 and a<100:
                return True
    return False

 
def isAccountNumber(ac):
    if (len(ac)==12):
        if not ac.isdigit():
            return False
    return True

def isBankName(bn):
    n=list(bn.split())
    for i in n:
        if i.isalpha():
            if i.istitle():
                return True
            else:
                print("First character of word must be capital")
                return False
        else:
            print("Must be character")
            return False

def AccountHolderName(acn):
    n=list(acn.split())
    for i in n:
        if i.isalpha():
            if i.istitle():
                return True
            else:
                print("First character of word must be capital")
                return False
        else:
            print("Must be character")
            return False


def isIFSC(number):
    a1=number[0:4]
    a2=number[5:6]
    a3=number[6:12]
    if len(number)==11:
        if not s1.isupper():
            return False
        if not s2.isdigit():
            return False
        if not s3.isalnum():
            return False
    return True
    
def isAadhar(aadhar):
    if len(aadhar)==12:
       if aadhar.isdigit():
           return True
    return False

def isPan(pan):
    if len(pan)==10:
        s1=pan[0:5]
        s2=pan[5:9]
        s3=pan[9:10]
        if s1.isalpha() and s1.isupper() and s2.isdigit() and s3.isalpha() and s3.isupper():
            return True
    return False
   
def DOB(birth):
    if len(birth)==10:
        dd=int(birth[0:2])
        mm=int(birth[3:5])
        yy=int(birth[6:10])
        if not dd>0 and dd<=31:
            return False
        if not mm>0 and mm<13:
            return False
        if not yy>1900 and yy<2023:
            return False
    return True



def isCity(city):
   if city.isalpha():
       return True

def isTypeAc(typeac):
    if typeac in ["savings","current","joint"]:
        return True
    return False

def isAddress(add):
   if add.isalnum():
       return True

def isBalance(bal):
   if bal.isdigit():
        b=int(bal)
        if b>0:
            return True
        else:
            return False


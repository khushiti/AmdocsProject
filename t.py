
from valid1 import *
class Bank:

    BankDict={}
    def __init__(self,bn,ifsc,ac,acn,age,gender,dob,add,city,typeac,bal,pan,aadhar):
        self.bn=bn
        self.ifsc=ifsc
        self.ac=ac
        self.acn=acn 
        self.age=age
        self.gender=gender
        self.dob=dob
        self.add=add
        self.city=city
        self.typeac=typeac
        self.bal=bal
        self.pan=pan
        self.aadhar=aadhar
        if self.bn in self.BankDict.keys():
            self.BankDict[self.typeac].append(self.acn)
        else:
            self.BankDict[self.typeac]=[self.acn]
    def display(self):
        print(self.bn," ",self.ifsc," ",self.ac," ",self.acn," ",self.age," ",self.gender," ",self.dob," ",self.add," ",self.city," ",self.typeac," ",self.acn," ",self.bal," ",self.pan," ",self.aadhar," ")
    def displaybalance(self):
        print(self.bal)
    def update_name(self,new):
        self.acn=new
    def update_address(self,newadd):
        self.add=newadd
    def update_dob(self,newdob):
        self.dob=newdob
        

    def transfer_funds(self,account,amount):
        if amount>0 and self.bal>=0:
            self.bal=self.bal-amount
            account.bal=account.bal+amount
            return true
        else:
            return False
banklist=[]
print("Bank Management System")
print(" ")
while True:
    print("************************")
    print("1:Create account")
    print("2:Display Account")
    print("3:Update Account Details")
    print("4:Deposit")
    print("5:Withdraw")
    print("6:funds Transfer")
    print("7:Search details of account holder")
    print("8:Balance Inquiry")
    print("9:Delete account")
    print("10:Exit")
    print("************************")
    choice=int(input("Enter your choice"))
    if(choice==1):
        while True:
            bn=input("Enter your bank name:")
            if isBankName(bn):
                break
            else:
                print("Invalid Bank Name")

        while True:
            ifsc=input("Enter your IFSC code:")
            if(isIFSC(ifsc)):
                break
            else:
                print("Invalid IFSC number")
            
        while True:
            ac=input("Enter your Account Number:")
            if(isAccountNumber(ac)):
                break
            else:
                print("Invalid Account Number")
                    
                    
        while True:
            acn=input("Enter account holder name:")
            if(AccountHolderName(acn)):
                break
            else:
                print("Invalid name")
        while True:
            age=input("Enter your age:")
            if(isAge(age)):
                break
            else:
                print("Invalid age")
            
        while True:
            gender=input("Enter your gender:")
            if(isGender(gender)):
                break
                
            else:
                print("Invalid")
        while True:
            dob=input("Enter date of birth in the form(DD-MM-YY):")
            if(DOB(dob)):
                break
            else:
                print("Invalid")
            
        while True:
            add=input("Enter your address:")
            if(isAddress(add)):
                break
            else:
                print("Invalid")
        while True:
            city=input("Enter your city:")
            if(isCity(city)):
                break
            else:
                print("Invalid")
        while True:
            typeac=input("Enter the type of your account:")
            if(isTypeAc(typeac)):
                break
            else:
                print("Invalid")
        while True:
            bal=input("Enter your account balance:")
            if(isBalance(bal)):
                break
            else:
                print("Invalid")
        while True:
            pan=input("Enter your pan card number:")
            if(isPan(pan)):
                break
            else:
                print("Invalid")

        while True:
            aadhar=input("Enter your aadhar number:")
            if(isAadhar(aadhar)):
                break
            else:
                print("Invalid")
        b=Bank(bn,ifsc,ac,acn,age,gender,dob,add,city,typeac,bal,pan,aadhar)
        banklist.append(b)

    elif(choice==2):
        for i in banklist:
            i.display()

    elif(choice==3):
        print(" ")
        print("Press A to update name")
        print("Press B to update address")
        print("Press C to update DOB")
        ch1=input("Enter your choice:")
        if ch1=='A':
            n2=input("Enter the name of account holder")
            for i in range(len(banklist)):
                if banklist[i].acn==n2:
                    new=input("Enter new name")
                    banklist[i].update_name(new)
        
        elif ch1=='B':
              n2=input("Enter the account number to update address:")
              for i in range(len(banklist)):
                if banklist[i].acn==n2:
                    newadd=input("Enter new name")
                    banklist[i].update_address(newadd)
        


        elif ch1=='C':
            for i in range(len(banklist)):
                if banklist[i].acn==n2:
                    newdob=input("Enter new name")
                    banklist[i].update_dob(newdob)
        


        else:
            print("Invalid choice")




    elif(choice==4):
        nm=input("Enter account holder name:")
        for i in range(len(banklist)):
            if banklist[i].acn==nm:
                amount=input("Enter amount to be deposited:")
                if(amount.isdigit()):
                    a=float(amount)
                    if(bal.isdigit()):
                       b=float(bal)
                    if(a>=b or a<=b):
                        banklist[i].bal=a+b

    elif(choice==5):
        nm=input("Enter account holder name:")
        for i in range(len(banklist)):
            if banklist[i].acn==nm:
                amount=input("Enter amount to be withdrawed")
                if amount.isdigit():
                    a=float(amount)
                    if bal.isdigit():
                        b=float(bal)
                        if(a<=b):
                            banklist[i].bal=b-a
                            print("Amount Withdrawed")
                        else:
                            print("Insufficient balance")

    elif(choice==6):
        acc1=input("Enter the First Account Number")
        acc2=input("Enter the Secons Account Number")
        amount=float(input("Enter the amount you want to transfer"))
        acc1_exists=False
        acc2_exists=False

        for b in banklist:
            if b.ac==acc1:
                acc1_exists=True
            elif b.ac==acc2:
                acc2_exists=True

        if acc1_exists and acc2_exists:
            for b in banklist:
                if b.ac==acc1:
                    sender=i
                elif b.ac==acc2:
                    account=i

            if sender.transfer_funds(account,number):
                print("Funds transfer successful")
                print("Balance for sender",sender.bal)
                print("New balance for reveiver",account.bal)
            else:
                print("Funds transfer failed")
        else:
            print("Accounts don't exists")
                
    elif(choice==7):
        print(" ")
        print("Press A to search by account number:")
        print("Press B to search by name:")
        print("Press C to search by type of account:")
        ch=input("Enter your choice:")
        if(ch=="A"):
            a1=int(input("Enter the account number to be searched:"))
            for i in banklist:
                if ac.isdigit():
                    a=int(ac)
                    if a1.isdigit():
                        a2=int(a1)
                        if a2==a1:
                            i.display()
        elif(choice=="B"):
            nm=input("Enter name to be searched:")
            for i in banklist:
                if i.acn==nm:
                    i.display()
        elif(choice=="C"):
            t=input("Enter type of account:")
            for i in banklist:
                if i.typeac==t:
                    i.display()
        else:
            print("Invalid choice!!")
        

    elif(choice==8):
        name=input("Enter account holder name:")
        for i in range(len(banklist)):
            if banklist[i].acn==name:
                print("Account balance is",banklist[i].bal,"INR")

    elif(choice==9):
        name=input("enter account holder name:")
        flag=True
        for i in banklist:
            if i.acn==name:
                flag==False
                banklist.remove(i)
                break
            if flag:
                print("Not found")

    elif(choice==10):
        print("Exit")
        break
            

                
            




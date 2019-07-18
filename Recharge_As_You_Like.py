def Data():
    amount=int(input("\n\t\tEnter your amount "))
    if amount>0:
        calculate=(amount/400)*1000
        print(calculate,"mb")
    else:
        print("Enter amount greater than 0")
    
def Talk_Time():
    amount1=int(input("\n\t\tEnter your talktime amount "))
    if amount1>0:
        calculate1=(amount1/150)*100
        s=amount1/(amount1-2.5)
        print("Talktime of " ,calculate1 ,"\nservice tax of" ,s, "\nRecharge is successful")
        print("Current balance is" , calculate1 ,"rs")
    else:
        print("Enter amount greater than 0")

def smart():
    amount1=int(input("\n\t\tEnter your amount "))
    if amount1>0:
        calculate1=(amount1/200)*100
        s=amount1/(amount1-2.53)
        calculate=(amount1/550)*1000        
        print("Talktime of " ,calculate1 ,"\nservice tax of" ,s, "\n")
        print("Current talktime balance is" , calculate1 ,"rs")
        print("Current data balance is" ,calculate,"mb")
        print("\n\tRecharge Successful\n")
    else:
        print("Enter amount greater than 0")
        
p=input("\twelcome to Recharge as you like \n  ")

w=int(input("Do you want to recharge(1/0)  "))

if w==1:
    
    print("\t\t\t welcome\t")
    name=input("\t\tEnter your name: \t")
    mobile=input("\t\tEnter mobile nummber: \t")
    plan=input("\t\tSelect your choice: data / talktime/ smart recharge\t ")#(0:data / 1:talktime) \t ")
    if(plan=='talktime' or plan == 'Talktime' or plan == 'TALKTIME'):
        Talk_Time()
    elif (plan == 'data' or plan == 'Data' or plan == 'DATA'):
        Data()
    else:
        smart()
    

elif w==0:
        print("thank you")
else:
    print("error")





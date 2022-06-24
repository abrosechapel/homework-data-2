# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 10:40:36 2022

@author: User
"""

#pin_input=input("insert your pin code: ")
#pin_code={'1192':["Enrico",100],'1193':["Luciano",2000]}
#pin_code={'1192':["Enrico",100],'1193':["Luciano",-10]}
def pin_validation(pin_code,pin_input):
    op=3
    pin_input=str(pin_input)
    try: 
        #while True:
            #assert 1<op<=3
            if len(pin_input)==4:
                   if pin_input in pin_code.keys():
                      return "True"
                      #break
                   elif  pin_input not in pin_code.keys():
                       #op-=1
                       #print("Wrong pin code, try again, you have {} attemps".format(op))
                       #pin_input=input("insert your pin code: ")
                       #return "pin code doen't exist try aggain"
                       return "False"
            elif len(pin_input)<4:
                   #op-=1
                   #print("Wrong pin code, try again, you have {} attemps".format(op))
                   #return "wrong pin code"
                   #pin_input=input("insert your pin code: ")
                   return "False"
                           
    except:                    
    #except AssertionError:
           #print("Wrong pin code,You don't have more attemps")
           #return "Wrong pin code"
           return False
    
                

#act=input("Do You want to do an operation? yes(y) or no(n): ")

def operation(pin_input,pin_code,act):
     if pin_validation(pin_code,pin_input)=="True":
         balance=pin_code[pin_input][1]
         #act=input("Do You want to do an operation? yes(y) or no(n): ")
         try:
          #while True:
            if len(act)==1 and act=="y":
               operation=input( "What operation do you want to do? " + " 1 balance 2 Withdraw ")
               if operation=="1":
                   if balance>0:
                      return balance
                      #return "You have in your account: {} ".format(balance)
                      #act=input("Do You want to do an operation? yes(y) or no(n): ")
                      #if act=="n" :
                          #break
                   elif balance<0:
                      return "incorrect ammount, You can't do an operation"
               elif operation=="2":
                   money=float(input("How much do you want to Withdraw? "))
                   if balance> money and balance>=0:
                       balance=balance-money
                       #pin_code[pin]=[name,balance]
                       return balance
                       #"Successful operation"
                       #act=input("Do You want to do an operation? yes(y) or no(n): ")
                       #if act=="n" :
                          #break
                       
                   elif balance<money:
                       raise ValueError
                   else:
                       return "transaction can't be done"
                       #break
            elif len(act)>1 and act !="n":
                 return "Wrong option"
                 #act=input("Do You want to do an operation? yes(y) or no(n): ")
                 #if act=="n" :
                       #return "wrong option"
                 #print("What operation do you want to do? ")
                 #operation=input(" 1 balance 2 Withdraw ")
            else:
                 return "Wrong option"
                 #act=input("Do You want to do an operation? yes(y) or no(n): ")
                 #if act=="n" :
                          #break
         except ValueError:
              return "The withdraw is more than the balance,transaction can't be done"
         except:
              return "transaction can't be done"
         #finally:
           #return "Thanks for use our service"
          
            
def update_balance(pin_input, pin_code, act):
    balance=operation(pin_input,pin_code, act)
    pin_code[pin_input][1]=balance
    return pin_code
    
    

    
    
    
    

    
   
    
    
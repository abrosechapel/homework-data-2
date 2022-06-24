# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 10:40:36 2022

@author: Carla Bailón Rosas

"""
###TASK 1 (Git and GitHub)###

##Question 1##

"""
Complete definitions for key Git & GitHub terminology
"""

#GIT WORKFLOW FUNDAMENTALS
#Working Directory
      #The working directory is created with the git init command, 
      #and it is the folder project and where it is located.
#Staging Area
      #It is the place where the things being recorded before use the commit command. 
      #The Staging Area is a simple file, usually stored in your Git directory, 
      #which collects information about what will be present in the next commit 
      #and then pushes our code to the Git repository.
#Local Repo (head)	
      #It is the repository installed or located in our computer.
#Remote repo (master)
      #It is installed in a remote computer as central repository. 
      #It could be in GitHub, GitLab. The remote repo allows us to synchronize 
      #our repository with another (or others) in a different location.

#WORKING DIRECTORY STATES:
#Staged
      #Staged are archive in staging but it has not been committed. The file 
      #is ready to be added to the local git database. They live inside Git 
      #and there is a record of them because they have been affected by the git 
      #add command. 
#Modified
      #The files has changes but has not been added to the staging area. 
      #In this state is currently working and there will be changes. 
      #The file has not been committed yet.
#Committed
      #This state indicates that the file is stored in the local database. 
      #We use the git commit command. The changes of the file have been stored 
      #like a snapshot.
 
#GIT COMMANDS:
#Git add
     #The git add command adds content from the working directory to the staging 
     #area (or 'index') for the next commit. When the git commit command is run, 
     #by default it only looks at this staging area, so git add is used to fabricate 
     #exactly what you'd like your next commit snapshot to be.
#Git commit
     #git commit captures a snapshot of the project's currently committed changes.
#Git push
     #The git push command allows you to push commits from your local branch 
     #in your local git repository to the remote repository.
#Git fetch
     #git fetch is the command that makes your local Git repository update 
     #with the latest information from the remote repository, but doensn’t do 
     #any file transfers to your local workspace.
#Git merge
     #The git merge tool is used to merge one or more branches into your 
     #active branch. It will then advance the current branch to the result 
     #of the merge.
#Git pull
     #git pull is used to pull and download content from a remote repository 
     #and instantly update the local repository to reflect that content.




###TASK 2 (Exception Handling)###

##Question 1##

"""
Simple ATM program
Using exception handling code blocks such as try/ except / else / finally, 
write a program that simulates an ATM machine to withdraw money.
(NB: the more code blocks the better, but try to use at least two key words 
e.g. try/except)
Tasks:
1.Prompt user for a pin code
2.If the pin code is correct then proceed to the next step, otherwise ask a 
  user to type in a password again. You can give a user a maximum of 3 
  attempts and then exit a program.
3.Set account balance to 100.
4.Now we need to simulate cash withdrawal
5.Accept the withdrawal amount
6.Subtract the amount from the account balance and display the remaining 
  balance (NOTE! The balance cannot be negative!)
7.However, when a user asks to ‘withdraw’ more money than they have on their 
  account, then you need to raise an error an exit the program. 

"""
#pin_code={'1192':["Enrico",100],'1193':["Luciano",2000]}--> you can use this instead the other

pin_input=input("insert your pin code: ")
def atm_program(pin_input):
    pin_code={'1192':["Enrico",100],'1193':["Luciano",-10]}
    op=3
    flag=False
    try:
        while True:
            assert 1<op<=3
            if len(pin_input)==4:
                   if pin_input in pin_code.keys():
                      name=pin_code[pin_input][0]
                      balance=pin_code[pin_input][1]
                      flag=True
                      break
                   elif  pin_input not in pin_code.keys():
                       op-=1
                       print("Wrong pin code, try again, you have {} attemps".format(op))
                       pin_input=input("insert your pin code: ")
            elif len(pin_input)<4:
                   op-=1
                   print("Wrong pin code, try again, you have {} attemps".format(op))
                   pin_input=input("insert your pin code: ")
                        
    except AssertionError:
           print("Wrong pin code,You don't have more attemps")
                
    if flag==True:
        print("****************************************************************************")
        print("*                                                                          *")
        print("*                   Welcome {} to  ATM SYSTEM                                 *".format(name))
        print("*                                                                          *")
        print("****************************************************************************")
        act=input("Do You want to do an operation? yes(y) or no(n): ")
        act=act.lower()
        try:
          while True:
            if len(act)==1 and act=="y":
               operation=input( "What operation do you want to do? " + " 1 balance 2 Withdraw ")
               if operation=="1":
                   #return balance
                   if balance>0:
                      print( "You have in your account: {} ".format(balance))
                      act=input("Do You want to do an operation? yes(y) or no(n): ")
                      if act=="n" :
                          break
                   elif balance<0:
                      print("incorrect ammount, You can't do an operation")
               elif operation=="2":
                   money=float(input("How much do you want to Withdraw? "))
                   if balance> money and balance>=0 :
                       balance=balance-money
                       pin_code[pin_input][1]=balance
                       print(pin_code)
                       print("Successful operation")
                       act=input("Do You want to do an operation? yes(y) or no(n): ")
                       if act=="n" :
                          break
                   elif balance<money:
                       raise ValueError
                       break
                   else:
                       print("transaction can't be done")
            elif len(act)>1 and act !="n":
                 print("Wrong option")
                 act=input("Do You want to do an operation? yes(y) or no(n): ")
                 if act=="n" :
                          break
            else:
                 print("Wrong option")
                 act=input("Do You want to do an operation? yes(y) or no(n): ")
                 if act=="n" :
                          break
        except ValueError:
              print("The withdraw is more than the balance")
              print("transaction can't be done")
        except:
              print("transaction can't be done")
        #else:
           #return balance
        finally:
            print("Thanks for use our service")
              
              
   
           
    
          
atm_program(pin_input)
   
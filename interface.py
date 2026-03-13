from Ironman import ironman_op
from Access import *


auth = Authentication()
int_acc = suite_access_protection()
print('\nHello Welcome to VS Technology')
while True:
    print()
    #section for creating password
    first_acc = int(input("If You are New User Choose 1 to Create Password\nIf you Forgot Your Password Choose 2 to Update\nIf you are already a user? choose any number to Login\nEnter Your Option:  "))
    if first_acc == 1:
        cr_pass = int_acc.create_pass()
        if cr_pass != True:
            continue
    
    #section for Updating Password
    elif first_acc == 2:
        updt_pass = int_acc.update_pass()
        if updt_pass != True:
            continue
    
    #Section for Login
    else:
         while True:
            #interface login
            login_int = auth.interface_access()
            if login_int:
                print("Welcome Sir select Operations ")
                break
            else:
                for_pass = int(input('Forgot Password ? Choose 1 : '))        
                if for_pass == 1: 
                    break                    
                else:
                    continue
    
            
        


        
        # print('Choose Operations')
        # op = input('What you need to do ?: ')

        # if op is None:
        #     break
        # else: continue
                






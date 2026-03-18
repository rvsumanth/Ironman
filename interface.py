from ironman_operations import *
from Access import *
from utils import *


auth = Authentication()
int_acc = suite_access_protection()
suite_op = ironman_op()

print('\nHello Welcome to VS Technology')
while True:
    print()
    #section for creating password
    first_acc = int(input("1. Create Password\n2. Update Password\nChoose any number to Login\nEnter Your Option:  "))
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
                # Selecting Opearations
                print("\nWelcome Sir select Operations ")
                suite_is_flying = 0
                while True:
                    sel_op = int(input('\nOperations: \n1. Fly \n2. Land \n3. Launch Missile\n4. exit \nEnter here: '))
                    #fly
                    if sel_op == 1:
                        if suite_is_flying ==1:
                            print("\nSuite is already Flying")
                            continue
                        else:
                            fly  = suite_op.start_ign()
                            if fly: 
                                suite_is_flying = 1
                                
                     #Land   
                    elif sel_op == 2:
                        if suite_is_flying == 0:
                            print("\nSuite is already in Land")
                            continue
                        else:
                            lnd = suite_op.stop_ign()
                            if lnd:
                                suite_is_flying = 0
                    
                    #Launch Missile
                    elif sel_op == 3:
                        launch = suite_op.launch_missile()
                    
                    #exit
                    else:
                        if suite_is_flying == 1:
                            lnd_frc = 0
                            while lnd_frc == 0:
                                log_force = land_forceful()
                                if log_force:
                                    lnd_frc = 1
                                    break
                                else: 
                                    continue

                            if lnd_frc == 1:
                                break

                        elif suite_is_flying == 0:        
                            print("Logged out")
                            break

                        else:
                            print("Log out unsuccessful")
                            continue

                    
            else:
                for_pass = int(input('Forgot Password ? Choose 1 or Choose any number to login again: '))        
                if for_pass == 1: 
                    break                    
                else:
                    continue
    
            
        


        
     
                






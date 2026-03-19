from ironman_operations import *
from Access import *
from utils import *
from config import *


auth = Authentication()
int_acc = suite_access_protection()
suite_op = ironman_op()
print('\n================================')
print('Hello Welcome to VS Technology')
print('================================')
while True:
    print()
    #section for creating password
    first_acc = int(input("1. Create Password | 2. Update Password\nChoose any number to Login\nEnter Your Option:  "))
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
                print('\n================================')
                print("Welcome Sir select Operations ")
                print('================================')
                suite_is_flying = 0
                start_time = None
                while True:
                    sel_op = int(input('Operations: \n1. Fly | 2. Land | 3. Launch Missile | 4. Check Altitude | 5. exit \nEnter here: '))
                    #fly
                    if sel_op == 1:
                        if suite_is_flying ==1:
                            print("\nSuite is already Flying\n")
                            continue
                        else:
                            fly  = suite_op.start_ign()
                            if fly: 
                                suite_is_flying = 1
                                start_time = time.time()
                                
                     #Land   
                    elif sel_op == 2:
                        if suite_is_flying == 0:
                            print("\nSuite is already in Land\n")
                            continue
                        else:
                            lnd = suite_op.stop_ign()
                            if lnd:
                                suite_is_flying = 0
                    
                    #Launch Missile
                    elif sel_op == 3:
                        launch = suite_op.launch_missile()
                    
                    #check altitude
                    elif sel_op == 4:
                        if suite_is_flying == 1 :
                            alti_check = suite_op.get_altitude(start_time, suite_is_flying)
                            fly_time = flying_time(start_time, suite_is_flying)
                            fli_min = fly_time/60
                            print(f'\nSuite is flying since {fli_min:.1f} minutes')
                            print(f'\nSuite Current altitude: {alti_check:.2f} meters\n ')
                        else: print('\nSuite is on land impossible to fetch altitude\n')

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
                            print('================================')      
                            print("Logged out")
                            print('================================')
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
    
            
        


        
     
                






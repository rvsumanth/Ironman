from Ironman import ironman_op
from Access import *


auth = Authentication()
acc = suite_access_protection()
while True:
    print('Hello Welcome')
    #section fro creating password
    first_acc = int(input("Firstime accessing? choose 1 to Create Password or Already a user? choose any number to Login: "))
    if first_acc == 1:
        cr_pass = acc.create_pass()
        if cr_pass : 
            print('Password Created!')
        else :
            print('Password Creation Denied! Retry it')

    else:
        #Section for Login
        access_pass = input("Hello Enter Password to Access Interface: ")
        if auth.interface_access(access_pass):
            print("Access Granted")
        else:
            print("Access Denied")
            #section for Forgot password
            forgot_pass = int(input("Forgot Password? Don't worry Choose 1 for Update Password or choose any number to login: "))
            if forgot_pass == 1:
                up_pass = acc.update_pass()
                if up_pass :
                    print('Updated Successfully')
                else:
                    print('Password Updation Denied! Retry with new one')
            else: continue
        
        print('Choose Operations')
        op = input('What you need to do ?: ')

        if op is None:
            break
        else: continue
                






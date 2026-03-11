from Ironman import ironman_op
from Access import *


while True:
    access_pass = input("Hello Enter Password to Access Interface: ")
    forgot_pass = int(input("Forgot Password ? Don't worry \n Choose 1 for Update Password"))
    auth = Authentication()
    if auth.interface_access(access_pass):
        print("Access Granted")

    else:
        print("Access Denied")
        break







x = ironman_op()

x.
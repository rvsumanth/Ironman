# from ironman_operations import *
from Access import *
import time

from ironman_operations import *

suite_op = ironman_op()
suite_auth = Authentication() 
suite_acss = suite_access_protection()

def land_forceful():
    log_out = int(input("\nSuite is on air.\nif you log out you loose all your controls\nLand the suite and get Log out\nEnter 1 to land suite:  "))
    if log_out ==1:
        land = suite_op.stop_ign()
        print("\nLogged out")
        return True
    else:
        print('\nInvalid Option')
        return False
    

    

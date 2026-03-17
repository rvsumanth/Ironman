import time

class ironman_op:
    def __init__(self):
        pass

    def start_ign(self):
        print("\nIgnition Started. Ready to fly")
        while True:
            fly = input('\nType "yes" to fly or Type "no" for cancel operation: ')
            if fly in ['yes', 'YES', 'Yes']:
                #5 sec time setted for flying
                sec = 5
                for i in range(sec,0,-1):
                    print(i)
                    time.sleep(1)
                print("\nFlying")
                return True
                break
            
            elif fly in ['No', 'no','NO']:
                print('\nTerminating')
                sec = 5
                for i in range(sec,0,-1):
                    print(i)
                    time.sleep(1)
                print('\nOperation Terminated. Ignition stoped')
                return False
                break
            
            else: 
                print("\nInvalid Command")
                continue
            

    def stop_ign(self):
        print('\nStoping Ignition. Ready to land')
        while True:
            land = input('\nType "yes" to land or Type "no" to cancel the landing: ')
            if land in ['yes', 'YES', 'Yes']:
                print("\nLanding")
                #Timer set to 10 sec for landing
                sec = 10
                for i in range(sec,0,-1):
                    print(i)
                    time.sleep(1)            
                print("\nLanded Successfully")
                #Timer set to 5sec to stop the ignition
                print('\nStoping Ignition') 
                resec = 5
                for i in range(resec, 0, -1):
                    print(i)
                    time.sleep(1)
                print("\nIgnition Stoped")
                return True
                break
            
            elif land in ['No', 'no','NO']:
                print("Operation Terminating")
                resec = 5
                for i in range(resec, 0, -1):
                    print(i)
                    time.sleep(1)
                print("\nOperation Terminated")
                return False
                break
            
            else:
                print('Invalid Command')
                continue



    def missile_sel():
        pass

    def beam():
        pass

    def trace_call():
        pass

    def trace_ip_dev():
        pass

    def track_img():
        pass

    def identify_img():
        pass

    def search():
        pass
    
#testing missile launching operation
import time
def launch_missile():
        print('\nInitiating Missile Lauching Program')
        #Number Missiles in Ammunation
        range_100 = 100
        range_500 = 100
        range_1000 = 100
        missiles = [100,500,1000]
        print(f'\nTotal Missiles Ammunation\n1. 100 meters ranged missiles: {range_100}\n2. 500 meters ranged missiles: {range_500}\n3. 1000 meters ranged missiles: {range_1000}')

        target_list = ['Building', 'Bunker', 'Tanker', 'Helicopter', 'Jet planes']

        while True:
            option = int(input('\nSelect Missile Range\n 1. 100m\n 2. 500m\n 3. 1000m\nGeneral Options\n 4. Missiles Quantity\n 5. Terminate Launching\nEnter your Option: '))
            
            if option == " " :
                print('\nInvalid Range')
                continue
            # 100 meter missile
            elif option == 1 :
                
                print(f'\nTotal Quantity of 100 meters Ranged missiles: {range_100}')
                if range_100 != 0:
                    
                    #Selecting Target
                    target = int(input('\nSelect Target\n1. Buildings\n2. Bunkers\n3. Tankers\n4. Helicopters\n5. Jet Planes\nEnter Your Option :  '))
                    
                    if target in [1,2,3,4,5]:
                        print('\nTarget Locked')

                        #selecting quantity of missiles
                        missile_qty =  int(input('\nEnter number of missiles to launch on target: '))

                        if missile_qty <= range_100 :
                            sec = 3

                            for i in range(1, missile_qty+1):
                                print(f'\nLaunching {missiles[option-1]}mtr missile {i} on {target_list[target-1]}')
                                for j in range(sec, 0, -1): 
                                    print('countdown: ')       #timer
                                    print(j)
                                    time.sleep(1)
                                print(f"\n{i} Missile launched Successfully")
                                range_100 -= 1              #decreasing missile quantity
                                print(f'Remaining 100 meters range missiles: {range_100}')
                            
                            # return True
                            

                        else:
                            print('\n Insufficient missile quantity')
                            # return False
                            continue
                                        
                    else:
                        print('\nInvalid Target')
                        # return False
                        continue
                
                else: 
                    print('Insufficient Missiles quantity\nLaunching cannot be initiated')
                    # return False
                    continue
                
            # 500 meter missile
            elif option == 2 :
                
                print(f'Total quantity of 500 meters ranged missiles: {range_500}')
                if range_500 != 0:
                    
                    #Selecting Target
                    target = int(input('\nSelect Target\n1. Buildings\n2. Bunkers\n3. Tankers\n4. Helicopters\n5. Jet Planes\nEnter Your Option :  '))
                    
                    if target in [1,2,3,4,5]:
                        print('\nTarget Locked')

                        #selecting quantity of missiles
                        missile_qty =  int(input('\nEnter number of missiles to launch on target: '))

                        if missile_qty <= range_500 :
                            sec = 3

                            for i in range(1, missile_qty+1):
                                print(f'\nLaunching {missiles[option-1]}mtr missile {i} on {target_list[target-1]}')
                                for j in range(sec, 0, -1): 
                                    print('countdown: ')       #timer
                                    print(j)
                                    time.sleep(1)
                                print(f"\n{i} Missile launched Successfully")
                                range_500 -= 1              #decreasing missile quantity
                                print(f'Remaining 500 meters range missiles: {range_500}')
                            
                            # return True
                        else:
                            print('\n Insufficient missile quantity')
                            # return False
                            continue
                                        
                    else:
                        print('\nInvalid Target')
                        # return False
                        continue
                
                else: 
                    print('Insufficient Missiles quantity\nLaunching cannot be initiated')
                    # return False
                    continue
                
            # 1000 meters missile
            elif option == 3 :
                
                print(f'Total quantity of 1000 meters ranged missiles: {range_1000}')
                if range_1000 != 0:
                    
                    #Selecting Target
                    target = int(input('\nSelect Target\n1. Buildings\n2. Bunkers\n3. Tankers\n4. Helicopters\n5. Jet Planes\nEnter Your Option :  '))
                    
                    if target in [1,2,3,4,5]:
                        print('\nTarget Locked')

                        #selecting quantity of missiles
                        missile_qty =  int(input('\nEnter number of missiles to launch on target: '))

                        if missile_qty <= range_1000 :
                            sec = 3

                            for i in range(1, missile_qty+1):
                                print(f'\nLaunching {missiles[option-1]}mtr missile {i} on {target_list[target-1]}')
                                for j in range(sec ,0, -1):
                                    print('countdown: ')        #timer changed
                                    print(j)
                                    time.sleep(1)
                                print(f"\n{i} Missile Launched Successfuly")
                                range_1000 -= 1              #decreasing missile quantity
                                print(f'Remaining 1000 meters range missiles: {range_1000}')
                            
                            # return True
                        else:
                            print('\n Insufficient missile quantity')
                            # return False 
                            continue
                                        
                    else:
                        print('\nInvalid Target')
                        # return False
                        continue
                
                else: 
                    print('Insufficient Missiles quantity\nLaunching cannot be initiated')
                    # return False 
                    continue

            #Getting Missile Quanity
            elif option == 4:
                print('\nMissile Quantity')
                print(f'100 mts(R) Missile: {range_100}\n500 mts(R) Missile: {range_500}\n1000 mts(R) Missile: {range_1000}')
            
            #Terminating Operation
            else:
                print('\nLaunching Terminated')
                return False
                break
       

launch_missile()
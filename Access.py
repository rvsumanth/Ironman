class suite_access_protection():
    interface_pass = []
    # def __init__(self):
    #     pass

    def create_pass(self):
        user_data = input('\nCreate a Password: ')
        if user_data == '':
            print("Password Creation Denied! Try again")
            return False
        else:
            self.interface_pass.append(user_data)
            print('Password Created') 
            return True
                

    def update_pass(self):
        user_data = input("\nEnter a new password to update: ")
        if user_data not in self.interface_pass and user_data != '' :
            self.interface_pass.append(user_data)
            print('Updated Successfully')
            return True
        else:
            print('Password Updation Denied! Retry with new one')
            return False
        




class Authentication(suite_access_protection):

    def __init__(self):
        super().__init__()
        pass


    def interface_access(self):
        user_enter_pass = input("\nEnter Password to Access Interface: ")
        if user_enter_pass in self.interface_pass :
            print('\nAccess Granted')
            return True
        else:
            print("\nWrong Password! Access Denied")
            return False




































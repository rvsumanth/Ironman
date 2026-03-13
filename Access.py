class suite_access_protection():
    interface_pass = []
    # def __init__(self):
    #     pass

    def create_pass(self):
        user_data = input('Create a Password: ')
        if user_data == '':
            print("Password Creation Denied! Try again")
            return False
        else:
            self.interface_pass.append(user_data)
            print('Password Created') 
            return True
                

    def update_pass(self):
        user_data = input("Enter a new password to update: ")
        if user_data not in self.interface_pass and user_data != '' :
            self.interface_pass.append(user_data)
            print('Updated Successfully')
            return True
        else:
            print('Password Updation Denied! Retry with new one')
            return False
        

    # def get_pass(self):
    #     return self.interface_pass 



class Authentication(suite_access_protection):

    def __init__(self):
        super().__init__()
        pass


    def interface_access(self):
        user_enter_pass = input("Enter Password to Access Interface: ")
        if user_enter_pass in self.interface_pass :
            print('Access Granted')
            return True
        else:
            print("Wrong Password! Access Denied")
            return False

    # def interface_pass_creating(self):
    #     x = self.create_pass()
    #     if x : 
    #         return "Password Created" , True
    #     return "Password Creation Denied! Try again" , False

    # def interface_login(self):
    #     user_enter_pass = input("Hello Enter Password to Access Interface: ")
    #     if self.interface_access(user_enter_pass):
    #         return 'Access Granted', True
    #     return 'Access Denied', False




































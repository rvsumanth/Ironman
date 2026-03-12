class suite_access_protection():
    interface_pass = []
    # def __init__(self):
    #     pass

    def create_pass(self):
        user_data = input('Create a Password: ')
        if user_data is not None:
            self.interface_pass.append(user_data) 
            return True
        return False
                

    def update_pass(self):
        user_data = input("Enter a new password to update: ")
        if user_data not in self.interface_pass and user_data is not None :
            self.interface_pass.append(user_data)
            return True
        return False
        

    # def get_pass(self):
    #     return self.interface_pass 



class Authentication(suite_access_protection):

    def __init__(self):
        super().__init__()
        pass


    def interface_access(self, user_enter_pass):
        if user_enter_pass in self.interface_pass :
            return True
        else:
            return False





































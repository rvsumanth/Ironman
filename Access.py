class suite_access_protection():
    interface_pass = ' '
    # def __init__(self):
    #     pass

    def create_pass(self,user_data):
        if user_data is not None:
            self.interface_pass = user_data
        # return self.interface_pass
        

    def get_pass(self):
        return self.interface_pass
        

    def update_pass(self,user_data):
        Updated_pass = ''
        if user_data != self.get_pass() and user_data is not None :
            Updated_pass = user_data
            self.interface_pass = Updated_pass
        


#testing
while True:
    n = suite_access_protection()
    a = int(input('1.create pass, 2.Update password'))
    if a == 1:
        
        print("Default password:",n.interface_pass)
        user_data = input("create a new password: ")
        n.create_pass(user_data)
        print('Password Created')
        print("display new password:",n.get_pass())
        
    
    elif a == 2:
        
        print("Default password:",n.interface_pass)
        update_data = input("Enter a password to update: ")
        n.update_pass(update_data)
        print("Password Updated")
        print("Updated password:",n.get_pass())
        
    else:
        print('Invalid Option')


# class Authentication(suite_access_protection):

#     def __init__(self):
#         super().__init__()
#         pass
    

#     def interface_access(self, user_enter_pass):
#         if user_enter_pass == self.get_pass() :
#             return True
#         else:
#             return False





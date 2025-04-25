'''1. Write a class called Password_manager. The class should have a list called old_passwords that
holds all of the user’s past passwords. The last item of the list is the user’s current pass word.
There should be a method called get_password that returns the current password and a method
called set_password that sets the user’s password. The set_password method should only
change the password if the attempted password is different from all the user’s past passwords.
Finally, create a method called is_correct that receives a string and returns a boolean True or
False depending on whether the string is equal to the current password or not.'''
                
class Password_manager:
    def __init__(self,old_passwords:list):
        self.old_passwords=old_passwords

    def get_password(self):
        return self.old_passwords[-1]
    
    def is_correct(self, pwd):
        return pwd not in self.old_passwords   

    def set_password(self, pwd):
        if self.is_correct(pwd):
            self.old_passwords.append(pwd)
            print("Password updated successfully") 
        else:
            print("This password is already used")          

    def show(self):
        print("Old passwords:", self.old_passwords)

a=[1,2,3]
b=Password_manager(a)
print("Current password =",b.get_password())
pwd=input("enter the password u want to set ")
b.set_password(pwd)
print("Current password =",b.get_password())
b.show()

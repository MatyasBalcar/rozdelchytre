#stores users in an array, no user can exist outside of it
users=[]

#template for a user
class User:
    def __init__(self, name):
        self.name =  name
        self.debt =0

#adds a user based on name
def addUser(name):
    users.append(User(name))

#add an expense
def addExpense(payer, people, amount):
    pass

    
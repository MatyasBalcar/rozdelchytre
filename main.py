#stores users in an array, no user can exist outside of it
users=[]

#template for a user
class User:
    def __init__(self, name):
        self.name =  name
        self.debt =0#negative is good
    #changes debt amount based on amount given
    def changeDebt(self, amount):
        self.debt+=amount
#adds a user based on name
def addUser(name):
    users.append(User(name))

#add an expense
def addExpense(payer, people, amount):
    #debt for the debtors
    debt =  amount / (len(people))
    #what the guy payed for the other people aka all - his share
    payed= (amount - debt)*-1
    payer.changeDebt(payed)
    print(f"added expense to {payer.name} of {payed}")
    #adding debt to all people but the payer
    for user in users:
        if user!=payer:
            user.changeDebt(debt)
addUser("bali")
addUser("fofo")

addExpense(users[0],users ,100)

print(users[0].debt)
    
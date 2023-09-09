#stores users in an array, no user can exist outside of it
users=[]

#template for a user
class User:
    def __init__(self, name):
        self.name =  name
        self.debt =0#negative is good
        self.debts_list= {}
    #changes debt amount based on amount given
    def changeDebt(self, amount):
        self.debt+=amount
    #adds the amount and payer to the dict
    def newDebt(self, amount, debtor):
        self.debts_list[debtor]=(amount)
#*adds a user based on name
def addUser(name):
    users.append(User(name))

#*add an expense
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
            user.newDebt(debt, payer.name)
#*shows expenses with users (totals)
def showExpenses(people):
    for user in people:
        if user.debt >0:
            print(f"User {user.name} owes {user.debt}. ")
        elif user.debt<0:
            print(f"User {user.name} is owed {user.debt *-1}")
        else:
            print(f"User doesnt owe anything.")
#*shows individuals debts for users
def showDebts(people):
    for user in people:
        if user.debts_list!={}:
            print(f"{user.name}'s debts")
            print(user.debts_list)
        else:
            print(f"{user.name} is up to date.")
#* -->TEST CODE<-- 
addUser("bali")
addUser("fofo")

addExpense(users[0],users ,100)

print(users[0].debt)

showExpenses(users)
showDebts(users)
#* -->END TEST CODE<--
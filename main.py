#stores users in an array, no user can exist outside of it
users=[]
users_dict={}
#template for a user
class User:
    def __init__(self, name):
        self.name =  name
        self.debt =0#negative is good
        self.debts_list= {}
        users_dict[self.name]=self
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

def setleDebts(debtor, payer):
    total=0
    for x in debtor.debts_list:
        if x == payer.name:
            total+=debtor.debts_list[x]
    print(f"{debtor.name} owes {payer.name}:{total} in total")
    ready=input("Do you want to settle? [y/n]")
    if ready=="y":
        to_delete=[]
        for x in debtor.debts_list:
            if x == payer.name:
                to_delete.append(x)
        for y in to_delete:
            del debtor.debts_list[y]
        debtor.changeDebt(-total)
        print(f"Debts between {debtor.name} and {payer.name} have been settled.")
    else:
        print('Debts have NOT been settled')

#* -->TEST CODE<-- 
#?call this function to test the code
def testFunc():

    addUser("bali")
    addUser("fofo")

    addExpense(users_dict['bali'],users ,100)


    showDebts(users)
    setleDebts(users_dict['fofo'], users_dict['bali'])
    showDebts(users)
#testFunc()

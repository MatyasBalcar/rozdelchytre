#imports
import time,pickle,os

#ELEMENTAL VARIABLES
#stores users in an array, no user can exist outside of it
users=[]
users_dict={}

run = True
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
    def save(self):
        #debts_list
        with open(str(self.name)+'.pkl','wb') as pkl:
            pickle.dump(self.debts_list,pkl)
#*Saves the information from users
def saveAppInfo(people):

    names = set()  # Use a set to store unique names

    for person in people:
        person.save()
        names.add(person.name)  # Add the name to the set

    # Open names.txt and read the current data
    with open('names.txt', 'r') as file:
        content = file.read()
        items = content.splitlines()

    # Iterate over the items and add them to the set
    for i in items:
        names.add(i)

    # Write the unique names back to names.txt
    with open("names.txt", "w") as f:
        for i in names:
            f.write(i + '\n')

    f.close()
#*Load apps info
def loadAppInfo():
    file = open('names.txt', 'r')
    content = file.read()
    items = content.splitlines()
    file.close()
    for name in items:
        addUser(name,users)
        with open(name+'.pkl','rb') as pkl:
            person=pickle.load(pkl)
        users_dict[name].debts_list=person    
#*deletes user
def deleteUser(user):
    #deletes the user from users array
    to_delete=[]
    for u in users:
        if u.name == user.name:
            to_delete.append(u)
    for u in to_delete:
        users.remove(u)
    print(f"to delete and users: {to_delete}")
    print(users)
    #deletes user from users dict
    del users_dict[user.name]

    #removes user.name from names.txt
    names = set()  # Use a set to store unique names

    for person in users:
        person.save()
        names.add(person.name)  # Add the name to the set

    # Open names.txt and read the current data
    with open('names.txt', 'r') as file:
        content = file.read()
        items = content.splitlines()

    # Iterate over the items and add them to the set
    for i in items:
        names.add(i)

    # Write the unique names back to names.txt
    names.discard(user.name)
    with open("names.txt", "w") as f:
        for i in names:
            f.write(i + '\n')

    f.close()
    #deletes the pkl file
    user_pkl_file = user.name + '.pkl'
    if os.path.exists(user_pkl_file):
        os.remove(user_pkl_file)
#*adds a user based on name
def addUser(name,people):
    people.append(User(name))
def showUsers(people):
    print("USERS:")
    for user in people:
        print(user.name)
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
#*Settles debts
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
#*Creates debt based on amount
def calculateDebtOnAmount(people,payer):
    total=0
    debts_dict={}
    for i in people:
        if i.name!=payer.name:
            amount=int(input(f"How much does {i.name} owe: "))
            total+=amount
            debts_dict[i.name]=amount
            i.changeDebt(amount)
            i.newDebt(amount,payer.name)
    payer.changeDebt(-total)
    print(f"Succesfully assigned debts and {payer.name} is now owed {total}")
    for i in debts_dict:
        print(i)
    

#*-->MAIN LOOP<--
loadAppInfo()

print("User's info loaded succesfully!")
while run:

    action=input("""Select an action to do: \n
                 [1] - ADD USER \n
                 [2] - ADD EXPENSE \n
                 [3] - SHOW DEBTS\n
                 [4] - SETTLE A DEBT\n
                 [5] - SHOW USERS \n
                 [6] - DELETE A USER\n
                 [7] - ADD EXPENSE (by amount - beta)\n
                 anything else - QUIT\n
                 """)
    if action=='1':
        name = input("Enter name: ")
        addUser(name,users)
    elif action=='2':
        payer = users_dict[input("Who paid: ")]
        amount = int(input("How much was the amount: "))
        addExpense(payer,users,amount)
    elif action=='3':
        showDebts(users)
    elif action=='4':
        debtor=users_dict[input("Who is the debtor: ")]
        payer=users_dict[input("Who is the payer: ")]
        setleDebts(debtor,payer)
    elif action=='5':
        showUsers(users)
    elif action=='6':
        showUsers(users)
        user_to_delete=input("Which user do you want to delete : ")
        deleteUser(users_dict[user_to_delete])
    elif action=="7":
        payer=users_dict[input("Who paid for this : ")]
        calculateDebtOnAmount(users,payer)

    else:
        print("Goodbye!")
        saveAppInfo(users)
        print("App info saved sucessfully!")
        time.sleep(5)
        run = False

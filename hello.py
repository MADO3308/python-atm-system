user_data = {
    'transactions' : [],
    'deposit_count' : 0,
    'withdraw_count' : 0,
    'name_change_count' : 0,
    'total_deposit' : 0,
    'total_withdraw' : 0,
    'name' : input("Please enter your name:\t"),
    'age' : float(input("Please enter your age:\t")),
    'balance' : float(input("Please enter your balacne:\t")),
    'pin' : "mado1230",
    'tries' : 3,
    'userpin' : input("What is your password?:\t"),
    
}
def showaccountinfo():
     print(f"""
           Name : {user_data['name']}
           Age : {user_data['age']}
           Balance : {user_data['balance']:.2f}
           """)
     if user_data['age']>=18:
        print("Adult : True")
     else:
         print("Adult : False")
     user_data["transactions"].append("Viewed Account Info")
def deposit():
    depo = float(input("How much do you want to deposit?"))
    if depo>0:
        user_data['balance'] += depo
        print(f"Your balance is: {user_data['balance']:.2f}")
        user_data["transactions"].append(f"Deposited ${depo:.2f}")
        user_data['deposit_count'] += 1
        user_data['total_deposit'] += depo
    else:
        print("Invalid amount")
def withdraw():
    withdraw = float(input("How much?:\t"))
    if withdraw <= 0:
        print("Invalid amount.")
        
    elif withdraw>user_data['balance']:
        print("Insufficient balance")
    else:
        print("The amount has been successfully withdrawn.")
        user_data['balance'] -= withdraw
        print(f"Your balance now is: {user_data['balance']:.2f}")
        user_data["transactions"].append(f"Withdrew ${withdraw:.2f}")
        user_data['withdraw_count'] += 1
        user_data['total_withdraw'] += withdraw
def changeusername():
    newname = input("What is your new name?:\t").lower()

    if len(newname) > 12:
        print("Please enter 12 characters or fewer.")

    elif " " in newname:
        print("Please remove the space!")

    elif not newname.isalpha():
        print("Username must not contain digits")

    else:
        user_data['name'] = newname

        print(
            f"Username updated successfully to "
            f"{user_data['name'].capitalize()}"
        )

        user_data["transactions"].append(
            f"Changed name to {newname}"
        )

        user_data['name_change_count'] += 1
def show_tran_history():
    if len(user_data["transactions"]) == 0:
        print("No transactions yet.")
    else:
        print("Transaction History:")
        for transaction in user_data["transactions"]:
            print(transaction)
def del_last_tran():
    if user_data["transactions"]:
        user_data["transactions"].pop()
        print("Last transaction deleted!")
    else:
        print("No transactions to delete.")
def clear_tran_history():
    user_data["transactions"].clear()
    print("History is already cleaned!")
def statistics():
    print(f"""
            ===== Statistics =====

    Balance : ${user_data['balance']:.2f}
    Transactions : {len(user_data["transactions"])}
    Deposits : {user_data['deposit_count']}
    Withdrawals : {user_data['withdraw_count']}
    Username Changes : {user_data['name_change_count']}
    Total Deposited : ${user_data['total_deposit']:.2f}
    Total Withdrawn : ${user_data['total_withdraw']:.2f}
            """)
def change_pass():
    old_pass = input("What is your old password?:\t")
    while old_pass != user_data["pin"]:
        user_data['tries'] -= 1
        if user_data['tries'] == 0:
            print("Your account has been locked.")
            exit()
        print("Wrong PIN")
        print(
            f"You have {user_data['tries']} attempts remaining."
        )
        old_pass = input("What is your old password?:\t")
    print("Correct PIN!")
    new_pass = input("What is your new password?:\t")
    while new_pass == old_pass:
        print("Please enter a different password.")
        new_pass = input("What is your new password?:\t")
    user_data['pin'] = new_pass
    user_data["transactions"].append(
        "Changed password"
    )
    print("PIN changed successfully!")

    user_data['tries'] = 3
def exit_program():
    print(f"Thank you for using our ATM, {user_data['name'].capitalize()}!")
def invalid_choice():
    print("Please enter one number of below")

while user_data['userpin'] != user_data["pin"]:
    user_data['tries'] -= 1
    if user_data['tries'] == 0:
        print("Your account has been locked.")
        exit()

    print("Wrong PIN")
    print(f"You have {user_data['tries']} attempts remaining.")

    user_data['userpin'] = input("What is your password?:\t")

print("Correct PIN!")
print(f"Welcome to our ATM program, {user_data['name'].capitalize()}")
    
while True:
    print("""
===== ATM =====
1. Show Account Info
2. Deposit
3. Withdraw
4. Change Username
5. Show Transaction History
6. Delete Last Transaction
7. Clear Transaction History
8. Statistics
9. Change password
10. Exit""")
    print("=" *30)
    choice = int(input("What are you need, sir?:\t"))
    print("=" *30)

    match choice:
        case 1:
            showaccountinfo()
            
        case 2:
            deposit()
           
        case 3:
            withdraw()
        case 4:
            changeusername()
        case 5:
            show_tran_history()
        case 6:
            del_last_tran()
        case 7:
            clear_tran_history()
        
        case 8:
            statistics()

        case 9:
            change_pass()
        
        case 10:
            exit_program()
            break
        case _:
            invalid_choice()
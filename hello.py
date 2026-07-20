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
            
        case 2:
            depo = float(input("How much do you want to deposit?"))
            if depo>0:
                user_data['balance'] += depo
                print(f"Your balance is: {user_data['balance']:.2f}")
                user_data["transactions"].append(f"Deposited ${depo:.2f}")
                user_data['deposit_count'] += 1
                user_data['total_deposit'] += depo
            else:
                print("Invalid amount")
           
        case 3:
            withdraw = float(input("How much?:\t"))
            if withdraw>user_data['balance']:
                print("Insufficient balance")
            else:
                print("The amount has been successfully withdrawn.")
                user_data['balance'] -= withdraw
                print(f"Your balance now is: {user_data['balance']:.2f}")
                user_data["transactions"].append(f"Withdrew ${withdraw:.2f}")
                user_data['withdraw_count'] += 1
                user_data['total_withdraw'] += withdraw
        case 4:
            newname = input("What is your new name?:\t").lower()
            if len(newname)>12:
                print("Please enter 12 characters or fewer.")
            elif " "in newname:
                print("Please remove the space!")
            elif not newname.isalpha():
                print("Username must not contain digits")
                
            else:
                user_data['name'] = newname

                print(f"Username updated successfully to {user_data['name'].capitalize()}")
                user_data["transactions"].append(f"Changed name to {newname}")
                user_data['name_change_count'] += 1
                
        case 5:
            
            if len(user_data["transactions"]) == 0:
                print("No transactions yet.")
            else:
                print("Transaction History:")
                for transaction in user_data["transactions"]:
                    print(transaction)
        case 6:
            if user_data["transactions"]:
               user_data["transactions"].pop()
               print("Last transaction deleted!")
            else:
                print("No transactions to delete.")
           
        case 7:
            user_data["transactions"].clear()
            print("History is already cleaned!")
        
        case 8:
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

        case 9:
            old_pass = input("What is your old password?:\t")
            while old_pass != user_data["pin"]:
                user_data['tries'] -= 1
                if user_data['tries'] == 0:
                    print("Your account has been locked.")
                    exit()
                else:
                    print("Wrong PIN")
                    print(f"You have {user_data['tries']} attempts remaining.")
                    old_pass = input("What is your old password?:\t")

            print("Correct PIN!")
            new_pass = input("What is your new password?:\t")
            while new_pass == old_pass:
                print("Please Enter differenet password")
                new_pass = input("What is your new password?:\t")
            user_data['pin'] = new_pass
            user_data["transactions"].append(f"Changed password")
            print("PIN changed successfully!")
            user_data['tries'] = 3
        
        case 10:
            print(f"Thank you for using our ATM, {user_data['name'].capitalize()}!")
            break
        case _:
            print("Please enter one number of below")
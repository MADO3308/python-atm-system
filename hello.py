

name = input("Please enter your name:\t")
age = float(input("Please enter your age:\t"))
balance = float(input("Please enter your balacne:\t"))
pin = "mado1230"
tries = 3
userpin = input("What is your password?:\t")
while userpin != pin:
    tries -= 1
    if tries == 0:
        print("Your account has been locked.")
        exit()

    print("Wrong PIN")
    print(f"You have {tries} attempts remaining.")

    userpin = input("What is your password?:\t")

print("Correct PIN!")
print(f"Welcome to our ATM program, {name.capitalize()}")
while True:
    print("""
===== ATM =====
1. Show Account Info
2. Deposit
3. Withdraw
4. Change Username
5. Exit""")
    print("=" *30)
    choice = int(input("What are you need, sir?:\t"))
    print("=" *30)

    match choice:
        case 1:
            print(f"""
            Name : {name}
            Age : {age}
            Balance : {balance:.2f}
            """)
            if age>=18:
                print("Adult : True")
            else:
                print("Adult : False")
        case 2:
            depo = float(input("How much do you want to deposit?"))
            if depo>0:
                balance += depo
                print(f"Your balance is: {balance:.2f}")
            else:
                print("Invalid amount")
        case 3:
            withdraw = float(input("How much?:\t"))
            if withdraw>balance:
                print("Insufficient balance")
            else:
                print("The amount has been successfully withdrawn.")
                balance -= withdraw
                print(f"Your balance now is: {balance:.2f}")
        case 4:
            newname = input("What is your new name?:\t").lower()
            if len(newname)>12:
                print("Please enter 12 characters or fewer.")
            elif " "in newname:
                print("Please remove the space!")
            elif not newname.isalpha():
                print("Username must not contain digits")
            else:
                name = newname

                print(f"Username updated successfully to {name.capitalize()}")
        case 5:
            print(f"Thank you for using our ATM, {name.capitalize()}!")
            break
        case _:
            print("Please enter one number of below")
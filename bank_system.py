def create_account(accounts):
    name = input("enter name: ")
    balance = int(input("enter initial balance: "))
    accounts.append([name, balance])

    print("account created!")


def show_account(accounts):
    if not accounts:
        print("no account!")
        return
    
    for i, acc in enumerate(accounts, start=1):
        print(f"{i}. {acc[0]} - {acc[1]}")


def search_account(accounts):
    if not accounts:
        print("not found!")
        return
    
    name = input("enter name too search:")

    for acc in accounts:
        if acc[0] == name:
            print(f"found: {acc[0]} - {acc[1]}")
            return
        
    print("not found!")


def deposit_account(accounts):
    name = input("enter account name: ")
    amount = int(input("enter amount: "))

    for acc in accounts:
        if acc[0] == name:
            acc[1] += amount
            print("deposit successful!")
            return
        
    print("account not found!")


def withdraw_account(accounts):
    name = input("enter account name: ")
    amount = int(input("enter amount: "))

    for acc in accounts:
        if acc[0] == name:
            if acc[1] >= amount:
                acc[1] -= amount
                print("withdraw successful!")
            else:
                print("not enough balance!")
            return
            
    print("account not found!")


# main program.

accounts = []

while True:
    print("\n=== bank system ===")
    print("1. create account")
    print("2. show accounts")
    print("3. search account")
    print("4. deposit too account")
    print("5. withdraw from account")
    print("6. exit")

    choice = input("choose:").strip()

    if choice == "1":
        create_account(accounts)

    elif choice == "2":
        show_account(accounts)

    elif choice == "3":
        search_account(accounts)

    elif choice == "4":
        deposit_account(accounts)

    elif choice == "5":
        withdraw_account(accounts)

    elif choice == "6":
        print("goodbye!")
        break
    else:
        print("invalid choice!")
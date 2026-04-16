def get_name(message):
    while True:
        name = input(message).strip()

        if name:
            return name
    
        print("name cannot be empty!")


def get_balance():
    while True:
        try:
            balance = int(input("enter balance: "))

            if balance < 0:
             print("balance cannot be negative!")
             continue
            else:
                return balance
        
        except ValueError:
            print("invalid input! please try again.")


def is_empty(accounts):
    if not accounts:
        print("no account!")
        return True
    return False


def create_account(accounts):
    name = get_name("enter account name: ")

    for acc in accounts:
        if acc[0] == name:
            print("this account name already exists!")
            return
        
    balance = get_balance()

    new_account = [name, balance]

    accounts.append(new_account)

    print(f"account '{name}' created successfully!")


def show_accounts(accounts):
    if is_empty(accounts):
        print("no account!")
        return
    
    for i, acc in enumerate(accounts, start=1):
        print(f"{i}. {acc[0]} - {acc[1]}")


def search_account(accounts):
    if is_empty(accounts):
        return None
    
    name = get_name("enter account name to search: ")

    for acc in accounts:
        if acc[0] == name:
            return acc

    return None


def deposit_account(accounts):
    acc = search_account(accounts)

    if not acc:
        print("account not found!")
        return
    
    amount = get_balance()
    if amount <= 0:
        print("invalid amount!")
        return

    acc[1] += amount

    print(f"deposit successfully! new balance: {acc[1]}")


def withdraw_account(accounts):
    acc = search_account(accounts)

    if not acc:
        print("account not found!")
        return
    
    amount = get_balance()
    if amount > acc[1]:
        print("not enough balance!")
        return
    
    acc[1] -= amount

    print(f"withdraw successfully! new balance: {acc[1]}")


def total_money(accounts):
    if is_empty(accounts):
        print("no balance!")
        return
    
    total = 0
    for acc in accounts:
        total += acc[1]

    print(f"total all money in bank: {total}")
    

def delete_account(accounts):
    if is_empty(accounts):
        return
    
    acc = search_account(accounts)

    if not acc:
        print("account not found!")
        return
    
    accounts.remove(acc)

    print("account removed successful!")


# main program 

accounts = []

while True:
    print("\n=== bank system ===")

    print("1. create account")
    print("2. show accounts")
    print("3. search account")
    print("4. deposit account")
    print("5. withdraw account")
    print("6. total money")
    print("7. delete account")
    print("8. exit")

    choice = input("choose: ").strip()

    if choice == "1":
        create_account(accounts)

    elif choice == "2":
        show_accounts(accounts)

    elif choice == "3":
        acc = search_account(accounts)

        if acc:
            print(f"{acc[0]} - {acc[1]}")
        else:
            print("account not found!")

    elif choice == "4":
        deposit_account(accounts)

    elif choice == "5":
        withdraw_account(accounts)

    elif choice == "6":
        total_money(accounts)

    elif choice == "7":
        delete_account(accounts)

    elif choice == "8":
        print("goodbye!")
        break

    else:
        print("invalid choice!")
        
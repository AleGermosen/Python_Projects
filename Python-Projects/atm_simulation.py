### ATM Simulation

# Print options
# User option input
# Create a method for solving each option

current_balance = 0

def balance():
    print(f"Your current balance is ${current_balance}.")

def deposit():
    global current_balance
    user_deposit = int(input("Enter the amount to deposit: $"))
    current_balance += user_deposit
    print(f"Successfully deposited ${user_deposit}.")

def withdraw():
    global current_balance
    user_withdraw = int(input("Enter the amount to withdraw: $"))
    if (current_balance - user_withdraw) < 0:
        print("Not enough balance.")
    else:
        current_balance -= user_withdraw
        print(f"Successfully withdrew ${user_withdraw}.")

list_apps = {
    1: balance, 
    2: deposit,
    3: withdraw,
    4: exit,
    }

def atm_simulation():
    print("""
    Welcome to the ATM!
    1. Check balance
    2. Deposit
    3. Withdraw
    4. Exit
    """)
    
    while True:
        user_choice = int(input("Please choose an option: "))
        if user_choice in list_apps:
            list_apps[user_choice]()
        else:
            print("Invalid choice.")

atm_simulation()
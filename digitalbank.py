
# Bank System - Customized Version with Withdrawal, Deposit, and Statement Functions
# Version that interacts with the user through a simple menu

# Initialize variables
balance = 0.0  # Initial account balance
withdrawals_made = []  # List to store withdrawals made
deposits_made = []  # List to store deposits made
daily_withdrawal_limit = 3  # Maximum number of withdrawals per day
withdrawal_limit = 500.0  # Maximum withdrawal per transaction
withdrawal_count = 0  # Counter for withdrawals made in a day

# Function to make a deposit into the account


def make_deposit():
    global balance  # Accessing the global balance variable
    try:
        # Get deposit amount from user
        deposit_amount = float(
            input("How much would you like to deposit (R$)? "))
        if deposit_amount > 100:
            balance += deposit_amount  # Update the balance
            deposits_made.append(deposit_amount)  # Store the deposit
            print(f"Deposit of R${deposit_amount:.2f} was successful!")
        else:
            print(f"Deposit amount must be greater than R$100 !")
    except ValueError:
        print("Please enter a valid numeric value.")

# Function to make a withdrawal from the account


def make_withdrawal():
    global balance, withdrawal_count  # Accessing global balance and withdrawal count
    try:
        # Get withdrawal amount from user
        withdrawal_amount = float(
            input("How much would you like to withdraw (R$)? "))
        if withdrawal_count >= daily_withdrawal_limit:
            print("You have reached the daily withdrawal limit! Try again tomorrow.")
        elif withdrawal_amount > withdrawal_limit:
            print(f"The maximum withdrawal limit is R${withdrawal_limit:.2f}!")
        elif withdrawal_amount > balance:
            print("Insufficient funds for this withdrawal!")
        else:
            balance -= withdrawal_amount  # Update the balance after withdrawal
            withdrawals_made.append(withdrawal_amount)  # Store the withdrawal
            withdrawal_count += 1  # Increment the withdrawal count
            print(f"Withdrawal of R${withdrawal_amount:.2f} was successful!")
    except ValueError:
        print("Please enter a valid numeric value.")

# Function to display the account statement


def show_statement():
    global balance  # Accessing the global balance variable
    if not withdrawals_made and not deposits_made:
        print("No transactions have been made yet.")
    else:
        print("\n--- Bank Statement ---")
        if withdrawals_made:
            print("Withdrawals made:")
            for withdrawal in withdrawals_made:
                print(f"- R${withdrawal:.2f}")
        if deposits_made:
            print("Deposits made:")
            for deposit in deposits_made:
                print(f"- R${deposit:.2f}")
        print(f"\nCurrent Balance: R${balance:.2f}")
        print("---------------------")

# Function to display the menu and interact with the user


def show_menu():
    while True:
        # Displaying the menu with options
        print("\n--- Bank Menu ---")
        print("1. Make Deposit")
        print("2. Make Withdrawal")
        print("3. Show Statement")
        print("4. Exit")

        # Get the user's choice
        option = input("Choose an option (1/2/3/4): ")

        # Process user's choice
        if option == '1':
            make_deposit()  # Call the deposit function
        elif option == '2':
            make_withdrawal()  # Call the withdrawal function
        elif option == '3':
            show_statement()  # Call the statement function
        elif option == '4':
            print("Exiting the system. Thank you for using our bank!")
            break  # Exit the loop and end the program
        else:
            print("Invalid option. Please choose a valid option (1, 2, 3, or 4).")


# Start the program by calling the function to show the menu
show_menu()

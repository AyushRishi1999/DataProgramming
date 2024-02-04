class Account:
    def __init__(self, id=0, balance=100.0):
        self.__id = id
        self.__balance = balance
    def get_id(self):
        return self.__id
    def get_balance(self):
        return self.__balance
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return True
        else:
            return False
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        else:
            return False

accounts = [Account(i) for i in range(10)]
while True:
    try:
        # Prompt user to enter an account id
        account_id = int(input("Enter an account id (0-9): "))
        if 0 <= account_id <= 9:
            while True:
                print("\nMain menu")
                print("1: check balance")
                print("2: withdraw")
                print("3: deposit")
                print("4: exit")
                choice = int(input("Enter a choice: "))
                if choice == 1:
                    print(f"The balance is {accounts[account_id].get_balance():.2f}")
                elif choice == 2:
                    amount = float(input("Enter an amount to withdraw: "))
                    if accounts[account_id].withdraw(amount):
                        print("Withdrawal successful.")
                    else:
                        print("Invalid withdrawal amount.")
                elif choice == 3:
                    amount = float(input("Enter an amount to deposit: "))
                    if accounts[account_id].deposit(amount):
                        print("Deposit successful.")
                    else:
                        print("Invalid deposit amount.")
                elif choice == 4:
                    break
                else:
                    print("Invalid choice. Please enter a valid choice (1-4).")
        else:
            print("Invalid account id. Please enter a valid id (0-9).")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    except Exception as e:
        print(f"An error occurred: {e}")

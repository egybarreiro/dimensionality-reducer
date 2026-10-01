class Account:
    def __init__(self):
        self.__balance = 0
        
    def deposit(self, amount):
        if amount > 0:
             self.__balance += amount
        else:
             print("The deposit amount needs to be greater than 0.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Not enough funds. Select another ammount.")
        else: 
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


    
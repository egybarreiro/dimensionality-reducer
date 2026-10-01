from account import Account


def main():

    print("My Account APP")

    account_info = Account()
    print(account_info)

    account_info.deposit(100)
    print(account_info.get_balance())

    account_info.withdraw(50)
    print(account_info.withdraw(50)) # 50

    account_info.withdraw(70)
    print(account_info.withdraw(70))     # "Insufficient Balance"

    return

if __name__ == "__main__":
    main()
def withdraw(amount, balance):
    try:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > balance:
            raise ValueError('Insufficient balance')
        else:
            balance -=amount
            print(f"Withdrawal of {amount} successfull, new balance is {balance}")
    except ValueError as ve:
        print(f"error {ve}")
    finally:
        return balance
atm_balance = 10000
atm_balance = withdraw(2000,atm_balance)
atm_balance = withdraw(10000,atm_balance)
atm_balance = withdraw(-100,atm_balance)
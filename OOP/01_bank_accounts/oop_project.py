from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(1000, "Sara")

Dave.getBalance()
Sara.getBalance()

Sara.deposit(500)

Dave.withdraw(10000)
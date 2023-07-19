from account import Account

first_account = Account(123, 'Alexandre', 500, 1000)

first_account.deposit(100)
first_account.deposit(100)
first_account.withdraw(150)

first_account.statement()

second_account = Account(456, 'Monteiro', 300, 1000)

first_account.deposit(100)
first_account.deposit(100)
first_account.withdraw(150)

second_account.statement()

first_account.set_limit(2000)

print(first_account.get_number())
print(first_account.get_limit())

second_account.set_limit(3000)

print(second_account.get_number())
print(second_account.get_limit())

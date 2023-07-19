from account import Account
from film import Film
from serie import Serie

print('\n==============================\n')

first_account = Account(123, 'Alexandre', 500, 1000)

print('First account:\n')

print('Number:', first_account.number)
print('Balance:', first_account.balance)
print('Limit:', first_account.limit)
first_account.statement()

first_account.withdraw(3000)

print('\n==============================\n')

second_account = Account(456, 'Monteiro', 300, 1000)

second_account.deposit(100)
second_account.deposit(100)
second_account.withdraw(150)
second_account.limit = 3000

print('Second account:\n')

print('Number:', second_account.number)
print('Balance:', second_account.balance)
print('Limit:', second_account.limit)
second_account.statement()

print('\n==============================\n')

print('Static methods:\n')

print('Bank codes:', Account.bank_codes())
print('Bank code:', Account.bank_code())

print('\n==============================\n')

print('Filmes:\n')

avengers = Film('Vingadores', 2018, 160)

print(
    f'Nome: {avengers.name}, Ano: {avengers.year}, Duração: {avengers.duration}'
)

print('\n==============================\n')

print('Series:\n')

big_bang_theory = Serie('Big Bang Theory', 2010, 10)

print(
    f'Nome: {big_bang_theory.name}, Ano: {big_bang_theory.year}, Temporadas: {big_bang_theory.seasons}'
)

print('\n==============================\n')

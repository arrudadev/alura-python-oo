class Account:
  def __init__(self, number, owner, balance, limit):
    self.number = number
    self.owner = owner
    self.balance = balance
    self.limit = limit

  def statement(self):
    print(f'Saldo de {self.balance} do titular {self.owner}')

  def deposit(self, value):
    self.balance += value

  def withdraw(self, value):
    self.balance -= value

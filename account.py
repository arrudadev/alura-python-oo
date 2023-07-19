class Account:
  def __init__(self, number, owner, balance, limit):
    self.__number = number
    self.__owner = owner
    self.__balance = balance
    self.__limit = limit

  def statement(self):
    print(f'Saldo de {self.__balance} do titular {self.__owner}')

  def deposit(self, value):
    self.__balance += value

  def withdraw(self, value):
    self.__balance -= value

  def get_number(self):
    return self.__number

  def get_limit(self):
    return self.__limit

  def set_limit(self, limit):
    self.__limit = limit

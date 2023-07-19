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

  @property
  def number(self):
    return self.__number

  @property
  def balance(self):
    return self.__balance

  @property
  def limit(self):
    return self.__limit

  @limit.setter
  def limit(self, limit):
    self.__limit = limit

  @staticmethod
  def bank_code():
    return "001"

  @staticmethod
  def bank_codes():
    return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

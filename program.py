class Program:
  def __init__(self, name: str, year: int) -> None:
    self._name = name.title()
    self.year = year
    self._likes = 0

  @property
  def likes(self) -> int:
    return self._likes

  def like(self) -> None:
    self._likes += 1

  @property
  def name(self) -> str:
    return self._name

  @name.setter
  def name(self, name: str) -> None:
    self._name = name.title()

  def __str__(self) -> str:
    return f'Nome: {self._name}, Likes: {self._likes}'

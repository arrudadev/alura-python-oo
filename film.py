class Film:
  def __init__(self, name: str, year: int, duration: int) -> None:
    self.__name = name.title()
    self.year = year
    self.duration = duration
    self.__likes = 0

  @property
  def likes(self) -> int:
    return self.__likes

  def like(self) -> None:
    self.__likes += 1

  @property
  def name(self) -> str:
    return self.__name

  @name.setter
  def name(self, name: str) -> None:
    self.__name = name.title()

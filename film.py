from program import Program


class Film(Program):
  def __init__(self, name: str, year: int, duration: int) -> None:
    super().__init__(name, year)
    self.duration = duration

  def __str__(self) -> str:
    return f'Nome: {self._name}, Likes: {self._likes}, Duração: {self.duration} min.'

from program import Program


class Film(Program):
  def __init__(self, name: str, year: int, duration: int) -> None:
    super().__init__(name, year)
    self.duration = duration

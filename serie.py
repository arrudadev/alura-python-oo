from program import Program


class Serie(Program):
  def __init__(self, name: str, year: int, seasons: int) -> None:
    super().__init__(name, year)
    self.seasons = seasons

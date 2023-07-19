from typing import List, Union

from film import Film
from serie import Serie

Program = Union[Film, Serie]


class Playlist:
  def __init__(self, name: str, programs: List[Program]) -> None:
    self.name = name
    self._programs = programs

  def __getitem__(self, item: Program) -> Program:
    return self._programs[item]

  def __len__(self) -> int:
    return len(self._programs)

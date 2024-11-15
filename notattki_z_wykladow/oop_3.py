# PPO:
#  - metody statyczne, czemu konstruktor jest złą opcją
#  - prywatny konstruktor: tak, ale nie w Pythonie
#  - destructor
#  - wyjątki
#  - interfejsy, czyste klasy abstrakcyjne
#  - problem z wielokrotnym dziedziczniem (diamond inheritance problem)
#  - przeciążenie metod: *args

from __future__ import annotations
import sys
from abc import ABC, abstractmethod


class HasCenterOfMass(ABC):
    @abstractmethod
    def cm(self) -> Point:
        pass

kwadrat = """Kwadrat_1
1 1
1 5
5 5
5 1
"""

other = """something_1
1 10
11 15
5 50
5 -90
"""
class Point(HasCenterOfMass):
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y
    # def __del__(self):
    #     print("Usuwam punkt", file=sys.stderr)

    def __str__(self):
        return f"{self.__x}\t{self.__y}"

    def cm(self) -> Point: return self

    @property
    def x(self) -> float: return self.__x

    @property
    def y(self) -> float: return self.__y

    @staticmethod
    def from_string(txt_line: str) -> Point:
        tokens = txt_line.split()
        x = float(tokens[0])
        y = float(tokens[1])
        return Point(x, y)

class Figura(HasCenterOfMass):
    def __init__(self, name: str):
        self.__points = []
        self.name = name

    @staticmethod
    def from_string(figure_txt: str) -> Figura:
        lines = figure_txt.split("\n")
        f = Figura(lines[0])
        for line in lines[1:]:
            if len(line) >= 3:
                try:
                    p = Point.from_string(line)
                    f.__points.append(p)
                except:
                    print(f"Can't create a point from '{line}' while creating {lines[0]}", file=sys.stderr)
        return f

    def __str__(self):
        out = self.name
        for p in self.__points:
            out += "\n" + p.__str__()
        return out

    def cm(self) -> Point:
        x, y = 0, 0
        for p in self.__points:
            x += p.x
            y += p.y
        n = len(self.__points)

        return Point(x/n, y/n)

figury = [Figura.from_string(kwadrat), Figura.from_string(other), Point(1,1)]
for f in figury:
    print(f.cm())








# p = Point(1,1)
# try:
#     p1 = Point.from_string("12")
#     print(p1)
#     del (p1)
# except:
#     print("p1 nie istenieje")

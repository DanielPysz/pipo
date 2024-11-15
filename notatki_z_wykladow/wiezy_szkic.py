from abc import ABC, abstractmethod
import math


class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_square_to(self, vj):
        d2 = (self.__x - vj.__x) * (self.__x - vj.__x)
        d2 += (self.__y - vj.__y) * (self.__y - vj.__y)
        return d2 + (self.__z - vj.__z) * (self.__z - vj.__z)

    def distance_to(self, vj):
        return math.sqrt(self.distance_square_to(vj))

class AbstractRestrainFunction(ABC):
    def evaluate(self, p1: Vec3, p2: Vec3) -> float:
        pass


class LinearRestrainFunction(AbstractRestrainFunction):

    def __init__(self, d0, k):
        """klasa, która liczy liniową karę za więzy

        E = k * | d_0 - d|

    gdzie d_0 i k to zadane parametry
        """
        self.__d0 = d0
        self.__k = k


    def evaluate(self, p1: Vec3, p2: Vec3) -> float:
        return abs(p1.distance_to(p2) - self.__d0) * self.__k


class LorentzianRestrainFunction(AbstractRestrainFunction):
    pass


class HarmonicRestrainFunction(AbstractRestrainFunction):
    """klasa, która liczy kwadratową karę za więzy

    E = k * (d_0 - d)^2

gdzie d_0 i k to zadane parametry
    """
    pass

class Dispatch:

    def add_maker(restr_name: str, maker): pass
    
    def make_energy(restr_fname: str) -> RestraintsEnergy : pass
    

class RestraintsEnergy:

    def add_restraint(r: AbstractRestraint):
        pass
        
    def read_file(self, fname: str) -> None:
        """Wczytuje plik z więzami"""
        pass

    def evaluate(self, atoms: list[Vec3]) -> float:
        pass



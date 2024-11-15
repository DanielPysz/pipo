# PPO:
#  - dziedziczenie klas
#  - składowe chronione
#  - reguły dostepu

from abc import abstractmethod, ABC


class Figura(ABC):
    def __str__(self): return "opis klasy figura"

    def __init__(self, x0, y0):
        self.__x = x0
        self.__y = y0
        self.stroke = "black"
        self.fill = "white"
        self.stroke_width = "1"

    def styl(self):
        return f"""fill="{self.fill}" stroke="{self.stroke}" stroke_width="{self.stroke_width}"""

    @abstractmethod
    def rysuj(self): pass

    @property
    def x(self): return self.__x

    @property
    def y(self): return self.__y


class Kolo(Figura):
    def __init__(self, x0, y0, r):
        super().__init__(x0, y0)
        self.__r = r

    def __str__(self):
        return f"koło w {self.x},{self.y}, r={self.__r}"

    def rysuj(self):
        print(f"""<circle cx="{self.x}" cy="{self.y}" r="{self.__r}" {self.styl()}"/>""")


class Kwadrat(Figura):
    def __init__(self, xc, yc, w):
        super().__init__(xc, yc)
        self.__w = w

    def rysuj(self):
        print(f"""<rect width="{self.__w}" height="{self.__w}" x="{self.x}" y="{self.y}" {self.styl()}"/>""")

if __name__ == "__main__":
    print('<svg width="300" height="130" xmlns="http://www.w3.org/2000/svg">')

    N = 10
    for i in range(N):
        x = i*50
        for j in range(N):
            y = j*50
            k = Kwadrat(x,y,50)
            k.fill = "black" if (i+j) % 2==0 else "white"
            k.rysuj()
    print('</svg>')





    # k = Kwadrat(4,5,12)
    # f = Figura(0, 0)
    # print(type(p))
    # print(type(k))
    # if isinstance(k, Figura):
    #     print("tak, k to figura")



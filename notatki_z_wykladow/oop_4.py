#  - enumeracje i dlaczego są cool
#  - obiekt vs funkcja : ten pierwszy przechowuje stan
#  - operacje powiazane z kluczem (napisem)

# - przeciążenie operatora indeksowania i wywołania (get-item, call-operator)
# - delegacja

from enum import Enum

class PlayerColor(Enum):
    WHITE = 1
    BLACK = 0


def ruch(kolor: PlayerColor, n_pol: int):
    pass


ruch(PlayerColor.WHITE, 1)
ruch(PlayerColor.BLACK, 1)
#PlayerColor.WHITE = 1
ruch(PlayerColor.WHITE, 2)
ruch(2, PlayerColor.WHITE)

class SavoirVivre:
    def __init__(self, greet):
        self.greet = greet
        self.__prev = ""

    def __call__(self, x):
        if self.__prev != "":
            print(f"{self.greet}, {x}! {self.__prev} just left!")
        else:
            print(f"{self.greet}, {x}!")
        self.__prev = x


# sorry = SavoirVivre("I'm sorry")

powitania = [SavoirVivre("Hello"), SavoirVivre("Good bye"), SavoirVivre("I'm sorry")]
for name in ["Bill", "John","Anna"]:
    for f in powitania:
        f(name)

# hello("Bill")
# bye("Bill")
# sorry("Bill")
# hello("John")
# bye("John")
# sorry("John")
# hello("Anna")
# bye("Anna")
# sorry("Anna")





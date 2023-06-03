from app.universe.universe_defs import *
from app.elements.element_list import *
from app.elements.element_defs import ElementType


def startup() -> None:
    universe = Universe()
    init_element_list(universe)
    print("##### All Elements!")
    for elt in universe:
        print("---------")
        print(elt)
        print("{0} - {1}".format(elt.number, elt.mass))
        print(elt.get_printable_electron_config())

    print("##### Noble Gases!")
    for elt in universe:
        if elt.element_type == ElementType.NOBLE_GAS:
            print(elt)

if __name__ == "__main__":
    startup()


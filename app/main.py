from app.universe.universe_defs import *
from app.elements.element_list import *
from app.elements.element_defs import ElementType


def startup() -> None:
    universe = Universe()
    init_element_list(universe)
    print("##### All Elements!")
    ix = 0
    while True:
        elt = universe.get_element_by_id(ix)
        if elt is None:
            break
        print("---------")
        print(elt)
        print("{0} - {1}".format(elt.number, elt.mass))
        print(elt.get_printable_electron_config())
        ix += 1

    print("##### Noble Gases!")
    ix = 0
    while True:
        elt = universe.get_element_by_id(ix)
        if elt is None:
            break
        if elt.element_type == ElementType.NOBLE_GAS:
            print(elt)
        ix += 1

if __name__ == "__main__":
    startup()


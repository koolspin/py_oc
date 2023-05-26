from elements.element_list import *


def startup():
    arr = init_element_list()
    print("##### All Elements!")
    for elt in arr:
        print(elt)
        print(elt.mass)

    print("##### Noble Gases!")
    for elt in arr:
        if elt.element_type == ElementType.NOBLE_GAS:
            print(elt)

if __name__ == "__main__":
    startup()


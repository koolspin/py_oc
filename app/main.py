import os
from elements.element_list import *


def startup():
    print("Hello!")
    arr = init_element_list()
    for elt in arr:
        print(elt)
        print(elt.mass)


if __name__ == "__main__":
    startup()


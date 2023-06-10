from app.universe.universe_defs import *
from app.elements.element_list import *
from app.elements.element_defs import ElementType


def startup() -> None:
    universe = Universe()
    # init_element_list(universe)
    test_universe(universe)
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

    print("##### Carbon Atoms!")
    elts = universe.get_elements_by_atomic_number(6)
    if elts is not None:
        for elt in elts:
            print(elt)

    print("##### Bonds!")
    bonds = universe.get_all_bonds()
    for bond in bonds:
        print(bond)
        left_element = universe.get_element_by_id(bond.left_id)
        right_element = universe.get_element_by_id(bond.right_id)
        print("  Left: {0}".format(left_element))
        print("  Right: {0}".format(right_element))

    print("##### Bonds from the first Carbon")
    all_carbon = universe.get_elements_by_atomic_number(6)
    first_carbon = all_carbon[0]
    print(first_carbon)
    all_bond_ids = first_carbon.get_all_bond_ids()
    for bond_id in all_bond_ids:
        bond = universe.get_bond_by_id(bond_id)
        print(bond)
        elt = universe.get_element_by_id(bond.right_id)
        print(elt)


if __name__ == "__main__":
    startup()


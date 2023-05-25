class Element():
    """
    A definition of a single element from the periodic table.
    """
    def __init__(self, number, mass, symbol, name):
        self._number = number
        self._mass = mass
        self._symbol = symbol
        self._name = name

    def __str__(self):
        return "{0} ({1})".format(self._symbol, self._name)

    @property
    def number(self):
        return self._number

    @property
    def mass(self):
        return self._mass

    @property
    def symbol(self):
        return self._symbol

    @property
    def name(self):
        return self._name


def init_element_list():
    element_by_atomic_num = []

    elt = Element(1, 1.0078, "H", "Hydrogen")
    element_by_atomic_num.append(elt)

    elt = Element(2, 4.0026, "He", "Helium")
    element_by_atomic_num.append(elt)

    elt = Element(3, 6.9410, "Li", "Lithium")
    element_by_atomic_num.append(elt)

    elt = Element(4, 9.0122, "Be", "Beryllium")
    element_by_atomic_num.append(elt)

    elt = Element(5, 10.811, "B", "Boron")
    element_by_atomic_num.append(elt)

    elt = Element(6, 12.011, "C", "Carbon")
    element_by_atomic_num.append(elt)

    elt = Element(7, 14.007, "N", "Nitrogen")
    element_by_atomic_num.append(elt)

    elt = Element(8, 15.999, "O", "Oxygen")
    element_by_atomic_num.append(elt)

    elt = Element(9, 18.998, "F", "Fluorine")
    element_by_atomic_num.append(elt)

    elt = Element(10, 20.180, "Ne", "Neon")
    element_by_atomic_num.append(elt)

    return element_by_atomic_num

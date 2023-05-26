from enum import Enum


class ElementType(Enum):
    ALKALI_METAL = 1
    ALKALINE_EARTH_METAL = 2
    TRANSITION_METAL = 3
    OTHER_METAL = 4
    METALLOID = 5
    NON_METAL = 6
    HALOGEN = 7
    NOBLE_GAS = 8
    LANTHANIDE = 9
    ACTINIDE = 10

class Element:
    """
    A definition of a single element from the periodic table.
    """
    def __init__(self, number, mass, symbol, name, period, group):
        self._number = number
        self._mass = mass
        self._symbol = symbol
        self._name = name
        self._period = period
        self._group = group
        self._element_type = ElementType.TRANSITION_METAL
        # Type rules
        if group == 1:
            self._element_type = ElementType.ALKALI_METAL
        elif group == 2:
            self._element_type = ElementType.ALKALINE_EARTH_METAL
        elif group == 17:
            self._element_type = ElementType.HALOGEN
        elif group == 18:
            self._element_type = ElementType.NOBLE_GAS
        # Exceptions
        if number in [1, 6, 7, 8, 15, 16, 34]:
            self._element_type = ElementType.NON_METAL
        if number in [5, 14, 32, 33, 51, 52]:
            self._element_type = ElementType.METALLOID
        if number in [13, 31, 49, 50, 81, 82, 83, 84, 113, 114, 115, 116]:
            self._element_type = ElementType.OTHER_METAL
        if 57 <= number <= 71:
            self._element_type = ElementType.LANTHANIDE
        if 89 <= number <= 103:
            self._element_type = ElementType.ACTINIDE


    def __str__(self):
        return "{0} ({1}) - {2}".format(self._symbol, self._name, self._element_type)

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

    @property
    def element_type(self):
        return self._element_type


def init_element_list():
    element_by_atomic_num = []

    elt = Element(1, 1.0078, "H", "Hydrogen", 1, 1)
    element_by_atomic_num.append(elt)

    elt = Element(2, 4.0026, "He", "Helium", 1, 18)
    element_by_atomic_num.append(elt)

    elt = Element(3, 6.9410, "Li", "Lithium", 2, 1)
    element_by_atomic_num.append(elt)

    elt = Element(4, 9.0122, "Be", "Beryllium", 2, 2)
    element_by_atomic_num.append(elt)

    elt = Element(5, 10.811, "B", "Boron", 2, 13)
    element_by_atomic_num.append(elt)

    elt = Element(6, 12.011, "C", "Carbon", 2, 14)
    element_by_atomic_num.append(elt)

    elt = Element(7, 14.007, "N", "Nitrogen", 2, 15)
    element_by_atomic_num.append(elt)

    elt = Element(8, 15.999, "O", "Oxygen", 2, 16)
    element_by_atomic_num.append(elt)

    elt = Element(9, 18.998, "F", "Fluorine", 2, 17)
    element_by_atomic_num.append(elt)

    elt = Element(10, 20.180, "Ne", "Neon", 2, 18)
    element_by_atomic_num.append(elt)

    elt = Element(11, 22.990, "Na", "Sodium", 3, 1)
    element_by_atomic_num.append(elt)

    elt = Element(12, 24.305, "Mg", "Magnesium", 3, 2)
    element_by_atomic_num.append(elt)

    elt = Element(13, 26.982, "Al", "Aluminium", 3, 13)
    element_by_atomic_num.append(elt)

    elt = Element(14, 28.086, "Si", "Silicon", 3, 14)
    element_by_atomic_num.append(elt)

    elt = Element(15, 30.974, "P", "Phosphorus", 3, 15)
    element_by_atomic_num.append(elt)

    elt = Element(16, 32.065, "S", "Sulfur", 3, 16)
    element_by_atomic_num.append(elt)

    elt = Element(17, 35.453, "Cl", "Chlorine", 3, 17)
    element_by_atomic_num.append(elt)

    elt = Element(18, 39.948, "Ar", "Argon", 3, 18)
    element_by_atomic_num.append(elt)

    return element_by_atomic_num

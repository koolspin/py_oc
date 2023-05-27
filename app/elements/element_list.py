from elements.element_defs import Element

def init_element_list():
    element_by_atomic_num = []

    # Period 1
    elt = Element(1, 1.0078, "H", "Hydrogen", 1, 1)
    element_by_atomic_num.append(elt)

    elt = Element(2, 4.0026, "He", "Helium", 1, 18)
    element_by_atomic_num.append(elt)

    # Period 2
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

    # Period 3
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

    # Period 4
    elt = Element(19, 39.098, "K", "Potassium", 4, 1)
    element_by_atomic_num.append(elt)

    elt = Element(20, 40.078, "Ca", "Calcium", 4, 2)
    element_by_atomic_num.append(elt)

    elt = Element(21, 44.956, "Sc", "Scandium", 4, 3)
    element_by_atomic_num.append(elt)

    elt = Element(22, 47.867, "Ti", "Titanium", 4, 4)
    element_by_atomic_num.append(elt)

    elt = Element(23, 50.942, "V", "Vanadium", 4, 5)
    element_by_atomic_num.append(elt)

    elt = Element(24, 51.996, "Cr", "Chromium", 4, 6)
    element_by_atomic_num.append(elt)

    elt = Element(25, 54.938, "Mn", "Manganese", 4, 7)
    element_by_atomic_num.append(elt)

    elt = Element(26, 55.845, "Fe", "Iron", 4, 8)
    element_by_atomic_num.append(elt)

    elt = Element(27, 58.933, "Co", "Cobalt", 4, 9)
    element_by_atomic_num.append(elt)

    elt = Element(28, 58.693, "Ni", "Nickel", 4, 10)
    element_by_atomic_num.append(elt)

    elt = Element(29, 63.546, "Cu", "Copper", 4, 11)
    element_by_atomic_num.append(elt)

    elt = Element(30, 65.380, "Zn", "Zinc", 4, 12)
    element_by_atomic_num.append(elt)

    elt = Element(31, 69.723, "Ga", "Gallium", 4, 13)
    element_by_atomic_num.append(elt)

    elt = Element(32, 72.640, "Ge", "Germanium", 4, 14)
    element_by_atomic_num.append(elt)

    elt = Element(33, 74.922, "As", "Arsenic", 4, 15)
    element_by_atomic_num.append(elt)

    elt = Element(34, 78.960, "Se", "Selenium", 4, 16)
    element_by_atomic_num.append(elt)

    elt = Element(35, 79.904, "Br", "Bromine", 4, 17)
    element_by_atomic_num.append(elt)

    elt = Element(36, 83.798, "Kr", "Krypton", 4, 18)
    element_by_atomic_num.append(elt)

    # Period 5
    elt = Element(37, 85.468, "Rb", "Rubidium", 5, 1)
    element_by_atomic_num.append(elt)

    elt = Element(38, 87.620, "Sr", "Strontium", 5, 2)
    element_by_atomic_num.append(elt)

    elt = Element(39, 88.906, "Y", "Yttrium", 5, 3)
    element_by_atomic_num.append(elt)

    elt = Element(40, 91.224, "Zr", "Zirconium", 5, 4)
    element_by_atomic_num.append(elt)

    elt = Element(41, 92.906, "Nb", "Niobium", 5, 5)
    element_by_atomic_num.append(elt)

    elt = Element(42, 95.950, "Mo", "Molybdenum", 5, 6)
    element_by_atomic_num.append(elt)

    elt = Element(43, 98.000, "Tc", "Technetium", 5, 7)
    element_by_atomic_num.append(elt)

    elt = Element(44, 101.070, "Ru", "Ruthenium", 5, 8)
    element_by_atomic_num.append(elt)

    elt = Element(45, 102.910, "Rh", "Rhodium", 5, 9)
    element_by_atomic_num.append(elt)

    elt = Element(46, 106.420, "Pd", "Palladium", 5, 10)
    element_by_atomic_num.append(elt)

    elt = Element(47, 107.870, "Ag", "Silver", 5, 11)
    element_by_atomic_num.append(elt)

    elt = Element(48, 112.410, "Cd", "Cadmium", 5, 12)
    element_by_atomic_num.append(elt)

    elt = Element(49, 114.820, "In", "Indium", 5, 13)
    element_by_atomic_num.append(elt)

    elt = Element(50, 118.710, "Sn", "Tin", 5, 14)
    element_by_atomic_num.append(elt)

    elt = Element(51, 121.760, "Sb", "Antimony", 5, 15)
    element_by_atomic_num.append(elt)

    elt = Element(52, 127.600, "Te", "Tellerium", 5, 16)
    element_by_atomic_num.append(elt)

    elt = Element(53, 126.900, "I", "Iodine", 5, 17)
    element_by_atomic_num.append(elt)

    elt = Element(54, 131.290, "Xe", "Xenon", 5, 18)
    element_by_atomic_num.append(elt)
    #

    return element_by_atomic_num

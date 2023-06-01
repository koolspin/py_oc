from typing import List
from elements.element_defs import Element

def init_element_list() -> List[Element]:
    element_by_atomic_num = []

    # Period 1
    elt = Element(1, 1.0078, "H", "Hydrogen", 1, 1, "1s^1")
    element_by_atomic_num.append(elt)

    elt = Element(2, 4.0026, "He", "Helium", 1, 18, "1s^2")
    element_by_atomic_num.append(elt)

    # Period 2
    elt = Element(3, 6.9410, "Li", "Lithium", 2, 1, "1s^2 2s^1")
    element_by_atomic_num.append(elt)

    elt = Element(4, 9.0122, "Be", "Beryllium", 2, 2, "1s^2 2s^2")
    element_by_atomic_num.append(elt)

    elt = Element(5, 10.811, "B", "Boron", 2, 13, "1s^2 2s^2 2p^1")
    element_by_atomic_num.append(elt)

    elt = Element(6, 12.011, "C", "Carbon", 2, 14, "1s^2 2s^2 2p^2")
    element_by_atomic_num.append(elt)

    elt = Element(7, 14.007, "N", "Nitrogen", 2, 15, "1s^2 2s^2 2p^3")
    element_by_atomic_num.append(elt)

    elt = Element(8, 15.999, "O", "Oxygen", 2, 16, "1s^2 2s^2 2p^4")
    element_by_atomic_num.append(elt)

    elt = Element(9, 18.998, "F", "Fluorine", 2, 17, "1s^2 2s^2 2p^5")
    element_by_atomic_num.append(elt)

    elt = Element(10, 20.180, "Ne", "Neon", 2, 18, "1s^2 2s^2 2p^6")
    element_by_atomic_num.append(elt)

    # Period 3
    elt = Element(11, 22.990, "Na", "Sodium", 3, 1, "1s^2 2s^2 2p^6 3s^1")
    element_by_atomic_num.append(elt)

    elt = Element(12, 24.305, "Mg", "Magnesium", 3, 2, "1s^2 2s^2 2p^6 3s^2")
    element_by_atomic_num.append(elt)

    elt = Element(13, 26.982, "Al", "Aluminium", 3, 13, "1s^2 2s^2 2p^6 3s^2 3p^1")
    element_by_atomic_num.append(elt)

    elt = Element(14, 28.086, "Si", "Silicon", 3, 14, "1s^2 2s^2 2p^6 3s^2 3p^2")
    element_by_atomic_num.append(elt)

    elt = Element(15, 30.974, "P", "Phosphorus", 3, 15, "1s^2 2s^2 2p^6 3s^2 3p^3")
    element_by_atomic_num.append(elt)

    elt = Element(16, 32.065, "S", "Sulfur", 3, 16, "1s^2 2s^2 2p^6 3s^2 3p^4")
    element_by_atomic_num.append(elt)

    elt = Element(17, 35.453, "Cl", "Chlorine", 3, 17, "1s^2 2s^2 2p^6 3s^2 3p^5")
    element_by_atomic_num.append(elt)

    elt = Element(18, 39.948, "Ar", "Argon", 3, 18, "1s^2 2s^2 2p^6 3s^2 3p^6")
    element_by_atomic_num.append(elt)

    # Period 4
    elt = Element(19, 39.098, "K", "Potassium", 4, 1, "1s^2 2s^2 2p^6 3s^2 3p^6 4s^1")
    element_by_atomic_num.append(elt)

    elt = Element(20, 40.078, "Ca", "Calcium", 4, 2, "1s^2 2s^2 2p^6 3s^2 3p^6 4s^2")
    element_by_atomic_num.append(elt)

    elt = Element(21, 44.956, "Sc", "Scandium", 4, 3, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^1 4s^2")
    element_by_atomic_num.append(elt)

    elt = Element(22, 47.867, "Ti", "Titanium", 4, 4, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^2 4s^2")
    element_by_atomic_num.append(elt)

    elt = Element(23, 50.942, "V", "Vanadium", 4, 5, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^3 4s^2")
    element_by_atomic_num.append(elt)

    elt = Element(24, 51.996, "Cr", "Chromium", 4, 6, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^5 4s^1")
    element_by_atomic_num.append(elt)

    elt = Element(25, 54.938, "Mn", "Manganese", 4, 7, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^5 4s^2")
    element_by_atomic_num.append(elt)

    elt = Element(26, 55.845, "Fe", "Iron", 4, 8, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^6 4s^2")
    element_by_atomic_num.append(elt)

    elt = Element(27, 58.933, "Co", "Cobalt", 4, 9, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^7 4s^2")
    element_by_atomic_num.append(elt)

    elt = Element(28, 58.693, "Ni", "Nickel", 4, 10, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^8 4s^2")
    element_by_atomic_num.append(elt)

    elt = Element(29, 63.546, "Cu", "Copper", 4, 11, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^1")
    element_by_atomic_num.append(elt)

    elt = Element(30, 65.380, "Zn", "Zinc", 4, 12, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2")
    element_by_atomic_num.append(elt)

    elt = Element(31, 69.723, "Ga", "Gallium", 4, 13, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^1")
    element_by_atomic_num.append(elt)

    elt = Element(32, 72.640, "Ge", "Germanium", 4, 14, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^2")
    element_by_atomic_num.append(elt)

    elt = Element(33, 74.922, "As", "Arsenic", 4, 15, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^3")
    element_by_atomic_num.append(elt)

    elt = Element(34, 78.960, "Se", "Selenium", 4, 16, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^4")
    element_by_atomic_num.append(elt)

    elt = Element(35, 79.904, "Br", "Bromine", 4, 17, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^5")
    element_by_atomic_num.append(elt)

    elt = Element(36, 83.798, "Kr", "Krypton", 4, 18, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6")
    element_by_atomic_num.append(elt)

    # Period 5
    elt = Element(37, 85.468, "Rb", "Rubidium", 5, 1, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 5s^1")
    element_by_atomic_num.append(elt)

    elt = Element(38, 87.620, "Sr", "Strontium", 5, 2, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 5s^2")
    element_by_atomic_num.append(elt)

    elt = Element(39, 88.906, "Y", "Yttrium", 5, 3, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^1 5s^2")
    element_by_atomic_num.append(elt)

    elt = Element(40, 91.224, "Zr", "Zirconium", 5, 4, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^2 5s^2")
    element_by_atomic_num.append(elt)

    elt = Element(41, 92.906, "Nb", "Niobium", 5, 5, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^4 5s^1")
    element_by_atomic_num.append(elt)

    elt = Element(42, 95.950, "Mo", "Molybdenum", 5, 6, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^5 5s^1")
    element_by_atomic_num.append(elt)

    elt = Element(43, 98.000, "Tc", "Technetium", 5, 7, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^5 5s^2")
    element_by_atomic_num.append(elt)

    elt = Element(44, 101.070, "Ru", "Ruthenium", 5, 8, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^7 5s^1")
    element_by_atomic_num.append(elt)

    elt = Element(45, 102.910, "Rh", "Rhodium", 5, 9, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^8 5s^1")
    element_by_atomic_num.append(elt)

    elt = Element(46, 106.420, "Pd", "Palladium", 5, 10, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10")
    element_by_atomic_num.append(elt)

    elt = Element(47, 107.870, "Ag", "Silver", 5, 11, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 5s^1")
    element_by_atomic_num.append(elt)

    elt = Element(48, 112.410, "Cd", "Cadmium", 5, 12, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 5s^2")
    element_by_atomic_num.append(elt)

    elt = Element(49, 114.820, "In", "Indium", 5, 13, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 5s^2 5p^1")
    element_by_atomic_num.append(elt)

    elt = Element(50, 118.710, "Sn", "Tin", 5, 14, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 5s^2 5p^2")
    element_by_atomic_num.append(elt)

    elt = Element(51, 121.760, "Sb", "Antimony", 5, 15, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 5s^2 5p^3")
    element_by_atomic_num.append(elt)

    elt = Element(52, 127.600, "Te", "Tellerium", 5, 16, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 5s^2 5p^4")
    element_by_atomic_num.append(elt)

    elt = Element(53, 126.900, "I", "Iodine", 5, 17, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 5s^2 5p^5")
    element_by_atomic_num.append(elt)

    elt = Element(54, 131.290, "Xe", "Xenon", 5, 18, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 5s^2 5p^6")
    element_by_atomic_num.append(elt)

    # Period 6
    elt = Element(55, 132.910, "Cs", "Caesium", 6, 1, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 5s^2 5p^6 6s^1")
    element_by_atomic_num.append(elt)

    elt = Element(56, 137.330, "Ba", "Barium", 6, 2, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 5s^2 5p^6 6s^2")
    element_by_atomic_num.append(elt)

    elt = Element(57, 138.910, "La", "Lanthanum", 6, 3, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 5s^2 5p^6 5d^1 6s^2")
    element_by_atomic_num.append(elt)

    # TODO: Lanthanides go here

    elt = Element(72, 178.490, "Hf", "Hafnium", 6, 4, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^14 5s^2 5p^6 5d^2 6s^2")
    element_by_atomic_num.append(elt)

    elt = Element(73, 180.950, "Ta", "Tantalum", 6, 5, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^14 5s^2 5p^6 5d^3 6s^2")
    element_by_atomic_num.append(elt)

    elt = Element(74, 183.840, "W", "Tungsten", 6, 6, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^14 5s^2 5p^6 5d^4 6s^2")
    element_by_atomic_num.append(elt)

    elt = Element(75, 186.210, "Re", "Rhenium", 6, 7, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^14 5s^2 5p^6 5d^5 6s^2")
    element_by_atomic_num.append(elt)

    elt = Element(76, 190.230, "Os", "Osmium", 6, 8, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^14 5s^2 5p^6 5d^6 6s^2")
    element_by_atomic_num.append(elt)

    elt = Element(77, 192.220, "Ir", "Iridium", 6, 9, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^14 5s^2 5p^6 5d^7 6s^2")
    element_by_atomic_num.append(elt)

    elt = Element(78, 195.080, "Pt", "Platinum", 6, 10, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^14 5s^2 5p^6 5d^9 6s^1")
    element_by_atomic_num.append(elt)

    elt = Element(79, 196.970, "Au", "Gold", 6, 11, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^14 5s^2 5p^6 5d^10 6s^1")
    element_by_atomic_num.append(elt)

    elt = Element(80, 200.590, "Hg", "Mercury", 6, 12, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^14 5s^2 5p^6 5d^10 6s^2")
    element_by_atomic_num.append(elt)

    elt = Element(81, 204.380, "Tl", "Thalium", 6, 13, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^14 5s^2 5p^6 5d^10 6s^2 6p^1")
    element_by_atomic_num.append(elt)

    elt = Element(82, 207.200, "Pb", "Lead", 6, 14, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^14 5s^2 5p^6 5d^10 6s^2 6p^2")
    element_by_atomic_num.append(elt)

    elt = Element(83, 208.980, "Bi", "Bismuth", 6, 15, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^14 5s^2 5p^6 5d^10 6s^2 6p^3")
    element_by_atomic_num.append(elt)

    elt = Element(84, 209.000, "Po", "Polonium", 6, 16, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^14 5s^2 5p^6 5d^10 6s^2 6p^4")
    element_by_atomic_num.append(elt)

    elt = Element(85, 210.000, "At", "Astatine", 6, 17, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^14 5s^2 5p^6 5d^10 6s^2 6p^5")
    element_by_atomic_num.append(elt)

    elt = Element(86, 222.000, "Rn", "Radon", 6, 18, "1s^2 2s^2 2p^6 3s^2 3p^6 3d^10 4s^2 4p^6 4d^10 4f^14 5s^2 5p^6 5d^10 6s^2 6p^6")
    element_by_atomic_num.append(elt)
    #

    return element_by_atomic_num

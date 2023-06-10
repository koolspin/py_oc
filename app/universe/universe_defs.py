from typing import List, Optional, Dict

from app.bonds.bond_defs import ChemicalBond
from app.elements.organic_elements import *
from importlib import *


class Universe:
    """
    Universe, in this context means a system for containing raw (unbound) elements as well as molecules,
    identifying instances of each as well as managing the relationships between them.
    """
    def __init__(self) -> None:
        # All atoms in the universe!
        self._element_by_id: List[Element] = []
        self._element_by_atomic_number: Dict[int, List[Element]] = {}
        self._bond_by_id: List[ChemicalBond] = []
        self._module = import_module("app.elements.organic_elements")

    def __iter__(self):
        return UniverseElementIter(self)

    def get_element_by_id(self, id: int) -> Optional[Element]:
        try:
            return self._element_by_id[id]
        except IndexError:
            return None

    def get_elements_by_atomic_number(self, number: int) -> Optional[List[Element]]:
        return self._element_by_atomic_number.get(number)

    def get_all_bonds(self) -> List[ChemicalBond]:
        return self._bond_by_id

    def get_bond_by_id(self, id: int) -> Optional[ChemicalBond]:
        try:
            return self._bond_by_id[id]
        except IndexError:
            return None

    def organic_factory(self, name: str, count: int) -> List[Element]:
        atoms = []
        id = len(self._element_by_id)
        for ix in range(count):
            try:
                klass = getattr(self._module, name)
                elt: Element = klass(id + ix)
                self._element_by_id.append(elt)
                elts_by_number = self._element_by_atomic_number.get(elt.number)
                if elts_by_number is None:
                    elts_by_number = [elt]
                    self._element_by_atomic_number[elt.number] = elts_by_number
                else:
                    elts_by_number.append(elt)
                atoms.append(elt)
            except AttributeError:
                break
        return atoms

    def element_factory(self, number: int, mass: float, symbol: str, name: str, period: int, group: int, config: str,
                        count: int) -> List[Element]:
        atoms = []
        id = len(self._element_by_id)
        for ix in range(count):
            elt = Element(number, mass, symbol, name, period, group, config, id + ix)
            self._element_by_id.append(elt)
            elts_by_number = self._element_by_atomic_number.get(elt.number)
            if elts_by_number is None:
                elts_by_number = [elt]
                self._element_by_atomic_number[elt.number] = elts_by_number
            else:
                elts_by_number.append(elt)
            atoms.append(elt)
        return atoms

    def bond_factory(self, left: int, right: int, count: int) -> int:
        id = len(self._bond_by_id)
        bond = ChemicalBond(left, right, count, id)
        self._bond_by_id.append(bond)
        left_elt = self.get_element_by_id(left)
        left_elt.add_bond(id)
        right_elt = self.get_element_by_id(right)
        right_elt.add_bond(id)


class UniverseElementIter:
    """
    Iterate over all elements in the Universe
    """
    def __init__(self, universe: Universe) -> None:
        self._universe = universe
        self._ix: int = 0

    def __iter__(self):
        return self

    def __next__(self) -> Element:
        elt = self._universe.get_element_by_id(self._ix)
        if elt is not None:
            self._ix += 1
            return elt
        else:
            raise StopIteration
from typing import List, Optional

from app.elements.organic_elements import *


class Universe:
    """
    Universe, in this context means a system for containing raw (unbound) elements as well as molecules,
    identifying instances of each as well as managing the relationships between them.
    """
    def __init__(self) -> None:
        # All atoms in the universe!
        self._element_by_id: List[Element] = []

    def __iter__(self):
        return UniverseElementIter(self)

    def get_element_by_id(self, id: int) -> Optional[Element]:
        try:
            return self._element_by_id[id]
        except IndexError:
            return None

    def MakeElementHydrogen(self) -> Element:
        id = len(self._element_by_id)
        elt = Hydrogen(id)
        self._element_by_id.append(elt)
        return elt

    def MakeElementCarbon(self) -> Element:
        id = len(self._element_by_id)
        elt = Carbon(id)
        self._element_by_id.append(elt)
        return elt

    def MakeElementOxygen(self) -> Element:
        id = len(self._element_by_id)
        elt = Oxygen(id)
        self._element_by_id.append(elt)
        return elt

    def MakeElementNitrogen(self) -> Element:
        id = len(self._element_by_id)
        elt = Nitrogen(id)
        self._element_by_id.append(elt)
        return elt

    def MakeElementPhosphorus(self) -> Element:
        id = len(self._element_by_id)
        elt = Phosphorus(id)
        self._element_by_id.append(elt)
        return elt

    def MakeElementSulfur(self) -> Element:
        id = len(self._element_by_id)
        elt = Sulfur(id)
        self._element_by_id.append(elt)
        return elt

    def MakeElement(self, number: int, mass: float, symbol: str, name: str, period: int, group: int, config: str) -> Element:
        id = len(self._element_by_id)
        elt = Element(number, mass, symbol, name, period, group, config, id)
        self._element_by_id.append(elt)
        return elt


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
from typing import Optional


class ChemicalBond:
    """
    A model of a chemical bond
    """
    def __init__(self, left_atom_id: int, right_atom_id: int, bond_count: int, id: Optional[int]):
        # The ID of this bond
        self._id = 0
        # The ID of the "left" atom
        self._left_atom_id = left_atom_id
        # The ID of the "right" atom
        self._right_atom_id = right_atom_id
        # Is this a single, double or triple bond
        # This equates to 2, 4 of 6 electrons being bound
        self._bond_count = bond_count
        if id is not None:
            self._id = id

    def __str__(self) -> str:
        return "{0}: {1}-{2} - {3}".format(self._id, self._left_atom_id, self._right_atom_id, self._bond_count)

    @property
    def id(self) -> int:
        return self._id

    @property
    def left_id(self) -> int:
        return self._left_atom_id

    @property
    def right_id(self) -> int:
        return self._right_atom_id

    @property
    def bond_count(self) -> int:
        return self._bond_count


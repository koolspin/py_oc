from typing import Optional

from app.elements.element_defs import Element


class Hydrogen(Element):
    """
    The lightest element.
    """
    name = "Hydrogen"
    def __init__(self, id: Optional[int]) -> None:
        super().__init__(1, 1.0078, "H", "Hydrogen", 1, 1, "1s^1", id)


class Carbon(Element):
    """
    The backbone of organic chemistry.
    """
    name = "Carbon"
    def __init__(self, id: Optional[int]) -> None:
        super().__init__(6, 12.011, "C", "Carbon", 2, 14, "1s^2 2s^2 2p^2", id)


class Oxygen(Element):
    """
    I like Oxygen.
    """
    name = "Oxygen"
    def __init__(self, id: Optional[int]) -> None:
        super().__init__(8, 15.999, "O", "Oxygen", 2, 16, "1s^2 2s^2 2p^4", id)


class Nitrogen(Element):
    """
    Just call me "Nitro"!
    """
    name = "Nitrogen"
    def __init__(self, id: Optional[int]) -> None:
        super().__init__(7, 14.007, "N", "Nitrogen", 2, 15, "1s^2 2s^2 2p^3", id)


class Phosphorus(Element):
    """
    """
    name = "Phosphorus"
    def __init__(self, id: Optional[int]) -> None:
        super().__init__(15, 30.974, "P", "Phosphorus", 3, 15, "1s^2 2s^2 2p^6 3s^2 3p^3", id)


class Sulfur(Element):
    """
    """
    name = "Sulfur"
    def __init__(self, id: Optional[int]) -> None:
        super().__init__(16, 32.065, "S", "Sulfur", 3, 16, "1s^2 2s^2 2p^6 3s^2 3p^4", id)

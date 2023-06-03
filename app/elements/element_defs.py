import re
from enum import Enum
from typing import List, Optional


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


class SubShellDesignation(Enum):
    TYPE_UNKNOWN = '?'
    S_TYPE = 's'
    P_TYPE = 'p'
    D_TYPE = 'd'
    F_TYPE = 'f'


class SubShell:
    """
    The definition of an electron shell
    """
    def __init__(self, electron_count: int, subshell_type: SubShellDesignation) -> None:
        self._electron_count: int = electron_count
        self._subshell_type: SubShellDesignation = subshell_type

    def __str__(self) -> str:
        if self._subshell_type != SubShellDesignation.TYPE_UNKNOWN:
            return "{0}^{1}".format(self._subshell_type.value, self._electron_count)
        else:
            return "?^{0}".format(self._electron_count)


class Element:
    """
    A definition of a single element from the periodic table.

    TODO:
    Should we add a representation for the electron configuration?
    Like: 1s^2 2s^2 2p^2
    Or should we calculate it based on the atomic number?
    """

    def __init__(self, number: int, mass: float, symbol: str, name: str, period: int, group: int, config: str, id: Optional[int]) -> None:
        # Note this id is used only to find unique atoms in our universe :-)
        # This is used only for stupid programming tricks and, as far as we know, this does not represent an attribute
        # of the physical world.
        self._id = 0
        #
        self._number: int = number
        self._mass: float = mass
        self._symbol: str = symbol
        self._name: str = name
        self._period: int = period
        self._group: int = group
        self._original_config: str = config
        self._electron_shells: List[List[SubShell]] = []
        self._set_element_type()
        self._populate_electron_shells_with_config(config)
        if id is not None:
            self._id = id

    def __str__(self) -> str:
        return "{0}: {1} ({2}) - {3}".format(self._id, self._symbol, self._name, self._element_type)

    @property
    def id(self) -> int:
        return self._id

    @property
    def number(self) -> int:
        return self._number

    @property
    def mass(self) -> float:
        return self._mass

    @property
    def symbol(self) -> str:
        return self._symbol

    @property
    def name(self) -> str:
        return self._name

    @property
    def element_type(self) -> ElementType:
        return self._element_type

    def get_printable_electron_config(self) -> str:
        electron_config = ""
        sh_num = 1
        for sh in self._electron_shells:
            for sub in sh:
                electron_config += "{0}{1} ".format(sh_num, sub)
            sh_num += 1
        return electron_config

    def _set_element_type(self) -> None:
        """
        Set the element type enum based on the atomic number.
        """
        self._element_type = ElementType.TRANSITION_METAL
        if self._group == 1:
            self._element_type = ElementType.ALKALI_METAL
        elif self._group == 2:
            self._element_type = ElementType.ALKALINE_EARTH_METAL
        elif self._group == 17:
            self._element_type = ElementType.HALOGEN
        elif self._group == 18:
            self._element_type = ElementType.NOBLE_GAS
        # Exceptions
        if self._number in [1, 6, 7, 8, 15, 16, 34]:
            self._element_type = ElementType.NON_METAL
        if self._number in [5, 14, 32, 33, 51, 52]:
            self._element_type = ElementType.METALLOID
        if self._number in [13, 31, 49, 50, 81, 82, 83, 84, 113, 114, 115, 116]:
            self._element_type = ElementType.OTHER_METAL
        if 57 <= self._number <= 71:
            self._element_type = ElementType.LANTHANIDE
        if 89 <= self._number <= 103:
            self._element_type = ElementType.ACTINIDE

    def _populate_electron_shells_with_config(self, electron_config: str) -> None:
        """
        I don't know all the rules concerning how electrons are actually distributed to the various shells and orbits.
        There are rules such as the Aufbau princle, the Pauli exclusion princible and Hund's rule, which I think I understand.
        But there also seems to be exceptions to these rules such as the electron config of Chromium where electrons
        seem to move between the s and d subshells in ways that violate the 3 rules above.
        So, for now, I'm going to provide this function which simply parses a string representation of an
        electron configuration in order to build the required graph.
        Here's an example of such a string: "1s^2 2s^2 2p^2"
        """
        all_shells: List[List[SubShell]] = []
        cur_shell: int = -1
        sub_shell: List[SubShell] = []
        sub_shells = electron_config.split()
        for sub in sub_shells:
            # Let's use a regex to parse each subshell (ex. 1s^2)
            ex_p = re.compile("(\d)([spdf])\^(\d+)")
            m = ex_p.match(sub)
            matches = m.groups()
            if len(matches) >= 3:
                shell = int(matches[0])
                sub_shell_type = matches[1]
                electron_count = int(matches[2])
                if shell != cur_shell:
                    if len(sub_shell) > 0:
                        all_shells.append(sub_shell)
                        sub_shell = []
                    cur_shell = shell
                sub = SubShell(electron_count, SubShellDesignation(sub_shell_type))
                sub_shell.append(sub)
        if len(sub_shell) > 0:
            all_shells.append(sub_shell)
        self._electron_shells = all_shells

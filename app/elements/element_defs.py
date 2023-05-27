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


class SubShellDesignation(Enum):
    TYPE_UNKNOWN = 0
    S_TYPE = 1
    P_TYPE = 2
    D_TYPE = 3
    F_TYPE = 4


class SubShell:
    """
    The definition of an electron shell
    """
    def __init__(self, electron_count, subshell_type):
        self._electron_count = electron_count
        self._subshell_type = subshell_type
        self._type_map = {SubShellDesignation.S_TYPE: 's', SubShellDesignation.P_TYPE: 'p',
                          SubShellDesignation.D_TYPE: 'd', SubShellDesignation.F_TYPE: 'f'}

    def __str__(self):
        if self._subshell_type != SubShellDesignation.TYPE_UNKNOWN:
            return "{0}^{1}".format(self._type_map[self._subshell_type], self._electron_count)
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

    def __init__(self, number, mass, symbol, name, period, group):
        self._number = number
        self._mass = mass
        self._symbol = symbol
        self._name = name
        self._period = period
        self._group = group
        self._electron_shells = []
        self._set_element_type()
        self._populate_electron_shells()

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

    def get_printable_electron_config(self) -> str:
        electron_config = ""
        sh_num = 1
        for sh in self._electron_shells:
            for sub in sh:
                electron_config += "{0}{1} ".format(sh_num, sub)
            sh_num += 1
        return electron_config

    def _set_element_type(self):
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

    def _populate_electron_shells(self):
        """
        Fills in the electron shells array based on the atomic number of the element.
        TODO: Can we use an algorithm here? Need to fill in the 6th and 7th period
        """
        self._electron_shells = self._create_period_shell()
        if self._period == 1:
            num_electrons = self._number
            sub_shell = []
            sub = SubShell(num_electrons, SubShellDesignation.S_TYPE)
            sub_shell.append(sub)
            self._electron_shells.append(sub_shell)
        elif self._period in [2, 3]:
            prev_shell_electrons = 2
            if self._period == 3:
                prev_shell_electrons = 10
            num_shell_electrons = self._number - prev_shell_electrons
            num_s_electrons = num_shell_electrons if num_shell_electrons <= 2 else 2
            num_p_electrons = num_shell_electrons - num_s_electrons
            sub_shell = []
            sub = SubShell(num_s_electrons, SubShellDesignation.S_TYPE)
            sub_shell.append(sub)
            if num_p_electrons >= 1:
                sub = SubShell(num_p_electrons, SubShellDesignation.P_TYPE)
                sub_shell.append(sub)
            self._electron_shells.append(sub_shell)
        elif self._period in [4, 5]:
            prev_shell_electrons = 18
            if self._period == 5:
               prev_shell_electrons = 36
            num_shell_electrons = self._number - prev_shell_electrons
            sub_shell = []
            num_s_electrons = 0
            num_p_electrons = 0
            num_d_electrons = 0
            if num_shell_electrons <= 2:
                # Potassium, Calcium
                num_s_electrons = num_shell_electrons
            elif 3 <= num_shell_electrons <= 5:
                # Scandium, Titanium, Vanadium
                num_s_electrons = 2
                num_d_electrons = num_shell_electrons - num_s_electrons
            elif num_shell_electrons == 6:
                # Chromium
                num_s_electrons = 1
                num_d_electrons = 5
            elif num_shell_electrons == 7:
                # Manganese
                num_s_electrons = 2
                num_d_electrons = 5
            elif num_shell_electrons == 8:
                # Iron
                num_s_electrons = 2
                num_d_electrons = 6
            elif num_shell_electrons == 9:
                # Cobalt
                num_s_electrons = 2
                num_d_electrons = 7
            elif num_shell_electrons == 10:
                # Nickel
                num_s_electrons = 2
                num_d_electrons = 8
            elif num_shell_electrons == 11:
                # Copper
                num_s_electrons = 1
                num_d_electrons = 10
            else:
                num_s_electrons = 2
                num_d_electrons = 10
                num_p_electrons = num_shell_electrons - 12
            sub = SubShell(num_s_electrons, SubShellDesignation.S_TYPE)
            sub_shell.append(sub)
            if num_p_electrons > 0:
                sub = SubShell(num_p_electrons, SubShellDesignation.P_TYPE)
                sub_shell.append(sub)
            if num_d_electrons > 0:
                prev_shell = self._electron_shells[-1]
                sub = SubShell(num_d_electrons, SubShellDesignation.D_TYPE)
                prev_shell.append(sub)
            self._electron_shells.append(sub_shell)

    def _create_period_shell(self):
        """
        Create the base shells by creating the shells as appropriate for the noble gas from
        the previous Period.
        For example, an element in Period 2 would rely on the base shells from Helium,
        the noble gas from Period 1
        """
        # This is a 2 dimensional array. Each entry represents a shell and consists of an array of subshells.
        all_period_shells = []
        previous_period = self._period - 1
        if previous_period > 0:
            # Helium
            sub_shell = []
            sub = SubShell(2, SubShellDesignation.S_TYPE)
            sub_shell.append(sub)
            all_period_shells.append(sub_shell)
        if previous_period > 1:
            # Neon
            sub_shell = []
            sub = SubShell(2, SubShellDesignation.S_TYPE)
            sub_shell.append(sub)
            sub = SubShell(6, SubShellDesignation.P_TYPE)
            sub_shell.append(sub)
            all_period_shells.append(sub_shell)
        if previous_period > 2:
            # Argon
            sub_shell = []
            sub = SubShell(2, SubShellDesignation.S_TYPE)
            sub_shell.append(sub)
            sub = SubShell(6, SubShellDesignation.P_TYPE)
            sub_shell.append(sub)
            all_period_shells.append(sub_shell)
        if previous_period > 3:
            # Krypton
            # add the d subshell to complete shell 3
            prev_shell = all_period_shells[-1]
            sub = SubShell(10, SubShellDesignation.D_TYPE)
            prev_shell.append(sub)
            # Now we can create shell 4
            sub_shell = []
            sub = SubShell(2, SubShellDesignation.S_TYPE)
            sub_shell.append(sub)
            sub = SubShell(6, SubShellDesignation.P_TYPE)
            sub_shell.append(sub)
            all_period_shells.append(sub_shell)
        if previous_period > 4:
            # Xenon
            # add the d subshell to complete shell 4
            prev_shell = all_period_shells[-1]
            sub = SubShell(10, SubShellDesignation.D_TYPE)
            prev_shell.append(sub)
            # Now we can create shell 5
            sub_shell = []
            sub = SubShell(2, SubShellDesignation.S_TYPE)
            sub_shell.append(sub)
            sub = SubShell(6, SubShellDesignation.P_TYPE)
            sub_shell.append(sub)
            all_period_shells.append(sub_shell)
        if previous_period > 5:
            # Radon
            # First, add to shell 4
            shell4 = all_period_shells[3]
            sub = SubShell(14, SubShellDesignation.F_TYPE)
            shell4.append(sub)
            # Next, add to shell 5
            shell5 = all_period_shells[4]
            sub = SubShell(10, SubShellDesignation.D_TYPE)
            shell5.append(sub)
            # Now we can create shell 6
            sub_shell = []
            sub = SubShell(2, SubShellDesignation.S_TYPE)
            sub_shell.append(sub)
            sub = SubShell(6, SubShellDesignation.P_TYPE)
            sub_shell.append(sub)
            all_period_shells.append(sub_shell)
        return all_period_shells

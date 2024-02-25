from enum import Enum

class OscillationSupport(Enum):
    NONE = 0
    HORIZONTAL = 1
    BOTH = 2

class PyDreoFanDefinition():

    def __init__(self, 
                preset_modes: list, 
                speed_range: range,
                oscillation_support: OscillationSupport):
                self.preset_modes = preset_modes
                self.speed_range = speed_range
                self.oscillation_support = oscillation_support

class PyDreoHeaterDefinition():

    def __init__(self, 
                preset_modes: list, 
                heat_range: range,
                ecolevel_range: range,
                oscillation_support: OscillationSupport):
                self.preset_modes = preset_modes
                self.heat_range = heat_range
                self.ecolevel_range = ecolevel_range
                self.oscillation_support = oscillation_support

from dataclasses import dataclass
from Options import Choice, DefaultOnToggle, NamedRange, OptionGroup, PerGameCommonOptions, Range, Removed, Toggle

class CaveGeneration(Choice):
    """ How Caves should be generated"""
    option_vanilla = 0
    option_kurumizome = 1
    option_fullrando = 2
    display_name = "Cave Generation"
    default = 0

@dataclass
class Pikmin2Options(PerGameCommonOptions):
    cave_gen: CaveGeneration
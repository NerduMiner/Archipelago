from BaseClasses import MultiWorld
from .Names import LocationName, ItemName
from worlds.AutoWorld import LogicMixin
from worlds.generic.Rules import add_rule, set_rule

def set_rules(world: MultiWorld, player: int):
    world.completion_condition[player] = lambda state: state.has(ItemName.onion_blue, player)

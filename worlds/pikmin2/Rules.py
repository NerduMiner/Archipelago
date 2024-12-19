from BaseClasses import MultiWorld
from .Names import LocationName, ItemName
from worlds.AutoWorld import LogicMixin
from worlds.generic.Rules import add_rule, set_rule

# This is currently just the standard pay off debt run where you collect 10,000 pokos
# worth of treasure
def set_rules(world: MultiWorld, player: int):
    world.completion_condition[player] = lambda state: state.has("Pokos", player, 10000)

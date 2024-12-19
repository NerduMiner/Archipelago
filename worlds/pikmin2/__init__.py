from typing import Any, Dict, List, Set, Tuple, TextIO

from BaseClasses import Item, MultiWorld, Location, Tutorial, ItemClassification, CollectionState
from .Items import item_table, item_groups
from .Locations import get_locations
from .Regions import create_regions
from .Options import Pikmin2Options
from .Rules import set_rules
from ..AutoWorld import World, WebWorld

class Pikmin2WebWorld(WebWorld):
    theme = "stone"
    setup = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Pikmin 2 Randomizer connected to an Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["NerduMiner"]
    )

    tutorials = [setup]

class Pikmin2World(World):
    """
    Pikmin 2 is an action strategy game starring the titular Captain Olimar.
    After sucessfully escaping PNF-404, Olimar finds himself thrust back onto the planet once again.
    With his partner Louie, the two must pay off a hefty debt with the help of the Pikmin.
    """

    game = "Pikmin 2"
    topology_present = True
    data_version = 0 # TODO: Remove when checksum is implemented
    web = Pikmin2WebWorld()

    item_name_to_id = {name: data.code for name, data, in item_table.items()}
    location_name_to_id = {location.name: location.code for location in get_locations(None, None)}    
    item_name_groups = item_groups

    options_dataclass = Pikmin2Options
    options: Pikmin2Options

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
    
    def create_regions(self):
        create_regions(self.multiworld, self.player, get_locations(self.multiworld, self.player))

    def create_items(self):
        pool: List[Item] = []
        for name, data in item_table.items():
            item = self.create_item(name)
            pool.append(item)
        
        self.multiworld.itempool += pool
    
    def create_item(self, name: str) -> Item:
        item_id: int = self.item_name_to_id[name]

        return Item(name,
                    item_table[name].classification,
                    item_id, self.player)

    # In Pikmin 2, Treasures have a value in "Pokos"
    # Debt Repayed goals require us to track the amount of money we currently have collected
    def collect(self, state: CollectionState, item: Item) -> bool:
        value = super().collect(state, item)

        if item.name in item_table:
            state.prog_items[self.player]["Pokos"] += item_table[item.name].value

        return value
    
    def remove(self, state: CollectionState, item: Item) -> bool:
        value = super().remove(state, item)

        if item.name in item_table:
           state.prog_items[self.player]["Pokos"] -= item_table[item.name].value
           if not state.prog_items[self.player]["Pokos"]:
               del state.prog_items[self.player]["Pokos"]
        
        return value

    def set_rules(self) -> None:
        set_rules(self.multiworld, self.player)

    def generate_basic(self):
        pass

    def generate_output(self, output_directory: str) -> None:
        pass
        

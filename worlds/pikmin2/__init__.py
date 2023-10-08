from typing import Any, Dict, List, Set, Tuple, TextIO

from BaseClasses import Item, MultiWorld, Location, Tutorial, ItemClassification
from .Items import item_table, item_groups
from .Locations import get_locations
from .Regions import create_regions
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

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
    
    def create_regions(self):
        create_regions(self.multiworld, self.player, get_locations(self.multiworld, self.player))

    def create_items(self):
        pool: List[Item] = []
        for name, data in item_table.items():
            for _ in range(data.count):
                item = self.create_item(name)
                pool.append(item)
        
        self.multiworld.itempool += pool
    
    def create_item(self, name: str) -> Item:
        item_id: int = self.item_name_to_id[name]

        return Item(name,
                    item_table[name].classification,
                    item_id, self.player)
        
    def set_rules(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def generate_basic(self):
        pass
        

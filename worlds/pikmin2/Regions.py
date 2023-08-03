from typing import List, Dict, Tuple, Optional, Callable
from BaseClasses import MultiWorld, Region, Entrance, Location, ItemClassification
from .Items import Pikmin2Item
from .Locations import LocationData
from .Names import LocationName, ItemName
from worlds.generic.Rules import add_rule

# Our Base ID, we will reserve this and the following 200 ids for our locations
baseID = 25000

def create_regions(multiworld: MultiWorld, player: int, locations: LocationData, location_cache: List[Location]):
    locations_per_region = get_locations_per_region(locations)

    regions = [
        create_region(multiworld, player, locations_per_region, location_cache, 'Menu'),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.vor_region1),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.vor_region2),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.vor_region3),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.ec_region),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.scx_region),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.fc_region),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.aw_region1),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.aw_region2),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.aw_region3),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.aw_region4),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.aw_region5),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.aw_region6),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.aw_region7),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.hob_region),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.wfg_region),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.bk_region),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.sh_region),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.pp_region1),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.pp_region2),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.pp_region3),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.pp_region4),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.pp_region5),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.pp_region6),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.pp_region7),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.cos_region),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.gk_region),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.sr_region),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.sc_region),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.ww_region1),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.ww_region2),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.ww_region3),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.ww_region4),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.coc_region),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.hoh_region),
        create_region(multiworld, player, locations_per_region, location_cache, LocationName.dd_region),
    ]

    multiworld.regions += regions

    # Connections
    
    # World Map
    connect(multiworld, player, ('Menu -> ' + LocationName.vor_region1), 'Menu', LocationName.vor_region1)
    connect(multiworld, player, ('Menu -> ' + LocationName.aw_region1), 'Menu', LocationName.aw_region1, lambda state: state.has(ItemName.spherical_atlas, player))
    connect(multiworld, player, ('Menu -> ' + LocationName.pp_region1), 'Menu', LocationName.pp_region1, lambda state: state.has(ItemName.geographical_projection, player))
    connect(multiworld, player, ('Menu -> ' + LocationName.ww_region1), 'Menu', LocationName.ww_region1, lambda state: state.has(ItemName.the_key, player))
    # Valley of Repose
    connect(multiworld, player, (LocationName.vor_region1 + ' -> ' + LocationName.vor_region2), LocationName.vor_region1, LocationName.vor_region2, lambda state: state.has(ItemName.onion_blue, player))
    connect(multiworld, player, (LocationName.vor_region1 + ' -> ' + LocationName.ec_region), LocationName.vor_region1, LocationName.ec_region)
    connect(multiworld, player, (LocationName.vor_region2 + ' -> ' + LocationName.vor_region3), LocationName.vor_region2, LocationName.vor_region3, lambda state: state.has(ItemName.onion_white, player))
    connect(multiworld, player, (LocationName.vor_region2 + ' -> ' + LocationName.fc_region), LocationName.vor_region2, LocationName.fc_region)
    connect(multiworld, player, (LocationName.vor_region3 + ' -> ' + LocationName.scx_region), LocationName.vor_region3, LocationName.scx_region)
    # Awakening Wood
    connect(multiworld, player, (LocationName.aw_region1 + ' -> ' + LocationName.aw_region2), LocationName.aw_region1, LocationName.aw_region2, lambda state: state.has(ItemName.onion_purple, player))
    connect(multiworld, player, (LocationName.aw_region1 + ' -> ' + LocationName.aw_region4), LocationName.aw_region1, LocationName.aw_region4, lambda state: state.has(ItemName.onion_white, player))
    connect(multiworld, player, (LocationName.aw_region1 + ' -> ' + LocationName.aw_region6), LocationName.aw_region1, LocationName.aw_region6, lambda state: state.has(ItemName.onion_blue, player))
    connect(multiworld, player, (LocationName.aw_region1 + ' -> ' + LocationName.hob_region), LocationName.aw_region1, LocationName.hob_region)
    connect(multiworld, player, (LocationName.aw_region2 + ' -> ' + LocationName.aw_region3), LocationName.aw_region2, LocationName.aw_region3, lambda state: state.has(ItemName.onion_yellow, player))
    connect(multiworld, player, (LocationName.aw_region2 + ' -> ' + LocationName.aw_region6), LocationName.aw_region2, LocationName.aw_region6, lambda state: state.has(ItemName.onion_white, player))
    connect(multiworld, player, (LocationName.aw_region2 + ' -> ' + LocationName.wfg_region), LocationName.aw_region2, LocationName.wfg_region)
    connect(multiworld, player, (LocationName.aw_region4 + ' -> ' + LocationName.aw_region5), LocationName.aw_region4, LocationName.aw_region5, lambda state: state.has(ItemName.onion_white, player) and state.has(ItemName.onion_blue, player))
    connect(multiworld, player, (LocationName.aw_region5 + ' -> ' + LocationName.sh_region), LocationName.aw_region5, LocationName.sh_region)
    connect(multiworld, player, (LocationName.aw_region6 + ' -> ' + LocationName.aw_region7), LocationName.aw_region6, LocationName.aw_region7, lambda state: state.has(ItemName.onion_yellow, player))
    connect(multiworld, player, (LocationName.aw_region7 + ' -> ' + LocationName.bk_region), LocationName.aw_region7, LocationName.bk_region)
    # Perplexing Pool
    connect(multiworld, player, (LocationName.pp_region1 + ' -> ' + LocationName.pp_region2), LocationName.pp_region1, LocationName.pp_region2, lambda state: state.has(ItemName.onion_yellow, player) and state.has(ItemName.onion_blue, player))
    connect(multiworld, player, (LocationName.pp_region1 + ' -> ' + LocationName.pp_region3), LocationName.pp_region1, LocationName.pp_region3, lambda state: state.has(ItemName.onion_white, player))
    connect(multiworld, player, (LocationName.pp_region1 + ' -> ' + LocationName.pp_region4), LocationName.pp_region1, LocationName.pp_region4, lambda state: state.has(ItemName.onion_yellow, player))
    connect(multiworld, player, (LocationName.pp_region1 + ' -> ' + LocationName.pp_region5), LocationName.pp_region1, LocationName.pp_region5, lambda state: state.has(ItemName.onion_yellow, player))
    connect(multiworld, player, (LocationName.pp_region1 + ' -> ' + LocationName.pp_region6), LocationName.pp_region1, LocationName.pp_region6, lambda state: state.has(ItemName.onion_blue, player))
    connect(multiworld, player, (LocationName.pp_region1 + ' -> ' + LocationName.pp_region7), LocationName.pp_region1, LocationName.pp_region7, lambda state: state.has(ItemName.onion_blue, player))
    connect(multiworld, player, (LocationName.pp_region1 + ' -> ' + LocationName.cos_region), LocationName.pp_region1, LocationName.cos_region)
    connect(multiworld, player, (LocationName.pp_region2 + ' -> ' + LocationName.sh_region), LocationName.pp_region2, LocationName.sh_region)
    connect(multiworld, player, (LocationName.pp_region4 + ' -> ' + LocationName.gk_region), LocationName.pp_region4, LocationName.gk_region)
    connect(multiworld, player, (LocationName.pp_region7 + ' -> ' + LocationName.sc_region), LocationName.pp_region7, LocationName.sc_region)
    # Wistful Wild
    connect(multiworld, player, (LocationName.ww_region1 + ' -> ' + LocationName.ww_region2), LocationName.ww_region1, LocationName.ww_region2, lambda state: state.has(ItemName.onion_yellow, player) and state.has(ItemName.onion_blue, player))
    connect(multiworld, player, (LocationName.ww_region1 + ' -> ' + LocationName.coc_region), LocationName.ww_region1, LocationName.coc_region)
    connect(multiworld, player, (LocationName.ww_region1 + ' -> ' + LocationName.ww_region3), LocationName.ww_region1, LocationName.ww_region3, lambda state: state.has(ItemName.onion_blue, player))
    connect(multiworld, player, (LocationName.ww_region2 + ' -> ' + LocationName.hoh_region), LocationName.ww_region2, LocationName.hoh_region)
    connect(multiworld, player, (LocationName.ww_region2 + ' -> ' + LocationName.ww_region3), LocationName.ww_region2, LocationName.ww_region3)
    connect(multiworld, player, (LocationName.ww_region3 + ' -> ' + LocationName.ww_region4), LocationName.ww_region3, LocationName.ww_region4, lambda state: state.has(ItemName.onion_white, player))
    connect(multiworld, player, (LocationName.ww_region4 + ' -> ' + LocationName.dd_region), LocationName.ww_region4, LocationName.dd_region)


def create_location(player: int, location_data: LocationData, region: Region,  # check where event items are assigned
                    location_cache: List[Location]) -> Location:
    location = Location(player, location_data.name, location_data.code, region)
    location.access_rule = location_data.rule

    if location_data.code is None:
        location.place_locked_item(Pikmin2Item(location_data.locked_item, ItemClassification.progression, None, player))

    location_cache.append(location)

    return location

def create_region(multiworld: MultiWorld, player: int, locations_per_region: Dict[str, List[LocationData]],
                  location_cache: List[Location], name: str) -> Region:
    region = Region(name, player, multiworld)
    region.multiworld = multiworld

    if name in locations_per_region:
        for location_data in locations_per_region[name]:
            location = create_location(player, location_data, region, location_cache)
            if location.locked == True:
                multiworld.worlds[player].locked_locations.append(location.name)
            region.locations.append(location)

    return region

def get_locations_per_region(locations: Tuple[LocationData, ...]) -> Dict[str, List[LocationData]]:
    per_region: Dict[str, List[LocationData]] = {}

    for location in locations:
        per_region.setdefault(location.parent_region, []).append(location)

    return per_region

def connect(multiworld: MultiWorld, player: int, name: str, source: str, target: str,
            rule: Optional[Callable] = None):
    source_region = multiworld.get_region(source, player)
    target_region = multiworld.get_region(target, player)

    connection = Entrance(player, name, source_region)

    if rule:
        connection.access_rule = rule

    """
    for region_to_type in multiworld.worlds[player].ghost_affected_regions:
        if region_to_type == target_region.name:
            if multiworld.worlds[player].ghost_affected_regions[region_to_type] == "Fire":
                add_rule(connection, lambda state: state.has("Water Element Medal", player), "and")
            elif multiworld.worlds[player].ghost_affected_regions[region_to_type] == "Water":
                add_rule(connection, lambda state: state.has("Ice Element Medal", player), "and")
            elif multiworld.worlds[player].ghost_affected_regions[region_to_type] == "Ice":
                add_rule(connection, lambda state: state.has("Fire Element Medal", player), "and")
    """

    source_region.exits.append(connection)
    connection.connect(target_region)
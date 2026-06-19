"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inventory = {}

    for item in items:
        if item not in inventory:
            inventory[item] = 1
            continue
        inventory[item] += 1
    return inventory

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    added_inventory = create_inventory(items)

    for item in inventory:
        if item not in added_inventory: 
            added_inventory.setdefault(item, inventory[item])
            continue
        if item in added_inventory: 
            added_inventory[item] += inventory[item]

    return added_inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    added_inventory = create_inventory(items)

    # for item in added_inventory:
    #     if item in inventory:
    #         inventory[item] -= added_inventory[item]
    #         if inventory[item] < 0: inventory[item] = 0
    # return inventory

    for key, value in added_inventory.items():
        if key in inventory:
            inventory[key] = max(0, inventory.get(key, 0) - value)

    return inventory



def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    if item in inventory: 
        del inventory[item]
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    inventory_list = []
    for key, value in inventory.items():
        if value > 0: inventory_list.append((key, value))
    return inventory_list

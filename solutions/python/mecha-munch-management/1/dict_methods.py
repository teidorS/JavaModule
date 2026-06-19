"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for item in items_to_add:
        if current_cart.get(item) is None:
            current_cart.setdefault(item, 1)
            continue
        current_cart[item] += 1
        
    return current_cart

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    cart = {}
    for note in notes:
        cart.setdefault(note, 1)
    return cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    return ideas | dict(recipe_updates)


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    refined_cart = []
    sorted_aisle_mapping = sort_entries(aisle_mapping)
    for item in reversed(sorted_aisle_mapping.items()):
        # refined_cart.append(item[1].insert(0, cart[item[0]]))
        if item[0] in cart:
            item[1].insert(0, cart[item[0]])
            refined_cart.append(item)
    return dict(refined_cart)


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    for item, (quantity, aisle, flag) in fulfillment_cart.items():
        if item in store_inventory:
            store_inventory[item][0] -= quantity
            if store_inventory[item][0] <= 0:
                store_inventory[item][0] = 'Out of Stock'
            
    return store_inventory

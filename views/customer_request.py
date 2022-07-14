CUSTOMERS = [
    {
            "id": 1,
            "name": "Jack Smith",
        },
        {
            "id": 2,
            "name": "Jane Johnson",
        }
]

def get_all_customers():
    """ function gets all animals from list
    """
    return CUSTOMERS

    # Function with a single parameter
def get_single_customer(id):
    """_summary_

    Args:
        id (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Variable to hold the found animal, if it exists
    requested_customer = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer
    
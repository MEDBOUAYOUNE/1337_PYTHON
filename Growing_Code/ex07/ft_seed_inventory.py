def ft_seed_inventory(seed_type : str, seed_quantity : int, seed_unit : str):
    """
    This function displays the seed inventory.
    """
    if seed_unit.lower() == "packets":
        print(f"{seed_type} seeds: {seed_quantity} {seed_unit} available")
    elif seed_unit.lower() == "grams":
        print(f"{seed_type} seeds: {seed_quantity} {seed_unit} total")
    elif seed_unit.lower() == "area":
        print(f"{seed_type} seeds: {seed_quantity} square meters")
    else:
        print(f"Unknown unit type")

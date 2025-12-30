def ft_harvest_total():
    """
    This function calculates the total harvest from the garden.
    """
    day_1 = int(input("Enter harvest for day 1: "))
    day_2 = int(input("Enter harvest for day 2: "))
    day_3 = int(input("Enter harvest for day 3: "))
    total_harvest = day_1 + day_2 + day_3
    print(f"Total harvest: {total_harvest}")

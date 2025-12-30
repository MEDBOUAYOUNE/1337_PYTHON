def ft_count_harvest_iterative():
    """
    This function counts down the days until harvest.
    """
    days_until_harvest = int(input("Days until harvest: "))
    for i in range(days_until_harvest):
        print(f"Day {i + 1}")
    print("Harvest time!")
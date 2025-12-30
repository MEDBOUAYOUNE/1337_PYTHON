def ft_count_harvest_recursive():
    """
    This function counts down the days until harvest.
    """
    days_harvested = int(input("Days until harvest: "))
    def count_down(counter):
        if days_harvested == counter:
            print(f"Day {counter}")
            print("Harvest time!")
        else:
            print(f"Day {counter}")
            count_down(counter + 1)
    count_down(1)

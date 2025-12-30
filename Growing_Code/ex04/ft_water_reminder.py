def ft_water_reminder():
    """
    This function reminds the user to water their plants.
    """
    days_since_watered = int(input("Enter number of days since last watering: "))
    print("Water the plants!" if days_since_watered > 2 else "Plants are fine.")

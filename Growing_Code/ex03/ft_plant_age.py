def ft_plant_age():
    """
    This function gets the age of a plant and checks if it's ready for harvest.
    """
    plant_age = int(input("Enter plant age in days: "))
    print("Plant needs more time to grow." if plant_age <= 60 else "Plant is ready to harvest!")
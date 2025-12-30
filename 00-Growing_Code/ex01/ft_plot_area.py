def ft_plot_area():
    """
        This function gets the dimensions of a plot and calculates its area.
    """
    input_length = int(input("Enter length: "))
    input_width = int(input("Enter width: "))
    area = input_length * input_width
    print(f"Plot area: {area}")
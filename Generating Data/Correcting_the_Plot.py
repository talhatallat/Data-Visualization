import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# Set chart title and label axes.➋
plt.title("Square Numbers", fontsize=24) #  title for the chart. fontsize parameters, control the size of the text on the chart.
plt.xlabel("Value", fontsize=14) # The xlabel() and ylabel() functions sets a title for each of the axes
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels.➍
plt.tick_params(axis='both', labelsize=14) #tick_params() styles the tick marks. The arguments shown here affect the tick marks on both the x- and y-axes (axes='both') and set the font size of the tick mark labels to 14

plt.show()

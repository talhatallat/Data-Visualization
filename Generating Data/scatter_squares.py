import matplotlib.pyplot as plt

x_values = list(range(1, 1001)) #  list of x-values containing the numbers 1 through 1000
y_values = [x**2 for x in x_values] #  looping through the x-value, squaring each number (x**2), and storing the results in y_values

plt.scatter(x_values, y_values, s=40) # scatter() creates single point in the middle of the chart and uses the s argument to set the size of the dots used to draw the graph.

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set the range for each axis.
plt.axis([0, 1100, 0, 1100000]) #  axis() function to specify the range of each axis

plt.show()

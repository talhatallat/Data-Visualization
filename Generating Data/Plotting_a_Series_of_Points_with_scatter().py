import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5] #  x_values list contains the numbers to be squared
y_values = [1, 4, 9, 16, 25] #  y_values contains the square of each number

plt.scatter(x_values, y_values, s=100)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()

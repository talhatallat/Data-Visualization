import matplotlib.pyplot as plt

plt.scatter(2, 4, s=200) # scatter() creates single point in the middle of the chart and uses the s argument to set the size of the dots used to draw the graph.
# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()

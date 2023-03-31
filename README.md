# Project description
The Data Visualization project generates data and creates a series of functional and beautiful visualizations of that data using matplotlib and Pygal.

-  Access data from online sources and feed it into a visualization package to create plots of weather data and a world population map.

-  Write a program to automatically download and visualize data.

## <a href="https://github.com/talhatallat/Data-Visualization/tree/main/Generating%20Data">Generating Data<a/>
Data visualization involves exploring data through visual representations. It’s closely associated with data mining, which uses code to explore the patterns and connections in a data set. A data set can be just a small list of numbers that fits in one line of code or many gigabytes of data.


People use Python for data-intensive work in genetics, climate research, political and economic analysis, and much more.

-  matplotlib to make simple plots, such as line graphs and scatter plots.
-  Pygal, focuses on creating visualizations that work well on digital devices. Pygal to emphasize and resize elements as the user interacts with your visualization, and you can easily resize the entire representation to fit on a tiny smartwatch or giant monitor. Use Pygal to explore what happens when you roll dice in various ways.

### Installing matplotlib on Windows
    pip3 install matplotlib 
    
### Testing matplotlib
    $ python
    >>> import matplotlib
    >>>
#### <a href="http://matplotlib.org/">The matplotlib Gallery<a/>

### <a href="https://github.com/talhatallat/Data-Visualization/blob/main/Generating%20Data/Plotting%20a%20Simple%20Line%20Graph.py">Plotting a Simple Line Graph<a/>

### <a href="https://github.com/talhatallat/Data-Visualization/blob/main/Generating%20Data/Changing_the_Label_Type_and_Graph_Thickness.py">Changing the Label Type and Graph Thickness<a/>

### <a href="https://github.com/talhatallat/Data-Visualization/blob/main/Generating%20Data/Correcting_the_Plot.py">Correcting the Plot<a/>

### <a href="https://github.com/talhatallat/Data-Visualization/blob/main/Generating%20Data/Plotting_and_Styling_Individual_Points_with_scatter().py">Plotting and Styling Individual Points with scatter()<a/>

### <a href="https://github.com/talhatallat/Data-Visualization/blob/main/Generating%20Data/Plotting_a_Series_of_Points_with_scatter().py">Plotting a Series of Points with scatter()<a/>

### <a href="https://github.com/talhatallat/Data-Visualization/blob/main/Generating%20Data/scatter_squares.py">Calculating Data Automatically<a/>

### Removing Outlines from Data Points
    # To remove the outlines around points, pass the argument edgecolor='none' when you call scatter():
    plt.scatter(x_values, y_values, edgecolor='none', s=40) # scatter() creates single point in the middle of the chart and uses the s argument to set the size of the dots used to draw the graph. 


### Defining Custom Colors
    # change the color of the points, pass c to scatter() with the name of a color to use
    plt.scatter(x_values, y_values, c='green', edgecolor='none', s=40)
   
![image](https://user-images.githubusercontent.com/73076876/229165357-b8f744a6-77c7-4708-b62c-99c63f7c18e5.png)


    # To define a color, pass the c argument a tuple with three decimal values (one each for red, green, and blue), using values between 0 and 1
    plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)

![image](https://user-images.githubusercontent.com/73076876/229165550-28a53252-3838-42a3-aaf8-e6de091f9163.png)


### Using a Colormap
    #  pass the list of y-values to c and then tell pyplot which colormap to use through the cmap argument. This code colors the points with lower y-values light blue and the points with larger y-values dark blue.
    plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

![image](https://user-images.githubusercontent.com/73076876/229165074-fc18d2f7-80a6-463d-9acd-89a2477fd427.png)

### Saving Your Plots Automatically
    #  first argument is a filename for the plot image, which will be saved in the same directory as scatter_squares.py. The second argument trims extra whitespace from the plot.
    plt.savefig('squares_plot.png', bbox_inches='tight')

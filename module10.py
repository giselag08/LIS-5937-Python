# Implementation of matplotlib function
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

# Create data:
data = {
    "German Shepard": 88,
    "Husky": 60,
    "Golden Retriever": 75,
    "Pitbull": 65
}

# Use keys and values as x and y axis values:
x_axis_data = data.keys()
y_axis_data = data.values()

# Plotting a bar graph:
ax.bar(x_axis_data, y_axis_data)

# Creating scatterplot
x = [88, 71, 60, 51, 71, 75, 65, 37]
y = [66, 49, 44, 35, 55, 65, 35, 29]
plt.scatter(x, y)
plt.show()

# Creating line graph
x = [37, 51, 60, 65, 71, 71, 75, 88]
y = [29, 35, 35, 44, 49, 55, 65, 66]
plt.plot(x, y)
plt.show()

# Creating ggplot
$ pip install ggplot
from ggplot import *
ggplot(aes(x='Breed', y='Weight'), data) +\
geom_line() +\
stat_smooth(colour='green', span=0.2)
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np

# Create some sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
fig, ax = plt.subplots()
line, = ax.plot(x, y, label='Sin(x)')

# Function to update the data
def update_data():
    new_y = np.cos(x)  # Update the data, for example, using a different function
    line.set_ydata(new_y)  # Update the y-data of the line
    #ax.legend()  # Redraw the legend if needed

# Button click event handler
def on_button_click(event):
    ax.clear()  # Clear the current plot
    update_data()  # Update the data
    ax.plot(x, line.get_ydata(), label='Cos(x)')  # Redraw the plot with the updated data
    #ax.legend(["This is my legend"], fontsize="x-large")
    #ax.legend()  # Redraw the legend if needed
    plt.draw()  # Redraw the figure

# Create a button
ax_button = plt.axes([0.81, 0.01, 0.1, 0.05])  # [x, y, width, height]
button = Button(ax_button, 'Update Data')

# Attach the button click event handler
button.on_clicked(on_button_click)

# Show the plot
plt.show()
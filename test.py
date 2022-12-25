import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Create a Matplotlib Figure and Axes
fig, ax = plt.subplots()

# Some data to plot
x = [1, 2, 3]
y = [2, 4, 6]

# Plot the data
ax.plot(x, y)

# Create a Tkinter root window
root = tk.Tk()

# Create a FigureCanvasTkAgg object and draw the Figure on it
canvas = FigureCanvasTkAgg(fig, root)
canvas.draw()

# Add the FigureCanvasTkAgg to the Tkinter window
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Run the Tkinter event loop
tk.mainloop()

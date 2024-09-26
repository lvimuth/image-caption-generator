import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)

# Line objects for the two rotating lines
line1, = ax.plot([], [], lw=2, label='Line 1')
line2, = ax.plot([], [], lw=2, label='Line 2')

# Trace of the path of the second line
trace2, = ax.plot([], [], 'b-', lw=1, label='Trace 2')

# Store the path for line 2
trace2_x, trace2_y = [], []

# Initialization function
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    trace2.set_data([], [])
    return line1, line2, trace2

# Update function for the animation
def update(frame):
    # Angle of rotation for both lines (same speed)
    angle1 = frame
    angle2 = frame * 2  # Second line rotates at double the speed
    
    # First line rotates around the origin (0, 0)
    x1 = np.cos(angle1)
    y1 = np.sin(angle1)
    
    # Second line rotates around the end of the first line but independent
    length = 1  # Length of the second line
    x2 = x1 + length * np.cos(angle2)
    y2 = y1 + length * np.sin(angle2)

    # Set the data for the lines
    line1.set_data([0, x1], [0, y1])
    line2.set_data([x1, x2], [y1, y2])

    # Append the new positions to the trace of the second line
    trace2_x.append(x2)
    trace2_y.append(y2)

    # Update the trace for line 2 (only draw the second line's trace)
    trace2.set_data(trace2_x, trace2_y)

    return line1, line2, trace2

# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 20 * np.pi, 2000), 
                    init_func=init, blit=True, interval=20)

# Show the animation
plt.legend()
plt.show()

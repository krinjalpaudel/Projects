import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

def projectile_motion(mass):
    # Constants
    g = 9.8  # Acceleration due to gravity (m/s^2)
    air_density = 1.2  # Air density (kg/m^3)
    drag_coefficient = 0.47  # Drag coefficient for a sphere
    cross_sectional_area = 0.01  # Cross-sectional area of the ball (m^2)

    # Initial conditions
    initial_velocity = 30.0  # Initial velocity (m/s)
    launch_angle = np.radians(45)  # Launch angle (degrees)
    time_step = 0.1  # Time step for numerical integration (s)

    # Initial components of velocity
    vx0 = initial_velocity * np.cos(launch_angle)
    vy0 = initial_velocity * np.sin(launch_angle)

    # Lists to store the trajectory data
    x_values = []
    y_values = []

    # Initial values
    x = 0.0
    y = 0.0
    vx = vx0
    vy = vy0

    # Simulation loop
    while y >= 0:
        # Append current position to the lists
        x_values.append(x)
        y_values.append(y)

        # Calculate forces
        gravitational_force = -mass * g
        air_resistance_force = -0.5 * air_density * vx**2 * drag_coefficient * cross_sectional_area

        # Calculate accelerations
        ax = air_resistance_force / mass
        ay = gravitational_force / mass

        # Update velocity using Euler method
        vx += ax * time_step
        vy += ay * time_step

        # Update position using Euler method
        x += vx * time_step
        y += vy * time_step

    return x_values, y_values

# GUI class
class ProjectileMotionGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Projectile Motion Simulation')
        self.geometry('800x600')

        self.create_widgets()

    def create_widgets(self):
        # Mass selection dropdown
        mass_label = ttk.Label(self, text='Select Mass (kg):')
        mass_label.grid(row=0, column=0, padx=10, pady=10)

        self.mass_var = tk.DoubleVar(value=1.0)
        mass_dropdown = ttk.Combobox(self, textvariable=self.mass_var, values=[1, 5, 10])
        mass_dropdown.grid(row=0, column=1, padx=10, pady=10)

        # Simulation button
        simulate_button = ttk.Button(self, text='Simulate', command=self.simulate)
        simulate_button.grid(row=0, column=2, padx=10, pady=10)

        # Matplotlib canvas
        self.figure, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    def animate(self, i):
        # Get selected mass
        mass = self.mass_var.get()

        # Simulate and update trajectory
        x_values, y_values = projectile_motion(mass)
        self.ax.clear()
        self.ax.plot(x_values, y_values, label=f'Mass = {mass} kg')
        self.ax.set_title('Projectile Motion')
        self.ax.set_xlabel('Horizontal Distance (m)')
        self.ax.set_ylabel('Vertical Distance (m)')
        self.ax.legend()
        self.ax.grid(True)

    def simulate(self):
        # Create animation
        animation = FuncAnimation(self.figure, self.animate, frames=100, interval=50, repeat=False)

        # Redraw canvas
        self.canvas.draw()

if __name__ == "__main__":
    app = ProjectileMotionGUI()
    app.mainloop()

import tkinter as tk

class DribblingBallSimulation:
    def __init__(self, master):
        self.master = master
        self.master.title("Dribbling Ball Simulation")

        # Ball parameters with default values
        self.radius = 40
        #self.mass = 1000
        self.initial_position = 300
        self.height = 400
        self.gravity = 0.005
        self.velocity = 0.0
        self.cor = 0.8  # Coefficient of restitution to simulate elasticity

        # Canvas setup
        self.canvas = tk.Canvas(self.master, width=400, height=600, bg="white")
        self.canvas.pack()

        # Start simulation button
        self.start_button = tk.Button(self.master, text="Start Simulation", command=self.start_simulation)
        self.start_button.pack()

    def update_mass(self, value):
        self.mass = float(value)

    def start_simulation(self):
        # Reset canvas
        self.canvas.delete("all")

        # Calculate initial position
        y = self.initial_position
        time_interval = 0.05

        # Simulation loop
        while y < self.initial_position + 300:
            # Update velocity and position
            self.velocity += self.gravity
            y += self.velocity

            # Bounce when hitting the ground
            if y > self.initial_position + 300 - self.radius:
                y = self.initial_position + 300 - self.radius
                self.velocity = -self.velocity * self.cor  # Apply coefficient of restitution

                # Adjust velocity based on mass for a more physically accurate simulation
                if self.mass > 1:
                # Reduce bounce for heavier objects
                    self.velocity *= (1 - self.mass / 20) * self.cor
                else:
                # Increase bounce for lighter objects
                    self.velocity *= (1 - self.mass / 40) * self.cor

            # Update canvas
            self.canvas.delete("ball")
            self.canvas.create_oval(200 - self.radius, y - self.radius, 200 + self.radius, y + self.radius,
                                    fill="blue", tags="ball")
            self.master.update()
            self.canvas.after(int(time_interval * 1000), self.canvas.update_idletasks())

# Create the main window
root = tk.Tk()
app = DribblingBallSimulation(root)
app.update_mass(10)  
root.mainloop()

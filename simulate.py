import numpy as np
import matplotlib.pyplot as plt

# Ellipse parameters
a = 5  # Semi-major axis
b = 3  # Semi-minor axis

# Generate points along the ellipse
theta = np.linspace(0, 2 * np.pi, 500)
x = a * np.cos(theta)
y = b * np.sin(theta)

# Plot the orbit
plt.figure(figsize=(6, 4))
plt.plot(x, y, label="Elliptical Orbit")
plt.plot(0, 0, 'yo', label="Focus (e.g., Sun)")  # Center of ellipse
plt.gca().set_aspect('equal')  # Equal scaling
plt.title("Simulation of Elliptical Orbit")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
plt.show()

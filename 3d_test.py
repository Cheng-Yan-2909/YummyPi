
import matplotlib.pyplot as plt
import numpy as np

# 1. Create the figure and setup 3D axes
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# 2. Generate coordinates for a 3D object (a wavy surface)
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))  # Calculation for the Z-height

# 3. Plot the 3D surface with a color map
surface = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

# 4. Add labels, title, and a color bar
ax.set_title("3D Wavy Surface Map", fontsize=14)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
fig.colorbar(surface, ax=ax, shrink=0.5, aspect=10)

# 5. Display the interactive 3D window
plt.show()


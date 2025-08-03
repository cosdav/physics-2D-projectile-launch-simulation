import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # m/s^2

# Functions
def show_plot(option):
    if option == 5:
        plt.plot(plots[5][0], plots[5][1], label="Trajectory")
        plt.scatter(v0x * t_hmax, h_max, color='red', label="Maximum height")
        plt.xlabel(plots[5][2])
        plt.ylabel(plots[option][3])
        plt.title("Oblique 2D Launch")
        plt.grid(True)
        plt.axis('equal')
        plt.legend()
        plt.show()
    else:
        plt.plot(t, plots[option][0], label=plots[option][1])
        plt.scatter(t_hmax, plots[option][2](), color='red', label='Maximum height')
        plt.xlabel("Time (s)")
        plt.ylabel(plots[option][1])
        plt.title("Oblique 2D Launch")
        plt.grid(True)
        plt.legend()
        plt.show()

def choose_plot():
    print("\nWhich metric do you want to see the graph of:\n\n"
          "1. Height (h)\n2. Velocity magnitude (v)\n"
          "3. Gravitational potential energy (Ep)\n4. Kinetic energy (Ec)\n5. Trajectory\n6. Mechanical energy")
    return int(input("Choose the number (0 to exit): "))

def height():
    return h_max

def velocity():
    return np.sqrt(np.pow(v0x, 2) + np.pow(v0y - g * t_hmax, 2))

def potential_energy():
    return m * g * h_max

def kinetic_energy():
    return 0.5 * m * velocity() ** 2

def mechanical_energy():
    return kinetic_energy() + potential_energy()

# Inputs
while True:
    try:
        m = float(input("\nMass of the body (Kg): "))
    except ValueError:
        print("The mass must be a number.")
        continue
    while m < 0:
        print("The mass cannot be less than 0.")
        m = float(input("Mass of the body (Kg): "))

    try:
        v0 = float(input("Initial velocity (m/s): "))
    except ValueError:
        print("The initial velocity must be a number.")
        continue

    try:
        theta = float(input("Angle with the Ox axis (degrees): "))
    except ValueError:
        print("The angle must be a number.")
        continue

    try:
        h0 = float(input("Initial height (m): "))
    except ValueError:
        print("The height must be a number.")
        continue

    while h0 < 0:
        print("Height cannot be less than 0.")
        h0 = float(input("Height of the body (m): "))
    break

# Velocity decomposition
theta = np.radians(theta)

v0x = v0 * np.cos(theta)
v0y = v0 * np.sin(theta)

# Time calculation
t_fall = (v0y + np.sqrt(np.pow(v0y, 2) + 2 * g * h0)) / g
t = np.append(np.arange(0, t_fall, 0.02), t_fall)

# Max height and range calculation
x_max = v0x * t_fall

if v0y < 0:
    h_max = h0
    t_hmax = 0
else:
    t_hmax = v0y / g
    h_max = h0 + v0y * t_hmax - 0.5 * g * np.pow(t_hmax, 2)

# Position and height calculation
h = h0 + v0y * t - 0.5 * g * np.pow(t, 2)
x = v0x * t

# Velocity calculation
vy = v0y - g * t
v = np.sqrt(np.pow(v0x, 2) + np.pow(vy, 2))

# Energy calculations
Ec = 0.5 * m * np.pow(v, 2)
Ep = m * g * h
Em = Ep + Ec

print(f"\nThe time of flight was {round(t_fall, 2)} seconds. The body reached a maximum height of {round(h_max, 2)} meters and a range of {round(x_max, 2)} meters.")

# Plot dictionary
plots = {1: [h, "Height (m)", height],
         2: [v, "Velocity magnitude (m/s)", velocity],
         3: [Ep, "Gravitational potential energy (J)", potential_energy],
         4: [Ec, "Kinetic energy (J)", kinetic_energy],
         5: [x, h, "Position (m)", "Height (m)"],
         6: [Em, "Mechanical energy (J)", mechanical_energy]}

# Choose plot
plot_choice = choose_plot()

while plot_choice not in [1, 2, 3, 4, 5, 6]:
    print("Invalid choice.")
    plot_choice = int(input("Choose a number (1 to 6): "))

# Plot
show_plot(plot_choice)

while True:
    plot_choice = choose_plot()

    if plot_choice == 0:
        break
    elif plot_choice in [1, 2, 3, 4, 5, 6]:
        show_plot(plot_choice)
    else:
        print("Invalid choice.")
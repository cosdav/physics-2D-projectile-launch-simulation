# physics-2D-projectile-launch-simulation

# Projectile Launch Simulation

This project simulates the 2D projectile motion of a body launched with an initial speed, angle, and height.  
It calculates and plots the height, velocity, kinetic and potential energy, mechanical energy, and the projectile's trajectory.

## Description

The simulation models the projectile under constant gravitational acceleration (9.81 m/s²), neglecting air resistance.  
The program asks for user input for the mass, initial velocity, launch angle, and initial height.  
It calculates the motion using kinematic equations, then plots different physical quantities versus time or position.

## Features

- User inputs for mass, initial velocity, launch angle, and height.
- Calculates maximum height, flight time, and horizontal range.
- Computes velocity, potential and kinetic energy at each time step.
- Interactive selection of graphs to display:
  - Height vs Time
  - Velocity vs Time
  - Potential Energy vs Time
  - Kinetic Energy vs Time
  - Mechanical Energy vs Time
  - Trajectory (x vs y)
- Plots graphs with matplotlib.

## How to use

1. Run the Python script.
2. Enter the requested parameters when prompted.
3. Choose which graph(s) you want to display by typing the corresponding number.
4. View the graphical output; repeat or exit by entering 0.

## Requirements

- Python 3.x
- numpy
- matplotlib

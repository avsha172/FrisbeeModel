# Frisbee Trajectory Predictor

This project is designed to simulate and predict the trajectory of a Frisbee in flight, visualizing the path it would take given certain initial conditions.

## Overview

The Frisbee Trajectory Predictor uses physics principles to compute the flight path of a Frisbee, producing graphs that illustrate the expected trajectory. The code takes into account various factors such as the initial throw velocity, angle, and the Frisbee's aerodynamic properties.

### Prerequisites

The script is written in Python.
it also uses numpy, matplotlib.animation.PillowWriter, matplotlib.pyplot and math.

## Usage

To run the simulation you just need to call simulation_handler and pass the frisbees starting conditions.
vy - starting velocity in the y dim, up.
vx - starting velocity in the x dim, forward, there is no z dim in my simulation.


python main.py

This will start the program and generate the trajectory graphs for a Frisbee's flight.

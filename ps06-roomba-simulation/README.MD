# 🧩 Problem Set 6: Simulating Robots

## Introduction

In this problem set, you will build a robot simulation program to estimate how much time a group of robots will take to clean the floor of a room. The robots will move around the room, cleaning the area they pass over. The goal is to determine the average number of time-steps needed before a specified fraction of the room is cleaned.

## Part I: The RectangularRoom and Robot Classes

In Part I, you will implement two classes: `RectangularRoom` and `Robot`.

### RectangularRoom Class

The `RectangularRoom` class represents a rectangular region containing clean or dirty tiles. The room has a width and height and contains tiles that are initially dirty. Each tile can be marked as cleaned when a robot moves to a given position. The `RectangularRoom` class provides methods to access information about the room's state and the number of tiles cleaned.

### Robot Class

The `Robot` class stores the position and heading of a robot. It also has a fixed speed. Subclasses of `Robot` will provide different movement strategies by implementing the `updatePositionAndClean()` method. The `StandardRobot` class, which inherits from `Robot`, has a standard movement strategy.

## Part II: Creating and Using the Simulator

In Part II, you will use the robot simulation to answer questions about the robots' performance. You will run multiple trials of the simulation and analyze the average number of time-steps needed to clean a specified fraction of the room.

### Problem #2

You will complete the `updatePositionAndClean()` method of the `StandardRobot` class to simulate the motion of the robot after a single time-step.

### Problem #3

In this problem, you will implement the `runSimulation()` function to run multiple trials of the simulation and calculate the mean number of time-steps needed to clean a specified fraction of the room. You will use this function to answer questions about different scenarios, such as the number of robots and room dimensions.

## Part III: Visualizing Robots (Optional)

In Part III, you have the option to use a Python tool called `pylab` to generate animations of the robots as they clean the room. This visualization can help you understand the simulation dynamics and debug your implementation.

## Problem #4

You will use the simulation to answer questions about the robots' performance and create plots using `pylab`.

1. Plot the mean time required to clean 80% of a 20×20 room with each of 1-10 robots.
2. Plot the mean time required for two robots to clean 80% of rooms with dimensions 20×20, 25×16, 40×10, 50×8, 80×5, and 100×4 (rooms with the same area).

## Problem #5

You will implement a new class called `RandomWalkRobot`, which inherits from `Robot`. This new robot will change direction randomly after each time-step, rather than only when hitting walls.

## Problem #6

You will compare the performance of the two types of robots (StandardRobot and RandomWalkRobot) and create an appropriate plot to visualize the results.

---
For more information about the MIT course and licensing terms, visit the [MIT OpenCourseWare](http://ocw.mit.edu/terms).
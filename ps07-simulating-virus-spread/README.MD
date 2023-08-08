# 🧩 Problem Set 7: Simulating the Spread of Disease and Virus Population

## Introduction

In this problem set, you will design and implement a stochastic simulation of patient and virus population dynamics. The simulation will model the spread of a virus within a person and allow us to study the effects of different treatments and conditions on the virus population.

## Part I: Implementing a Simple Simulation (No Drug Treatment)

In Part I, you will implement a simple virus population model where the patient does not take any drugs, and the viruses do not acquire resistance to drugs. The simulation will model how the virus population changes over time, considering the birth and clearance probabilities of virus particles.

### SimpleVirus Class

You will implement the `SimpleVirus` class, which represents a simple virus particle. Each virus particle has a maximum reproduction probability (`maxBirthProb`) and a maximum clearance probability (`clearProb`). The `SimpleVirus` class will have methods to determine whether a virus particle is cleared at a time step (`doesClear()`) and whether it reproduces at a time step (`reproduce(popDensity)`).

### SimplePatient Class

You will also implement the `SimplePatient` class, representing a simplified patient with a virus population. The patient does not take any drugs, and the virus population has no drug resistance. The `SimplePatient` class will have methods to update the state of the virus population for a single time step (`update()`) and get the current total virus population (`getTotalPop()`).

## Part II: Running and Analyzing a Simple Simulation (No Drug Treatment)

In Part II, you will run the simulation for 300 time steps and plot the total virus population as a function of time. The simulation will be repeated many times to get an average case representation. You will use `pylab` to create the plot, including axes labels, a key for the curves, and a title.

## Part III: Probabilities

In Part III, you will work on some probability exercises related to coin flips and rolling dice. You will calculate the probability of different events and then implement a Monte Carlo simulation to solve the Yahtzee problem.

By completing this problem set, you will gain insights into how viruses spread within a patient and how different factors can affect the virus population dynamics. You will also practice and understand simple probability and statistics concepts. Enjoy the exploration and happy coding!

---
For more information about the MIT course and licensing terms, visit the [MIT OpenCourseWare](http://ocw.mit.edu/terms).
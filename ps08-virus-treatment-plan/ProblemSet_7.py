# Problem Set 7: Simulating the Spread of Disease and Virus Population Dynamics
# Name:
# Collaborators:
# Time:

import numpy
import random
import pylab

'''
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 1
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):

        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.
        maxBirthProb: Maximum reproduction probability (a float between 0-1)
        clearProb: Maximum clearance probability (a float between 0-1).
        """

        # TODO

        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def doesClear(self):

        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step.
        returns: True with probability self.clearProb and otherwise returns
        False.
        """

        # TODO

        if random.random() <= self.clearProb:
            return True
        else:
            return False


    def reproduce(self, popDensity):

        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.

        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """

        # TODO

        if random.random() <= (self.maxBirthProb * ( 1 - popDensity)):
            return SimpleVirus(self.maxBirthProb, self.clearProb)
        else:
            raise NoChildException


class SimplePatient(object):

    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """

    def __init__(self, viruses, maxPop):

        """

        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the  maximum virus population for this patient (an integer)
        """

        # TODO
        self.viruses = viruses
        self.maxPop = maxPop


    def getTotalPop(self):

        """
        Gets the current total virus population.
        returns: The total virus population (an integer)
        """

        # TODO
        return len(self.viruses)


    def update(self):

        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:

        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.
        - The current population density is calculated. This population density
          value is used until the next call to update()
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.

        returns: The total virus population at the end of the update (an
        integer)
        """

        # TODO

        for virus in self.viruses:
            if virus.doesClear():
                # print "cleared"
                self.viruses.remove(virus)

            try:
                # print "reproduced"
                self.viruses.append(virus.reproduce((float(self.population)/self.maxPop)))
            except NoChildException:
                pass

        # print self.population
        return self.population


    population = property(getTotalPop)


#
# PROBLEM 2
#
def simulationWithoutDrug(virusCount, maxPop, maxBirthProb, clearProb, steps, trials):

    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).
    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.

    virusCount = amount of virsuses ( integer >= 0 )
    maxPop = max population of viruses ( integer >= virusCount )
    maxBirthPro = Maximum Reproduction Probability for a Virus Particle () float between 0-1 )
    clearProb = Maximum Clearance Probability for a Virus Particle ( float between 0-1 )
    steps = how many time steps to take ( integer > 0 )

    """

    # TODO
    populationAverages = []

    for x in range(steps):
        populationAverages.append(0)

    for x in range(trials):
        viruses = [] #list of SimpleVirus instances
        populations = []

        for x in range(virusCount):
            viruses.append(SimpleVirus(maxBirthProb, clearProb))

        # print viruses

        patient = SimplePatient(viruses, maxPop)

        for x in range(steps):
            update = patient.update()
            populationAverages[x] += update
            populations.append(update)

        pylab.plot(populations, 'r')


    for x,each in enumerate(populationAverages):
        populationAverages[x] = each/trials


    pylab.plot(populationAverages)
    pylab.ylabel("Virus Population")
    pylab.xlabel("Simulation Step")
    pylab.title("Virus Population over 300 Life Cycles")
    pylab.legend(["Virus Population"])
    pylab.show()

    print ("populations")
    return ("populations")




if __name__ == '__main__':
    simulationWithoutDrug(100, 1000, .1, .05, 300, 20)


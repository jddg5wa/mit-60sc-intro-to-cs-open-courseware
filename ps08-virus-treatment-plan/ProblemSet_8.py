# 6.00 Problem Set 8
#
# Name:
# Collaborators:
# Time:

import numpy
import random
import matplotlib.pyplot as plt
from ProblemSet_7 import *

#
# PROBLEM 1
#
class ResistantVirus(SimpleVirus):

    """
    Representation of a virus which can have drug resistance.
    """

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):

        """

        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)
        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'grimpex',False}, means that this virus
        particle is resistant to neither guttagonol nor grimpex.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.

        """


        # TODO

        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        self.resistances = resistances
        self.mutProb = mutProb



    def isResistantTo(self, drug):

        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.

        drug: The drug (a string)
        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """

        # TODO

        if drug.lower() in self.resistances:
            if self.resistances.get(drug.lower()):
                return True
            else:
                return False
        else:
            return False


    def reproduce(self, popDensity, activeDrugs):

        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient class.

        If the virus particle is not resistant to any drug in activeDrugs,
        then it does not reproduce. Otherwise, the virus particle reproduces
        with probability:

        self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent).

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.

        For example, if a virus particle is resistant to guttagonol but not
        grimpex, and `self.mutProb` is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        grimpex and a 90% chance that the offspring will not be resistant to
        grimpex.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.

        • reproduces if not resistant to activeDrugs
        • else reproduces with prob self.maxBirthProb * (1 - popDensity)
        • if reproduces then returns instance of offspring with same stats
        • for each drug resistance trait, offspring has prob 1-mutProb of
        inheriting that resistance and probability mutProb of switching the trait in offspring

        """
        # TODO
        doesReproduce = True
        inheritedResistances = {}

        for drug in activeDrugs:
            if self.isResistantTo(drug) == False:
                doesReproduce = False

        if doesReproduce and random.random() <= self.maxBirthProb*(1-popDensity):
            for drug in self.resistances:
                if random.random() <= (1 - self.mutProb): # inherent resistance
                    inheritedResistances[drug] = self.resistances.get(drug)
                    # print("inherited:" + str(inheritedResistances[drug]))

                else: #switch resistance
                    inheritedResistances[drug] = not self.resistances.get(drug)
                    # print("switched:" + str(inheritedResistances[drug]))
        else:
            raise NoChildException()

        return ResistantVirus(self.maxBirthProb, self.clearProb, inheritedResistances, self.mutProb)








class Patient(SimplePatient):

    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the  maximum virus population for this patient (an integer)
        """
        # TODO

        self.viruses = viruses
        self.maxPop = maxPop
        self.perscriptions = []


    def addPrescription(self, newDrug):

        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: list of drugs being administered to a patient is updated
        """
        # TODO
        # should not allow one drug being added to the list multiple times

        if newDrug not in self.perscriptions:
            self.perscriptions.append(newDrug)


    def getPrescriptions(self):

        """
        Returns the drugs that are being administered to this patient.
        returns: The list of drug names (strings) being administered to this
        patient.
        """

        # TODO

        return self.perscriptions


    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])

        returns: the population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        # TODO

        resistantVirusPop = 0

        for virus in self.viruses:

            drugResistResults = []
            for drug in drugResist:
                if virus.isResistantTo(drug):
                    drugResistResults.append(True)
                else:
                    drugResistResults.append(False)
            if all(drugResistResults):
                resistantVirusPop += 1

        return resistantVirusPop


    def update(self):

        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly
        - The current population density is calculated. This population density
          value is used until the next call to update().
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.
          The listof drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: the total virus population at the end of the update (an
        integer)
        """
        # TODO

        for virus in self.viruses:
            if virus.doesClear():
                self.viruses.remove(virus)
            else:
                try:
                    self.viruses.append(virus.reproduce((len(self.viruses)/self.maxPop),self.perscriptions))
                except NoChildException:
                    pass

        return len(self.viruses)


def createViruses(amountOfViruses, maxBirthProb, clearProb, resistances, mutProb):
    """
    This function initializes mutliple ResistantViruses with proper attiributse
    and returns them.

    amountOfViruses: the amount of viruses to be initialized
    maxBirthProb: Maximum reproduction probability (a float between 0-1)
    clearProb: Maximum clearance probability (a float between 0-1).

    resistances: A dictionary of drug names (strings) mapping to the state
    of this virus particle's resistance (either True or False) to each drug.
    e.g. {'guttagonol':False, 'grimpex',False}, means that this virus
    particle is resistant to neither guttagonol nor grimpex.

    mutProb: Mutation probability for this virus particle (a float). This is
    the probability of the offspring acquiring or losing resistance to a drug.

    returns: list of viruses
    """
    viruses = []

    for x in range(0,amountOfViruses):
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))

    return viruses



#
# PROBLEM 2
#


def simulationWithDrug(trials, preDrugTimeSteps, postDrugTimeSteps, perscriptions, startingVirusPop, maxVirusPop, maxVirusBirthProb, virusClearProb, virusResistances, virusMutProb):

    """

    Runs simulations and plots graphs for problem 4.
    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.
    total virus population vs. time and guttagonol-resistant virus population
    vs. time are plotted
    """
    # TODO

    virusPops = [] # total virus population for each trial run
    resistantVirusPops = [] # resistant virus population for each trial run
    avgVirusPops = [] #average total virus population for each trial run
    avgResistantVirusPops = [] #average resistant virus population for each trial run

    for x in range(preDrugTimeSteps + postDrugTimeSteps): #populate avgVirusPops and avgResistantVirusPops
        avgVirusPops.append(0)
        avgResistantVirusPops.append(0)

    for trial in range(trials): #run trials
        testPatient = Patient(createViruses(startingVirusPop, maxVirusBirthProb, virusClearProb, virusResistances, virusMutProb), maxVirusPop) #create patient
        trialVirusPops = []
        trialResistantVirusPops = []

        for step in range(0, preDrugTimeSteps): #trial pre-drug
            trialVirusPops.append(testPatient.update()) #update patient
            trialResistantVirusPops.append(testPatient.getResistPop([perscriptions[0]])) #get resist virus pop

        testPatient.addPrescription(perscriptions[0]) #drug added

        for step in range(0, postDrugTimeSteps): #trial steps post drug
            trialVirusPops.append(testPatient.update()) #update patient
            trialResistantVirusPops.append(testPatient.getResistPop([perscriptions[0]])) #get resist virus pop

        for x in range(preDrugTimeSteps + postDrugTimeSteps): #plot all data points for trial
            pylab.plot(x+1, trialVirusPops[x], '.b', label = "Virus Pop" if x == 0 and trial == 0 else "")
            pylab.plot(x+1, trialResistantVirusPops[x], '.k', label = "Resistant Virus Pop" if x == 0 and trial == 0 else "")

            avgVirusPops[x] += trialVirusPops[x] #add step virus population totals to use for average later
            avgResistantVirusPops[x] += trialResistantVirusPops[x]

        #save each trials step population data for future viewing.
        virusPops.append(trialVirusPops)
        resistantVirusPops.append(trialResistantVirusPops)

    # print (avgVirusPops)

    for x in range(len(avgVirusPops)): #create averages from total virus counts over all trials.
        avgVirusPops[x] = avgVirusPops[x]/trials
        avgResistantVirusPops[x] = avgResistantVirusPops[x]/trials

    # print ("Virus Pops Per Step:")
    # print (virusPops)
    # print ("Resistant Virus Pops Per Step:")
    # print (resistantVirusPops)
    # print ("")
    # print ("Average Virus Pops Per Step:")
    # print (avgVirusPops)
    # print ("Average Resistant Virus Pops Per Step:")
    # print (avgResistantVirusPops)

    pylab.plot(avgVirusPops, '-r', label = "Avg Virus Pop")
    pylab.plot(avgResistantVirusPops, '-g', label = "Avg Resistant Virus Pop")
    pylab.ylabel("Virus Population")
    pylab.xlabel("Simulation Step")
    pylab.title("The Spread of Disease and Virus Population with Delayed Drug(s) \n ""Trials: " + str(trials) +"   Steps: " + str(preDrugTimeSteps + postDrugTimeSteps) + "   Drug(s) Added At Step: " + str(preDrugTimeSteps))

    pylab.legend(loc = 'upper left')

    pylab.show()

#
# PROBLEM 3
#

def simulationDelayedTreatment(trials, preDrugTimeSteps, postDrugTimeSteps, perscriptions, startingVirusPop, maxVirusPop, maxVirusBirthProb, virusClearProb, virusResistances, virusMutProb):

    """
    Runs simulations and make histograms for problem 5.
    Runs multiple simulations to show the relationship between delayed treatment
    and patient outcome.
    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).
    """

    # TODO

    trialVirusPops = []

    for trial in range(trials):
        testPatient = Patient(createViruses(startingVirusPop, maxVirusBirthProb, virusClearProb, virusResistances, virusMutProb), maxVirusPop) #create patient
        virusPop = 0

        for step in range(0, preDrugTimeSteps): #trial pre-drug
            testPatient.update() #update patient

        testPatient.addPrescription(perscriptions[0])
        # print("Perscription Given")

        for step in range(0, postDrugTimeSteps): #trial steps post drug
            testPatient.update() #update patient

        trialVirusPops.append(len(testPatient.viruses))

    plt.hist(trialVirusPops, 30, range=[0, maxVirusPop], facecolor='green', align='mid')
    pylab.xlim([0,600])
    pylab.title("The Spread of Disease and Virus Population with Delayed Drug(s) \n ""Trials: " + str(trials) +"   Steps: " + str(preDrugTimeSteps + postDrugTimeSteps) + "   Drug(s) Added At Step: " + str(preDrugTimeSteps))
    pylab.xlabel("Final Virus Population")
    pylab.ylabel("# of Patients")
    pylab.show()







#
# PROBLEM 4
#

def simulationTwoDrugsDelayedTreatment(trials, firstDrugTimeSteps, secondDrugTimeSteps, postDrugTimeSteps, perscriptions, startingVirusPop, maxVirusPop, maxVirusBirthProb, virusClearProb, virusResistances, virusMutProb):

    """
    Runs simulations and make histograms for problem 6.
    Runs multiple simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    150, 75, 0 timesteps between adding drugs (followed by an additional 150
    timesteps of simulation).
    """

    # TODO
    trialVirusPops = []

    for trial in range(trials):
        testPatient = Patient(createViruses(startingVirusPop, maxVirusBirthProb, virusClearProb, virusResistances, virusMutProb), maxVirusPop) #create patient
        virusPop = 0

        for step in range(0, firstDrugTimeSteps): #trial pre-firstdrug
            testPatient.update() #update patient

        testPatient.addPrescription(perscriptions[0])
        # print("Perscription Given")

        for step in range(0, secondDrugTimeSteps): #trial pre-seconddrug
            testPatient.update() #update patient

        testPatient.addPrescription(perscriptions[1])

        for step in range(0, postDrugTimeSteps): #trial steps post-drug
            testPatient.update() #update patient

        trialVirusPops.append(len(testPatient.viruses))

    plt.hist(trialVirusPops, 30, range=[0, maxVirusPop], facecolor='green', align='mid')
    pylab.xlim([0,600])
    pylab.title("The Spread of Disease and Virus Population with Delayed Drug(s) \n ""Trials: " + str(trials) +"   Steps: " + str(firstDrugTimeSteps + secondDrugTimeSteps + postDrugTimeSteps) + "   Drug(s) Added At Step: " + str(firstDrugTimeSteps) + " & " + str(secondDrugTimeSteps + firstDrugTimeSteps))
    pylab.xlabel("Final Virus Population")
    pylab.ylabel("# of Patients")
    pylab.show()




#
# PROBLEM 5
#

def simulationTwoDrugsVirusPopulations(trials, firstDrugTimeSteps, secondDrugTimeSteps, postDrugTimeSteps, perscriptions, startingVirusPop, maxVirusPop, maxVirusBirthProb, virusClearProb, virusResistances, virusMutProb):

    """

    Run simulations and plot graphs examining the relationship between
    administration of multiple drugs and patient outcome.
    Plots of total and drug-resistant viruses vs. time are made for a
    simulation with a 300 time step delay between administering the 2 drugs and
    a simulations for which drugs are administered simultaneously.

    """
    #TODO

    resistantVirusPops = [] # resistant virus population for each trial run
    # avgVirusPops = [] #average total virus population for each trial run
    # avgResistantVirusPops = [] #average resistant virus population for each trial run
    totalSteps = firstDrugTimeSteps + secondDrugTimeSteps + postDrugTimeSteps

    # for x in range(totalSteps): #populate avgVirusPops and avgResistantVirusPops
    #     avgVirusPops.append(0)
    #     avgResistantVirusPops.append(0)

    pylab.figure(num=None, figsize=(16, 8), dpi=80, facecolor='w', edgecolor='k') #create figure for plotting on

    for trial in range(trials): #run trials
        testPatient = Patient(createViruses(startingVirusPop, maxVirusBirthProb, virusClearProb, virusResistances, virusMutProb), maxVirusPop) #create patient
        virusPops = []
        firstDrugResistPops = []
        secondDrugResistPops = []
        dualDrugResistPops = []

        for step in range(0, firstDrugTimeSteps): #trial pre-firstdrug
            virusPops.append(testPatient.update()) #update patient
            firstDrugResistPops.append(testPatient.getResistPop([perscriptions[0]])) #get first drug resistant virus pop
            secondDrugResistPops.append(testPatient.getResistPop([perscriptions[1]])) #get second drug resistant virus pop
            dualDrugResistPops.append(testPatient.getResistPop([perscriptions[0], perscriptions[1]])) #get dual drug resistant virus pop

        testPatient.addPrescription(perscriptions[1]) #drug added

        for step in range(0, secondDrugTimeSteps): #trial pre-seconddrug
            virusPops.append(testPatient.update()) #update patient
            firstDrugResistPops.append(testPatient.getResistPop([perscriptions[0]])) #get first drug resistant virus pop
            secondDrugResistPops.append(testPatient.getResistPop([perscriptions[1]])) #get second drug resistant virus pop
            dualDrugResistPops.append(testPatient.getResistPop([perscriptions[0], perscriptions[1]])) #get dual drug resistant virus pop

        testPatient.addPrescription(perscriptions[0]) #drug added

        for step in range(0, postDrugTimeSteps): #trial steps post-drug
            virusPops.append(testPatient.update()) #update patient
            firstDrugResistPops.append(testPatient.getResistPop([perscriptions[0]])) #get first drug resistant virus pop
            secondDrugResistPops.append(testPatient.getResistPop([perscriptions[1]])) #get second drug resistant virus pop
            dualDrugResistPops.append(testPatient.getResistPop([perscriptions[0], perscriptions[1]])) #get dual drug resistant virus pop

        for x in range(totalSteps): #plot all data points for trial
            pylab.plot(x+1, virusPops[x], '.b', label = "Virus Pop" if x == 0 and trial == 0 else "", marker='.')
            pylab.plot(x+1, firstDrugResistPops[x], '.k', label = str(perscriptions[0]).title() + " Resistant Virus Pop" if x == 0 and trial == 0 else "", marker='.')
            pylab.plot(x+1, secondDrugResistPops[x], '.m', label = str(perscriptions[1]).title() + " Resistant Virus Pop" if x == 0 and trial == 0 else "", marker='.')
            pylab.plot(x+1, dualDrugResistPops[x], '.c', label = str(perscriptions[0]).title() + " & " + str(perscriptions[1]).title() + " Resistant Virus Pop" if x == 0 and trial == 0 else "", marker='.')

            # avgVirusPops[x] += virusPops[x] #add step virus population totals to use for average later
            # avgResistantVirusPops[x] += firstDrugResistPops[x]\

        # print(dualDrugResistPops)
        # print(secondDrugResistPops)
        # print(firstDrugResistPops)


    # print (avgVirusPops)

    # for x in range(len(avgVirusPops)): #create averages from total virus counts over all trials.
    #     avgVirusPops[x] = avgVirusPops[x]/trials
    #     avgResistantVirusPops[x] = avgResistantVirusPops[x]/trials

    # print ("Virus Pops Per Step:")
    # print (virusPops)
    # print ("Resistant Virus Pops Per Step:")
    # print (resistantVirusPops)
    # print ("")
    # print ("Average Virus Pops Per Step:")
    # print (avgVirusPops)
    # print ("Average Resistant Virus Pops Per Step:")
    # print (avgResistantVirusPops)

    # pylab.plot(avgVirusPops, '-r', label = "Avg Virus Pop")
    # pylab.plot(avgResistantVirusPops, '-g', label = "Avg Resistant Virus Pop")
    pylab.ylabel("Virus Population")
    pylab.xlabel("Simulation Step")
    pylab.title("The Spread of Disease and Virus Population with Delayed Drug(s) \n ""Trials: " + str(trials) +"   Steps: " + str(totalSteps) + "   Drug(s) Added At Step: " + str(firstDrugTimeSteps) + " & " + str(secondDrugTimeSteps + firstDrugTimeSteps))

    pylab.legend(loc = 'upper left')

    pylab.show()


#SIMULATION FOR PROBLEM 2-----------
# simulationWithDrug(20, 150, 150, ["guttagonol"], 100, 1000, .1, .05, {"guttagonol":False}, 0.005)
#-----------------------------------

#SIMULATION FOR PROBLEM 3-----------
#Test steps [0, 75, 150, 300] before drug administration
# simulationDelayedTreatment(300, 0, 150, ["guttagonol"], 100, 1000, .1, .05, {"guttagonol":False}, 0.005)\
# simulationDelayedTreatment(300, 75, 150, ["guttagonol"], 100, 1000, .1, .05, {"guttagonol":False}, 0.005)
# simulationDelayedTreatment(300, 150, 150, ["guttagonol"], 100, 1000, .1, .05, {"guttagonol":False}, 0.005)
# simulationDelayedTreatment(300, 300, 150, ["guttagonol"], 100, 1000, .1, .05, {"guttagonol":False}, 0.005)

#-----------------------------------

#SIMULATION FOR PROBLEM 4-----------
#Test steps [0, 75, 150, 300] before drug administration
# simulationTwoDrugsDelayedTreatment(300, 150, 0, 150, ["guttagonol", "grimpex"], 100, 1000, .1, .05, {"guttagonol":False, "grimpex":False}, 0.005)
# simulationTwoDrugsDelayedTreatment(300, 150, 75, 150, ["guttagonol", "grimpex"], 100, 1000, .1, .05, {"guttagonol":False, "grimpex":False}, 0.005)
# simulationTwoDrugsDelayedTreatment(300, 150, 150, 150, ["guttagonol", "grimpex"], 100, 1000, .1, .05, {"guttagonol":False, "grimpex":False}, 0.005)
# simulationTwoDrugsDelayedTreatment(300, 150, 300, 150, ["guttagonol", "grimpex"], 100, 1000, .1, .05, {"guttagonol":False, "grimpex":False}, 0.005)
#-----------------------------------

#SIMULATION FOR PROBLEM 5-----------
#Test steps [0, 300] before drug administration
# simulationTwoDrugsVirusPopulations(15, 150, 0, 150, ["guttagonol", "grimpex"], 100, 1000, .1, .05, {"guttagonol":False, "grimpex":False}, 0.005)
simulationTwoDrugsVirusPopulations(10, 150, 300, 150, ["guttagonol", "grimpex"], 100, 1000, .1, .05, {"guttagonol":False, "grimpex":False}, 0.005)
#-----------------------------------
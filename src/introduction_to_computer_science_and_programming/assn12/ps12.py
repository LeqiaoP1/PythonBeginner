# 6.00 Problem Set 12
#
# Name:
# Collaborators:
# Time:

import numpy
import random
import pylab

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """    

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
        self.maxBirthProb = maxBirthProb
        self.maxClearProb = clearProb
        
    def doesClear(self):
        """
        Stochastically determines whether this virus is cleared from the
        patient's body at a time step. 

        returns: Using a random number generator (random.random()), this method
        returns True with probability self.clearProb and otherwise returns
        False.
        """
        return (random.random() <= self.maxClearProb)
    
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
        if (random.random() > self.maxBirthProb * (1 - popDensity)):
            raise NoChildException()
        else:
            return SimpleVirus(self.maxBirthProb, self.maxClearProb)

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
        self.viruses = viruses[:] # deep copy
        self.maxPop = maxPop

    def getTotalPop(self):
        """
        Gets the current total virus population. 

        returns: The total virus population (an integer)
        """
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

        returns: the total virus population at the end of the update (an
        integer)
        """
              
        self.viruses[:] = [x for x in self.viruses if not x.doesClear()]
        
        totalPop = self.getTotalPop()
        propDensity = totalPop*1.0/self.maxPop
        
        for i in range(totalPop):
            try:
                obj = self.viruses[i].reproduce(propDensity)
                self.viruses.append(obj)
            except NoChildException:
                #print "No child!"
                pass

        return self.getTotalPop()

#
# PROBLEM 2
#

def problem2():
    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).    

    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.    
    """
    virues = [SimpleVirus(0.1, 0.05) for i in range(100)]
    patient = SimplePatient(virues, 2000)

    x_t = range(300)
    y_pop = [0 for t in x_t]
    
    for t in x_t:
        patient.update()
        y_pop[t] = patient.getTotalPop()

    
    pylab.plot(x_t, y_pop)
    pylab.title(" Patient takes no drug ")
    pylab.xlabel(" time step ")
    pylab.ylabel(" total number of viruses ")
    pylab.show()
    
#
# PROBLEM 3
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
        self.resist_dict = dict(resistances) # hard deep copy
        self.mutProb = mutProb
        super( ResistantVirus, self).__init__(maxBirthProb, clearProb)
        
        
    def getResistance(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.        

        drug: the drug (a string).

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        return (drug in self.resist_dict.keys()) and self.resist_dict[drug]
        
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
        """
        if all(self.getResistance(drug) for drug in activeDrugs):
            # having a chance to reproduce itself
            if (random.random() > self.maxBirthProb * (1 - popDensity)):
                raise NoChildException()
            else:
                # apply the mutProb for each drug-resist
                child_resist = dict(self.resist_dict) # init by coping parents
                for drug in self.resist_dict.keys():
                    if (random.random() < self.mutProb): # switching occurs
                        child_resist[drug] = not self.resist_dict[drug]
                        
                return ResistantVirus(self.maxBirthProb, self.maxClearProb, child_resist, self.mutProb)
        else: # not reproduciable due to one of drugs
            raise NoChildException()
            
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
        self.drug_list = []
        super(Patient, self).__init__(viruses, maxPop)

    
        
    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the 
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: list of drugs being administered to a patient is updated
        """
        if newDrug not in self.drug_list:
            self.drug_list.append(newDrug)
            

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.drug_list
        
        
    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in 
        drugResist.        

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])

        returns: the population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        count = 0
        for v in self.viruses:
            if all(v.getResistance(drug) for drug in drugResist):
                count = count + 1

        return count

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
        self.viruses[:] = [x for x in self.viruses if not x.doesClear()]
        
        totalPop = self.getTotalPop()
        propDensity = totalPop*1.0/self.maxPop
        
        for i in range(totalPop):
            try:
                obj = self.viruses[i].reproduce(propDensity, self.drug_list)
                self.viruses.append(obj)
            except NoChildException:
                #print "No child!"
                pass

        return self.getTotalPop()

#
# PROBLEM 4
#

def problem4():
    """
    Runs simulations and plots graphs for problem 4.

    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.

    total virus population vs. time  and guttagonol-resistant virus population
    vs. time are plotted
    """
    virues = [ResistantVirus(0.1, 0.05, {'guttagonol':False}, 0.005) for i in range(100)]
    patient = Patient(virues, 1000)

    x_t = range(300)
    y_pop = [0 for t in x_t] # init

    print "at begin: pop of virus with resistance: ", patient.getResistPop(['guttagonol'])
    
    for t in range(150):
        patient.update()
        y_pop[t] = patient.getTotalPop()

    print "before taking drug: pop of virus with resistance: ", patient.getResistPop(['guttagonol'])
    patient.addPrescription('guttagonol')

    for t in range(150, 300):
        patient.update()
        y_pop[t] = patient.getTotalPop()

    print "after taking drug for some time: pop of virus with resistance: ", patient.getResistPop(['guttagonol'])
    
    pylab.plot(x_t, y_pop)
    pylab.title(" Patient takes 'guttagonol' after the 150th step")
    pylab.xlabel(" time steps ")
    pylab.ylabel(" number of viruses(may with drug-resistance)")
    pylab.show()
    

#
# PROBLEM 5
#
        
def problem5():
    """
    Runs simulations and make histograms for problem 5.

    Runs multiple simulations to show the relationship between delayed treatment
    and patient outcome.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).    
    """
    delays = [300, 225, 150, 75, 0]
    final_pop = []

    virues = [ResistantVirus(0.1, 0.05, {'guttagonol':False}, 0.005) for i in range(100)]
    
    for delay in delays:
        print "simulation for %d steps delay"%(delay)
        y_pop = [0 for t in range(delay+150)]
        
        patient = Patient(virues, 1000)
        for t in range(delay):
            patient.update()
            y_pop[t] = patient.getTotalPop()

        patient.addPrescription('guttagonol')

        for t in range(delay, delay+150):
            patient.update()
            y_pop[t] = patient.getTotalPop()
        
        final_pop.append(y_pop[-1])

    pylab.bar(delays, final_pop, width=5)
    pylab.title("delay effect of drug treatment")
    pylab.xlabel("delay before the 150 steps long treatment")
    pylab.ylabel("total number of viruses after treatment")
    pylab.show()


#
# PROBLEM 6
#
import matplotlib.pyplot as plt
def problem6():
    """
    Runs simulations and make histograms for problem 6.

    Runs multiple simulations to show the relationship between administration
    of multiple drugs and patient outcome.
    
    Histograms of final total virus populations are displayed for lag times of
    150, 75, 0 timesteps between adding drugs (followed by an additional 150
    timesteps of simulation).
    """
    delays = sorted([300, 225, 150, 75, 0])
    treatments = [['guttagonol'], ['grimpex'], ['new']]
    #treatments = [['guttagonol'], ['guttagonol', 'grimpex']]
    final_pop = []

    virues = [ResistantVirus(0.1, 0.05, {'guttagonol':False, 'grimpex':False, 'new':False}, 0.005) for i in range(100)]

    for treatment in treatments:
        y_pop_delays = []
        for delay in delays:
            print "simulation for %d steps delay"%(delay)
            y_pop = [0 for t in range(delay+150)]

            # new patient for study
            patient = Patient(virues, 1000)
            for t in range(delay):
                patient.update()
                y_pop[t] = patient.getTotalPop()

            # apply all given drugs
            for drug in treatment:
                patient.addPrescription(drug)

            for t in range(delay, delay+150):
                patient.update()
                y_pop[t] = patient.getTotalPop()

            y_pop_delays.append(y_pop[-1])
            
        final_pop.append(y_pop_delays)


    print final_pop
    # visualization
    
    bar_w = 5
    x_shift = 0
    colors = ['r', 'b', 'g']
    for i in range(len(treatments)):
        plt.bar([(x + x_shift) for x in delays], final_pop[i], bar_w, color=colors[i], label=str(treatments[i]))
        x_shift += bar_w

    plt.legend()
    plt.title("delay effect of drug treatment")
    plt.xlabel("delay before the 150 steps long treatment")
    plt.ylabel("total number of viruses after treatment")
    plt.show()

#
# PROBLEM 7
#
     
def problem7():
    """
    Run simulations and plot graphs examining the relationship between
    administration of multiple drugs and patient outcome.

    Plots of total and drug-resistant viruses vs. time are made for a
    simulation with a 300 time step delay between administering the 2 drugs and
    a simulations for which drugs are administered simultaneously.        
    """
    # TODO

## added test caes
def test_simple():
    virus_10 = [SimpleVirus(0.4,0.2) for i in range(10)]
    pat_1 = SimplePatient( virus_10, 200 )
    print "before update \t", pat_1.getTotalPop()
    print "after update \t", pat_1.update()


def test_resistance():
    virus_20 = [ResistantVirus(0.4,0.2, {'guttagonol':False, 'grimpex':False}, 0.1) for i in range(10)]
    pat_2 = Patient(virus_20, 200)
    pat_2.addPrescription('guttagonol')
    pat_2.addPrescription('grimpex')
    print "before update \t", pat_2.getTotalPop()
    print "after update \t", pat_2.update()
    print "virus resistant to drugs \t", pat_2.getResistPop(['guttagonol'])


if __name__ == "__main__":
    #test_resistance()
    problem5()
    #pass

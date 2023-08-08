# 6.00 Problem Set 9
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

SUBJECT_FILENAME = "subjects.txt"
SHORT_SUBJECT_FILENAME = "shortened_subjects.txt"
VALUE, WORK = 0, 1

class schoolSubject:
    def __init__(self, name, value, work):
        self.name = name
        self.value = value
        self.work = work

#
# Problem 1: Building A Subject Class
#
def loadSubjects(filename):
    """
    Returns a list of class objects which include a name, value, and work, where the 
    name is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: list of class objects which include a name, value, and work,
    """

    # The following sample code reads lines from the specified file and prints
    # each one.

    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a class with subject name,
    # value, and work.
    inputFile = open(filename)
    subjects = []
    for line in inputFile:
        data = line.rstrip('\n').split(',') #remove /n from end of line and split strings into a list
        subjects.append(schoolSubject(data[0], int(data[1]), int(data[2]))) #assign strings to proper dictionary keys/values
    return subjects

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    for subject in subjects:
        res = res + subject.name + '\t' + str(subject.value) + '\t\t' + str(subject.work) + '\n'
        totalVal += subject.value
        totalWork += subject.work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print (res)

# printSubjects(loadSubjects(SHORT_SUBJECT_FILENAME))

#
# Problem 2: Subject Selection By Greedy Optimization
#

def cmpValue(subject1, subject2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    # TODO...
    if subject1.value > subject2.value:
        return True
    else: 
        return False

def cmpWork(subject1, subject2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    # TODO...
    if subject1.work < subject2.work:
        return True
    else: 
        return False

def cmpRatio(subject1, subject2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    # TODO...
    # print ("sub1: " + str(subInfo1) + "  sub2: " + str(subInfo2))
    if subject1.value/subject1.work > subject2.value/subject2.work:
        return True
        # print ("True")
    else:
        return False
        # print ("False")

def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a list of classes repressenting a school subjecting including 
    a name(str), value(int), work(int) subjects selected by the algorithm, 
    such that the total work of subjects in the list of classes is not 
    greater than maxWork.  The subjects are chosen using a greedy algorithm.  
    The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...

    assignedSubjects = {}
    totalWork = 0
    bestChoice = None
# totalWork <= maxWork and
    i = 0
    while  i < len(subjects): 
        for subject1 in subjects.items(): #grab subject 1
            if subject1[1][1] + totalWork <= maxWork and subject1[0] not in assignedSubjects: # check if subject1 is valid subject (e.g. isn't already assigned, won't cause max work to go over)
                for subject2 in subjects.items(): #grab subject 2 to compare to subject 1
                    # print ("sub1: " + str(subject1) + "  sub2: " + str(subject2))
                    if subject2[1][1] + totalWork <= maxWork and subject2[0] not in assignedSubjects and subject1[0] != subject2[0]: # check if subject2 is valid subject (e.g. isn't already assigned, won't cause max work to go over, is not subject1)
                        if comparator(subject1[1], subject2[1]): #check if subject 1 is best option
                            bestChoice = True
                        else:
                            bestChoice = False
                            break #if subject1 is ever not best choice then break out of comparison loop; do not keep comparing
                if bestChoice == True: #subject 1 is best choice
                    # print ("bestChoice: " + str({subject1[0]:subject1[1]}))
                    assignedSubjects.update({subject1[0]:subject1[1]}) 
                    totalWork += subject1[1][1]
            # print ("total work: " + str(totalWork))
        i += 1 
        # print (i)

    return assignedSubjects   



#Input a list of subject classes (each have a name(str), work(int), value(int)) and a maxWork(int) value. Returns a list of lists where the sub lists are all combinations of subjects that, when their work(int) is added together, equal less than maxWork(int).

#Takes one subject and checks if it is valid with all previous valid subjects. The moves onto next subject. If no more valid subjects can be found it returns a blank list and the current valid combination of subjects is saved.   


allCombinations = []    

def getValidCombinations(subjects, maxWork, currentWork, previousCombination):
    global allCombinations

    for subject in subjects:
        if subject.work + currentWork <= maxWork and subject not in previousCombination:
            currentCombination = previousCombination + [subject]
            nextCombination = getValidCombinations(subjects, maxWork, subject.work + currentWork, currentCombination)
            if nextCombination == [] and all(set(currentCombination) != set(i) for i in allCombinations):
                allCombinations.append(currentCombination)
    return []

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a list of classes  repressenting a school subjecting including a
    name(str), value(int), work(int) which represents the globally optimal selection 
    of subjects using a brute force algorithm.

    subjects: list of classes  repressenting a school subjecting including a
    name(str), value(int), work(int)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...
    # seperatedSubjects = dictToList(subjects)
    # print (seperatedSubjects)
    # print (listToDict(seperatedSubjects))

    getValidCombinations(subjects, maxWork, 0, [])

    bestSubjects = []
    bestSubjectsValue = 0

    for subjectCombination in allCombinations:
        currentValue = 0
        for subject in subjectCombination:
            currentValue += subject.value
        if currentValue > bestSubjectsValue:
            bestSubjects = subjectCombination
            bestSubjectsValue = currentValue

    printSubjects (bestSubjects)





if __name__ == '__main__':
    function = bruteForceAdvisor #function to be tested
    short_subjects = {'1.00': (7, 7), '15.01': (9, 6), '6.01': (5, 3), '6.00': (16, 8)}
    subjects = loadSubjects(SHORT_SUBJECT_FILENAME)
    maxWork = 7

    if function == greedyAdvisor:     
        print ("assigned subjects: " + str(function(subjects, maxWork, cmpRatio)))

    if function == bruteForceAdvisor:
        bruteForceAdvisor(subjects, maxWork)
        
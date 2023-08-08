import random
import pylab

def coinFlip():
    if random.random() < .5:
        return "heads"
    else:
        return "tails"


def coinFlipSequence(sequenceLength):
    flipSequence = ()
    for x in range(sequenceLength):
        flipSequence += (coinFlip(),)

    return flipSequence


def matchSequencesSimulation(numSequences, flipSequence, sequenceLength):
    matches = []

    for step in range(numSequences):
        newFlipSequence = coinFlipSequence(sequenceLength)
        # print newFlipSequence
        if newFlipSequence == flipSequence:
            matches.append(newFlipSequence)

    if matches != []:
        # print matches
        return float(len(matches))/numSequences

    else:
        return 0


def percentHeadsSimulation(numSequences, minPercentHeads, sequenceLength):
    matches = []

    for step in range(1, numSequences+1):
        newFlipSequence = coinFlipSequence(sequenceLength)
        heads = 0
        for flip in newFlipSequence:
            if flip == "heads":
                heads += 1     
        if heads > 0:
            if heads/sequenceLength >= minPercentHeads:
                matches.append(newFlipSequence)

    if matches != []:
        return float(len(matches))/numSequences

    else:
        return 0


def runSimulations(numTrials, numFlipsPerTrial, percentHeadsToTails, flipSequence, sequenceLength):
    headsToTails = []
    probHeadsToTails = 0.0

    flipSequenceMatch = []
    probFlipSequenceMatch = 0.0

    for x in range(numTrials):
        headsToTails.append(percentHeadsSimulation(numFlipsPerTrial, percentHeadsToTails, sequenceLength))
        flipSequenceMatch.append(matchSequencesSimulation(numFlipsPerTrial, flipSequence, sequenceLength))
        pylab.plot( x, headsToTails[x], "rx")
        pylab.plot( x, flipSequenceMatch[x], "bx")

    for each in headsToTails:
        probHeadsToTails += each
    probHeadsToTails = float(probHeadsToTails)/len(headsToTails)

    for each in flipSequenceMatch:
        probFlipSequenceMatch += each
    probFlipSequenceMatch = float(probFlipSequenceMatch)/len(flipSequenceMatch)

    print probHeadsToTails
    print probFlipSequenceMatch

    pylab.yscale('log')
    pylab.ylabel('Probability')
    pylab.xlabel('Trial')
    pylab.legend(["Heads to Tails", "Matching Sequence"])
    pylab.title("Probability of coin flip sequences matching given sequence or having more heads than tails.")
    pylab.show()



runSimulations(500, 1000000, float(2)/3, ("heads","heads","tails"), 3) 







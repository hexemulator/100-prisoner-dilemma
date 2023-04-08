"""
@name: 100-prisoner-dilemma.py
@author: Brandon Stanton
@date: April 8th, 2023

REQUIREMENT:
'random' python library for selecting box:paper pairings!

This is a script that runs the '100 prisoners dilemma' as detailed below:
https://en.wikipedia.org/wiki/100_prisoners_problem

Me working on this was inspired by this video:
https://www.youtube.com/watch?v=iSNsgj1OCLA

Expected result:
As the number of experiments and prisoner count increase-- it will approach approx. 30.7% success rate

Possible issues:
Using a 'randomizer' which may not actually provide enough randomization to provide a good enough test

Observed results:
Between runs of 1000+ times conducting the experiment-- seems to average out around the expected result?
"""

import random
random.seed()


def conduct_experiment(prisonercount: int) -> bool:
    paperList = []      # list of numbered slips of paper
    numberedBoxes = {}  # dictionary of numbered boxes (key), and numbered slips of paper (value)

    number_of_tries = prisonercount/2  # in the experiment, each prisoner has n/2 tries to find their number

    # populate the paperList: write all the numbers from 1 up to n into the paperList
    counter = prisonercount
    while counter > 0:
        paperList.append(counter)
        counter -= 1

    remainingBoxes = paperList.copy()  # create a list of boxes that remain to have a slip of paper placed into it

    # with all the slips of paper now present-- we will begin putting them into boxes, until none remain of either
    while len(paperList) > 0:
        randomBoxSelection = random.choice(remainingBoxes)  # select a random box number from remaining boxes
        remainingBoxes.remove(randomBoxSelection)  # remove box choice from the roster
        randomPaperSelection = random.choice(paperList)  # select a random slip of paper from remaining papers
        paperList.remove(randomPaperSelection)  # remove paper choice from the roster

        numberedBoxes[randomBoxSelection] = randomPaperSelection  # place the slip of paper into the box

    # for each prisoner numbered from 1, up to n-- will go into the room, and open up each box, starting with own number
    for number in range(1, prisonercount+1):
        attempt = 0
        firstBoxNumber = number
        slipFound = False

        while attempt < number_of_tries:

            if attempt == 0:
                nextBoxNumber = numberedBoxes[firstBoxNumber]  # if this is the first box
            else:
                nextBoxNumber = numberedBoxes[nextBoxNumber]  # if this is a box after the first one...

            if nextBoxNumber == number:
                slipFound = True
                break

            attempt += 1  # increment attempt counter

        # if a prisoner exits the room without finding their slip of paper-- then failure!
        if slipFound is False:
            return False

    if slipFound is True:
        return True


if __name__ == '__main__':

    prisonerCount = int(input("How many prisonners should there be? (greater than 100): "))  # the user will enter the number of prisoners
    experimentCount = int(input("How many times would you like to conduct the experiment? (larger is better): "))

    successCount = 0

    for expC in range(experimentCount):
        if conduct_experiment(prisonerCount) is True:
            successCount += 1

    successRate = successCount/experimentCount
    print(f'{successCount} successful escapes! Success rate of: {str(successRate)}%')
    print('Experiment end, goodbye!')
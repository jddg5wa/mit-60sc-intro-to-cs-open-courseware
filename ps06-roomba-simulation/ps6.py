# Problem Set 6: Simulating robots
# Name:
# Collaborators:
# Time:
from __future__ import division
import math
import random

import ps6_visualize
import pylab

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

# === Problems 1


class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        if width > 0 and height > 0:
            self.width = width
            self.height = height

            self.tileAmount = self.width * self.height
            self.tileCoordinates = []
            self.tileClean = []
            x = 0
            y = 0

            for x in range(self.height):
                x += 1
                for y in range(self.width):
                    y += 1
                    self.tileCoordinates.append((x, y))

        else:
            raise ValueError('Room: Width or Height is less than 1.')

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        self.tilePos = (int(pos.getX()), int(pos.getY()))
        # print "unclean",self.tilePos

        if self.tilePos not in self.tileClean:
            # print "clean tile:",self.tilePos
            self.tileClean.append(self.tilePos)

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        self.tilePos = (m, n)
        if self.tilePos in self.tileClean:
            return True
        else:
            return False

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return len(self.tileClean)

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        x = random.randint(0, self.width)
        y = random.randint(0, self.height)
        return Position(x, y)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        x = pos.getX()
        y = pos.getY()

        if x >= 0 and x <= self.width and y >= 0 and y <= self.height:
            return True
        else:
            return False


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        self.position = room.getRandomPosition()
        self.direction = random.randint(0, 360)

        self.room.cleanTileAtPosition(self.position)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position

    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    # def updatePositionAndClean(self):
    #     """
    #     Simulate the raise passage of a single time-step.

    #     Move the robot to a new position and mark the tile it is on as having
    #     been cleaned.
    #     """

    #     self.position = self.position.getNewPosition(self.angle, self.speed)
    #     self.room.cleanTileAtPosition(self.position)

# === Problem 2


class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current direction.
    When it hits a wall, it chooses a new direction randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        self.newPos = self.position.getNewPosition(self.direction, self.speed)
        old_direction = self.direction
        # print "newPos", "x", int(self.newPos.getX()), "y", int(self.newPos.getY())

        if self.room.isPositionInRoom(self.newPos):
            self.setRobotPosition(self.newPos)
            self.room.cleanTileAtPosition(self.newPos)
            # print self.newPos.getX(),self.newPos.getY()

        else:
            x = 0
            # p_x, p_y = [], []
            while self.room.isPositionInRoom(self.newPos) == False:
                self.direction = random.randint(0, 360)
                self.newPos = self.position.getNewPosition(self.direction, self.speed)
                # p_x.append(self.newPos.x); p_y.append(self.newPos.y)
                x += 1
                if x > 100000:
                    # import matplotlib.pyplot as plt
                    # plt.plot(p_x, p_y)
                    # plt.show()
                    raise ValueError('Stuck in Loop', self.newPos.getX(),self.newPos.getY(), self.direction, old_direction)
        self.setRobotPosition(self.newPos)
        self.room.cleanTileAtPosition(self.newPos)


# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    """
    stepCounts = []
    for t in range(num_trials):
        print ("Robot", t+1)
        anim = ps6_visualize.RobotVisualization(num_robots, width, height, .25)
        roomToClean = RectangularRoom(width, height)
        percentCleanTiles = roomToClean.getNumCleanedTiles()/roomToClean.getNumTiles()
        # print "tiles cleaned (beg):", roomToClean.getNumCleanedTiles()
        # print "tiles unclean (beg):", roomToClean.getNumTiles()
        steps = 0
        robots = []


        for i in range(num_robots):
            # print "r = ",r
            robots.append(robot_type(roomToClean, speed))

        while percentCleanTiles < min_coverage:
            for each in robots:
                each.updatePositionAndClean()
                percentCleanTiles = roomToClean.getNumCleanedTiles()/roomToClean.getNumTiles()
                # print percentCleanTiles
                steps += 1
            anim.update(roomToClean, robots)
        stepCounts.append(steps)
        # print roomToClean.tileClean
        # for each in roomToClean.tileClean:
        #     tiles = []
        #     if each in tiles:
        #         raise ValueError("duplicate tile")
        #     else:
        #         tiles.append(each)
        # print "tiles cleaned (end):", roomToClean.getNumCleanedTiles()
        # print "tiles unclean (end):", roomToClean.getNumTiles()
    # print "stepCounts = ",stepCounts
    return mean(stepCounts)




def mean(numbers):
    """
    returns the mean for a series of numbers

    numbers: a list or tuple of numbers 
    """
    meanStepCount = 0.00

    for each in numbers:
        meanStepCount += float(each)

    return meanStepCount/len(numbers)

# avg = runSimulation(50, .5, 20, 20, 1.00, 20, StandardRobot)
# print "Average Steps for 20x20 (100%) with 20 Robot(s) is", avg

# avg = runSimulation(1, 1.0, 10, 10, .75, 100, StandardRobot)
# print "Average Steps for 10x10 (75%) should be approx 190 but is", avg

# avg = runSimulation(1, 1.0, 10, 10, .90, 100, StandardRobot)
# print "Average Steps for 10x10 (90%) should be approx 310 but is", avg

# avg = runSimulation(1, 1.0, 20, 20, 1.00, 100, StandardRobot)
# print "Average Steps for 20x20 (100%) should be approx 3250 but is", avg

# === Problem 4

# 1) How long does it take to clean 80% of a 20x20 room with each of 1-10 robots?

# 2) How long does it take two robots to clean 80% of rooms with dimensions 
#      20x20, 25x16, 40x10, 50x8, 80x5, and 100x4?

def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """ 
    print ("calculating plot")
    averageSteps = []
    robots = []
    roomSize = (20,20)
    roomAreas = []
    averageSteps = []
    robotSpeed = 1.0
    percentTilesCleaned = .8
    trials = 50
    robots = 10

    for r in range(robots):
        avg = runSimulation(robots, robotSpeed, roomSize[0], roomSize[1], percentTilesCleaned, trials, StandardRobot)
        averageSteps.append(avg)
        robots.append(r+1)

    print (robots)
    print (averageSteps)

    pylab.plot(robots,averageSteps)
    pylab.title("Time/steps it takes an amount of robots robots to clean 80% of a 20x20 room", percentage, "% of room size" + roomSize[0] + "by" + roomSize[1])
    pylab.xlabel("Robots")
    pylab.ylabel("Time/steps")
    pylab.show()

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    print ("calculating plot")
    roomSizes = [(20,20),(25,16),(40,10),(50,8),(80,5),(100,4)]
    roomAreas = []
    averageSteps = []
    robotSpeed = 1.0
    percentTilesCleaned = .8
    trials = 50
    robots = 2

    for x in range(len(roomSizes)):
        avg = runSimulation(robots, robotSpeed, roomSizes[x][0], roomSizes[x][1], percentTilesCleaned, trials, StandardRobot)
        averageSteps.append(avg)
        roomAreas.append(roomSizes[x][0] * roomSizes[x][1])

    print (averageSteps)

    pylab.plot(roomAreas, averageSteps)
    pylab.title("Time/steps it takes robot to clean 80% of 400 tiles in various room shapes.")
    pylab.ylabel("Time/steps")
    pylab.xlabel("Room Area")
    pylab.show()

def showPlot3():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    print ("calculating plot")
    roomSizes= [(5,5),(10,10),(20,20),(40,40),]
    roomAreas = []
    averageSteps = []
    robotSpeed = 1.0
    percentTilesCleaned = .7
    trials = 20
    robots = 3

    for x in range(len(roomSizes)):
        avg = runSimulation(robots, robotSpeed, roomSizes[x][0], roomSizes[x][1], percentTilesCleaned, trials, StandardRobot)
        averageSteps.append(avg)
        roomAreas.append(roomSizes[x][0] * roomSizes[x][1])

    print (averageSteps)

    pylab.plot(roomAreas, averageSteps)
    pylab.title("Time/steps it takes robot to clean 100% percent of various room areas")
    pylab.ylabel("Time/steps")
    pylab.xlabel("Room Area")
    pylab.show()

# showPlot3()

# === Problem 5

class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random after each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        self.direction = random.randint(0, 360)
        self.newPos = self.position.getNewPosition(self.direction, self.speed)
        # print "newPos", "x", int(self.newPos.getX()), "y", int(self.newPos.getY())

        if self.room.isPositionInRoom(self.newPos):
            self.setRobotPosition(self.newPos)
            self.room.cleanTileAtPosition(self.newPos)
            # print self.newPos.getX(),self.newPos.getY()

        else:
            x = 0
            # p_x, p_y = [], []
            while self.room.isPositionInRoom(self.newPos) == False:
                self.direction = random.randint(0, 360)
                self.newPos = self.position.getNewPosition(self.direction, self.speed)
                # p_x.append(self.newPos.x); p_y.append(self.newPos.y)
                x += 1
                if x > 100000:
                    # import matplotlib.pyplot as plt
                    # plt.plot(p_x, p_y)
                    # plt.show()
                    raise ValueError('Stuck in Loop', self.newPos.getX(),self.newPos.getY(), self.direction, old_direction)
        self.setRobotPosition(self.newPos)
        self.room.cleanTileAtPosition(self.newPos)

# avg = runSimulation(1, 1, 10, 10, 1.00, 1, RandomWalkRobot)

# # === Problem 6

# # For the parameters tested below (cleaning 80% of a 20x20 square room),
# # RandomWalkRobots take approximately twice as long to clean the same room as
# # StandardRobots do.
def showPlot3():
    """
    Produces a plot comparing the two robot strategies.
    """
    print ("calculating plot")
    roomSizes= [(5,5),(10,10),(20,20),(40,40)]
    robotSpeed = 1.0
    percentTilesCleaned = .8
    trials = 50
    robots = 2

    print ('\n','Random Walk Robot Tests')
    randomRobotData = getSimulationData(robots, robotSpeed, roomSizes, percentTilesCleaned, trials, RandomWalkRobot)

    print ('\n','Standard Robot Tests')
    standardRobotData = getSimulationData(robots, robotSpeed, roomSizes, percentTilesCleaned, trials, StandardRobot)

    pylab.plot(randomRobotData[0], randomRobotData[1], 'r-')
    pylab.plot(standardRobotData[0], standardRobotData[1], 'g-')
    pylab.title("Time/steps it takes robot to clean 80% of various room sizes.")
    pylab.ylabel("Time/steps")
    pylab.xlabel("Room Area")
    pylab.legend(['random robot', 'standard robot'], loc='upper left')
    pylab.show()

def getSimulationData(num_robots, speed, rooms, min_cleaned, num_trials,
                  robot_type):
    roomAreas = []
    averageSteps = []

    for x in range(len(rooms)):
        print ('\n', "Room:", x+1, "------------------------------", )
        print ('\n')
        avg = runSimulation(num_robots, speed, rooms[x][0], rooms[x][1], min_cleaned, num_trials, robot_type)
        averageSteps.append(avg)
        roomAreas.append(rooms[x][0] * rooms[x][1])
    
    return [roomAreas, averageSteps]

# showPlot3()

avg = runSimulation(10, 1, 20, 20, 1.00, 1, RandomWalkRobot)
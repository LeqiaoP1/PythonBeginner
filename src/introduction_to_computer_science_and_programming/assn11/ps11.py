# Problem Set 11: Simulating robots
# Name:
# Collaborators:
# Time:

import math

import random
import pylab
import ps11_visualize


# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).

        x: a real number indicating the x-coordinate
        y: a real number indicating the y-coordinate
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

        angle: integer representing angle in degrees, 0 <= angle < 360
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


# === Problems 1 and 2

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
        self.height = height
        self.width = width
        self.dirty_rooms = [[x, y] for x in range(width) for y in range(height)]
        self.clean_rooms = []

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        m = int(pos.getX())
        n = int(pos.getY())
        if not self.isTileCleaned(m, n):
            self.dirty_rooms.remove([m, n])
            self.clean_rooms.append([m, n])


    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return [m, n] in self.clean_rooms

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.height * self.width

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return len(self.clean_rooms)

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        r_x = random.uniform(0, self.width)
        r_y = random.uniform(0, self.height)

        return Position(r_x, r_y)

    def isPositionInRoom(self, pos):
        """
        Return True if POS is inside the room.

        pos: a Position object.
        returns: True if POS is in the room, False otherwise.
        """
        return (pos.getX() >= 0 and pos.getX() < self.width) and (pos.getY() >= 0 and pos.getY() < self.height)


class BaseRobot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in
    the room.  The robot also has a fixed speed.

    Subclasses of BaseRobot should provide movement strategies by
    implementing updatePositionAndClean(), which simulates a single
    time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified
        room. The robot initially has a random direction d and a
        random position p in the room.

        The direction d is an integer satisfying 0 <= d < 360; it
        specifies an angle in degrees.

        p is a Position object giving the robot's position.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = float(speed)

        self.position = self.room.getRandomPosition()
        self.direction = int(random.uniform(0, 360))


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


class Robot(BaseRobot):
    """
    A Robot is a BaseRobot with the standard movement strategy.

    At each time-step, a Robot attempts to move in its current
    direction; when it hits a wall, it chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        predict_pos = self.position.getNewPosition(self.direction, self.speed)

        # if not in-room, then regenerate the direction and predict next position
        while not self.room.isPositionInRoom(predict_pos):
            self.direction = int(random.uniform(0, 360))
            predict_pos = self.position.getNewPosition(self.direction, self.speed)
        
        self.position = predict_pos # update with an in-room position
        self.room.cleanTileAtPosition(self.position)


# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type, visualize):
    """
    Runs NUM_TRIALS trials of the simulation and returns a list of
    lists, one per trial. The list for a trial has an element for each
    timestep of that trial, the value of which is the percentage of
    the room that is clean after that timestep. Each trial stops when
    MIN_COVERAGE of the room is clean.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE,
    each with speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    Visualization is turned on when boolean VISUALIZE is set to True.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    visualize: a boolean (True to turn on visualization)
    """

    trial_records = [[] for t_id in range(num_trials)]
    
    for t_id in range(num_trials):
        if visualize:
            anim = ps11_visualize.RobotVisualization(num_robots, width, height, 1)
        # reinitil Room and Robots for each new trial
        room = RectangularRoom(width, height)
        robots = [robot_type(room, speed) for r in range(num_robots)]
        coverage = 0.0
        while (coverage < min_coverage):
            for r in robots:
                r.updatePositionAndClean()
                
            if visualize:
                anim.update(room, robots)
            coverage = (1.0 * room.getNumCleanedTiles() / room.getNumTiles())
            trial_records[t_id].append(coverage)

        if visualize:
            anim.done()

    return trial_records



# === Provided function
def computeMeans(list_of_lists):
    """
    Returns a list as long as the longest list in LIST_OF_LISTS, where
    the value at index i is the average of the values at index i in
    all of LIST_OF_LISTS' lists.

    Lists shorter than the longest list are padded with their final
    value to be the same length.
    """
    # Find length of longest list
    longest = 0
    for lst in list_of_lists:
        if len(lst) > longest:
           longest = len(lst)
    # Get totals
    tots = [0]*(longest)
    for lst in list_of_lists:
        for i in range(longest):
            if i < len(lst):
                tots[i] += lst[i]
            else:
                tots[i] += lst[-1]
    # Convert tots to an array to make averaging across each index easier
    tots = pylab.array(tots)
    # Compute means
    means = tots/float(len(list_of_lists))
    return means


# === Problem 4
def p4_helper(list_of_lists):
    """ average length of all nested lists """
    number_trials = len(list_of_lists)
    assert( not(number_trials == 0) )
    l_sum = sum( [len(list_of_lists[i]) for i in range(number_trials)] )
    return l_sum/number_trials
    
def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on room size.
    """
    rooms = [[5, 5], [10,10], [15,15], [20,20], [25,25]]
    x_data = []
    y_data = []
    for room in rooms:
        x_data.append( room[0] * room[1] )
        list_steps = runSimulation(1, 1.0, room[0], room[1], 0.75, 10, Robot, False)
        
        y_data.append( p4_helper(list_steps) )

    pylab.plot(x_data, y_data)
    pylab.title('dependence on sizes of room with single robot(speed = 1.0)')
    pylab.xlabel('room size')
    pylab.ylabel('steps needed to clean 75%')
    pylab.show()


def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    number_of_robots = range(1, 11)
    x_data = number_of_robots
    y_data = []
    for nr_rb in number_of_robots:
        list_steps = runSimulation(nr_rb, 1.0, 25, 25, 0.75, 10, Robot, False)
        y_data.append( p4_helper(list_steps) )

    pylab.plot(x_data, y_data)
    pylab.title('dependence on number of robots(speed:1.0)')
    pylab.xlabel('number of robots in room (size: 25*25)')
    pylab.ylabel('steps needed to clean 75%')
    pylab.show()
    

def showPlot3():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    rooms = [[20, 20], [25, 16], [40, 10], [50, 8], [8, 50], [100, 4]]
    
    x_data = []
    y_data = []
    for room in rooms:
        x_data.append( room[0]*1.0/room[1])
        list_steps = runSimulation(2, 1.0, room[0], room[1], 0.75, 20, Robot, False)       
        y_data.append( p4_helper(list_steps) )

    # resort the ratio
    sorted_x = sorted(x_data)
    sorted_index = sorted(range(len(x_data)), key=lambda x:x_data[x])
    sorted_y = [y_data[i] for i in sorted_index]
    pylab.plot(sorted_x, sorted_y)
    pylab.title('dependence on W/H-ratio of room with two robots(speed = 1.0)')
    pylab.xlabel('W/H Ratio of rooms with same size: 400')
    pylab.ylabel('steps needed to clean 75%')
    pylab.show()


from matplotlib import pyplot as plt
def showPlot4():
    """
    Produces a plot showing cleaning time vs. percentage cleaned, for
    each of 1-5 robots.
    """
    coverages = [x * 0.1 for x in range(1, 10)]
    
    for nr_robots in [1, 2, 3, 4, 5]:
        y_steps = []
        for cov in coverages:
            trial_steps = runSimulation(nr_robots, 1.0, 25, 25, cov, 10, Robot, False)
            y_steps.append( p4_helper(trial_steps) )

    
        plt.plot(coverages, y_steps, label="nr:%d"%(nr_robots))
    

    pylab.title('dependence on requried coverage of cleaned tiles')
    pylab.xlabel('required coverages in the room(size: 25*25)')
    pylab.ylabel('steps needed')
    plt.legend()
    plt.show()

# === Problem 5

class RandomWalkRobot(BaseRobot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement
    strategy: it chooses a new direction at random after each
    time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        self.room.cleanTileAtPosition(self.position)

        self.direction = int(random.uniform(0, 360))
        predict_pos = self.position.getNewPosition(self.direction, self.speed)
        
        # if not in-room, then regenerate the direction and predict next position
        while not self.room.isPositionInRoom(predict_pos):
            self.direction = int(random.uniform(0, 360))
            predict_pos = self.position.getNewPosition(self.direction, self.speed)
        
        self.position = predict_pos # update with an in-room position

        
# === Problem 6

def showPlot5():
    """
    Produces a plot comparing the two robot strategies.
    """
    coverages = [x * 0.1 for x in range(2, 9)]

    # for standard robot
    y_steps = []
    for cov in coverages:
        trial_steps = runSimulation(1, 1.0, 20, 20, cov, 20, Robot, False)
        y_steps.append( p4_helper(trial_steps) )
        
    plt.plot(coverages, y_steps, label="Standard Walk")

    # for new randomwalk robot
    y_steps = []
    for cov in coverages:
        trial_steps = runSimulation(1, 1.0, 20, 20, cov, 20, RandomWalkRobot, False)
        y_steps.append( p4_helper(trial_steps) )
        
    plt.plot(coverages, y_steps, label="Random Walk")

    pylab.title('dependence on requried coverage of cleaned tiles')
    pylab.xlabel('required coverages in the room(size:20x20)')
    pylab.ylabel('steps needed by one robot(speed:1.0)')
    plt.legend()
    plt.show()

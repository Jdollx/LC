"""
There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers position and speed, both of length n.

position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)
The destination is at position target miles.

A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.

"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # n cars traveling same way
        # given array of int position and speed (both length n)
        # destination = target
        # cars cannot pass each other, but can drive at same speed
        # fleet = cars driving same position and speed

        # sort the cars in descending order by position
        # this way we can see what cars can catch up with each other
        # reverse speed and position together
        cars = sorted(zip(position, speed), reverse=True)

        # initiate stack to hold number of fleets
        s = []

        # iterate through the list
        for pos, spd in cars:
            # calculate how much time it will take for each car to make it 
            # to its destination
            # this prevents us needing to calculate car speeds against each other
            ttd = (target - pos) / spd

            # now we can use the stack to compare our ttds
            # if our current ttd is > than top of stack, a new fleet is formed
            # this is because they're going different speeds (slower)
            # if its the same, they join the fleet

            # check if stack empty
            if not s or ttd > s[-1]:
                s.append(ttd)

            # else, the car joins an already existing fleet
        # by the end, the length of our stack will show our fleets
        return len(s)

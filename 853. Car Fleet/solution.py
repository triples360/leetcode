"""
This solution has more to do with thinking than using any data structure.

Lets take it step by step as to how to do so.

1) We might wanna sort the cars by their positions from left to right
   with their speeds. This way, we could get a better insight of how 
   the cars are moving.

2) We may wanna take a direction from where to travel the array;
   Since the cars are going in the right direction, the fleets are 
   going to be decided from right to left.
   So, lets travel the array in that direction (right to left or last to first)

3) Lets say there are multiple cars ahead of a car called carA. All the cars
   ahead of carA (say car1, car2, ..., carN) will merge together to form a car fleet.
   How can we find out if carA will also merge with them or not.
   Now if you think about it, it only matters if carA will catch upto carn or not.
   There could be two cases:
   i) carA catches up to carN before the target.
      In this case, since carA catches upto carN, it will catch up to all cars in the fleet
      as per the 3rd point. So, they all form just one fleet.
   ii) carA cannot catch up to carN before the target.
      In this case, carA will not be able to join the fleet. Because the fleet reaches
      the target together with carN. carA not being able to reach it means that
      it is its own car fleet. So, the number of car fleets in this case is 2.

4) We just simply go through the array picking two the last car of the last fleet we
   have seen and checking if the curr car can catchu up to the last car of the last fleet.
   If yes, we go to the previous car.
   If not, then the curr car becomes the new last fleet and we add the answer with 1.

"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        for i in range(len(position)):
            pos_speed.append( (position[i], speed[i]) )
        
        pos_speed.sort()
        res = 1
        last_fleet = (pos_speed[-1][0], pos_speed[-1][1])
        
        for i in range(len(pos_speed) - 2, -1, -1):
            if(last_fleet[1] == pos_speed[i][1]):
                meeting_point = -1
            else:
                meeting_point = (pos_speed[i][0]*last_fleet[1] - pos_speed[i][1]*last_fleet[0])/(last_fleet[1] - pos_speed[i][1])
            if(meeting_point < pos_speed[i][0] or meeting_point > target):
                res += 1
                last_fleet = (pos_speed[i][0], pos_speed[i][1])
        
        return res


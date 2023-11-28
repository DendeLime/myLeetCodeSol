# https://leetcode.com/problems/gas-station/
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # create start and car data

        # loop till circuit is complete 
            # get sum of all gas - cost
            # fuel - cost of the current location

            # if fuel < 0 then
                # start + 1
                # fuel = 0

            # move to next location
            
        # loop
        # if the sum of the gas < cost then there is no solution
        # return start


        fuel = 0
        _sum = 0
        start = 0

        for i in range(len(gas)):
            _sum += gas[i] - cost[i]
            fuel += gas[i] - cost[i]
            if fuel < 0:
                fuel = 0
                start = i + 1

        if _sum < 0:
            return -1

        return start


class Solution:
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        for i in range(n):
            runner = i
            tank = 0
            while runner != (i+n-1)%n:
                tank += gas[runner]
                if tank < cost[runner]:
                    break
                tank = tank - cost[runner]
                runner = (runner+1) % n
            if runner == (i+n-1)%n:
                return i
        return -1

Solution().canCompleteCircuit([2,3,4], [3,4,3])

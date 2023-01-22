from typing import Counter


class Solution(object):
    def leastInterval(self, tasks,n):
            count=[value for value in Counter(tasks).values()]
            count.sort()
            max_freq=count.pop()
            room=max_freq-1
            idle=(room)*n
            while count and idle > 0:
                idle -= min(room, count.pop())
            return max(0,idle)+len(tasks)

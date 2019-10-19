class Solution1_1:
    """自己实现"""
    def distanceBetweenBusStops(self, distance, start, destination):

        start, destination = start % len(distance), destination % len(distance)

        if start == destination:
            return 0
        elif start > destination:
            start, destination = destination, start

        routeA = sum(distance[start: destination])
        routeB = sum(distance[destination:] + distance[:start])
        return min(routeA, routeB)

class Solution1_2:
    """
      - 减法是一种思维
      - 仔细阅读题目后发现，这道题不需要 %
    """
    def distanceBetweenBusStops(self, distance, start, destination):

        sum_distance = sum(distance)

        if start > destination:
            start, destination = destination, start

        # 注 start == destination无须判断，sum([]) = 0
        distance_A = sum(distance[start: destination])

        return min(distance_A, sum_distance - distance_A)
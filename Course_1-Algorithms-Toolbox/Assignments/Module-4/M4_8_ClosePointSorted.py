from collections import namedtuple
from math import sqrt

Point = namedtuple('Point', 'x y')

def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2

def strip_distance(points, low, mid, high, d):
    x_mid = (points[mid+1].x + points[mid].x) / 2
    strip = [point for point in points[low:high+1] if (point.x - x_mid) ** 2 <= d]
    sorted_y = sorted(strip, key=lambda point: point.y)
    
    min_distance = d
    for i in range(len(sorted_y)):
        for j in range(i+1, min(i+8, len(sorted_y))):
            min_distance = min(min_distance, distance_squared(sorted_y[i], sorted_y[j]))
    
    return min_distance

def brute_force(points, low, high):
    min_distance = float('inf')
    for i in range(low, high):
        for j in range(i+1, high+1):
            min_distance = min(min_distance, distance_squared(points[i], points[j]))
    return min_distance

def closest_pair(points, low, high):
    if high - low <= 3:
        return brute_force(points, low, high)
    
    mid = (low + high) // 2
    d1 = closest_pair(points, low, mid)
    d2 = closest_pair(points, mid+1, high)
    d = min(d1, d2)
    ds = strip_distance(points, low, mid, high, d)
    
    return min(d, ds)

if __name__ == '__main__':
    input_n = int(input())
    input_points = [Point(*map(int, input().split())) for _ in range(input_n)]

    print("{0:.9f}".format(sqrt(closest_pair(input_points, 0, len(input_points)-1))))

from collections import namedtuple
from math import sqrt

Point = namedtuple('Point', 'x y')

def DistanceSquared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2

def StripDistance(points,low,mid,high,d):
    mid_point = points[mid]
    strip = []
    for i in range(low,high+1):
        if (points[i].x-mid_point.x)**2<d:
            strip.append(points[i])
    sorted_y = sorted(strip, key=lambda x: x[1])
    if len(sorted_y)<=1:
        return d
    ds = DistanceSquared(sorted_y[0], sorted_y[1])
    for i in range(len(strip)):
        for j in range(i+1,len(strip)):
            ds_temp = DistanceSquared(sorted_y[i], sorted_y[j])
            ds = min(ds_temp,ds)
            if j-i==3: break
    return ds

def BruteForce(points,low,high):
    min = DistanceSquared(points[low],points[low+1])
    for i in range(low,high):
        for j in range(i+1,high+1):
            if DistanceSquared(points[i],points[j])<min:
                min = DistanceSquared(points[i],points[j])
    return min


def ClosePoint(points, low, high):
    sorted_x = sorted(points, key=lambda x: x[0])
    if high-low<=2:
        return BruteForce(points,low,high)
    mid = low+(high-low)//2
    d1 = ClosePoint(sorted_x,low,mid)
    d2 = ClosePoint(sorted_x,mid,high)
    d = min(d1,d2)
    ds = StripDistance(sorted_x,low,mid,high,d)
    return min(d,ds)

if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(ClosePoint(input_points,0,len(input_points)-1))))

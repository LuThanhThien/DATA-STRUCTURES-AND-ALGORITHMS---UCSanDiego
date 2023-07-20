from collections import namedtuple
from math import sqrt



Point = namedtuple('Point', 'x y')

def DistanceSquared(first_point, second_point):
    # find square distance of two points
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2

def StripDistance(points,d):
    n = len(points)
    sorted_y = sorted(points, key=lambda x: x[1])
    ds = d
    for i in range(n):
        for j in range(i+1,n):
            if (sorted_y[j].y-sorted_y[i].y)>=ds:
                break
            ds_temp = DistanceSquared(sorted_y[i], sorted_y[j])
            ds = min(ds_temp,ds)
    return ds

def BruteForce(points,n):
    dmin = float("inf")
    for i in range(n):
        for j in range(i+1,n):
            if DistanceSquared(points[i],points[j])<dmin:
                dmin = DistanceSquared(points[i],points[j])
    return dmin


def ClosePoint(points,n):
    sorted_x = sorted(points, key=lambda x: x[0])
    if n<=3:
        return BruteForce(points,n)
    mid = n//2
    mid_point = sorted_x[mid]
    d1 = ClosePoint(sorted_x,mid)
    d2 = ClosePoint(sorted_x[mid:],n-mid)
    d = min(d1,d2)
    strip=[]
    for i in range(n):
        if abs(points[i].x-mid_point.x)<d:
            strip.append(points[i])
    ds = StripDistance(strip,d)
    return min(d,ds)


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(ClosePoint(input_points,len(input_points)))))
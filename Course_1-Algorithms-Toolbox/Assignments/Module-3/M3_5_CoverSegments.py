from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def SegmentSort(n,left,right):
    left_sort = left.copy()
    right_sort = right.copy()
    #Sort the left
    for i in range(1,n):
        left_key = left_sort[i]
        right_key = right_sort[i]
        j = i - 1
        while j>=0 and left_sort[j]>left_key:
            left_sort[j+1] = left_sort[j]
            right_sort[j+1] = right_sort[j]
            j -= 1
        left_sort[j+1] = left_key
        right_sort[j+1] = right_key
    return left_sort, right_sort

def CoverSegments(n,left,right):
    right_sort, left_sort = SegmentSort(n,right,left)
    points = []
    while len(left_sort)>0:
        i = 0
        min = right_sort[i]
        i += 1
        while  i<len(left_sort):
            if min>=left_sort[i] and min<=right_sort[i]:
                left_sort.pop(i)
                right_sort.pop(i)
            else: i+=1
        points.append(min)
        left_sort.pop(0)
        right_sort.pop(0)
    return points


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n = data[0]
    left = data[1:(2 * n + 2):2]
    right = data[2:(2 * n + 2):2]
    points = CoverSegments(n,left,right)
    print(len(points))
    print(*points)

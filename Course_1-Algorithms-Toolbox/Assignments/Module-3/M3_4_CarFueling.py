from sys import stdin

def CarFueling(d,m,stops):
    n = len(stops)
    segment = 0
    l = 0
    right = 0
    while right<=n:
        r = l + m
        if r>=d: return segment
        while right<n and stops[right]<=r:
            right +=1
        if l==stops[right-1]: break
        segment+=1
        l = stops[right-1]
    return -1

if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(CarFueling(d, m, stops))
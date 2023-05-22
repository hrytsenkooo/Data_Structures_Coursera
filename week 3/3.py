import sys

n, m = map(int, input().split())
lines = list(map(int, input().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)


def getParent(table):
    # find parent and compress path
    if table != parent[table]:
        parent[table] = getParent(parent[table])
    return parent[table]


def merge(destination, source):
    global ans
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return False

    # merge two components
    # use union by rank heuristic
    # update ans with the new maximum table size
    if rank[realDestination] < rank[realSource]:
        parent[realDestination] = realSource
        lines[realSource] += lines[realDestination]
        lines[realDestination] = 0
    else:
        parent[realSource] = realDestination
        lines[realDestination] += lines[realSource]
        lines[realSource] = 0
        if rank[realDestination] == rank[realSource]:
            rank[realDestination] += 1
    ans = max(ans, lines[realSource], lines[realDestination])
    return True


for i in range(m):
    destination, source = map(int, input().split())
    merge(destination - 1, source - 1)
    print(ans)

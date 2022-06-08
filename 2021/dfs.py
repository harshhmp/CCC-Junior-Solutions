nums = input().split(" ")
nodes = [[]]
visited = [False]

for i in range(int(nums[0])):
    nodes.append([])
    visited.append(False)

for i in range(int(nums[1])):
    road = input().split(" ")
    nodes[int(road[0])].append(int(road[1]))
    nodes[int(road[1])].append(int(road[0]))


def dfs(u, v):
    if visited[u]:
        return False
    else:
        visited[u] = True

    if u == v:
        return True

    out = False

    for i in nodes[u]:
        out = out or dfs(i, v)

        if out:
            return True

    return out


if dfs(int(nums[2]), int(nums[3])):
    print("GO SHAHIR!")
else:
    print("NO SHAHIR!")

from collections import defaultdict

def convert(a):
    adjList = defaultdict(list)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 1:
                adjList[i].append(j)
    return adjList

a =  [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 0, 1, 0, 0]
    , [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    , [0, 0, 0, 0, 0, 1, 0, 0, 1, 0]]  # adjacency matrix
AdjList = convert(a)
print("Adjacency List:")

for i in AdjList:
    print(i, end="")
    for j in AdjList[i]:
        print(" -> {}".format(j), end="")
    print()

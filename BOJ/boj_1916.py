import heapq
import sys

V = int(sys.stdin.readline())
E = int(sys.stdin.readline())

mygraph = [[] for _ in range(V+1)]
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split(' '))
    mygraph[u].append((v,w))

start, end = map(int, sys.stdin.readline().split(' '))

def dijkstra(graph, start):
    # 초기화
    distances = {node: float('inf') for node in range(1, len(graph))}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances


answer = dijkstra(mygraph, start)
print(answer[end])


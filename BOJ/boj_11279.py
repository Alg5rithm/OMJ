import heapq
import sys

n = int(input())
heap = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(heap, (-x))
    else:
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)

# 최대 힙 (Max Heap)
# - 각 노드의 키 값이 자식 노드의 키 값보 작지 않은 트리
# - 이자, 완전 이진 트리

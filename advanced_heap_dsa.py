import heapq

heap = []
heapq.heappush(heap,3)
heapq.heappush(heap,1)
heapq.heappush(heap,4)
heapq.heappush(heap,2)

print(heapq.heappop(heap))
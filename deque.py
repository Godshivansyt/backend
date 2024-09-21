from collections import deque

#  create deque
dq = deque([1,2,3,4,5,6])
# append  to th right 
dq.append(7)
print(dq)
# append to the left 
dq.appendleft(8)
print(dq)
# pop from the righgt
dq.pop()
print(dq)
#  pop from the left 
dq.popleft()
print(dq)



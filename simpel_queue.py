from collections import deque
queue = deque([1,2,3,4,5])
print('antrian sekarang:',)

queue.append(6)
print('antrian masuk:',)
print('antrian sekarang:',queue)

queue.append(7)
print('antrian masuk:',7)
print('antrian sekarang:',)

out = queue.popleft()
print('antrian keluar:',queue)
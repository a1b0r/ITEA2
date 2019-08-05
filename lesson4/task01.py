import time
N = 1000000

comp_time_start = time.time()

new_list1 = [x ** 2 for x in range(N) ]

for_time_start, comp_time_end = time.time(), time.time() - comp_time_start

new_list2 = []
for i in range(N):
    new_list2.append(i ** 2)

for_time_end = time.time() - for_time_start

print(comp_time_end)
print(for_time_end)
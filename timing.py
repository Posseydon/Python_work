import time

x = 0
while x < 1000000:
    start_iteration = time.time()

    x += 1
    #print(x)

finish_iteration = time.time()

print("Count time is while loop: " + str(finish_iteration - start_iteration))

start_iteration_for = time.time()
for item in range(1, 1000000):
    item += 1.01
    #print(item)
finish_iteration_for = time.time()

print("Count time is for loop: " + str(finish_iteration_for - start_iteration_for))

start_iteration_list = time.time()
[i * 1 for i in range(1, 1000000)]
finish_iteration_list = time.time()

print("Count time is for loop: " + str(finish_iteration_list - start_iteration_list))

start_iteration_set = time.time()

{y for y in range(1, 1000000)}

finish_iteration_set = time.time()

print("Count time is for loop: " + str(finish_iteration_set - start_iteration_set))


start_iteration_dict = time.time()
letters = ['a', 'b', 'c']
{a : b for a in letters for b in range(1, 1000000)}

finish_iteration_dict = time.time()

print("Count time is for loop: " + str(finish_iteration_dict - start_iteration_dict))

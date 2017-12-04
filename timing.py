import time

x = 0
start_iteration = time.time()
def func_whileloop(x):
    while x < 1000000:
        x += 1

finish_iteration = time.time()

print("Count time: " + str(finish_iteration - start_iteration))

start_iteration_for = time.time()
def func_forloop():
    for item in range(1, 1000000):
        pass
finish_iteration_for = time.time()

print("Count time: " + str(finish_iteration_for - start_iteration_for))

start_iteration_list = time.time()
def func_iterlist():
    [i for i in range(1, 1000000)]
finish_iteration_list = time.time()

print("Count time: " + str(finish_iteration_list - start_iteration_list))

start_iteration_set = time.time()

def func_iterset():
    {y for y in range(1, 1000000)}

finish_iteration_set = time.time()

print("Count time: " + str(finish_iteration_set - start_iteration_set))


start_iteration_dict = time.time()
def func_iterdict():
    {n: n for n in range(1, 1000000)}

finish_iteration_dict = time.time()

print("Count time: " + str(finish_iteration_dict - start_iteration_dict))

func_whileloop(0)
func_forloop()
func_iterlist()
func_iterset()
func_iterdict()

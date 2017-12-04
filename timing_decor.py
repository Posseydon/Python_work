import time

def timing_decor(func):
    def wrapper(*args):
        start_iteration = time.time()
        func(*args)
        finish_iteration = time.time()

        print("Fuction execution time is:%2.2f " % (finish_iteration - start_iteration))

    return wrapper

@timing_decor
def func_whileloop(x):
    while x < 1000000:
        x += 1



@timing_decor
def func_forloop():
    for item in range(1, 1000000):

        pass


@timing_decor
def func_iterlist():

    [i for i in range(1, 1000000)]


@timing_decor
def func_iterset():

    {y for y in range(1, 1000000)}


@timing_decor
def func_iterdict():

    {n: n for n in range(1, 1000000)}

func_whileloop(0)
func_forloop()
func_iterlist()
func_iterset()
func_iterdict()

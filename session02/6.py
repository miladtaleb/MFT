import timeit
lst1 = list(range(10))
exec_1 = 'list(map(lambda x: x*x, ' + str(lst1) + '))'
exec_2 = '[x*x for x in ' + str(lst1) + ']'
time_1 = timeit.timeit(exec_1, number=10000)
time_2 = timeit.timeit(exec_2, number=10000)
print("When inputs are 10 items:")
print("Latency (s) map function:\t" + str(time_1))
print("Latency (s) list comprehension:\t" + str(time_2))

lst2 = list(range(10000))
exec_1 = 'list(map(lambda x: x*x, ' + str(lst2) + '))'
exec_2 = '[x*x for x in ' + str(lst2) + ']'
time_1 = timeit.timeit(exec_1, number=10000)
time_2 = timeit.timeit(exec_2, number=10000)
print("When inputs are 10000 items:")
print("Latency (s) map function:\t" + str(time_1))
print("Latency (s) list comprehension:\t" + str(time_2))
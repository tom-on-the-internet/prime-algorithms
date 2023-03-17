# Import time module
import time

count = 1000000
my_list = []
# record start time
start = time.time()

for i in range(count):
    print(i)
    my_list.append(0)
    # my_list.insert(0, 0)

# record end time
end = time.time()

# print the difference between start
# and end time in milli. secs
print("The time of execution of above program is :", (end - start) * 10**3, "ms")

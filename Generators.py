Generators:
# Basically generators are used to improve the performance and save memory space
# let me explain with one small examples, i have 100 numbers and i want addition of all those numbers, if your write general addition example
# i will give you the result but all these addition calculations are done in memory.Here one important thing is if you don't have any internal
# memory to calculate or very less memory then you will not get output. To over come memory issue we will use generators, it will calculate all the
# don't keep value until for next value adding into existing value.

# let me explain in another way:
# for example you have large data file(example 10 millions of records) in file and you want to count it. example, If we use regular code to count it will take
#     10MB and these count are done in internal memory, but if you use generators i will take only 2 MB of memory
# next methods to get next value calling it explicitly.
#You have large data file but less memory, to do calcualtion with less memory we will use generators:
# Regular code:
def add_numbers(numbers):
    for i in numbers:
        print(i+i)

input=add_numbers([1,2,3,4,5,6])
print(next(input))

#Ex-1:(yield)
def add_numbers(numbers):
    for i in numbers:
        yield(i+i)

input=add_numbers([1,2,3,4,5,6])
print(next(input))

#Ex-2:
def file_read_m(input_file_path):
    file_open=open(input_file_path, 'r')
    read=file_open.readlines()
    for i in read:
        yield i
input_pass=file_read_m('/Users/raj/Documents/Pycharm_Pythoncode/Data_set/cursor_file.txt')
print(next(input_pass))

# 7-modulo-fizzbuzz-01.py

# we make an empty list to store all the numbers
fizzbuzz_list = []
# a initial variable to add the numbers
numbers = 0

# we will loop the list 100 times
for one_to_a_hundred_range in range(100):
    # we will be adding
    numbers = numbers + 1
    fizzbuzz_list.append(numbers)

'''
# print to see if it's working:
for number in fizzbuzz_list[:100]:
    print(number)

print("...")
'''

for number in fizzbuzz_list:
    if number % 3 == 0 and number % 5 == 0:
        print(str(number) + "\tFIZZBUZZ!!!!")
    elif number % 3 == 0:
        print(str(number) + "\tFizz")
    elif number % 5 == 0:
        print(str(number) + "\tBuzz")
    else:
        print(number)

print("...")
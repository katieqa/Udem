# list
grades_list = [77, 80, 90]
# tuple - immutable, cannot increase size
grades_tuple = (77, 80, 90)
# set of grades - unique and unordered
grades_set = {77, 80, 90}

# print avg grade list
print("list average")
print(sum(grades_list) / len(grades_list))

# add to list
grades_list.append(100)
print("grades list")
print(grades_list)

# add to tuple by creating a new tuple
print("grades tuple")
grades_tuple = grades_tuple + (100,)  # must have comma
print(grades_tuple)

print("grades set")
print(grades_set)  # will not print duplicates, only unique values

# change item in a list
print(grades_list[0])
grades_list[0] = 60
print(grades_list)

# add to set
grades_set.add(60)
print(grades_set)

## advanced set operations

your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}

print(your_lottery_numbers.intersection(winning_numbers)) #will only print values that occur in both

print(your_lottery_numbers.union((winning_numbers))) #add sets together

print({1,2,3,4}.difference({1,2})) #difference btwn two sets
print(your_lottery_numbers.difference(winning_numbers))
print(winning_numbers.difference(your_lottery_numbers))



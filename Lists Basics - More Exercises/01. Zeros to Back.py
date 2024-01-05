string_list = [int(x) for x in input().split(', ')]

count_zero = [0 for i in range(string_list.count(0))]
numbers_list = [i for i in string_list if i != 0]

print(numbers_list + count_zero)

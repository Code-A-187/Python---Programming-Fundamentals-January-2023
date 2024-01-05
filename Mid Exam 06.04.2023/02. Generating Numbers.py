def only_digits(string):
    digit_list = []
    for el in string:
        if el.isdigit():
            digit_list.append(int(el))
    return digit_list


integers_list = [int(x) for x in input().split()]

data = input()

while data != 'END':
    if 'add to start' in data:
        integers_list[:0] = only_digits(data)
    elif 'remove greater than' in data:
        num = data.split()
        number = int(num[3])
        integers_list[:] = [x for x in integers_list if x <= 5]
    elif 'replace' in data:
        data = data.split()
        value = int(data[1])
        replacement = int(data[2])
        for i in range(len(integers_list)):
            if integers_list[i] == value:
                integers_list[i] = replacement
    elif 'remove at index' in data:
        integers = only_digits(data)
        index = integers[0]
        if 0 <= index and index in range(len(integers_list)):
            integers_list.remove(integers_list[index])
    elif data == "find even":
        even_list = []
        for el in integers_list:
            if el % 2 == 0:
                even_list.append(el)
        print(' '.join(map(str, even_list)))
    elif data == 'find odd':
        odd_list = []
        for el in integers_list:
            if el % 2 != 0:
                odd_list.append(el)
        print(' '.join(map(str, odd_list)))
    data = input()

print(', '.join(map(str, integers_list)))

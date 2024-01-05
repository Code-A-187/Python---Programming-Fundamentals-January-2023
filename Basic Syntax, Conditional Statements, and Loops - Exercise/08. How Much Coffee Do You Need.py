coffee_count = 0
while True:
    string = input()
    if string == 'END':
        break
    if string == 'coding' or string == "dog" or string == 'cat' or string == 'movie':
        coffee_count += 1
    elif string == 'CODING' or string == "DOG" or string == 'CAT' or string == 'MOVIE':
        coffee_count += 2

if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)

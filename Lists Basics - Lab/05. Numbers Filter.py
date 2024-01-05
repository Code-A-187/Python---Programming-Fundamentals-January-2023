# Input
n = int(input())

numbers = []
even_list = []
odd_list = []
negative_list = []
positive_list = []

# Logic
for i in range(n):
    current_number = int(input())
    if current_number >= 0:
        positive_list.append(current_number)
    else:
        negative_list.append(current_number)
    if current_number % 2 == 0:
        even_list.append(current_number)
    else:
        odd_list.append(current_number)
# Output
command = input()
if command == "even":
    print(even_list)
elif command == "odd":
    print(odd_list)
elif command == "negative":
    print(negative_list)
elif command == "positive":
    print(positive_list)

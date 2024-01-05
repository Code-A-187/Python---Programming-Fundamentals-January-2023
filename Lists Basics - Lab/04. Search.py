# Input
n = int(input())
magic_word = input()
strings_list = []
exclusive_list = []
# Logic
for i in range(n):
    string = input()
    strings_list.append(string)

    if magic_word in string:
     exclusive_list.append(string)
# Output
print(strings_list)
print(exclusive_list)

start = ord(input())
end = ord(input())
string = input()

sum_chars = 0
for char in string:
    if start < ord(char) < end:
        sum_chars += ord(char)
print(sum_chars)

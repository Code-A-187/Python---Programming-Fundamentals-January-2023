def get_char(start, end):
    result = []
    for num in range(ord(start) + 1, ord(end)):
        result.append(chr(num))

    return result


start_char = input()
end_char = input()

print(' '.join(get_char(start_char, end_char)))

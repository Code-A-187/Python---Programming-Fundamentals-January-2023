while True:
    string = input()
    if string == 'End':
        break
    if string == "SoftUni":
        continue
    for ch in string:
        print(f'{ch}{ch}', end='')
    print()

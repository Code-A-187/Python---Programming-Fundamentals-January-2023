seq_integers = [int(x) for x in input().split()]

average = sum(seq_integers) / len(seq_integers)

result = []

for i in seq_integers:
    if i > average:
        result.append(i)

if len(result) == 0:
    print(f'No')
else:
    descented_list = sorted(result, reverse=True)
    sliced_list = descented_list[:5]
    print(' '.join(map(str, sliced_list)))

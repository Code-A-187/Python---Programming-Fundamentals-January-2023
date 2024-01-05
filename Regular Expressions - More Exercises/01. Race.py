import re

runners_list = [x for x in input().split(', ')]

runners_dict = {}

pattern_names = r"[A-Za-z]"
pattern_nums = r"\d"
data = input()

while data != 'end of race':
    name = ''.join(re.findall(pattern_names, data))
    number = re.findall(pattern_nums, data)
    if name in runners_list:
        if name not in runners_dict:
            runners_dict[name] = sum(int(x) for x in number)
        else:
            runners_dict[name] += sum(int(x) for x in number)
    data = input()
# сортиране по число от горе-надолу(descending)
sorted_runners = sorted(runners_dict.items(), key=lambda x: -x[1])

print(f'1st place: {sorted_runners[0][0]}\n2nd place: {sorted_runners[1][0]}\n3rd place: {sorted_runners[2][0]}')

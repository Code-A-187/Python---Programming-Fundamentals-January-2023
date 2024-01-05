
offers_list = input().split(", ")

count_of_beggars = int(input())

result = [0] * count_of_beggars

for idx in range(len(offers_list)):
    beggar_idx = idx % count_of_beggars
    num = int(offers_list[idx])
    result[beggar_idx] += num

print(result)

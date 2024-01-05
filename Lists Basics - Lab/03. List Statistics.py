# Input
n = int(input())
count_positives = []
sum_negatives = []
# Logic
for _ in range(n):
    nums = int(input())
    if nums >= 0:
        count_positives.append(nums)
    else:
        sum_negatives.append(nums)
# Output
print(count_positives)
print(sum_negatives)
print(f"Count of positives: {len(count_positives)}")
print(f"Sum of negatives: {sum(sum_negatives)}")

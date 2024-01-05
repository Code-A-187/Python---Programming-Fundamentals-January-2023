deck = input().split()
shuffles = int(input())

for _ in range(shuffles):
    first_half = []
    second_half = []

    for idx in range(1, len(deck) - 1):
        card = deck[idx]
        if idx < len(deck) / 2:
            first_half.append(card)
        else:
            second_half.append(card)

    shuffled = []
    first_half_idx = 0
    second_half_idx = 0
    for idx in range(len(first_half) * 2):
        if idx % 2 == 0:
            shuffled.append(second_half[second_half_idx])
            second_half_idx += 1
        else:
            shuffled.append(first_half[first_half_idx])
            first_half_idx += 1

    deck = [deck[0]] + shuffled + [deck[-1]]

# Output

print(deck)

food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
guinea_weight = float(input()) * 1000


fine = True

for i in range(1, 30 + 1):
    food -= 300
    if i % 2 == 0:
        hay -= food * 0.05
    if i % 3 == 0:
        cover -= guinea_weight / 3
    if food <= 0 or hay <= 0 or cover <= 0:
        print(f'Merry must go to the pet store!')
        fine = False
        break
if fine:
    print(f'Everything is fine! Puppy is happy! Food: {food/1000:.2f}, Hay: {hay/1000:.2f}, Cover: {cover/1000:.2f}.')

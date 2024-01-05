# Input
capacity = 255
num = int(input())
tank = 0
# Logic
for i in range(num):
    water_litres = int(input())
    if tank + water_litres > capacity:
        print("Insufficient capacity!")
    else:
        tank += water_litres
print(tank)

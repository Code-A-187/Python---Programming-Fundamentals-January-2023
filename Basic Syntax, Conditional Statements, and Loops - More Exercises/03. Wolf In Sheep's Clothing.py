animals_str = input().split(', ')
animals_str.reverse()

for index, animals in enumerate(animals_str):
    if animals == "wolf" and index == 0:
        print("Please go away and stop eating my sheep")
    elif animals == "wolf":
        print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")

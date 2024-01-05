waiting_people = int(input())
lift_cabins = [int(x) for x in input().split()]

for i in range(len(lift_cabins)):
    loading = min(4 - lift_cabins[i], waiting_people)
    lift_cabins[i] += loading
    waiting_people -= loading

if waiting_people > 0:
    print(f"There isn't enough space! {waiting_people} people in a queue!\n"
          f"{' '.join(map(str, lift_cabins))}")
elif len([cart for cart in lift_cabins if cart < 4]) > 0:
    print(f"The lift has empty spots!\n"
          f"{' '.join(map(str, lift_cabins))}")
elif waiting_people == 0 and len([cart for cart in lift_cabins if cart < 4]) == 0:
    print(f"{' '.join(map(str, lift_cabins))}")

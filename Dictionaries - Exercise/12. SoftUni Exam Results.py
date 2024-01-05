# Input

name_by_language = {}
points_by_name = {}

# Logic
while True:
    line = input()
    if line == "exam finished":
        break

    if "banned" not in line:
        args = line.split("-")
        name = args[0]
        language = args[1]
        points = args[2]

        if language not in name_by_language:
            name_by_language[language] = []

        name_by_language[language].append(name)

        if name not in points_by_name:
            points_by_name[name] = []

        points_by_name[name].append(points)

    else:
        args = line.split("-")
        name = args[0]
        command = args[1]

        points_by_name.pop(name)

# Output

print("Results:")
for name, points in points_by_name.items():
    print(f"{name} | {max(points)}")

print("Submissions:")
for language, name in name_by_language.items():
    print(f"{language} - {len(name)}")
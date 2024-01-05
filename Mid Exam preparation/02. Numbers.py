list_num = input().split()

while True:
    end = input()
    if end == "Finish":
        break
    else:
        command = end.split()
    if "Add" in command:
        list_num.append(command[1])
    elif "Remove" in command:
        list_num.remove(command[1])
    elif "Replace" in command:
        for i in range(len(list_num)):
            if list_num[i] == command[1]:
                list_num[i] = command[2]
                break
    elif "Collapse" in command:
        for i in range(len(list_num)):
            if int(list_num[i]) < int(command[1]):
                None

print(*list_num, sep=" ")

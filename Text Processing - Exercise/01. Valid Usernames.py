from string import ascii_letters, digits
# Input
usernames = input().split(", ")

allowed_chars = ascii_letters + digits + "-" + "_"

# Logic
for username in usernames:
    if len(username) < 3 or len(username) > 16:
        continue

    contains_forbidden_char = False
    for char in username:
        if char not in allowed_chars:
            contains_forbidden_char = True
            break

    if contains_forbidden_char:
        continue
# Output
    print(username)

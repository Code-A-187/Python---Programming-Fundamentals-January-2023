from string import ascii_letters, digits
# Input
usernames = input().split(", ")

allowed_chars = ascii_letters + digits + "-" + "_"

# Logic
for username in usernames:
    if len(username) < 3 or len(username) > 16:
        continue

    contains_allowed_char = all([char in allowed_chars for char in username])
    if not contains_allowed_char:
        continue
# Output
    print(username)

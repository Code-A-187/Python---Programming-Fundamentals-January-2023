# Input
tail = input()
body = input()
head = input()

# Logic
meerkat = [tail, body, head]
# Output
meerkat[0], meerkat[2] = meerkat[2], meerkat[0]

print(meerkat)

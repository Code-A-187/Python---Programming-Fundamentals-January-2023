import re

text = input()

matches = re.findall(r'([=/])([A-Z][A-Za-z]{2,})\1', text)

destinations = []

for match in matches:
    destination = match[1]
    destinations.append(destination)

print(f"Destinations: {', '.join(destinations)}")

travel_points = 0

for destination in destinations:
    travel_points += len(destination)

print(f'Travel Points: {travel_points}')

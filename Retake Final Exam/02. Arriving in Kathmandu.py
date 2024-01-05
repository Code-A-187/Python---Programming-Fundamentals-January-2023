import re

data = input()
pattern = r'^(?P<name>[A-Za-z0-9\!\@\#\$\?]+)=(?P<length>[0-9]+)<<(?P<geohashcode>.*)$'
name_pattern = r'[A-Za-z0-9]'
while data != 'Last note':
    match_data = re.match(pattern, data)
    if match_data:
        data = re.finditer(pattern, data)
        for info in data:
            peak_data = info.groupdict()
            if int(peak_data['length']) == len(peak_data['geohashcode']):
                peak_name = ''.join(re.findall(name_pattern, peak_data['name']))
                print(f"Coordinates found! {peak_name} -> {peak_data['geohashcode']}")
            else:
                print(f"Nothing found!")
    else:
        print(f"Nothing found!")
    data = input()

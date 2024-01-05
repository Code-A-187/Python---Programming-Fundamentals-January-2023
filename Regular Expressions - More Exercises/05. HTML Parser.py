import re

data = input()

title_pattern = r'<title>(?P<title>[^<>]*)<\/title>'

title_patt = re.finditer(title_pattern, data)

for part in title_patt:
    extracted_title = part.groupdict()
    print(f'Title: {extracted_title["title"]}')

body_pattern = r'<body>.*<\/body>'

body_patt = ''.join(re.findall(body_pattern, data))

content_patt = r'>([^><]*)<'

body = ''.join(re.findall(content_patt, body_patt))
content = body.replace('\\n', '')

print(f'Content: {content}')


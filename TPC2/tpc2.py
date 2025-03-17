import re

file_path = 'obras.csv'

with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    file_content = ''.join(lines)


file_content_split = file_content.split(';')

pattern_nome = r'^(.*?)[;]'
pattern_apcd = r'(?<=;).+?(?=;)'
pattern_description = r';(\"[\s\S]*?\");'
pattern_id = r'([O]\d+)'

matches_nome = re.findall(pattern_nome, file_content)
print(matches_nome)


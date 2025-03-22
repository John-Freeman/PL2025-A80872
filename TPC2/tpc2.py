import re
from collections import Counter
file_path = "TPC2\obras.csv"

with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    file_content = ''.join(lines[1:])

#remover paragrafos dentro de uma coluna
paragraphless_text = re.sub(r'(\n\s{8})', '', file_content)

pattern_description = r';(\"[\s\S]*?\");'

#remove todas as descriçoes que começam e acabam com "
descriptionless_text = re.sub(pattern_description, ';', paragraphless_text)

#separa a string numa lista de listas
rows = [re.findall(r"[^;\n]+", row) for row in descriptionless_text.split("\n")]
#print(rows)

#remove quaisquer descriçao que ainda nao tenha sido removida pelos passos anteriores
for x in rows:
    if x[1].isnumeric():
        pass
    else: x.pop(1)

#lista ordenada de autores
authors = [sublist[3] for sublist in rows]
print(sorted(authors))

#numero de obras por periodo
period = [sublist[2] for sublist in rows]
print(dict(Counter(period)))

#dicionario com periodos como chave é inicializado
periodL = ['Barroco', 'Clássico', 'Medieval', 'Renascimento', 'Século XX', 'Romântico', 'Contemporâneo']
music_dict = {period: [] for period in periodL}

titles = [sublist[0] for sublist in rows]
#titulos das musicas sao associados a um periodo e colocados no dicionario
i = 0
for x in period:
    music_dict[period[i]].append(titles[i])
    i += 1
print(music_dict)

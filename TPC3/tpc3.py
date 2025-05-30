import re

#text = "# este é um ***Exemplo***"
#text = """1. *Primeiro item*
#2. **Segundo item**
#3. Terceiro item"""
text = input()
#Ordem do mais especifico ao mais generico
text = re.sub(r"^(#+)\s*(.*)", lambda m: f"<h{len(m.group(1))}>{m.group(2)}</h{len(m.group(1))}>", text)

text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)
text = re.sub(r"\*(.*?)\*", r"<i>\1</i>", text)

text = re.sub(r"[!\[](.*?)[\]][(](.*?)[)]", r'<a href="\2">"\1"</a>"', text)
text = re.sub(r"[\[](.*?)[\]][(](.*?)[)]", r'<a href="\1" alt = "\2"/>"', text)

if (bool(re.search(r"\d+.\s*(.*)", text))):
    text = re.sub(r"\d+.\s*(.*)", r"<il>\1</il>", text)
    text = f"<ol>\n{text}\n</ol>"

print(text)
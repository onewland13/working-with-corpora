from tei_reader import TeiReader
reader = TeiReader()
corpora = reader.read_file('./tei-files/Schopenhauer-1.xml') # or read_string
# print(corpora.text)

# show element attributes before the actual element text
# print(corpora.tostring(lambda x, text: str(list(a.key + '=' + a.text for a in x.attributes)) + text))
# corpora.map(lambda x, text: print(text) if isinstance(text, str) else print(''))
for attr in corpora.divisions: 
    print(attr)
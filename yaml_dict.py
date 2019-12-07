import yaml

document = """
  a: 1
  b:
    c: 3
    d: 4
"""

# print(yaml.dump(yaml.load(document)))
print((yaml.load(document, Loader=yaml.Loader)))
with open('test.yml') as dictionary:
  structure = yaml.load(dictionary)
  print(structure["Verb"])
# print(document)
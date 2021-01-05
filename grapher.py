import os

from graphviz import Graph


dot = Graph(comment='Character Linker',
            engine='neato',
            )
dot.attr(overlap='false', splines='true')
dot.node_attr.update(color='green', style='filled')
dot.node('Mario', color='red')

characters = {}

for filename in os.listdir(os.getcwd() + '/data'):
    dot.node(filename, color='lightblue2')
    with open(os.path.join(os.getcwd() + '/data', filename), 'r') as f:  # open in readonly mode
        for c in f.readlines():
            c = c.strip()
            if c == '' or c.startswith('#'):
                continue
            if c in characters:
                characters[c].append(filename)
            else:
                characters[c] = [filename]

for char, titles in characters.items():
    if len(titles) > 1:  # change this to 0 to include all characters
        for title in titles:
            dot.edge(char, title)

dot.render('test-output/output.gv', view=True)

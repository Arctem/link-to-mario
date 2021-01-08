import os

from graphviz import Digraph


dot = Digraph(comment='Character Linker',
              engine='dot',
              format='svg',
              )
dot.attr(overlap='false', splines='true')
dot.node_attr.update(color='green', style='filled')
dot.node('Mario', color='red')

characters = {}
games = {}

for filename in os.listdir(os.getcwd() + '/data'):
    games[filename] = []
    with open(os.path.join(os.getcwd() + '/data', filename), 'r') as f:  # open in readonly mode
        for c in f.readlines():
            c = c.strip()
            if c == '' or c.startswith('#'):
                continue
            games[filename].append(c)
            if c in characters:
                characters[c].append(filename)
            else:
                characters[c] = [filename]

visited = set()
seen_chars = {'Mario'}
seen_games = set()

while len(seen_chars) > 0:
    while seen_chars:
        char = seen_chars.pop()
        for game in characters[char]:
            if game not in visited:
                seen_games.add(game)
                dot.node(game, color='lightblue2')
                dot.edge(char, game)
        visited.add(char)
    while seen_games:
        game = seen_games.pop()
        for char in games[game]:
            if char not in visited:
                seen_chars.add(char)
                dot.node(char, color='green')
                dot.edge(game, char)
                visited.add(game)

dot.render('test-output/output.gv', view=True)

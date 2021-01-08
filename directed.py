import os

from graphviz import Digraph

COLOR_ORDER = ['red', 'orange', 'yellow', 'yellowgreen', 'green', 'blue', 'purple']

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
visited_this_loop = set()
seen_chars = {'Mario'}
seen_games = set()
distance = 0

while len(seen_chars) > 0:
    distance += 1
    while seen_chars:
        char = seen_chars.pop()
        for game in characters[char]:
            if game not in visited:
                seen_games.add(game)
                dot.node(game, color='lightblue2')
                dot.edge(char, game)
        visited_this_loop.add(char)
    visited = visited.union(visited_this_loop)
    visited_this_loop = set()
    while seen_games:
        game = seen_games.pop()
        for char in games[game]:
            if char not in visited:
                seen_chars.add(char)
                dot.node(char, color=COLOR_ORDER[distance])
                dot.edge(game, char)
                visited_this_loop.add(game)
    visited = visited.union(visited_this_loop)
    visited_this_loop = set()

dot.render('test-output/output.gv', view=True)

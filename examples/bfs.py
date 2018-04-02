from gvanim import Animation, render, gif

import Queue


N = ["Start", "A","B", "C", "Ziel"]
G = {N[0]:[N[1],N[2],N[3]], N[1]:[], N[2]:[N[3],N[1]], N[3]:[N[4]], N[4]:[]}
goal = N[4]

pre = dict()

def color_path(u):
    try:
        ga.highlight_edge(pre[u],u,color="magenta")
        color_path(pre[u])
    except:
        pass

ga = Animation()
for v, adj in G.items():
    for u in adj:
        ga.add_edge( v, u )
ga.next_step()

seen = { v:False for v in  N }
fringe = Queue.Queue()
fringe.put(N[0])

while not fringe.empty():
    v = fringe.get()
    color_path(v)
    if v == goal:
        ga.highlight_node( v, color = 'green' )
        break
    ga.highlight_node( v, color = 'magenta' )
    ga.next_step()
    seen[ v ] = True
    ga.highlight_node( v, color = 'red' )
    for u in G[ v ]:
        if not seen[ u ]:
            ga.highlight_node( u, color = 'blue')
            fringe.put(u)
            seen [u] = True
            pre[u] = v
    ga.next_step()



graphs = ga.graphs()
files = render( graphs, 'bfs', 'png' )
gif( files, 'bfs', 200 )
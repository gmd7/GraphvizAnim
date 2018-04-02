from gvanim import Animation, render, gif

import Queue


N = ["Start", "A","B", "C", "Ziel"]
G = {N[0]:[N[1],N[2],N[3]], N[1]:[], N[2]:[N[3],N[1]], N[3]:[N[4]], N[4]:[]}
goal = N[4]

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
    if v == goal:
        break
    ga.highlight_node( v, color = 'yellow' )
    ga.next_step()
    seen[ v ] = True
    ga.highlight_node( v, color = 'red' )
    print "   ",v,":",
    for u in G[ v ]:
        if not seen[ u ]:
            print u,
            ga.highlight_node( u, color = 'blue')
            fringe.put(u)
    print ""
    ga.next_step()

graphs = ga.graphs()
for g in graphs:
    print g
files = render( graphs, 'dfv', 'png' )
gif( files, 'dfv', 200 )
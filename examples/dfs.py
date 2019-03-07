from gvanim import Animation, render, gif, slides, addQueueState

import Queue, os


N = ["Start", "A", "B", "C", "D", "Ziel"]
G = {N[0]:[N[1],N[2],N[3]], N[1]:[N[2]], N[2]:[N[1],N[3],N[5]], N[3]:[N[4]], N[4]:[]}
start = N[0]
goal = N[5]

pre = dict()

def color_path(u, animation, path_color = "magenta"):
    try:
        animation.highlight_edge(pre[u],u,color=path_color)
        color_path(pre[u],animation)
    except:
        pass

ga = Animation()
gb = Animation()

seen = { v:False for v in  N }
fringe = Queue.LifoQueue()

queuename = ""
if isinstance( fringe, Queue.LifoQueue):
    queuename = "Stack"
elif isinstance( fringe, Queue.Queue):
    queuename = "Queue"

queueStates = []

def add_text_to_queue_states(message):
    addQueueState(queueStates, '\n' + message + '\n\n' + queuename + ': in,out <-> [ ' + " ".join(reversed(list(fringe.queue))) + " ]\n")


queueStates = []

for v, adj in G.items():
    for u in adj:
        ga.add_edge( v, u )

add_text_to_queue_states("0. Startknoten *" + start + "* auf " + queuename + " legen")

ga.next_step()
gb.next_step()


fringe.put(start)
gb.add_node(start)

ga.highlight_node( start, color = 'blue')
gb.highlight_node( start, color = 'blue')

add_text_to_queue_states("0. Startknoten *" + start + "* liegt auf " + queuename)

ga.next_step()
gb.next_step()

while not fringe.empty():
    v = fringe.get()
    color_path(v, ga)
    color_path(v, gb)
    if v == goal:
        ga.highlight_node( v, color = 'green' )
        gb.highlight_node( v, color = 'green' )

        add_text_to_queue_states("1. Knoten *" + v + "* von " + queuename + " nehmen. Zielknoten -> ENDE")

        ga.next_step()
        gb.next_step()
        break
    else:
        ga.highlight_node( v, color = 'magenta' )
        gb.highlight_node( v, color = 'magenta' )

        add_text_to_queue_states("1. Knoten *" + v + "* von " + queuename + " nehmen")

        ga.next_step()
        gb.next_step()

        seen[ v ] = True

        ga.highlight_node( v, color = 'red' )
        gb.highlight_node( v, color = 'red' )

        color_path(v, ga)
        color_path(v, gb)

        add_text_to_queue_states("2. Knoten *" + v + "* ist kein Zielknoten")

        ga.next_step()
        gb.next_step()


        for u in G[ v ]:
            if not seen[ u ]:
                gb.add_node(u)
                gb.add_edge(v, u)

                ga.highlight_node( u, color = 'blue')
                gb.highlight_node( u, color = 'blue')

                fringe.put(u)
                pre[u] = v

        color_path(v, ga)
        color_path(v, gb)

        add_text_to_queue_states( "3. Kindknoten von *" + v + "* auf " + queuename + " legen.")

        ga.next_step()
        gb.next_step()



graphs_a = ga.graphs("circo")
files1 = render( graphs_a, os.path.basename(__file__)[:-3]+'_graph', 'svg' )

graphs_b = gb.graphs("dot")
files2 = render( graphs_b, os.path.basename(__file__)[:-3]+'_tree', 'svg' )

slides( files1, files2, queueStates, os.path.basename(__file__)[:-3] )
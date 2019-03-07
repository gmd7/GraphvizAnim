import gvanim
from gvanim.animation import Animation
from gvanim.render import render, gif, slides, addQueueState

import Queue, os

# Wege Statt Zustande der QueueStack, Doppelte Knoten vom Stak entfernen und im Baum markieren
#

#G = {N[0]:[N[1],N[2],N[3]], N[1]:[N[2]], N[2]:[N[1],N[3],N[5]], N[3]:[N[4]], N[4]:[]}
#N = ["Start", "A", "B", "C", "Ziel"]
#goal = N[4]
#G = {N[0]:[(3,N[1]),(6,N[2]),(2,N[3])], N[1]:[(2,N[2])], N[2]:[(3,N[1]),(1,N[3]),(4,N[5])], N[3]:[(4,N[4])], N[4]:[]}
#N = ["Start", "A", "B", "C", "D", "Ziel"]
#G = {N[0]:[N[1],N[3]], N[3]:[N[2]], N[2]:[N[1],N[3],N[5]], N[1]:[N[4]], N[4]:[N[6]],N[5]:[N[1],N[4]],N[6]:[N[1],N[7]]}
#N = ["Start", "A", "B", "C", "D", "E", "F", "Ziel"]
#goal = N[7]

# s = "Start"
# a=s
# b = "B"
# c = "C"
# d = "D"
# e = "E"
# f = "F"
# z = "Ziel"
# N = [s,b,c,d,e,f,z]
# G = {s:[b,f],b:{a,e,z},c:{d,z},d:{c,e,f},e:{a,b,d},f:{a,b,d},z:{b,c}}

s = "Start"
a=s
b = "B"
c = "C"
d = "D"
e = "E"
f = "F"
z = "Ziel"
N = [s,b,c,d,e,f,z]
G = {s:[b,d,f],b:{d},c:{z},d:{c,e},e:{s,c,f},f:{d},z:{b,c}}


start = s
goal = z

id = 1

prea = dict()
preb = dict()

def color_path(u, pre, animation, path_color = "magenta"):
    try:
        animation.highlight_edge(pre[u],u,color=path_color)
        color_path(pre[u], pre, animation)
    except:
        pass

ga = Animation()
gb = Animation()

seen = { v:False for v in  N }

fringe = Queue.LifoQueue()
#fringe = Queue.Queue()
#fringe = Queue.PriorityQueue()

def outputState():
    listseen = [k for k in seen if seen[k] == True ]
    listseen.sort()
    print (listseen, "\t", list(fringe.queue))

def getSeen():
    listseen = [k for k in seen if seen[k] == True ]
    listseen.sort()
    return listseen

queuename = ""
if isinstance( fringe, Queue.LifoQueue):
    queuename = "Stack"
    queuepre = ': in,out <-> [ '
    queuepost = " ]\n"
    basename = "search_dfs_"
elif isinstance( fringe, Queue.PriorityQueue):
    queuename = "Priority Queue"
    queuepre = ': in -> [ '
    queuepost = " ] -> out\n"
    basename = "search_ucs_"
elif isinstance( fringe, Queue.Queue):
    queuename = "Queue"
    queuepre = ': in -> [ '
    queuepost = " ] -> out\n"
    basename = "search_bfs_"

basename += str(id)

queueStates = []

def add_text_to_queue_states(message):
    addQueueState(queueStates, '\n' + message + '\n\n' + queuename + queuepre +  " ".join(reversed([n["label"] for n in list(fringe.queue)])) + queuepost+'\n\n' + "closed set: " + str( getSeen()))


queueStates = []

for v, adj in G.items():
    for u in adj:
        ga.add_edge( v, u )

add_text_to_queue_states("0. Startknoten *" + start + "* auf " + queuename + " legen")

outputState()
ga.next_step()
gb.next_step()


k=0
node = {"id":"n"+str(k), "label":start}
fringe.put(node)

gb.add_node(node["id"])
gb.label_node(node["id"],node["label"])

ga.highlight_node( node["label"], color = 'blue')
gb.highlight_node( node["id"], color = 'blue')

add_text_to_queue_states("0. Startknoten *" + start + "* liegt auf " + queuename)

outputState()

ga.next_step()
gb.next_step()

while not fringe.empty():
    v = fringe.get()
    color_path(v["label"], prea, ga)
    color_path(v["id"], preb, gb)

    if v["label"] == goal:
        ga.highlight_node( v["label"], color = 'green' )
        gb.highlight_node( v["id"], color = 'green' )

        add_text_to_queue_states("1. Knoten *" + v["label"] + "* von " + queuename + " nehmen. Zielknoten -> ENDE")

        outputState()
        ga.next_step()
        gb.next_step()
        break
    elif not seen[v["label"]]:
        ga.highlight_node( v["label"], color = 'magenta' )
        gb.highlight_node( v["id"], color = 'magenta' )

        add_text_to_queue_states("1. Knoten *" + v["label"] + "* von " + queuename + " nehmen")
        outputState()
        ga.next_step()
        gb.next_step()

        seen[ v["label"] ] = True

        ga.highlight_node( v["label"], color = 'red' )
        gb.highlight_node( v["id"], color = 'red' )

        color_path(v["label"], prea, ga)
        color_path(v["id"], preb, gb)

        add_text_to_queue_states("2. Knoten *" + v["label"] + "* ist kein Zielknoten")

        outputState()
        ga.next_step()
        gb.next_step()


        for u in G[ v["label"] ]:
            if not seen[ u ]:
                k=k+1
                node = {"id" : "n"+str(k), "label" : u}
                gb.add_node(node["id"])
                gb.label_node(node["id"], node["label"])
                gb.add_edge(v["id"], node["id"])

                ga.highlight_node( u, color = 'blue')
                gb.highlight_node( node["id"], color = 'blue')

                fringe.put(node)
                #if isinstance( fringe, Queue.Queue):
                #    seen [u] = True
                prea[node["label"]] = v["label"]
                preb[node["id"]] = v["id"]

        color_path(v["label"], ga, prea)
        color_path(v["id"], gb,preb)

        add_text_to_queue_states( "3. Kindknoten von *" + v["label"] + "* auf " + queuename + " legen.")

        outputState()
        ga.next_step()
        gb.next_step()



graphs_a = ga.graphs("circo")
files1 = render( graphs_a, basename + '_graph', 'svg' )

graphs_b = gb.graphs("dot")
files2 = render( graphs_b, basename + '_tree', 'svg' )

slides( files1, files2, queueStates, basename)

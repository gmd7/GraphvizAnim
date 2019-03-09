from queue import PriorityQueue, LifoQueue, Queue

import gvanim
from gvanim.animation import Animation
from gvanim.render import render, gif, slides, addQueueState
from queue import *
from gvanim.graph import *
import os

graph_id = 3
g = Graph()
start = g.add_new_vertex("Start", 1)
a = g.add_new_vertex("B", 2)
b = g.add_new_vertex("C", 3)
c = g.add_new_vertex("D", 4)
d = g.add_new_vertex("E", 5)
e = g.add_new_vertex("F", 6)
goal = g.add_new_vertex("Ziel", 7)
g.add_edge(Edge(start, a, 20))
g.add_edge(Edge(start, b, 10))
g.add_edge(Edge(a, c, 12))
g.add_edge(Edge(b, d, 9))
g.add_edge(Edge(c, e, 14))
g.add_edge(Edge(e, goal, 11))
g.add_edge(Edge(c, d, 11))


path = []


def color_path(path, animation, path_color="magenta"):
    for edge in path:
        try:
            animation.highlight_edge(edge, color=path_color)
        except:
            pass


graph_animation = Animation()
decision_tree_animation = Animation()

print(g.get_vertices())

seen = {v: False for v in g.get_vertices()}

# fringe = LifoQueue()
# fringe = Queue()

fringe = Queue()

def outputState():
    listseen = [k.label for k in seen if seen[k] == True]
    listseen.sort()
    # print(listseen, "\t", list(fringe.queue))


def getSeen():
    listseen = [k.label for k in seen if seen[k] == True]
    listseen.sort()
    return listseen


queuename = ""
if isinstance(fringe, LifoQueue):
    queuename = "Stack"
    queuepre = ': in,out <-> [ '
    queuepost = " ]\n"
    basename = "search_dfs_"
elif isinstance(fringe, PriorityQueue):
    queuename = "Priority Queue"
    queuepre = ': in -> [ '
    queuepost = " ] -> out\n"
    basename = "search_ucs_"
elif isinstance(fringe, Queue):
    queuename = "Queue"
    queuepre = ': in -> [ '
    queuepost = " ] -> out\n"
    basename = "search_bfs_"

basename += str(graph_id)

queueStates = []


def add_text_to_queue_states(message):
    addQueueState(queueStates, '\n' + message + '\n\n' + queuename + queuepre + " ".join(
        reversed([n.label for n in list(fringe.queue)])) + queuepost + '\n\n' + "besucht: " + str(getSeen()))


queueStates = []

for v in g.edges.keys():
    for e in g.edges[v]:
        graph_animation.add_edge(e)

add_text_to_queue_states("0. Startknoten *" + start.label + "* auf " + queuename + " legen")

outputState()
graph_animation.next_step()

fringe.put(start)

graph_animation.add_node(start)
graph_animation.highlight_node(start, color='blue')

add_text_to_queue_states("0. Startknoten *" + start.label + "* liegt auf " + queuename)

outputState()

graph_animation.next_step()

while not fringe.empty():
    v = fringe.get()
    color_path(path, graph_animation)

    if v == goal:
        print("goal reached")
        graph_animation.highlight_node(v, color='green')
        add_text_to_queue_states("1. Knoten *" + v.label + "* von " + queuename + " nehmen. Zielknoten -> ENDE")

        outputState()
        graph_animation.next_step()
        break

    elif not seen[v]:
        print("Neighbours -> fringe")
        graph_animation.highlight_node(v, color='magenta')

        add_text_to_queue_states("1. Knoten *" + v.label + "* von " + queuename + " nehmen")
        outputState()
        graph_animation.next_step()

        seen[v] = True

        graph_animation.highlight_node(v, color='red')

        color_path(path, graph_animation)

        add_text_to_queue_states("2. Knoten *" + v.label + "* ist kein Zielknoten")

        outputState()
        graph_animation.next_step()

        for edge in g.edges[v]:
            u = edge.to
            if not seen[u]:
                graph_animation.add_node(u)
                graph_animation.add_edge(edge)

                graph_animation.highlight_node(u, color='blue')

                fringe.put(u)
                print("put neighbor on fringe")
                # if isinstance( fringe, Queue.Queue):
                #    seen [u] = True
                path.append(edge)

        color_path(path, graph_animation)

        add_text_to_queue_states("3. Kindknoten von *" + v.label + "* auf " + queuename + " legen.")

        outputState()
        graph_animation.next_step()

graphs_a = graph_animation.graphs("circo")
files1 = render(graphs_a, basename + '_graph', 'svg')

graphs_b = decision_tree_animation.graphs("dot")
files2 = render(graphs_b, basename + '_tree', 'svg')

slides(files1, files2, queueStates, basename)
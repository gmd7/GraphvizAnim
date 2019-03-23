'''
Todo:
* Edges only oneway
'''

from queue import PriorityQueue, LifoQueue, Queue

import gvanim
from gvanim.animation import Animation
from gvanim.render import render, gif, slides
from queue import *
from gvanim.graph import *
import os
import copy

def color_path(path, animation, path_color="magenta"):
    # print("start coloring path" )
    for edge in path.edges:
        print("edge he" + str(edge))
        animation.highlight_edge(edge, color=path_color)
        # try:
        #
        # except:
        #     pass

def state_table_table_row(msg, queue, closed):
    erg = "| " + msg + " | " + queue_to_string(queue) + " | " + closed_set_to_string(closed) + " |\n"
    return erg

def queue_to_string(fringe):
    erg = ""
    if fringe.empty():
        pass
    # elif isinstance(fringe, PriorityQueue):
    #     l= [str(n) for n,w in list(fringe.queue)]
    #     erg = ", ".join(reversed(l))
    else:
        l = [str(n) for n, w in list(fringe.queue)]
        erg = ", ".join(reversed(l))
    return erg

def closed_set_to_string(seen):
    listseen = [k.label for k in seen if seen[k] == True]
    listseen.sort()
    return "[" + ", ".join(listseen) + "]"

def addQueueState( queue_states, message=None):
    if message != None:
        text = "\n" + message + "\n"
    else:
        text = ""
    queue_states.append( text )

def add_text_to_queue_states(queue_states, message, fringe, closed_set, queuename , queuepre, queuepost ):
    # print (message + '\n\n' + queuename + queuepre )
    # print (type(fringe))
    # print(type(queue_to_string(fringe)))
    # print("" + queue_to_string(fringe))

    addQueueState(queue_states, '\n' + message + '\n\n' + queuename + queuepre + queue_to_string(fringe) + queuepost + '\n\n' + "besucht: " + str(
        closed_set_to_string(closed_set)))

def run_search(g, graph_id,start, goal, fringe):

    graph_animation = Animation()
    decision_tree_animation = Animation()

    seen = {v: False for v in g.get_vertices()}

    queuename = ""
    basename = "search_" + str(graph_id)

    if isinstance(fringe, LifoQueue):
        queuename = "Stack"
        queuepre = ': in,out <-> [ '
        queuepost = " ]\n"
        basename += "_dfs"
    elif isinstance(fringe, PriorityQueue):
        queuename = "Priority Queue"
        queuepre = ': in -> [ '
        queuepost = " ] -> out\n"
        basename += "_ucs"
    elif isinstance(fringe, Queue):
        queuename = "Queue"
        queuepre = ': in -> [ '
        queuepost = " ] -> out\n"
        basename += "_bfs"

    state_table_md  = "| Bemerkung | " + queuename + " | Menge besuchter Knoten |\n"
    state_table_md += "|---------------------------|---------------------------|------------|\n"
    state_table_md += state_table_table_row("Anfangszustand",fringe, seen)



    queueStates = []

    for v in g.edges.keys():
        for e in g.edges[v]:
            graph_animation.add_edge(e)
    msg = "0. Startknoten *" + start.label + "* auf " + queuename + " legen"
    add_text_to_queue_states(queueStates, msg, fringe, seen, queuename , queuepre, queuepost )

    # outputState()

    graph_animation.next_step()
    decision_tree_animation.next_step()

    start2 = Vertex(start.label, 999)

    paths={}

    paths['graph'] = Path(start)
    paths['tree'] = Path(start2)

    fringe.put((paths['graph'], paths['tree']))

    state_table_md += state_table_table_row(msg, fringe, seen)

    graph_animation.add_node(start)
    graph_animation.highlight_node(start, color='blue')

    decision_tree_animation.add_node(start2)
    decision_tree_animation.highlight_node(start2, color='blue')

    msg = "0. Startknoten *" + start.label + "* liegt auf " + queuename
    add_text_to_queue_states(queueStates, msg, fringe, seen, queuename , queuepre, queuepost )

    # outputState()

    graph_animation.next_step()
    decision_tree_animation.next_step()

    k=1000
    while not fringe.empty():
        paths['graph'], paths['tree'] = fringe.get()

        color_path(paths['graph'], graph_animation)
        color_path(paths['tree'], decision_tree_animation)

        v = paths['graph'].get_last_vertex()
        vtree = paths['tree'].get_last_vertex()

        # print("v: " + str(v.id) + " : " + str(type(v)))
        if v == goal:
            color_path(paths['graph'], graph_animation, path_color="green")
            color_path(paths['tree'], decision_tree_animation, path_color="green")
            graph_animation.highlight_node(v, color='green')
            decision_tree_animation.highlight_node(vtree, color='green')

            msg = "1. Pfad *" + str(paths['graph']) + "* von " + queuename + " nehmen. Ziel errreicht -> ENDE"
            add_text_to_queue_states(queueStates, msg, fringe, seen, queuename, queuepre, queuepost)
            state_table_md += state_table_table_row(msg, fringe, seen)

            graph_animation.next_step()
            decision_tree_animation.next_step()
            break

        else:
            graph_animation.highlight_node(v, color='magenta')
            decision_tree_animation.highlight_node(vtree, color='magenta')

            msg = "1. Pfad *" + str(paths['graph']) + "* von " + queuename + " nehmen"
            add_text_to_queue_states(queueStates, msg, fringe, seen, queuename, queuepre, queuepost)
            state_table_md += state_table_table_row(msg, fringe, seen)

            color_path(paths['graph'], graph_animation)
            color_path(paths['tree'], decision_tree_animation)

            graph_animation.next_step()
            decision_tree_animation.next_step()
            if not seen[v]:

                graph_animation.highlight_node(v, color='red')
                decision_tree_animation.highlight_node(vtree, color='red')

                color_path(paths['graph'], graph_animation)
                color_path(paths['tree'], decision_tree_animation)

                seen[v] = True

                msg = "2. Pfad *" + str(paths['graph']) + "* endet nicht im Zielknoten, Knoten " + str(v) + " als besucht markieren"
                add_text_to_queue_states(queueStates, msg, fringe, seen, queuename, queuepre, queuepost)
                state_table_md += state_table_table_row(msg,fringe, seen)

                graph_animation.next_step()
                decision_tree_animation.next_step()

                seen[v] = True
                if isinstance(fringe,LifoQueue):
                    edges = sorted(g.edges[v],key = lambda v: v.to.label, reverse=True)
                else:
                    edges = sorted(g.edges[v],key = lambda v: v.to.label)

                for edge in edges:
                    u = edge.to

                    k += 1
                    utree = Vertex(u.label, k)

                    edge_tree = Edge(vtree,utree,edge.weight)

                    if not seen[u]:
                        graph_animation.add_node(u)
                        graph_animation.add_edge(edge)

                        decision_tree_animation.add_node(utree)
                        decision_tree_animation.add_edge(edge_tree)

                        new_path={}

                        pg = copy.copy(paths['graph'])
                        pg.add_edge(edge)
                        new_path['graph'] = pg

                        pt = copy.copy(paths['tree'])
                        print("edge tree")
                        print(edge_tree)
                        pt.add_edge(edge_tree)
                        new_path['tree'] = pt

                        fringe.put((new_path['graph'], new_path['tree']))

                        state_table_md += state_table_table_row("3. Neuer Kindknoten: " + str(u),fringe, seen)

                        graph_animation.highlight_node(u, color='blue')
                        decision_tree_animation.highlight_node(utree,color='blue')

                color_path(paths['graph'], graph_animation)
                color_path(paths['tree'], decision_tree_animation)

                msg = "3. Pfade mit den neuen unbesuchten Kindknoten auf " + queuename + " legen."
                add_text_to_queue_states(queueStates, msg, fringe, seen, queuename, queuepre, queuepost)

                graph_animation.next_step()
                decision_tree_animation.next_step()
            else:
                graph_animation.highlight_node(v, color='magenta')
                decision_tree_animation.highlight_node(vtree, color='magenta')

                msg = "2. Knoten wurde schon besucht"
                add_text_to_queue_states(queueStates, msg, fringe, seen, queuename, queuepre, queuepost)

                color_path(paths['graph'], graph_animation)
                color_path(paths['tree'], decision_tree_animation)

                graph_animation.next_step()
                decision_tree_animation.next_step()

                graph_animation.highlight_node(v, color='red')
                decision_tree_animation.highlight_node(vtree, color='red')


    graphs_a = graph_animation.graphs("neato")
    files1 = render(graphs_a, basename + '_graph', 'svg')

    graphs_b = decision_tree_animation.graphs("dot")
    files2 = render(graphs_b, basename + '_tree', 'svg')

    slides(files1, files2, queueStates, basename, state_table_md = state_table_md)

graph_id = 1
g = Graph()
start = g.add_new_vertex("Start", 1)
a = g.add_new_vertex("B", 2)
b = g.add_new_vertex("C", 3)
c = g.add_new_vertex("D", 4)
d = g.add_new_vertex("E", 5)
e = g.add_new_vertex("F", 6)
goal = g.add_new_vertex("Ziel", 7)
g.add_edge(Edge(start, a))
g.add_edge(Edge(start, b))
g.add_edge(Edge(a, c))
g.add_edge(Edge(a, b))
g.add_edge(Edge(b, d))
g.add_edge(Edge(c, e))
g.add_edge(Edge(e, goal))
g.add_edge(Edge(e, a))
g.add_edge(Edge(c, d))

fringe = Queue()
run_search(g, graph_id,start, goal, fringe)
fringe = LifoQueue()
run_search(g, graph_id,start, goal, fringe)

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
g.add_edge(Edge(a, b, 9))
g.add_edge(Edge(b, d, 9))
g.add_edge(Edge(c, e, 14))
g.add_edge(Edge(e, goal, 11))
g.add_edge(Edge(e, a, 13))
g.add_edge(Edge(c, d, 11))
fringe = PriorityQueue()
run_search(g, graph_id,start, goal, fringe)
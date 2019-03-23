class Vertex(object):
    def __init__(self, label, id):
        self.id = id
        self.label = label

    def __str__(self):
        return self.label

    def __eq__(self, other):
        return other is not None and self.id == other.id

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(id)

    def get_id(self):
        return self.id

    def get_label(self):
        return self.label

    def getNodeName(self):
        return 'n' + str(self.id)

class Edge(object):
    def __init__(self, frm, to, weight=None):
        print (str(type(frm)) + " " + str(type(to)))
        print (str(frm.label) + " " + str(to.label))
        self.frm = frm
        self.to = to
        self.weight = weight

    def __eq__(self, other):
        return other is not None and self.frm.id == other.frm.id and self.to.id == other.to.id

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if self.frm < other.frm:
            return True
        elif self.frm == other.frm:
            return self.to <= other.to
        else:
            return False

    def __hash__(self):
        return hash(str(self.frm.id) + " " + str(self.to.id))

    def __str__(self):
        return str(self.frm) + "->" + str(self.to)

    def getFrom(self):
        return self.frm

    def getTo(self):
        return self.to

    def getWeight(self):
        return self.weight


class Digraph(object):
    def __init__(self):
        self.vertices = set()
        self.edges = {}

    def add_vertex(self, v):
        self.vertices.add(v)
        if not v in self.edges.keys():
            self.edges[v]=[]

    def add_new_vertex(self, label, id):
        new_vertex = Vertex(label, id)
        self.vertices.add(new_vertex)
        if not new_vertex in self.edges.keys():
            self.edges[new_vertex]=[]
        return new_vertex

    def add_edge(self, edge):
        start = edge.frm
        self.add_vertex(start)
        self.add_vertex(edge.to)
        self.edges[start].append(edge)

    def hasVertex(self, v):
        return v in self.vertices

    def get_vertices(self):
        return self.vertices

class Path(object):
    def __init__(self,start = None):
        if start is not None:
            self.vertices = [start]
        else:
            self.vertices = []
        self.edges = []
        self.cost = 0

    def __copy__(self):
        newone = Path()
        newone.vertices = self.vertices[:]
        newone.edges = self.edges[:]
        newone.cost = self.cost
        return newone

    def __iter__(self):
        yield from self.vertices

    def __str__(self):
        if len(self.vertices) == 0:
            return ""
        else:
            erg = ""
            for v in self.vertices:
                erg += "->" + str(v)
            if self.cost > 0:
                erg += " (" + str(self.cost) + ")"
            return erg

    def __eq__(self, other):
        if other is None:
            return False
        if len(self.vertices) == len(other.vertices):
            for k in range(len(self.vertices)):
                if self.vertices[k] != other.vertices[k]:
                    return False
            return True
        else:
            return False

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.cost < other.cost

    def add_vertex(self, vertex, weight=0):
        if (len(self.vertices) > 0):
            self.edges.append(Edge(self.get_last_vertex(), vertex, weight))
        self.vertices.append(vertex)
        self.cost += weight

    def add_edge(self, edge):
        if (len(self.vertices) == 0):
            self.vertices.append(edge.frm)

        if (self.get_last_vertex() == edge.frm):
            self.edges.append(edge)
            self.vertices.append(edge.to)
            if not edge.weight is None:
                self.cost += edge.weight

    def get_last_vertex(self):
        return self.vertices[-1]

    def get_next_to_last_vertex(self):
        return self.vertices[-2]

    def getCost(self):
        return self.cost

class Graph(Digraph):
    def add_edge(self, edge):
        super().add_edge(edge)
        self.edges[edge.to].append(Edge(edge.to,edge.frm, edge.weight))
        print("ll")
class Vertex:
    def __init__(self, label, id):
        self.id = id
        self.label = label

    def __str__(self):
        return str(self.id) + "L" + self.label

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(id)

    def get_id(self):
        return self.id

    def get_label(self):
        return self.label


class Edge:
    def __init__(self, frm, to, weight=None):
        self.frm = frm
        self.to = to
        self.weight = weight

    def __eq__(self, other):
        return self.frm.id == other.frm.id and self.to.id == other.to.id

    def __ne__(self, other):
        return not self == other

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


class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = {}

    def add_vertex(self, v):
        self.vertices.add(v)
        if not v in self.edges:
            self.edges[v]=[]

    def add_new_vertex(self, label, id):
        new_vertex = Vertex(label, id)
        self.vertices.add(new_vertex)
        if not new_vertex in self.edges:
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

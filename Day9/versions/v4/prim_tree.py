# A Tree Object for Prim's Algorithm
class Vertex(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Vertex>: ' + self.name

    def set_name(self, name):
        self.name = name


class Graph(object):
    def __init__(self, name):
        self.name = name
        self.vertices = {}
            
    def __repr__(self):
        return '<Tree> ' + self.name

    def __str__(self):
        string = []
        
        string.append('Graph: ' + self.name)
        string.append('-------------------------')
        for name, info in self.vertices.items():
            string.append('{} connectes to:'.format(name))
            for neighbor, cost in info[1].items():
                string.append('--> {} (Cost: {})'.format(neighbor, cost))

        return '\n'.join(string)

    def __contains__(self, v_name):
        return v_name in self.vertices

    def rename(self, name):
        self.name = name

    def add_vertex(self, vertex):
        if vertex not in self:
            self.vertices[vertex.name] = [vertex, {}]

    def find(self, vertex_name):
        try:
            return self.vertices[vertex_name][0]
        except KeyError:
            return None

class Tree(object):    
    def __init__(self, name):
        self.name = name
        self.vertices = {}
        self.edges = {}
        self.cost = 0
            
    def __repr__(self):
        return '<Tree> ' + self.name

    def __str__(self):
        if len(self.edges) > 0:
            string = []
            for e in self.edges.values():
                string.append('{} --({})--> {}'.format(e[0], e[2], e[1]))
            string.append('Total Cost: {}'.format(self.cost))
            return '\n'.join(string)
        return '{} is empty.'.format(self.name)

    def rename(self, name):
        self.name = name

    def add_vertex(self, vertex):
        self.vertices[vertex.name] = vertex

    def add_edge(self, v1, v2, cost):
        self.edges[len(self.edges)] = (v1.name, v2.name, cost)
        self.cost += cost

    def __contains__(self, vertex_name):
        for x in self.vertices.values():
            if x[0].name == vertex_name:
                return True
        return False

    def find(self, vertex_name):
        try:
            return [x for x in self.vertices.values() if x[0].name == vertex_name][0]
        except IndexError:
            return None

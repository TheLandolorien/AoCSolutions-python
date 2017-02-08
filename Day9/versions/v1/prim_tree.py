# A Tree Object for Prim's Algorithm

class Vertex(object):
    def __init__(self, name, tree=None):
        self.name = name
        self.siblings = {}
        self.tree = tree

    def __repr__(self):
        return '<Vertex> ' + self.name

    def set_name(self, name):
        self.name = name

    def add_sibling(self, sibling, weight):
        self.siblings[sibling.name] = weight
        sibling.siblings[self.name] = weight
        
        try:
            self.tree.add_vertex(sibling)
            self.tree.add_edge(self, sibling, weight)
        except AttributeError:
            print 'You must add <Vertex> {} to a tree before adding a sibling.'.format(self.name)
            raise

    def set_tree(self, tree):
        self.tree = tree


class Tree(object):    
    def __init__(self, name, root=None):
        self.name = name
        self.vertices = {}
        self.edges = {}
        if root:
            self.add_vertex(root)

    def __str__(self):
        return '\n'.join(['{} to {}: {}'.format(x.split('_')[0], x.split('_')[1], self.edges[x][0]) for x in self.edges if self.edges[x][1]])
            
    def __repr__(self):
        return '<Tree> ' + self.name

    def rename(self, name):
        self.name = name

    def set_root(self, root):
        self.vertices[0] = root
        root.set_tree(self)

    def add_vertex(self, vertex):
        if not self.contains(vertex):
            self.vertices[len(self.vertices)] = vertex
        vertex.set_tree(self)

    def add_edge(self, v1, v2, weight):
        edge_name = '{}_{}'.format(v1.name, v2.name)
        alt_edge_name = '{}_{}'.format(v2.name, v1.name)
        self.edges[edge_name] = (weight, True)
        self.edges[alt_edge_name] = (weight, False)

    def contains(self, vertex):
        return vertex in self.vertices.values()

    def find(self, vertex_name):
        try:
            return [x for x in self.vertices.values() if x.name == vertex_name][0]
        except IndexError:
            return None

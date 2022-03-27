class Vertex:
    def __init__(self, value):
        self.value = value
        self.__neighbours = []

    def getNeighbours(self):
        '''
        Returns a list of neighbour Vertex objects.
        '''
        return self.__neighbours

    def getNeighboursName(self):
        '''
        Returns a list of neighbour Vertex values.
        '''
        return [vertex.value for vertex in self.__neighbours]

    def addNeighbour(self, vertex):
        if not isinstance(vertex, Vertex):
            vertex = Vertex(vertex)
        self.__neighbours.append(vertex)


    def __str__(self):
        return f'Vertex: {self.value}, Neighbours: {self.__neighbours}'
        
    def __repr__(self):
        return f'<Vertex Object> value: {self.value}, neighboursList: {self.__neighbours}'


class Edge:
    def __init__(self, origin, destination, weight=1, bi_directional=False):
        self.__origin = origin
        self.__destination = destination
        self.__weight = weight
        self.__bi_directional = bi_directional

    def getOrigin(self):
        return self.__origin

    def setOrigin(self, new_origin):
        self.__origin = new_origin

    def getDestination(self):
        return self.__destination

    def setDestination(self, new_destination):
        self.__destination = new_destination

    def getWeight(self):
        return self.__weight

    def setWeight(self, new_weight):
        self.__weight = new_weight

    def getBiDirectional(self):
        return self.__bi_directional

    def setBiDirectional(self, new_bi_directional):
        self.__bi_directional =  new_bi_directional

    def __str__(self):
        return f'''Edge: Weight: {self.__weight}
Origin: {self.__origin}
Destination: {self.__destination}
Bi_Directional: {self.__bi_directional}'''

    def __repr__(self):
        return f'''<Edge Object> {self.__origin=}, {self.__destination=}, {self.__weight=}, {self.__bi_directional}'''


class Graph:
    def __init__(self, *args, **kwargs):
        self.__vertices = [Vertex(value) for value in args]
        self.__order = len(args)
        self.__size = 0

    def getSize(self):
        return self.__size

    def setSize(self, new_size):
        self.__size = new_size

    def getOrder(self):
        return self.__order

    def setOrder(self, new_order):
        self.__order = new_order

    def getVertices(self):
        '''
        Returns a list of Vertex objects.
        '''
        return self.__vertices

    def getVertexValues(self):
        '''
        Returns a list of Vertex values.
        '''
        return [vertex.value for vertex in self.__vertices]

    def getVertexByValue(self, value):
        for vertex in self.__vertices:
            if vertex.value == value:
                return vertex
        raise LookupError(f'{value} not in Graph vertices.')

    def addVertex(self, value):

        if value not in self.getVertexValues():
            new_vertex = Vertex(value)
            self.__vertices.append(new_vertex)
        else:
            raise NameError(f'Vertex "{value}" already exists.')
        
        self.__order += 1
        return self


    def removeVertex(self, value: str): 

        if value not in self.getVertexValues():
            raise NameError(f'Vertex "{value}" not in Graph.')

        index = self.getVertexValues().index(value)
        del self.__vertices[index]
        for vertex in self.getVertices():
            vertex_neighbours = vertex.getNeighboursName()
            if value in vertex_neighbours:
                index = vertex_neighbours.index(value)
                del vertex_neighbours[index]

        self.__size -= 1        
        return self
        

    def addEdge(self, origin: Vertex, destination: Vertex, weight: int = 1,  bi_directional: bool = False):
        
        if not isinstance(bi_directional, bool):
            raise ValueError('<bi_directional> must be True or False.')
        
        if weight != 1:
            raise NotImplementedError('Weight for Edges is under development.')
            
        if not bi_directional:

            if origin in self.getVertexValues() and destination in self.getVertexValues():
                origin_vertex = self.getVertexByValue(origin)
                destination_vertex = self.getVertexByValue(destination)

                if destination_vertex not in origin_vertex.getNeighbours():
                    origin_vertex.addNeighbour(destination_vertex)
                else:
                    raise NameError(f'{destination} is already connected to {origin}')

                if origin_vertex not in destination_vertex.getNeighbours():
                    destination_vertex.addNeighbour(origin_vertex)
                else:
                    raise NameError(f'"{origin}" is already connected to "{destination}"')

                self.__size += 1
                return self
            
            elif origin not in self.getVertexValues():
                raise LookupError(f'Vertex "{origin}" not in Graph vertices, add it first.')
            
            else:
                raise LookupError(f'Vertex "{destination}" not in Graph vertices, add it first.')
        
        else:
            raise NotImplementedError('Bi-Directional Edges is under development.')

        
    def removeEdge(self, origin, destination):
        raise NotImplementedError('Removing Edges is under development.')

    def __str__(self):
        result = 'Graph: { \n'
        for vertex in self.__vertices:
            result += f'{vertex.value}: {vertex.getNeighboursName()} \n'
        return result + '}'


graph = Graph('A', 'B', 'C')
# graph.addVertex('A')
graph.removeVertex('A')
# graph.addVertex('A')
graph.addVertex('A')
graph.addEdge('A', 'B')
# graph.addEdge('A', 'B')
# graph.removeEdge('A', 'B')


print(graph)
import matplotlib.pyplot as pyplot


class Window:
    def __init__(self, name, title, x="Time (s)"):
        self.name = name
        self.title = title
        self.xlabel = x
        self.graphs = []
        self.figure = False

    def add_graph(self, y):
        graph = Graph(y)
        self.graphs.append(graph)
        return graph

    def render(self):
        self.figure = pyplot.figure(self.name,figsize=(10,8))
        i = 0
        for graph in self.graphs:
            i += 1
            pyplot.subplot(2, 1, i)
            for line in graph.lines:
                pyplot.plot(line.x, line.y, label=line.name)
            if i == 1:
                pyplot.title(self.title)
            pyplot.legend()
            pyplot.grid(True)
        pyplot.ylabel(graph.ylabel)
        pyplot.xlabel(self.xlabel)
        pyplot.show()


class Graph:
    def __init__(self, y):
        self.ylabel = y
        self.lines = []

    def add_line(self, name):
        line = Line(name)
        self.lines.append(line)
        return line


class Line:
    def __init__(self, name):
        self.name = name
        self.x = []
        self.y = []

    def add_value(self, x, y):
        self.x.append(x)
        self.y.append(y)

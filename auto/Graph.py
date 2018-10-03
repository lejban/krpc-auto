import matplotlib.pyplot as plt


class Window:
    def __init__(self, name, title, x="Time (s)"):
        self.name = name
        self.title = title
        self.xlabel = x
        self.graphs = []
        self.figure = False

    def add_graph(self, graph):
        self.graphs.append(graph)

    def render(self):
        self.figure = plt.figure(self.name)
        i = 0
        for graph in self.graphs:
            i += 1
            plt.subplot(2, 1, i)
            plt.plot(graph.x, graph.y)
            if i == 1:
                plt.title(self.title)
            plt.ylabel(graph.ylabel)
            plt.grid(True)
        plt.xlabel(self.xlabel)
        plt.show()


class Graph:
    def __init__(self, name, y):
        self.name = name
        self.ylabel = y
        self.x = []
        self.y = []

    def add_value(self, x, y):
        self.x.append(x)
        self.y.append(y)

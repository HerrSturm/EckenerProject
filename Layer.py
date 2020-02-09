
class Layer(object):

    names = set()
    callbacks = []

    @staticmethod
    def newLayer(layer):
        l = len(Layer.names)
        Layer.names.add(layer.name)
        if len(Layer.names) > l:
            [callback(layer.name) for callback in Layer.callbacks]

    @staticmethod
    def onNewLayer(callback):
        Layer.callbacks.append(callback)

    def __init__(self, name):
        self.name = name
        Layer.newLayer(self)

    def __eq__(self, other):
        return self.name == other.name


class LayerMap:

    def __init__(self):
        self.map = dict()
        self.trackedNames = set()
        for name in Layer.names:
            self.add(name)
        Layer.onNewLayer(lambda name: self.add(name))

    def add(self, name):
        if name in self.trackedNames:
            return
        self.trackedNames.add(name)
        for tracked in self.trackedNames:
            self.map[frozenset((name, tracked))] = True

    def matches(self, name0, name1):
        if type(name0) is Layer: name0 = name0.name
        if type(name1) is Layer: name1 = name1.name
        return self.map[frozenset((name0, name1))]

    def setMatch(self, name0, name1, match):
        if type(name0) is Layer: name0 = name0.name
        if type(name1) is Layer: name1 = name1.name
        if name0 not in self.trackedNames: return
        if name1 not in self.trackedNames: return
        self.map[frozenset((name0, name1))] = match

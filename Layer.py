
class Layer(object):

    names = set()
    callbacks = []

    @staticmethod
    def newLayer(layer):
        diff = layer.names - Layer.names
        Layer.names |= layer.names
        if len(diff) > 0:
            [callback(diff) for callback in Layer.callbacks]

    @staticmethod
    def onNewLayer(callback):
        Layer.callbacks.append(callback)

    @staticmethod
    def all():
        return Layer()

    def __init__(self, *names):
        self.names = set(names)
        Layer.newLayer(self)

    def __eq__(self, other):
        return (len(self.names) == 0 or len(other.names) == 0 or
            len(self.names & other.names) > 0)


class LayerMap:

    def __init__(self):
        self.map = dict()
        self.trackedNames = set()
        for name in Layer.names:
            self.add(name)
        Layer.onNewLayer(lambda names: self.addMultiple(names))

    def add(self, name):
        if name in self.trackedNames:
            return
        self.trackedNames.add(name)
        for tracked in self.trackedNames:
            self.map[frozenset((name, tracked))] = True

    def addMultiple(self, names):
        for name in names:
            self.add(name)

    def matchesSingle(self, name0, name1):
        return self.map[frozenset((name0, name1))]

    def matches(self, layer0, layer1):
        for name0 in layer0.names:
            for name1 in layer1.names:
                if self.matchesSingle(name0, name1):
                    return True
        return False

    def setMatchSingle(self, name0, name1, match):
        if type(name0) is Layer: name0 = name0.name
        if type(name1) is Layer: name1 = name1.name
        if name0 not in self.trackedNames: return
        if name1 not in self.trackedNames: return
        self.map[frozenset((name0, name1))] = match

    def setMatch(self, layer0, layer1, match):
        for name0 in layer0.names:
            for name1 in layer1.names:
                self.setMatchSingle(name0, name1, match)


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
        for name in Layer.names:
            self.add(name)
        Layer.onNewLayer(lambda name: self.add(name))

    def add(self, name):
        for key in self.map.keys():
            self.map[key][name] = True
        self.map[name] = dict()

    def matches(self, name0, name1):
        if type(name0) is Layer: name0 = name0.name
        if type(name1) is Layer: name1 = name1.name
        if name0 not in self.map or name1 not in self.map:
            return False
        return ((name1 in self.map[name0] and self.map[name0][name1]) or
                (name0 in self.map[name1] and self.map[name1][name0]))

    def setMatch(self, name0, name1, match):
        if type(name0) is Layer: name0 = name0.name
        if type(name1) is Layer: name1 = name1.name
        if name0 not in self.map or name1 not in self.map:
            return
        if name1 in self.map[name0]:
            self.map[name0][name1] = match
            return
        if name0 in self.map[name1]:
            self.map[name1][name0] = match
            return

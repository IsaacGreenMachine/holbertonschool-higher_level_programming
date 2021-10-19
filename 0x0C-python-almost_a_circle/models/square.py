#!/usr/bin/python3
""
from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)
    
    @property
    def size(self):
        return self.width
    
    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        attributes = ["id", "size", "x", "y"]
        if args and len(args) > 0:
            for a in range(len(args)):
                setattr(self, attributes[a], args[a])
        else:
            for k in kwargs:
                if k in attributes:
                    setattr(self, k, kwargs.get(k))
    
    def to_dictionary(self):
        attributes = ["id", "size", "x", "y"]
        d = {}
        for a in attributes:
            d.update({a: getattr(self, a)})
        return d


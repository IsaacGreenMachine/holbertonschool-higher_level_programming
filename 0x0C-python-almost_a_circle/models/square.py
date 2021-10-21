#!/usr/bin/python3
"This is the module for a square class"


from models.rectangle import Rectangle


class Square(Rectangle):
    "Square is child of rectangle. width & height -> sizeXsize"
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        "returns def of square when print() or str() used"
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        "returns size (width)"
        return self.width

    @size.setter
    def size(self, size):
        "sets size based on rectangle width and height"
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        "updates attributes of this instance. compatible with kwargs and args"
        attributes = ["id", "size", "x", "y"]
        if args and len(args) > 0:
            for a in range(len(args)):
                setattr(self, attributes[a], args[a])
        else:
            for k in kwargs:
                if k in attributes:
                    setattr(self, k, kwargs.get(k))

    def to_dictionary(self):
        "returns dict representation of object instance"
        attributes = ["id", "size", "x", "y"]
        d = {}
        for a in attributes:
            d.update({a: getattr(self, a)})
        return d

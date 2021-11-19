#!/usr/bin/python3
"""This module defines class Base. Used for other shapes"""

import json
import turtle


class Base:
    """base of all classes in project. used to manage ids"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init for Base. if given id, set to id, else set id to nth object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """list of dictionaries -> json format"""
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves json format from list_objs to type.json file"""
        name = cls.__name__ + ".json"
        with open(name, "w+") as f:
            if list_objs is None or len(list_objs) == 0:
                f.write("[]")
            else:
                lst = []
                for o in list_objs:
                    lst.append(o.to_dictionary())
                f.write(cls.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """returns obj from json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates a new object from given info"""
        if cls.__name__ == "Rectangle":
            dum = cls(1, 1, 0, 0)
        if cls.__name__ == "Square":
            dum = cls(1, 0, 0)
        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        """returns object from data stored in json format in type.json file"""
        filename = cls.__name__ + ".json"
        objlist = []
        try:
            with open(filename, "r") as f:
                jsonlist = cls.from_json_string(f.read())
                for j in jsonlist:
                    objlist.append(cls.create(**j))
                return objlist
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        left = -turtle.window_width()/2 + 5
        right = turtle.window_width()/2 - 5
        top = turtle.window_height()/2 - 5
        bottom = turtle.window_height()/2 + 5
        turtle.penup()
        turtle.setpos(left, top)
        turtle.pendown()
        for r in list_rectangles:
            if turtle.xcor() + r.width >= turtle.window_width()/2 - 5:
                turtle.penup()
                turtle.setpos(left, turtle.ycor - turtle.window_height/3)
                turtle.pendown()
            for i in range(2):
                for j in range(r.width):
                    turtle.forward(1)
                turtle.right(90)
                for k in range(r.height):
                    turtle.forward(1)
                turtle.right(90)
            turtle.penup()
            turtle.forward(r.width + 10)
            turtle.pendown()
        for s in list_squares:
            if turtle.xcor() + s.width >= turtle.window_width()/2 - 5:
                turtle.penup()
                turtle.setpos(left, turtle.ycor - turtle.window_height/3)
                turtle.pendown()
            for i in range(4):
                for j in range(s.width):
                    turtle.forward(1)
                turtle.right(90)
            turtle.penup()
            turtle.forward(s.width + 10)
            turtle.pendown()

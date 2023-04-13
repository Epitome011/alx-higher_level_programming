#!/usr/bin/python3
""" Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """returns the dictionary representation of the object's instance variables"""
    return obj.__dict__

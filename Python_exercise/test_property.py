#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Duck(object):
    def __init__(self):
        self._name = None 
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    
    name = property(get_name, set_name)

class Duck2(object):
    def __init__(self):
        self._name = None
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name    
    
a = Duck2()
print a.name
a.name = "changed"
print a.name
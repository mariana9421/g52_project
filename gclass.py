# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 09:31:01 2026

@author: ritam
"""

class Gclass:
    def __init__(self):
        pass

    @classmethod
    def from_string(cls, str_data):
        str_list = str_data.split(";")
        strarg = 'cls(str_list[0]'
        for i in range(1, len(str_list)):
            strarg += ',str_list[' + str(i) + ']'
        strarg += ')'
        return eval(strarg)

    
    @classmethod
    def reset(cls):
        cls.obj = dict()
        cls.lst = list()
        cls.pos = 0
    
    
    @classmethod
    def get_id(cls, id):
        
        id = int(id)
        if id == 0:
            if len(cls.lst) == 0:
                id = 1
            else:
                id = max(cls.lst) + 1
        return id
    
    
    @classmethod
    def getlines(cls, att, value):
        return [obj.id for obj in list(cls.obj.values()) if getattr(obj, att) == value]

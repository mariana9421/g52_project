# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 09:31:47 2026

@author: ritam
"""


from gclass import Gclass
import datetime

class Category(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    
    att = ['_id', '_name', '_comments']
    
    header = 'Category'
    
    des = ['Id', 'Name', 'Comments']
    
    def __init__(self, id, name, comments):
        super().__init__()
        
     
        id = Category.get_id(id)
        self._id = id
        self._name = name
        self._comments = comments
       
        

        Category.obj[id] = self
        
      
        Category.lst.append(id)
    

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
    
 
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    

    @property
    def comments(self):
        return self._comments
    

    @comments.setter
    def comments(self, comments):
        self._comments = comments
    
  


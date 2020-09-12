# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 08:12:41 2020

@author: Dinesh
"""
class Adder:
    def setValues(self, x, y): #setter
        self.__x = x
        self.__y = y
    def calculate(self1):
        self1.__sum = self1.__x + self1.__y #self variable name can be anything
    def getSum(self): #Getter
        return self.__sum
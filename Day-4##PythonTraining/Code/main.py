# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 08:13:09 2020

@author: Dinesh
"""
from AdderProc import Adder

def main():
    adder =  Adder() #new keyword is not needed unlike other languages
    adder.setValues(5,4)
    adder.calculate()
    print(adder.getSum())

if __name__ == '__main__':
    main()
#!/usr/bin/python3
# -*- coding: utf-8 -*-
from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):
        """
        Constructor. Inicializamos las variables con las claves
        y sus atributos que seremos capaces de reconocer.
        """

        self.list = []
        self.att = {'root-layout': ['width', 'height', 'background-color'],
                    'region': ['id', 'top', 'bottom', 'left', 'right'],
                    'img': ['src', 'region', 'begin', 'dur'],
                    'audio': ['src', 'begin', 'dur'],
                    'textstream': ['src', 'region']}



    def get_tags(self):
        """imprime la list creada que contiene en cada posicion un name con la
        clave y un diccionario con los atributos"""

        return self.list

if __name__ == '__main__':

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())

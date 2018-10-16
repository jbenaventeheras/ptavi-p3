#!/usr/bin/python3
# -*- coding: utf-8 -*-
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        """
        Constructor. Inicializamos las variables con las claves
        y sus atributos que seremos capaces de reconocer.
        """

        self.listafinal = []
        self.att = {'root-layout': ['width', 'height', 'background-color'],
                    'region': ['id', 'top', 'bottom', 'left', 'right'],
                    'img': ['src', 'region', 'begin', 'dur'],
                    'audio': ['src', 'begin', 'dur'],
                    'textstream': ['src', 'region']}

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta, primer blucle
        mientras nombre pasado por paser se encuentre en archivo, entrando al
        segundo bucle para esa clave busca con get en sus atributos añadiendolo
        al dicc creado y finalmente añadiendo la clave y el dicc a list
        """

        dicc = {}
        while name in self.att:
            for att in self.att[name]:
                dicc[att] = attrs.get(att, 'elemeto inexistente')
            self.listafinal.append([name, dicc])
            break

    def get_tags(self):
        """imprime la list creada que contiene en cada posicion un name con la
        clave y un diccionario con los atributos"""
        return self.listafinal

    def imprimir_tags(self):

        for name in self.listafinal:
            print(name)


if __name__ == '__main__':

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    cHandler.get_tags()
    cHandler.imprimir_tags()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 19:33:08 2023

@author: davidysofia
"""

import matplotlib.pyplot as plt


class Minerales:  
    def __init__(self, nombre, dureza, lustre, rompimiento_por_fractura, color, composicion, sistema_cristalino, specific_gravity):  # Cambiado "specific gravity" a "specific_gravity"
        self.nombre = nombre
        self.dureza = dureza
        self.lustre = lustre
        self.rompimiento_por_fractura = rompimiento_por_fractura
        self.color = color
        self.composicion = composicion
        self.sistema_cristalino = sistema_cristalino
        self.specific_gravity = specific_gravity  
    
    def es_silicato(self):
        valor=False
        if 'Si' in self.composicion and 'O' in self.composicion :
           valor=True
        return valor
        
                
    def color_comun(self):
        figure, axes = plt.subplots()
        Drawing_colored_circle = plt.Circle(( 0.5, 0.5), 0.2, color=self.color)
        axes.set_aspect( 1 )
        axes.add_artist( Drawing_colored_circle )
        plt.title('{}'.format(self.nombre))
        plt.show()
    
    
    def densidad(self):
        densidad_agua = 1000
        densidad = densidad_agua * self.specific_gravity 

        return densidad
    
    def imprimir_consola(self):
        print("Su dureza es: " + str(self.dureza))
        print("Su tipo de rompimiento es: " + str(self.rompimiento_por_fractura))
        print("Su sistema de organización de átomos es: " + str(self.sistema_cristalino))
        
    def organizar_minerales():
    
        with open("minerales.txt") as file:

            lineas=file.readlines()
            prom_densidad=0.0
            count=0
            for linea in lineas[1:]:
                datos=linea.strip().split("\t")
                nombre, dureza, rompimiento, color, composicion,lustre, gravedad, sistema = datos
                mineral = Minerales(nombre, dureza, lustre, rompimiento, color, composicion, sistema, float(gravedad))
                if mineral.es_silicato()==True:
                    count+=1
                prom_densidad+=mineral.densidad()
            prom_densidad/=17
        return "El número silicatados de minerales en la lista es: "+ str(count)+" y la densidad promedio de los minerales es: "+str(prom_densidad)+ " kg/m^3"
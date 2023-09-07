#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 21:07:40 2023

@author: davidysofia
"""
import mineral as Min
def organizar_minerales():
    
    with open("minerales.txt") as file:

        lineas=file.readlines()
        prom_densidad=0.0
        count=0
        for linea in lineas[1:]:
            datos=linea.strip().split("\t")
            nombre, dureza, rompimiento, color, composicion,lustre, gravedad, sistema = datos
            mineral = Min.Minerales(nombre, dureza, lustre, rompimiento, color, composicion, sistema, float(gravedad))
            if mineral.es_silicato()==True:
                count+=1
            prom_densidad+=mineral.densidad()
        prom_densidad/=17
    return "El número silicatados de minerales en la lista es: "+ str(count)+" y la densidad promedio de los minerales es: "+str(prom_densidad)+ " kg/m^3"
        
       
    


    

    
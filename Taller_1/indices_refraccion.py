import numpy as num
import matplotlib.pyplot as plt
import os

def procesaryml(ruta: str)->list:
    result = []
    f =  open(ruta)
    line = f.readline()
    while line != "":
        if  line[:8] == "        " and line.strip() != "":
            result.append((line.strip().split(" ")[0],line.strip().split(" ")[1]))
        line = f.readline()
    return result


def graficar(ruta, nombre)->None:
    x = []
    y = []
    i = 0
    n = 0
    epsilon = 0 
    datos = procesaryml(ruta)
    fig,axs =plt.subplots()
    for dato in datos:
        i+=1
        n+=float(dato[1])
        x.append(float(dato[0]))
        y.append(float(dato[1]))
    n = n/i
    for valor in y:
        epsilon += num.square(valor-n)
    epsilon = num.sqrt(epsilon/i) 
    axs.plot(x,y)
    axs.set_title( "Material: "+ nombre +  ", n Promedio: " + str(round(n,2))+ ", Desviacion Estandar: " + str(round(epsilon,2)))
    axs.set_ylabel("Indice de refraccion(n)")
    axs.set_xlabel("Longitud de Onda(λ)")
    fig.savefig(ruta+".png")
    return None

##Para realizar el punto 1.4 entonces seria necesario invocar a la funcion de la siguiente forma:
#graficar("./Categoria/Plasticos Comerciales/Kapton","Kapton")
#graficar("./Categoria/Adhesivos Opticos/NOA1348","NOA1348")

def generalizacion(rutadir_padre)->None:
    for pdir in os.scandir(rutadir_padre):
        if os.path.isdir(pdir):
            for file in os.scandir(pdir):
                graficar(file.path,file.name) 
    return None
#Finalmente para realizar el punto 1.5 se debe invocar la funcion.
generalizacion("./Categoria")
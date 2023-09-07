import mineral as mn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class ExpansionTermicaMineral(mn.Minerales):
     def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv
    
     def organizar_datos(self):
         datos=pd.read_csv(self.archivo_csv)
         self.Temperatura=list(datos["celsius_temperature"])
         self.Volumen=list(datos["volume_cc"])
     def calculo_coeficiente(self):
        self.coeficiente = []
        self.organizar_datos()
        for i in range(0,len(self.Volumen)):
            if i==len(self.Volumen)-1:
                dv = self.Volumen[i] - self.Volumen[i - 1]
                dT = self.Temperatura[i] - self.Temperatura[i - 1]
            else:
                dv = self.Volumen[i + 1] - self.Volumen[i - 1]
                dT = self.Temperatura[i + 1] - self.Temperatura[i - 1]
            derivada = dv / dT
            coef_expansion = derivada / self.Volumen[i]
            self.coeficiente.append(coef_expansion)
            self.desviacion=np.std(self.coeficiente)
     def grafica_v_a(self):
         fig,axs = plt.subplots(nrows=1,ncols=2,figsize=(10,5))
         axs[0].plot(self.Temperatura, self.Volumen)
         axs[0].set_xlabel("Temperatura(ºC") 
         axs[0].set_ylabel("Volumen(cm^3)")
         axs[0].set_title("Volumen en Funcion de la Temperatura")
         axs[1].plot(self.Temperatura,self.coeficiente)
         axs[1].set_xlabel("Temperatura(ºC")
         axs[1].set_ylabel("Coeficiente(α)")
         axs[1].set_title("Coeficiente en Funcion de la Temperatura")
         return fig,axs
     
     def unir_todo(self):
         self.organizar_datos()
         self.calculo_coeficiente()
         self.grafica_v_a()
         return self.coeficiente, self.desviacion
     
        
    

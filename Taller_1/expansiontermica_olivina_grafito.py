import expansiontermicamineral as exp
import matplotlib.pyplot as plt
import os

directory = os.getcwd() +"/Taller_1/"

olivine = exp.ExpansionTermicaMineral(directory + "olivine_angel_2017.csv")
olivine.organizar_datos()
olivine.calculo_coeficiente()
fig1,axs1 = olivine.grafica_v_a()
fig1.suptitle("Olivine angel 2017")
fig1.set_size_inches(10,7)
fig1.savefig(directory + "olivine_angel_2017")


graphite = exp.ExpansionTermicaMineral(directory + "graphite_mceligot_2016.csv")
graphite.organizar_datos()
graphite.calculo_coeficiente()
fig1,axs1 = graphite.grafica_v_a()
fig1.suptitle("Graphite mceligot 2016")
fig1.set_size_inches(10,7)
fig1.savefig(directory + "graphite_mceligot_2016")

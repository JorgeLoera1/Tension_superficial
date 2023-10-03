# EQUIPO 1
# programa hecho para el calculo de la tension superficial

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

l1=22.8         # longitudes de las pipetas cm
l01=14.2
V1=1            # volumen de las pipetas
V01=0.1

alturasp1=np.empty(8)   # mediciones de alturas cm
alturasp01=np.empty(8)

d1=np.sqrt((4*V1)/(3.1415*l1))     # diametros de las pipetas en cm
d01=np.sqrt((4*V01)/(3.1415*l01))    

d1_m=(1/100)*d1  # diametros de las pipetas en m
d01_m=(1/100)*d01
print("----------------------------------------------------------------------------")
print("diametros de la pipetas de 1 ml: "+ str(d1)+" cm")       
print("diametros de la pipetas de 0.1 ml: "+ str(d01)+" cm")
print("----------------------------------------------------------------------------")

# lectura de las bases de datos de las mediciones
df1=pd.read_csv("pipeta1.txt")
df2=pd.read_csv("pipeta01.txt")
print("----------------------------------------------------------------------------")
print("TABLA PIPETA 1 ml")
print(df1)
print("----------------------------------------------------------------------------")
print("TABLA PIPETA 0.1 ml")
print(df2)
print("----------------------------------------------------------------------------")

# valores de las alturas promedio para distintas concentraciones de la pipeta 1 ml
P1M1=df1["0"]
x0_1=np.mean(P1M1)
alturasp1[0]=x0_1

P1M2=df1["0.5"]
x05_1=np.mean(P1M2)
alturasp1[1]=x05_1

P1M3=df1["1"]
x1_1=np.mean(P1M3)
alturasp1[2]=x1_1

P1M4=df1["2"]
x2_1=np.mean(P1M4)
alturasp1[3]=x2_1

P1M5=df1["3"]
x3_1=np.mean(P1M5)
alturasp1[4]=x3_1

P1M6=df1["5"]
x5_1=np.mean(P1M6)
alturasp1[5]=x5_1

P1M7=df1["10"]
x10_1=np.mean(P1M7)
alturasp1[6]=x10_1

P1M8=df1["20"]
x20_1=np.mean(P1M8)
alturasp1[7]=x20_1

print("----------------------------------------------------------------------------")
alturasp1_metros=(1/100)*alturasp1 # alturas promedios en m
print("Las alturas promedio para cada concentracion en la pipeta de 1 ml en cm son:")
print(alturasp1)   #alturas promedio para cada concentracion en metros pipeta 1 ml


# valores de las alturas promedio para distintas concentraciones de la pipeta 0.1 ml
P01M1=df2["0"]
x0_01=np.mean(P01M1)
alturasp01[0]=x0_01

P01M2=df2["0.5"]
x05_01=np.mean(P01M2)
alturasp01[1]=x05_01

P01M3=df2["1"]
x1_01=np.mean(P01M3)
alturasp01[2]=x1_01

P01M4=df2["2"]
x2_01=np.mean(P01M4)
alturasp01[3]=x2_01

P01M5=df2["3"]
x3_01=np.mean(P01M5)
alturasp01[4]=x3_01

P01M6=df2["5"]
x5_01=np.mean(P01M6)
alturasp01[5]=x5_01

P01M7=df2["10"]
x10_01=np.mean(P01M7)
alturasp01[6]=x10_01

P01M8=df2["20"]
x20_01=np.mean(P01M8)
alturasp01[7]=x20_01

print("----------------------------------------------------------------------------") 
alturasp01_metros=(1/100)*alturasp01 # alturas promedio en m
print("Las alturas promedio para cada concentracion en la pipeta de 0.1 ml en cm son:")
print(alturasp01)   #alturas promedio para cada concentracion en metros pipeta 0.1 ml
print("----------------------------------------------------------------------------")



conc=[float("0"),float("0.5"),float("1"),float("2"),float("3"),float("5"),float("10"),float("20")]   #valores de las concentraciones
g=9.8  # valor de la gravedad
masa_h2o=0.4 # masa en kg 
volumen_h2o=0.0004 # m3
rhoh2o=997  #densidad del agua en kg/m3
rhoj=910  #densidad jabon en kg/m3
floats=np.array(conc)
masaj=masa_h2o*floats*(1/100)  # masas del jabon para cada concentracion kg
volumen_j=masaj/rhoj  # volumenes del jabon

voltot=volumen_h2o+volumen_j   # volumen total del sistema para cada concentracion     

rhotot=(masa_h2o+masaj)/voltot # densidad total del sistema para cada concentracion 
print("----------------------------------------------------------------------------")
print("las masas del jabon seran en kg :   "+str(masaj))
print("----------------------------------------------------------------------------")
print("los volumenes del jabon seran en m3 :   "+str(volumen_j))  
print("----------------------------------------------------------------------------")
print("Los volumenes totales seran m3: "+str(voltot))
print("----------------------------------------------------------------------------")
print("Las densidades totales seran kg/m3: "+ str(rhotot))


# calculo de las tensiones superficiales para las pipetas
gamma1=(g*rhotot*d1_m*alturasp1_metros)/(4)    # unidades N/m
gamma01=(g*rhotot*d01_m*alturasp01_metros)/(4)

print("----------------------------------------------------------------------------")

print("Los valores de las tensiones superficiales son: ")
print("para la pipeta de 1 ml: " +str(gamma1)+" N/m")
print("para la pipeta de 0.1 ml: " +str(gamma01)+" N/m")




#  graficas alturas promedios                                                             
# para la pipeta de 1 ml y 0.1 ml
plt.scatter(conc,alturasp1, label="Pipeta 1 ml", color="r")
plt.scatter(conc,alturasp01, label="Pipeta 0.1 ml", color="b")
plt.xlabel("% de concentración")
plt.ylabel("Altura promedio [cm]")
plt.title("Altura promedio en función de la concentración")
plt.legend()
plt.grid()
plt.show()


#  graficas tension superficial 
# para la pipeta de 1 ml y 0.1 ml
plt.scatter(conc,gamma1, label="Pipeta 1 ml", color="r")
plt.scatter(conc,gamma01, label="Pipeta 0.1 ml", color="b")
plt.plot(conc,gamma1, color="gray")
plt.plot(conc,gamma01, color="gray")
plt.xlabel("% de concentración")
plt.ylabel(r"Tensión superficial $\gamma$ [N/m]" )
plt.title(r"Tensión superficial $\gamma$ en función de la concentración")
plt.legend()
plt.grid()
plt.show()

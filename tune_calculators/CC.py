# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 15:03:38 2021

@author: xaea12
"""

known_K = input("Is de procesversterking gekend? [y]/n: ")

if known_K == "y" or known_K == None:
    K = float(input("Geef de procesversterking: "))
    td = float(input("Geef de dode tijd in seconden: "))
    tau = float(input("Geef de tijdsconstante in seconden: "))
else:
    start_step = float(input("Geef de beginwaarde van de stap: "))
    eind_step = float(input("Geef de eindwaarde van de stap: "))
    span_step = float(6)
    start_PV = float(input("Geef de beginwaarde van de proces variabele: "))
    eind_PV = float(input("Geef de eindwaarde van de proces variabele: "))
    span_PV = float(1500)
    
    K = ((eind_PV - start_PV)/span_PV) / ((eind_step - start_step)/span_step)
    print("De procesversterking is: ", K)

# Cohen-Coon

typereg = input("Welke regelaar wil je ontwerpen? P, PI of PD: ")

if typereg == "P":
    Kc = 1.03/K * (tau/td + 0.34)
    print("Kc parameter is: ", round(Kc))
elif typereg == "PI":
    Kc = 0.9/K * (tau/td + 0.092)
    Ti = 3.33 * td * ((tau+0.092*td)/(tau+2.22*td))
    print("Kc parameter is: ", round(Kc))
    print("Ti parameter is: ", round(Ti))
else:
    print("Error")
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 15:50:57 2021

Automate the calculation of PID parameters using the Ziegler-Nichols Closed-Loop (Ultimate Cycle) tuning method. 

@author: xaea12
"""

Ku = float(input("Geef de ultime versterking in: "))
T = float(input("Geef de periode van de sinus in seconden: "))

# Ultimate Cycle

typereg = input("Welke regelaar wil je ontwerpen? [all], P, PI of PID: ")

if typereg == None or typereg == "all":
    Kc = Ku/2
    print("P regelaar: Kc=", Kc)
    Kc = Ku/2.2
    Ti = T/1.2
    print("PI regelaar: Kc= {}, Ti= {}".format(Kc, Ti))
    Kc = Ku/1.7
    Ti = T/2
    Td = T/8
    print("PID regelaar: Kc= {}, Ti= {} en Td = {}".format(Kc, Ti, Td))
elif typereg == "P":
    Kc = Ku/2
    print("Kc parameter is: ", Kc)
elif typereg == "PI":
    Kc = Ku/2.2
    Ti = T/1.2
    print("Kc parameter is: ", Kc)
    print("Ti parameter is: ", Ti)
elif typereg == "PID":
    Kc = Ku/1.7
    Ti = T/2
    Td = T/8
    print("Kc parameter is: ", Kc)
    print("Ti parameter is: ", Ti)
    print("Td parameter is: ", Td)
else:
    print("Error")
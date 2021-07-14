##### Libraries #####

from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual

import control as c
from control.matlab import * 

import matplotlib.pyplot as plt

import numpy as np
import ipywidgets as widgets

##### Functions #####

#  Ontwerp het proces
def ontw_proces(z0, z1, p0, p1, p2, dodet):
    s = c.TransferFunction.s
    G = (z1*s + z0) / (p2*(s**2) + p1*s + p0)
    return G
    
# Ontwerp de regelaar    
def ontw_regelaar(Kp, Ti, Td):
    s = c.TransferFunction.s
    C = Kp * (1 + (1/(Ti*s)) + (Td*s))
    return C

# Visualiseer het stapantwoord van het proces
def f(z0, z1, p0, p1, p2, dodet):
    #ontw_proces(z0, z1, p0, p1, p2, dodet)
    s = c.TransferFunction.s
    G = (z1*s + z0) / (p2*(s**2) + p1*s + p0)
    T,y = c.step_response(G)
    plt.plot(T, np.ones(len(T)),'r--')
    Tdodet = T + dodet
    plt.plot(Tdodet, y)
    plt.xlim(0,10)
    plt.ylim(0,2)
    plt.xlabel('tijd[s]')
    plt.ylabel('amplitude[-]')
    plt.title('Open lus proces stapantwoord')
    print('Transferfunctie model: ',G)
    
# Visualiseer OL met stapantwoord
def vis_sys(C,G):
    sys = C * G
    T,y = c.step_response(sys)
#     plt.figure(figsize=[20,10])
    plt.plot(T, np.ones(len(T)),'r--')
    plt.plot(T, y)
    plt.xlim(0,30)
    plt.ylim(0,max(y))
    plt.xlabel('tijd[s]')
    plt.ylabel('amplitude[-]')
    plt.title('Open lus proces stapantwoord')
    plt.show()
    print('Systeem', sys)
    
# Visualiseer afstellen OL met stapantwoord
def vis_sys_tune(z0, z1, p0, p1, p2, dodet, Kp, Ti, Td):
#     G = ontw_proces(z0.value, z1.value, p0.value, p1.value, p2.value, dodet.value) 
#     C = ontw_regelaar(Kp.value, Ti.value, Td.value)
    G = ontw_proces(z0, z1, p0, p1, p2, dodet) 
    C = ontw_regelaar(Kp, Ti, Td)
    vis_sys(C,G)
    print('Proces', G)
    print('Regelaar', C)   

# Maak een gesloten-lus systeem
def clsys(C,G,H):
    sys = c.parallel(c.series(C,G), H)
    return sys

# Analyseer het systeem
def systeemanalyse(sys):
    step(sys)
    impulse(sys)
    bode(sys)
    nyquist(sys)
    margin(sys)
    #sisotool(sys)
    return

# Geeft de procedure details weer
# def printprocedure(methode):
#     if methode == methodes[0]:
#     break

# # procedures
# class procedures:
#     """Class met stappenplannen voor verschillende afstelregels"""
#     def __init__(self):
#         self.data = []
        
#     def stp_intuitie(self):
#         txt = '''
#             Enkele vuistregels:
#             De proportionele versterking vergroten zal de stabiliteit verlagen.
#             * De error zal sneller verkleinen wanneer de integratietijd vergroot.
#             * De T_i (= integratietijd) verlagen zal de stabiliteit verlagen.
#             * De T_d (= afgeleidetijd) verhogen zal de stabiliteit verhogen.
#             * Elimineer alle componenten die onnodige fasevertraging kunnen veroorzaken, want deze hebben een groot effect op de fasemarge. Enkele voorbeelden zijn filters en versterkers.
#             * In een **cascade** systeem regelen we eerst de binnenlus en dan pas de buitenlus. De binnenlus werkt op een hogere frequentie en is vergelijkbaar met een laag-doorlaat filter.)

#             '''




#!/usr/bin/env python
# coding: utf-8

# In[2]:


from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual

import control as c
from control.matlab import * 

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

import numpy as np
import math
import ipywidgets as widgets

#  Ontwerp het proces
def ontw_proces(z0, z1, p0, p1, p2, dodet):
    s = c.TransferFunction.s
    G = (z1*s + z0) / (p2*(s**2) + p1*s + p0)
    delay = c.pade(dodet,10)
    dnum = delay[0]
    dden = delay[1]
    delay_tf = c.tf(dnum,dden)
    #join
    G = c.series(G,delay_tf)
    return G
    
def ontw_regelaar(Kp, Ti, Td):
    # Regelaar design uit parameters 
    s = c.TransferFunction.s
    C = Kp * (1 + (1/(Ti*s)) + (Td*s))
    return C

   
       
    
###########################################################
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
    sys = olsys(C,G)
    T,y = c.step_response(sys)
    plt.plot(T, np.ones(len(T)),'r--')
    plt.plot(T, y)
    plt.xlim(0,10)
    plt.ylim(0,2)
    plt.xlabel('tijd[s]')
    plt.ylabel('amplitude[-]')
    plt.title('Open lus proces stapantwoord')
    print('Systeem', sys)
    
# Visualiseer afstellen OL met stapantwoord
def vis_sys_tune(z0, z1, p0, p1, p2, dodet, Kp, Ti, Td):
#     G = ontw_proces(z0.value, z1.value, p0.value, p1.value, p2.value, dodet.value) 
#     C = ontw_regelaar(Kp.value, Ti.value, Td.value)
    G = ontw_proces(z0, z1, p0, p1, p2, dodet) 
    C = ontw_regelaar(Kp, Ti, Td)
    sys = c.series(C,G)
    T,y = c.step_response(sys)
    plt.plot(T, np.ones(len(T)),'r--')
    plt.plot(T, y)
    plt.xlim(0,10)
    plt.ylim(0,2)
    plt.xlabel('tijd[s]')
    plt.ylabel('amplitude[-]')
    plt.title('Open lus proces stapantwoord')
    print('Proces', G)
    print('Regelaar', C)
    print('Systeem', sys)    


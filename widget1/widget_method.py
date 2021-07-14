##### Libraries #####

import ipywidgets as widgets
from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual

##### Widget #####

# kies de methode waarmee je de PID wilt afstellen
methodes = ['Intuïtie', 
             'Empirische procedure',
            'Afstelkaart',
             'Transient respons Z-N', 
             'Transient respons CHR', 
             'Transient respons C-C',
             '']

choise = widgets.Select(
    options= methodes,
    rows=8,
    description='Methode:',
    disabled=False
)

choise


# PID controller
Kp = widgets.FloatSlider(description = 'Proportioneel', value=1, min=minim, max=maxim)
Ti = widgets.FloatSlider(description = 'Intergratietijd', value=1, min=0, max=100)
Td = widgets.FloatSlider(description = 'Afgeleidetijd', value=1, min=0, max=100)
print('PID regelaar versterking:')
out = widgets.interactive_output(ontw_regelaar, {'Kp': Kp, 'Ti': Ti, 'Td': Td})
widgets.HBox([widgets.VBox([Kp, Ti, Td]), out])
import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual

# Widget items

plantchoice = widgets.RadioButtons(
    options=['FOPTD','PTD','IPTD','IFOPTD','DIPTD', 'geen idee'],
    description='soorten procesmodellen: ',
    disable=False
    )

sys_response = widgets.RadioButtons(
    options=['Stapantwoord','Setpoint-tracking','Sensitiviteit verstoring','Algemene prestaties'],
    description='Plot prestatie',
    disable=False
    )
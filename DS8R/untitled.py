import sys
sys.path.append(r"C:\Users\PERLadmin\Desktop\DOREA_Task_Battery\PAL\DS8R")

from ds8r import DS8R

# create an object of the DS8R class and set parameter values.
ctl = DS8R(demand=80, pulse_width=300)

# apply parameters and trigger
ctl.run()
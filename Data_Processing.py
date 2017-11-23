import pandas as pd
import sys
import numpy as np

import pylab
import matplotlib
import matplotlib.pyplot as plt

data = pd.read_csv('Data/Position_Velocity_Torque_Measurement/Trial_1_PWM_0.5.csv')
    
def st_t_onumber(x):
    import numbers
    # if any number
    if isinstance(x,numbers.Number):
        return x
    # if non a number try convert string to float or it
    for type_ in (int, float):
        try:
            return type_(x)
        except ValueError:
            continue
            
sorted_data = [];
for i in range(len(data)):
    A = data['Angular Position,Angular Velocity,Torque'][i].split(',')
    A = [st_t_onumber(x) for x in A]
    sorted_data.append(A)            
            
t = [];      # time
x1 = [];     # angular discplacement
x2 = [];     # angular velocity
x3 = [];     # torque

for i in range(len(data)):
    t.append(sorted_data[i][0])
    x1.append(sorted_data[i][1])
    x2.append(sorted_data[i][2])
    x3.append(sorted_data[i][3])
    
# Response vs. Time
pylab.plot(t,x1,'-b', label=r'${\Theta}$ (rad)');
pylab.plot(t,x2,'r',label=r'$\dot{\Theta}$ (rad/s)');
pylab.plot(t,x3,'m',label=r'${\tau}$ (Nm)');
pylab.legend(loc='center right')
plt.xlabel('Time(ms)')
plt.ylabel('Response')
plt.title('Response vs. Time(ms)')
plt.show();

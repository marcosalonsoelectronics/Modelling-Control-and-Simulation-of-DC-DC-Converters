# -*- coding: utf-8 -*-
"""
Buck converter with current-mode control
"""
from math import pi, log10, sqrt
from control import tf, bode_plot, margin, step_response
import matplotlib.pyplot as plt
# Create Laplace variable
s = tf('s')
Vi=12; f=100e3; w= 2*pi*f
L= 100e-6; C=10e-6; rc=200e-3; R=5
m= 7e4; m1=5e4; ma=m1/2
a= (m1 - ma)/(m + ma)
wc= sqrt(12)*f; fc=wc/(2*pi)
xi= (sqrt(3)/2)*(1-a)/(1+a)
Go= R*(1 + rc*C*s)/(1 + (R+rc)*C*s)
Gi= wc**2/( s**2 + 2*xi*wc*s + wc**2)
fz= 1/(2*pi*rc*C); fp= 1/(2*pi*(R+rc)*C)
Gc=Gi*Go
print("a= ", a)
print("fc (kHz)= ", fc/1000); print("xi= ", xi)
print("fz (kHz)= ", fz/1000); print("fp (kHz)= ", fp/1000)
# Plot Plant's Bode
# Note that once Hz is true, omega_limits are in Hz
mag, phase, omega = bode_plot(Go, dB=True, Hz=True, omega_limits=(10,1e6), \
                              omega_num=100, color="blue", label="Go(s)" )  
mag, phase, omega = bode_plot(Gi, dB=True, Hz=True, omega_limits=(10,1e6), \
                              omega_num=100, color="red", label="Gi*(s)" )   
mag, phase, omega = bode_plot(Gc, dB=True, Hz=True, omega_limits=(10,1e6), \
                              omega_num=100, color="green", label="Gc(s)" )
plt.legend()
plt.savefig("Buck-current-mode.png", dpi=300)


    
'''    
i=25
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi) 
i=50
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi) 
i=75
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi) 
i=82
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
'''





















# -*- coding: utf-8 -*-
from math import pi, log10, sqrt
from control import tf, bode_plot
import matplotlib.pyplot as plt
# Buck converter data
L= 100e-6; C=10e-6; R=100; rc=0.5; rl=0.05
VB= 10; D=0.5; f=100e3
k= 2*L*f/R
# Output voltage in DCM
Vo= VB * 2/( 1 + sqrt(1 + 4*k/D**2) )
# Coefficients
ksd= D*(VB-Vo)/L/f; kso= -D**2/2/L/f; ksb= D**2/2/L/f
kdd= D*(VB-Vo)**2/L/f/Vo; kdo= D**2*(1-VB**2/Vo**2)/2/L/f; 
kdb= D**2*(VB/Vo - 1)/L/f
kd= ksd + kdd; ko= kso + kdo; kb= ksb + kdb; kt= kso*kb - ksb*ko
# Transfer functions
s = tf('s')
Gd = kd*R*( 1 + rc*C*s)/( 1-ko*R + (R+rc-ko*R*rc)*C*s )
Gb = kb*R*( 1 + rc*C*s)/( 1-ko*R + (R+rc-ko*R*rc)*C*s )
Zi =  ( 1-ko*R + (R+rc-ko*R*rc)*C*s ) / ( ksb + R*kt + ( ksb*(R+rc) + kt*R*rc  )*C*s  )
Zo = R*( 1 + rc*C*s)/( 1-ko*R + (R+rc-ko*R*rc)*C*s )
# Pole and zero frequencies
fp= (1-ko*R)/( (R+rc-ko*R*rc)*C )/2/pi
fz= 1/(2*pi*rc*C)
# Print results
print("Output Voltage= ", Vo)
print("Frequency of the pole= ", fp)
print("Frequency of the zero= ", fz)
print("")

print("Duty cycle to output voltage transfer function")
print("----------------------------------------------")
mag, phase, omega = bode_plot(Gd, dB=True, Hz=True, omega_limits=(10,1000e3), \
                              omega_num=100 )
i=20; print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=40; print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=60; print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=70; print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)

print("Audio susceptibility transfer function")
print("--------------------------------------")
mag, phase, omega = bode_plot(Gb, dB=True, Hz=True, omega_limits=(10,1000e3), \
                              omega_num=100 )
i=20; print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=40; print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=60; print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=70; print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)

print("Input impedance transfer function")
print("---------------------------------")
mag, phase, omega = bode_plot(Zi, dB=True, Hz=True, omega_limits=(10,1000e3), \
                              omega_num=100 )
i=20; print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=40; print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=60; print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=70; print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)

print("Output impedance transfer function")
print("----------------------------------")
mag, phase, omega = bode_plot(Zo, dB=True, Hz=True, omega_limits=(10,1000e3), \
                              omega_num=100 )
i=20; print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=40; print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=60; print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=70; print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)

plt.savefig("Bode.png", dpi=300)






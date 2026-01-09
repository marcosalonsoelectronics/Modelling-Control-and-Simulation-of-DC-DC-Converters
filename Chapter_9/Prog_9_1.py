from math import pi, log10, sqrt
import numpy as np
from control import tf, bode_plot, margin, step_response
import matplotlib.pyplot as plt
# Buck converter data
Vb= 10; Vo= 5; D= Vo/Vb; R= 1; f=100e3
Lo= 50e-6; Co= 10e-6; rc=0.16
# Create Laplace variable
s = tf('s')
# Transfer functions: buck converter, modulator, sensor, and plant
Gd= (Vo/D)*(1+rc*Co*s)/(Lo*Co*(1+rc/R)*s**2+(Lo/R+rc*Co)*s + 1)
# PWM modulator
Vpp=10
wc= sqrt(12)*f; fc=wc/(2*pi); xi=sqrt(3)/2
Gpwm= (1/Vpp)*wc**2/( s**2 + 2*xi*wc*s + wc**2)
G=Gd*Gpwm;
H=0.5*s/(s+1e-10); # H=0.5; Need to do this trick to represent a constant
wp=1/sqrt(Lo*Co)   # Plant cut-off frequency
# Compensator
kc=2;   # high frequency gain
wzc=wp; # frequency of the zero
C= kc*(1 + s/wzc)/(s/wzc)
# OPA-based compensator components. We choose: C2=10 nF
C2=10e-9; R2=1/(wzc*C2); R1=R2/kc
# Loop gain
T=G*H*C
# Plot Plant's Bode
# Note that one Hz is true, omega_limits are in Hz
mag, phase, omega = bode_plot(G, dB=True, Hz=True, omega_limits=(10, 500e3), \
                              omega_num=100, color="blue" , label="G(s)" )
mag, phase, omega = bode_plot(H, dB=True, Hz=True, omega_limits=(10, 500e3), \
                              omega_num=100,  color="red", label="H(s)"  )
mag, phase, omega = bode_plot(C, dB=True, Hz=True, omega_limits=(10, 500e3), \
                              omega_num=100,  color="orange", label="C(s)"   )
mag, phase, omega = bode_plot(T, dB=True, Hz=True, omega_limits=(10, 500e3), \
                              omega_num=100 ,  color="green", label="T(s)")
# Get gain margin, phase margin, and frequencies    
gm, pm, wcg, wcp = margin(T)
ax1,ax2 = plt.gcf().axes     # get subplot axes
plt.sca(ax1)                 # select magnitude plot
plt.ylim(-80,80)
plt.sca(ax2)                 # select magnitude plot
plt.ylim(-270, 45, 45)
plt.yticks(np.arange(-270, 45, 45)) 
plt.legend()
plt.savefig("example-8-10-1-modulator-effect.png", dpi=300)

print("----------------------------------------------")
print("Results: ")
print("----------------------------------------------")
print("Bandwidth frequency(kHz)= ", (wcp/(2*pi))/1000)
print("Phase margin(deg)= ", pm)
print("----------------------------------------------")
print("Compensator components: ")
print("----------------------------------------------")
print("C2(nF)= ", C2/1e-9)
print("R2 (kOhm.)= ", R2/1000)
print("R1 (kOhm.)= ", R1/1000)





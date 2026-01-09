from math import pi, log10, sqrt
import numpy as np
from control import tf, bode_plot, margin, step_response
import matplotlib.pyplot as plt
# Buck converter data
Vb= 10; Vo= 5; D= Vo/Vb; R= 1
Lo= 50e-6; Co= 10e-6; rc=0.16
# Create Laplace variable
s = tf('s')
# Transfer functions: buck converter, modulator, sensor, and plant
Gd= (Vo/D)*(1+rc*Co*s)/(Lo*Co*(1+rc/R)*s**2+(Lo/R+rc*Co)*s + 1)
Gpwm=0.1; G=Gd*Gpwm
H=0.5*s/(s+1e-10); # H=0.5; Need to do this trick to represent a constant
wp=1/sqrt(Lo*Co)   # Plant cut-off frequency
wz=1/(rc*Co)       # ESR zero frequency
# Compensator
kc=3e5;   # gain
wzc=wp; # frequency of the double zero
wpc=wz; # frequency of the double pole
C= kc*(1 + s/wzc)**2/( s*(1+s/wpc)**2 )
# OPA-based compensator components. We choose: C2=10 nF
C2=10e-9;
R3=1/(C2*wpc); R1=1/(wzc*C2) - R3; C1= 1/(R1*kc);
R2=C2*(R1+R3)/C1; C3= R3*C2/R2
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
plt.ylim(-180, 45, 45)
plt.yticks(np.arange(-180, 45, 45)) 
plt.legend()
plt.savefig("Example-8-10-2.png", dpi=300)
print("----------------------------------------------")
print("Results: ")
print("----------------------------------------------")
print("Bandwidth frequency(kHz)= ", (wcp/(2*pi))/1000)
print("Phase margin(deg)= ", pm)
print("----------------------------------------------")
print("Compensator components: ")
print("----------------------------------------------")
print("R1 (kOhm.)= ", R1/1000)
print("R2 (kOhm.)= ", R2/1000)
print("R3 (kOhm.)= ", R3/1000)
print("C1(nF)= ", C1/1e-9)
print("C2(nF)= ", C2/1e-9)
print("C3(nF)= ", C3/1e-9)




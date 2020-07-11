from uncertainties import ufloat    
import numpy as np                                    

D=ufloat(18.9*10**(-3),1.6*10**(-3))                              
ID=ufloat(2.49*10**(-3),0.14*10**(-3))                            
m=0.22289
c=ufloat(396.014,4.443)
b=ufloat(4.420,0.250)

print("I Drillachse", m*b/c)

T_kl=ufloat(1.16,0.06)
T_gr=ufloat(2.25,0.05)

print("Großer Zylinder über T", D/4/np.pi**2*T_gr**2)
print("Kleiner Zylinder über T", D/4/np.pi**2*T_kl**2)
print("Großer Zylinder über T minus I_D", D/4/np.pi**2*T_gr**2-ID)

T_ps1=ufloat(0.40,0.02)
T_ps2=ufloat(0.91,0.02)

print("Pose1 über T", D/4/np.pi**2*T_ps1**2)
print("Pose2 über T", D/4/np.pi**2*T_ps2**2)
print("Pose1 über T minus I_D", D/4/np.pi**2*T_ps1**2-ID)
print("Pose2 über T minus I_D", D/4/np.pi**2*T_ps2**2-ID)
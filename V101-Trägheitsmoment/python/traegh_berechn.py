import numpy as np
#Pose 1
#Damit ich mögliche Fehler später verifizieren kann, schreibe ich gerade ein py programm, was anhand der Geometrie 
#die Trägheitsmomente bestimmt. 

#Beine = Zylinder
l_oberb=6.0
l_unterb=7.0
r_oberb=0.9
r_unterb=0.8
a_bein=1.25
m_oberb=5.8
m_unterb=5.4

I_oberb=0.5*m_oberb*r_oberb**2+m_oberb*a_bein**2
I_unterb=0.5*m_unterb*r_unterb**2+m_unterb*a_bein**2

print("Trägheitsmoment Oberschenkel ",I_oberb)
print("Trägheitsmoment Unterschenkel ",I_unterb)

#Fuß=halber liegender Zylinder
l_fuß=4.2
r_fuß=0.7
a_fuß=a_bein
m_fuß=2.5

#    *0.5 --> weil halber Zylinder
I_fuß=0.5*m_fuß*(r_fuß**2/4+l_fuß**2/12)+m_fuß*a_fuß**2

print("Trägheitsmoment Fuß ",I_fuß)

#Becken=Zylinder
r_beck=2.0
h_beck=3.3
m_beck=15.8

I_beck=0.5*m_beck*r_beck**2

print("Trägheitsmoment Becken ",I_beck)

#Torso=Quader
b_tor=4.0
h_tor=5.0
t_tor=4.7
m_tor=35.7

I_tor=1/12*m_tor*(b_tor**2+t_tor**2)

print("Trägheitsmoment Torso ",I_tor)

#"Kugel"
r_kug=1.4
h_kug=1.8
m_kug=3.6

I_kug=(12*r_kug**2-h_kug**2)**(-1)*(m_kug/20)*(8*(12*r_kug**2+h_kug**2)*r_kug**2+3*(4*r_kug**2-h_kug**2)**2)

print("Trägheitsmoment Kugel ",I_kug)

#Kopf=Kegelstumpf
h_kop=5.0
r_oben=1.9
r_unten=1.4
m_kop=16.4

#m/I_oben entspricht m/I von dem Kegel mit r=r_oben
#m/I_unten entspricht m/I von dem Kegel mit r=r_unten
V_kop=(1/3)*np.pi*r_oben**2 *(h_kop/(r_oben-r_unten)*r_oben) -(1/3)*(h_kop*r_oben/(r_oben-r_unten)-h_kop)*np.pi*r_unten**2
V_oben=(1/3)*np.pi*r_oben**2*(h_kop*r_oben/(r_oben-r_unten))
V_unten=V_oben-V_kop
m_oben=m_kop*(V_oben/V_kop)
m_unten=m_kop*(V_unten/V_kop)

I_oben=(3/10)*m_oben*r_oben**2
I_unten=(3/10)*m_unten*r_unten**2
I_kop=I_oben-I_unten

print("Trägheitsmoment Kopf ",I_kop)

#Arme&Hände=Zylinder
a_arm=3.0
l_obar=5.5
r_obar=0.75
m_obar=3.7
l_unar=4.5
r_unar=0.75
m_unar=3.0
l_hand=3.0
r_hand=0.75
m_hand=2.0

I_obar=0.5*m_obar*r_obar**2
I_unar=0.5*m_unar*r_unar**2
I_hand=0.5*m_hand*r_hand**2

print("Trägheitsmoment Oberarm ",I_obar)
print("Trägheitsmoment Unterarm ",I_unar)
print("Trägheitsmoment Hand ",I_hand)


# Ausgabe:
# 
# Trägheitsmoment Oberschenkel  11.4115
# Trägheitsmoment Unterschenkel  10.1655
# Trägheitsmoment Fuß  5.896875
# Trägheitsmoment Becken  31.6
# Trägheitsmoment Torso  113.31775000000002
# Trägheitsmoment Kugel  4.287663905325443
# Trägheitsmoment Kopf  23.174515188335356
# Trägheitsmoment Oberarm  1.0406250000000001
# Trägheitsmoment Unterarm  0.84375
# Trägheitsmoment Hand  0.5625

#Pose 2
print("Pose2\nTrägheitsmomente von Torso, Becken, Kugel, Kopf bleiben.")

#Beine = Zylinder
l_oberb=6.0
l_unterb=7.0
r_oberb=0.9
r_unterb=0.8
m_oberb=5.8
m_unterb=5.4
a_oberb=3.8
a_unterb=10.2

I2_oberb=m_oberb*(r_oberb**2/4+l_oberb**2/12)+m_oberb*a_oberb**2
I2_unterb=m_unterb*(r_unterb**2/4+l_unterb**2/12)+m_unterb*a_unterb**2

print("Oberbein ", I2_oberb)
print("Unterbein ", I2_unterb)

#Fuß=halber liegender Zylinder
l_fuß=4.2
r_fuß=0.7
a2_fuß=14.0
m_fuß=2.5

I2_fuß=(1/4)*m_fuß*r_fuß**2+m_fuß*a_fuß**2

print("Fuß ", I2_fuß)

#Arme&Hände=Zylinder
l_obar=5.5
r_obar=0.75
m_obar=3.7
l_unar=4.5
r_unar=0.75
m_unar=3.0
l_hand=3.0
r_hand=0.75
m_hand=2.0
a_unar=10.4
a_obar=5.4
a_hand=14.2

I2_obar=m_obar*(r_obar**2/4+l_obar**2/12)+m_obar*a_obar**2
I2_unar=m_unar*(r_unar**2/4+l_unar**2/12)+m_unar*a_unar**2
I2_hand=m_hand*(r_hand**2/4+l_hand**2/12)+m_hand*a_hand**2

print("Oberarm ", I2_obar)
print("Unterarm ", I2_unar)
print("Hand ", I2_hand)
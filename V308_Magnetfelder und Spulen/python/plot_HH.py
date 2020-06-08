#irgendwas mache ich falsch...

#nein.. machst du nicht. der code ist ok. das Problem sind die tex-header.
#erst die Ursache und dann die zwei Lösungen.
#Ursache: es gibt die Datei matplotlibrc (scheinbar keine Dateiendung). das ist eine Textdatei, die matplotlib sagt, wie er was zu formatieren hat.
#bspw. kann man die Schriftgröße ändern, die Achsen dicker machen, backgroundcolor etc..
#matplotlib sucht IMMER im gleichen Ordner nach dieser Datei (matplotlibrc). wenn er sie nicht findet, nimmt er die standardeinstellungen.
#wenn doch, übernimmt er die Konfiguration in dieser Datei.
#er findet aber die in der Datei angegebene header-matplotlib.tex nicht. das ist aber quatsch, weil sie existiert.
#ich habe viel Zeit damit verbracht herauszufinden, warum er die nicht findet, aber das ist echt fummelig und unübersichtlich..
#letztlich gibt es 2 Lösungen:
#a) du löschst die matplotlibrc aus dem Ordner (oder benennst sie um). die ist als Backup nochmal im Überordner. du kannst sie also nach belieben löschen und wieder einfügen.
#b) du schreibst in der Konsole vor dem Ausruck python, den Ausdruck TEXINPUTS=$(pwd): . in Summe also   TEXINPUTS=$(pwd): python plot_HH1.py
# pwd ist in diesem Falle ein Befehl und heißt print (current) work directory. er fügt als pwd also das Verzeichnis ein, von dem das Programm aus geöffnet wurde (also der Pfad, den die konsole anzeigt)
#die tex-header sind nur wichtig, wenn du z.b. als Achsenbeschriftung Latex-code verwendest. dadurch dauert das Erstellen der Plots auch viel länger.
#zum debuggen bzw. rumprobieren empfiehlt sich also, die header erstmal wegzulassen und am Ende die Achsenbeschriftung vernünftig mit Latex zu machen
#ich glaube dieses Anliegen hat mich insgesmt 3 Stunden gekostet. hoffe, ich konnte dir diese Zeit ersparen ;)
#HH1 = Helmholtz 1. Messung

import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams.update({
'font.family': 'serif',
'text.usetex': True,
'pgf.rcfonts': False,
'pgf.texsystem': 'lualatex',
'pgf.preamble': r'\usepackage{unicode-math}\usepackage{siunitx}',
})

my_0=4*np.pi*10**(-7)
I=3.03
R=62.5 #in mm --> B wird in kT ausgerechnet, weil ein Faktor 10^3 "übrig bleibt"
factor=0.5*my_0 *I*R*R

d1=62.5
plt.clf()
#Plot1
#x=np.array([7,9,10.5,12,13.5,68.5,69,70,75,80,85,90,95,100])
x=np.array([-7.75,-5.75,-4.25,-2.75,-1.25,53.75,54.25,55.25,60.25,65.25,70.25,75.25,80.25,85.25])
y=np.array([4.239,4.231,4.234,4.260,4.239,3.003,2.960,2.891,2.666,2.445,2.219,2.018,1.839,1.662])
plt.plot(x,y,'r.',label='Messwerte')
z=np.linspace(-15,95)
plt.plot(z,10**8*factor*(R*R + (z-0.5*d1)**2)**(-1.5) + 10**8*factor*(R*R + (z+0.5*d1)**2)**(-1.5),label='Erwartete Kurve')
plt.legend()
plt.grid()
#axvline(x=-31.25)
#axvline(x=31.25)
plt.xlabel(r'$y\,/\,\mathrm{mm}$')
plt.ylabel(r'$B\,/\,\mathrm{mT}$')
#plt.plot([7,9,10.5,12,13.5,68.5,69,70,75,80,85,90,95,100],[4.239,4.231,4.234,4.260,4.239,3.003,2.960,2.891,2.666,2.445,2.219,2.018,1.839,1.662],'ro')
plt.savefig('plot1.pdf')

d2=52
plt.clf()
#Plot2
x=np.array([-28.5,-19.5,-8.5,-2,8.5,19,73,79.5,84.5,89.5,94.5,124.5,154.5,194.5])
y=np.array([3.091,2.976,2.887,2.882,2.945,3.081,2.639,2.410,2.194,2.031,1.849,1.036,0.615,0.366])
plt.plot(x,y,'r.',label='Messwerte')
z=np.linspace(-40,210)
plt.plot(z,10**8*factor*(R*R + (z-0.5*d2)**2)**(-1.5) + 10**8*factor*(R*R + (z+0.5*d2)**2)**(-1.5),label='Erwartete Kurve')
plt.legend()
plt.grid()
#axvline(x=-52)
#axvline(x=52)
plt.xlabel(r'$y\,/\,\mathrm{mm}$')
plt.ylabel(r'$B\,/\,\mathrm{mT}$')
plt.savefig('plot2.pdf')

d3=65
plt.clf()
#Plot3
x=np.array([-41.5,-26.5,-18.5,-3.5,2.5,14.5,30.5,85.5,100.5,106.5,114.5,122.5,130.5,141.5,159.5])
y=np.array([2.754,2.420,2.288,2.199,2.211,2.354,2.688,2.529,2.007,1.789,1.540,1.315,1.128,0.909,0.663])
plt.plot(x,y,'r.',label='Messwerte')
z=np.linspace(-55,175)
plt.plot(z,10**8*factor*(R*R + (z-0.5*d3)**2)**(-1.5) + 10**8*factor*(R*R + (z+0.5*d3)**2)**(-1.5),label='Erwartete Kurve')
plt.legend()
plt.grid()
#axvline(x=-65)
#axvline(x=65)
plt.xlabel(r'$y\,/\,\mathrm{mm}$')
plt.ylabel(r'$B\,/\,\mathrm{mT}$')
plt.savefig('plot3.pdf')

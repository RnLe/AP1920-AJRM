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

import matplotlib.pyplot as plt
import numpy as np

x=np.array([7,9,10.5,12,13.5,68.5,69,70,75,80,85,90,95,100])
y=np.array([4.239,4.231,4.234,4.260,4.239,3.003,2.960,2.891,2.666,2.445,2.219,2.018,1.839,1.662])
plt.plot(x,y,'ro')
#plt.plot([7,9,10.5,12,13.5,68.5,69,70,75,80,85,90,95,100],[4.239,4.231,4.234,4.260,4.239,3.003,2.960,2.891,2.666,2.445,2.219,2.018,1.839,1.662],'ro')
plt.savefig('plot1.pdf')
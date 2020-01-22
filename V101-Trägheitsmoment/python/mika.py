import numpy as np

x = np.genfromtxt("messwerte.csv",delimiter=",",unpack=True,usecols=0)
y = np.genfromtxt("messwerte.csv",delimiter=",",unpack=True,usecols=1)

#### damit deklariert ihr die erste Spalte der datei "Messwerte.csv" als array x, die zweite als array y usw

#nun rechnet ihr mit eurem Messergebnis wie ihr wollt, am ende erhaltet ihr das array "ergebnis"
#Python schreibt SEHR viele Nachkommastellen, wenn ihr nicht aufpasst. Bevor ihr also eure Ergebnisse + Messwerte
#in eine neue csv datei schreibt, damit man diese in Latex einbinden kann, muss gerundet werden.

Ergebnisrund = ["%.3f" % elem for elem in ergebnis]

# Jeder Wert im array "Ergebnis" wird auf 3 dezimalstellen gerundet.
# Jetzt schreiben wir unsere Messergebnisse + Ergebnis in eine CSV Datei

with open("tabelle1.csv", "w") as f:
    writer= csv.writer(f)
    writer.writerows(zip(ergebnisrund,xrund,yrund))

# ihr öffnet die Datei "Tabelle1.csv" mit "w" (schreib) rechten. Wenn die Datei also nicht exisiert, wird diese erstellt und 
# die arrays "Ergebnisrund" usw werden rein geschrieben.
#
############################################################
# der nachfolgende Teil bezieht sich NICHT mehr auf eure Python datei, sondern auf die Latex datei, in der ihr eine Tabelle erstellen
# wollt mit euren messwerten + Ergebnissen
#in die Präambel:
\usepackage{csvsimple}
#################################
\begin{table}
  \centering
  \caption{Messwerte x und y sowie das Ergebnis nach Gleichung blabla.}
  \csvreader[tabular=c|c|c,
  head=false, 
  table head= $x\:/\:\si{\mega\hertz}$ & $y\:/\:\si{\centi\meter}$ & $Ergebnis \:/\: \si{\milli\tesla}$ \\\midrule,
  late after line= \\]
  {messwerte.csv}{1=\eins, 2=\zwei, 3=\drei}{$\num{\eins}$ & $\num{\zwei}$ & $\num{\drei}$}
  \label{tab:messwerte}
\end{table}
#head=false, damit das programm nicht in der csvdatei nach dem Namen der Header sucht
# Der Name der einzelnen spalten -> Table head. das "\:/\:" steht dafür, damit das "/" Zeichen angezeigt wird und nicht als befehl interpretiert wird
#1=\eins usw steht als deklarierung für die namen der einzelnen spalten, damit sie aufgerufen werden können. Das \num steht dafür, 
# ihr euch nicht mit dem Dezimaltrenner "," oder "." ärgern müsst. Late after line damit er am ende einer spalte nicht nach weiteren ergebnissen sucht sondern
# in die nächste spalte übergeht
import numpy as np
import csv

prefix = 'data/' if 'python' in __file__ else '../data/'

xAuslEigen, yAuslEigenKraft = np.genfromtxt(prefix + 'MessAuslenkungKraft.txt', unpack=True)
a1Eigen, a2Eigen, ZeitTrägEigen = np.genfromtxt(prefix + 'MessTrägheitEigen.txt', unpack=True)
ZeitTrägK1 = np.genfromtxt(prefix + 'MessTrägheitZylinderGroß.txt')
ZeitTrägK2 = np.genfromtxt(prefix + 'MessTrägheitZylinderKlein.txt')
ZeitTrägP1 = np.genfromtxt(prefix + 'MessTrägheitPuppePose1.txt')
ZeitTrägP2 = np.genfromtxt(prefix + 'MessTrägheitPuppePose2.txt')

KraftProAuslenkung =  np.round(yAuslEigenKraft / xAuslEigen * 1000, 2)
KraftProAuslenkungMittel = np.round(KraftProAuslenkung.mean(), 2)
KraftProAuslenkungSigma = np.round(KraftProAuslenkung.std(), 2)

ZeitTrägEigenMittel = np.round(ZeitTrägEigen.mean(), 2)
ZeitTrägK1Mittel = np.round(ZeitTrägK1.mean(), 2)
ZeitTrägK2Mittel = np.round(ZeitTrägK2.mean(), 2)
ZeitTrägP1Mittel = np.round(ZeitTrägP1.mean(), 2)
ZeitTrägP2Mittel = np.round(ZeitTrägP2.mean(), 2)

ZeitTrägEigenSigma = np.round(ZeitTrägEigen.std(), 2)
ZeitTrägK1Sigma = np.round(ZeitTrägK1.std(), 2)
ZeitTrägK2Sigma = np.round(ZeitTrägK2.std(), 2)
ZeitTrägP1Sigma = np.round(ZeitTrägP1.std(), 2)
ZeitTrägP2Sigma = np.round(ZeitTrägP2.std(), 2)

ZeitTrägAlleMittel = [ZeitTrägEigenMittel, ZeitTrägK1Mittel, ZeitTrägK2Mittel, ZeitTrägP1Mittel, ZeitTrägP2Mittel]
ZeitTrägAlleSigma = [ZeitTrägEigenSigma, ZeitTrägK1Sigma, ZeitTrägK2Sigma, ZeitTrägP1Sigma, ZeitTrägP2Sigma]
BeschrMess = ['Dünner Stab', 'Zylinder_{groß}', 'Zylinder_{klein}', 'Holzfigur Pose 1', 'Holzfigur Pose 2']

def writeToCsv(filename, rows):
    with open(filename + '.csv', "w") as f:
        writer = csv.writer(f)
        try: writer.writerows(rows)     # if rows is not iterable this will throw an error
        except: writer.writerow(rows)   # and this exception will catch it and call the function for single-row handling

writeToCsv(prefix + 'RechKraftProAusl', zip(KraftProAuslenkung))
writeToCsv(prefix + 'RechKraftProAuslMittSigm', (KraftProAuslenkungMittel, KraftProAuslenkungSigma))
writeToCsv(prefix + 'RechTrägK1MittSigm', (ZeitTrägK1Mittel, ZeitTrägK1Sigma))
writeToCsv(prefix + 'RechTrägK2MittSigm', (ZeitTrägK2Mittel, ZeitTrägK2Sigma))
writeToCsv(prefix + 'RechTrägP1MittSigm', (ZeitTrägP1Mittel, ZeitTrägP1Sigma))
writeToCsv(prefix + 'RechTrägP2MittSigm', (ZeitTrägP2Mittel, ZeitTrägP2Sigma))
writeToCsv(prefix + 'RechTrägAlleMittSigm', zip(BeschrMess, ZeitTrägAlleMittel, ZeitTrägAlleSigma))

import pandas as pd
import statistics
import csv
import numpy as np


"Colando os dados em listas"

with open('Cotas.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')

    AmbevCotas = []
    BardellaCotas = []
    BombrilCotas = []
    BraskemCotas = []
    PetrobrasCotas = []
    ValeCotas = []
    IbovespaCotas = []
    PoupançaCotas = []
    CDICotas = []
    SelicCotas = []


    for row in readCSV:
        Ambev = row[0]
        Bardella = row[1]
        Bombril = row[2]
        Braskem = row[3]
        Petrobras = row[4]
        Vale = row[5]
        Ibovespa = row[6]
        Poupança = row[7]
        CDI = row[8]
        Selic = row[9]

        AmbevCotas.append(Ambev)
        BardellaCotas.append(Bardella)
        BombrilCotas.append(Bombril)
        BraskemCotas.append(Braskem)
        PetrobrasCotas.append(Petrobras)
        ValeCotas.append(Vale)
        IbovespaCotas.append(Ibovespa)
        PoupançaCotas.append(Poupança)
        CDICotas.append(CDI)
        SelicCotas.append(Selic)

' Transformando str para int'

FloatAmbev = []
FloatBardell = []
FloatBombril = []
FloatBraskem = []
FloatPetrobras = []
FloatVale = []
FloatIbovespa = []
FloatPoupança = []
FloatCDI = []
FloatSelic = []

for val in AmbevCotas:
    FloatAmbev.append(float(val))

for val in BardellaCotas:
    FloatBardell.append(float(val))

for val in BombrilCotas:
    FloatBombril.append(float(val))

for val in BraskemCotas:
    FloatBraskem.append(float(val))

for val in PetrobrasCotas:
    FloatPetrobras.append(float(val))

for val in ValeCotas:
    FloatVale.append(float(val))

for val in IbovespaCotas:
    FloatIbovespa.append(float(val))

for val in PoupançaCotas:
    FloatPoupança.append(float(val))

for val in CDICotas:
    FloatCDI.append(float(val))

for val in SelicCotas:
    FloatSelic.append(float(val))

'Lista de retornos'

retornoAmbev = []
retornoBardell = []
retornoBombril = []
retornoBraskem = []
retornoPetrobras = []
retornoVale = []
retornoIbovespa = []
retornoPoupança = []
retornoCDI = []
retornoSelic = []

quantidadeDeCotas = len(FloatAmbev)

i = 0

while i < quantidadeDeCotas -1:

    rent = FloatAmbev[i+1]/FloatAmbev[i]
    retornoAmbev.append(float(rent))
    rent = FloatBardell[i + 1] / FloatBardell[i]
    retornoBardell.append(float(rent))
    rent = FloatBombril[i + 1] / FloatBombril[i]
    retornoBombril.append(float(rent))
    rent = FloatBraskem[i + 1] / FloatBraskem[i]
    retornoBraskem.append(float(rent))
    rent = FloatPetrobras[i + 1] / FloatPetrobras[i]
    retornoPetrobras.append(float(rent))
    rent = FloatVale[i + 1] / FloatVale[i]
    retornoVale.append(float(rent))
    rent = FloatIbovespa[i + 1] / FloatIbovespa[i]
    retornoIbovespa.append(float(rent))
    rent = FloatPoupança[i + 1] / FloatPoupança[i]
    retornoPoupança.append(float(rent))
    rent = FloatCDI[i + 1] / FloatCDI[i]
    retornoCDI.append(float(rent))
    rent = FloatSelic[i + 1] / FloatSelic[i]
    retornoSelic.append(float(rent))

    i += 1

"Média dos retornos"

medAmbev = statistics.mean(retornoAmbev) - 1
medBardell = statistics.mean(retornoBardell) - 1
medBombril = statistics.mean(retornoBombril) - 1
medBraskem = statistics.mean(retornoBraskem) - 1
medPetrobras = statistics.mean(retornoPetrobras) - 1
medVale = statistics.mean(retornoVale) - 1
medIbovespa = statistics.mean(retornoIbovespa) - 1
medPoupança = statistics.mean(retornoPoupança) - 1
medCDI = statistics.mean(retornoCDI) - 1
medSelic = statistics.mean(retornoSelic) - 1

matrixMedRetornos = np.array([[medAmbev],[medBardell],
                              [medBombril],[medBraskem],
                              [medPetrobras],[medVale],
                              [medIbovespa],[medPoupança],
                              [medCDI],[medSelic]])

"Desvio Padrão de amostra de população"

DVPOPAmbev = statistics.stdev(retornoAmbev, xbar=None)
DVPOPBardell = statistics.stdev(retornoBardell, xbar=None)
DVPOPBombril = statistics.stdev(retornoBombril, xbar=None)
DVPOPBraskem = statistics.stdev(retornoBraskem, xbar=None)
DVPOPPetrobras = statistics.stdev(retornoPetrobras, xbar=None)
DVPOPVale = statistics.stdev(retornoVale, xbar=None)
DVPOPIbovespa = statistics.stdev(retornoIbovespa, xbar=None)
DVPOPPoupança = statistics.stdev(retornoPoupança, xbar=None)
DVPOPCDI = statistics.stdev(retornoCDI, xbar=None)
DVPOPSelic = statistics.stdev(retornoSelic, xbar=None)

matrixDV = np.array([[DVPOPAmbev],[DVPOPBardell],[DVPOPBombril],[DVPOPBraskem],[DVPOPPetrobras],[DVPOPVale],[DVPOPPoupança],[DVPOPCDI],[DVPOPSelic]])

"Dataframe Covariância"

#matrizDeRetornos = np.row_stack((FloatAmbev, FloatBardell, FloatBombril, FloatBraskem, FloatPetrobras,
#                           FloatVale, FloatIbovespa, FloatPoupança, FloatCDI, FloatCDI))

#Covariancia = np.asmatrix(np.cov(matrizDeRetornos))

#print(Covariancia)

retornoAmbev = retornoAmbev

d = {'Ambev': retornoAmbev, 'Bardell': retornoBardell,
     'Bombril': retornoBombril,'Braskem': retornoBraskem,
     'Petrobras': retornoPetrobras,'Vale': retornoVale,
     'Ibovespa': retornoIbovespa,'Poupança': retornoPoupança,
     'CDI': retornoCDI,'SELIC': retornoSelic}

df = pd.DataFrame(data=d)
pdCOV = df.cov()

matrixcov = []


# Fabio -----------------------------------------------------
#array_matrix = df.reset_index().values
#array_matrix = df.reset_index().values.ravel().view()
#array_matrix = np.array(df.to_records().view(type=np.matrix))
array_matrix = np.array(pdCOV.to_records().view(type=np.matrix))



print(pdCOV)
print()
print(array_matrix)

# ----------------------------------------------------------------


with open('cov.csv','w') as arquivo:
    arquivo.write(str(pdCOV))

with open('Cov.csv') as csvfile2:
    readCSV2 = csv.reader(csvfile2, delimiter=';')
    x = []
    x = row[0]
    print(x)

"SHARPE"

"O Certo"

#sharpeAmbev = (medAmbev - medCDI)/DVPOPAmbev
#sharpeBardell = (medBardell - medCDI)/DVPOPBardell
#sharpeBombril = (medBombril - medCDI)/DVPOPBombril
#sharpeBraskem = (medBraskem - medCDI)/DVPOPBraskem
#sharpePetrobras = (medPetrobras - medCDI)/DVPOPPetrobras
#sharpeVale = (medVale - medCDI)/DVPOPVale
#sharpeIbovespa = (medIbovespa - medCDI)/DVPOPIbovespa
#sharpePoupança = (medPoupança - medCDI)/DVPOPPoupança
#sharpeCDI = (medCDI - medCDI)/DVPOPCDI
#sharpeSelic = (medSelic - medCDI)/DVPOPSelic

"Deletar depois"

sharpeAmbev = medAmbev/DVPOPAmbev
sharpeBardell = medBardell/DVPOPBardell
sharpeBombril = medBombril/DVPOPBombril
sharpeBraskem = medBraskem/DVPOPBraskem
sharpePetrobras = medPetrobras/DVPOPPetrobras
sharpeVale = medVale/DVPOPVale
sharpeIbovespa = medIbovespa/DVPOPIbovespa
sharpePoupança = medPoupança/DVPOPPoupança
sharpeCDI = medCDI/DVPOPCDI
sharpeSelic = medSelic/DVPOPSelic

"Pessos de alocação"

PesoAmbev = 0.1
PesoBardell = 0.1
PesoBombril = 0.1
PesoBraskem = 0.1
PesoPetrobras = 0.1
PesoVale = 0.1
PesoIbovespa = 0.1
PesoPoupança = 0.1
PesoCDI = 0.1
PesoSelic = 0.1

matrixPesos = np.array([[PesoAmbev],[PesoBardell],[PesoBombril],[PesoBraskem],[PesoPetrobras],[PesoVale],[PesoIbovespa],[PesoPoupança],[PesoCDI],[PesoSelic]])
matrixPesos2 = np.matrix(matrixPesos)


TotalAlocação = PesoAmbev + PesoBardell + PesoBombril + PesoPetrobras + PesoBraskem + PesoVale + PesoIbovespa + PesoPoupança + PesoCDI + PesoSelic


"Rentabilidade da Carteira"


matrizDeRetornos = matrixMedRetornos * matrixPesos
retornosDaCarteira = np.sum(matrizDeRetornos)
#print(retornosDaCarteira)

"Desvio padrão da Carteira"

#DPcarteira = np.sqrt(matrixPesos.T * Covariancia * matrixPesos)
#print(DPcarteira)







# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 11:30:54 2025

@author: Jon-k
"""
#Kjør hele programet for at tilgangen til support_uke_24.xlsx skal laste inn sikkelig. 
#Dette gjøres før man kjører hver enkelt deloppgave-program..
#%% del 1

import pandas as pd

# Last inn data fra Excel-filen
file_path = 'support_uke_24.xlsx'
data = pd.read_excel(file_path)

# Fyll ut manglende ukedager med verdien over
data['Ukedag'] = data['Ukedag'].ffill()

# Lagre hver kolonne i de respektive arrayene
u_dag = data['Ukedag'].to_numpy()
kl_slett = data['Klokkeslett'].to_numpy()
varighet = data['Varighet'].to_numpy()
score = data['Tilfredshet'].to_numpy()

# Vis de første elementene av hver array for å verifisere resultatene
print("Ukedag:", u_dag[:5])
print("Klokkeslett:", kl_slett[:5])
print("Samtalens varighet:", varighet[:5])
print("Kundens tilfredshet:", score[:5])

#%% del b

import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the Excel file
file_path = 'support_uke_24.xlsx'
data = pd.read_excel(file_path)

# Store each column in the respective arrays
u_dag = data.iloc[:, 0].to_numpy()

# Count the number of requests for each weekday
calls_per_day = pd.Series(u_dag).value_counts()

# Plot the data
plt.figure(figsize=(10, 6))
calls_per_day.plot(kind='bar')
plt.title('Antall teleforner pr. dag')
plt.xlabel('Dagen i uken')
plt.ylabel('Antall telefoner')
plt.show()



#%% del c

import pandas as pd

# Last inn data fra Excel-filen
file_path = 'support_uke_24.xlsx'
data = pd.read_excel(file_path)

# Konverter varighet til timedelta objekter
data['Varighet'] = pd.to_timedelta(data['Varighet'])

# Finn korteste og lengste samtaletid
minste_varighet = data['Varighet'].min()
lengste_varighet = data['Varighet'].max()

# Skriv resultatene til skjermen med informativ tekst
print(f'Den korteste samtaletiden loggført for uke 24 er: {minste_varighet}')
print(f'Den lengste samtaletiden loggført for uke 24 er: {lengste_varighet}')



#%% del d

import pandas as pd

# Last inn data fra Excel-filen
file_path = 'support_uke_24.xlsx'
data = pd.read_excel(file_path)

# Lagre hver kolonne i de respektive arrayene
u_dag = data.iloc[:, 0].to_numpy()
kl_slett = data.iloc[:, 1].to_numpy()
varighet = data.iloc[:, 2].to_numpy()
score = data.iloc[:, 3].to_numpy()

# Vis de første elementene av hver array for å verifisere resultatene
print("Ukedag:", u_dag[:5])
print("Klokkeslett:", kl_slett[:5])
print("Samtalens varighet:", varighet[:5])
print("Kundens tilfredshet:", score[:5])

# Konverter varighet til timedelta objekter
data['Varighet'] = pd.to_timedelta(data['Varighet'])

# Beregn gjennomsnittlig samtaletid
gjennomsnittlig_varighet = data['Varighet'].mean()

# Skriv resultatet til skjermen med informativ tekst
print(f'Gjennomsnittlig samtaletid for uke 24 er: {gjennomsnittlig_varighet}')


#%% del e

import pandas as pd
import matplotlib.pyplot as plt

# Last inn data fra Excel-filen
file_path = 'support_uke_24.xlsx'
data = pd.read_excel(file_path)

# Konverter klokkeslett til datetime-objekter for enkel gruppering
data['Klokkeslett'] = pd.to_datetime(data['Klokkeslett'], format='%H:%M:%S').dt.time

# Definer tidsbolker
tidspunkt_labels = ['08-10', '10-12', '12-14', '14-16']
tidspunkt_ranges = [(pd.to_datetime('08:00:00').time(), pd.to_datetime('10:00:00').time()),
                    (pd.to_datetime('10:00:00').time(), pd.to_datetime('12:00:00').time()),
                    (pd.to_datetime('12:00:00').time(), pd.to_datetime('14:00:00').time()),
                    (pd.to_datetime('14:00:00').time(), pd.to_datetime('16:00:00').time())]

# Tell antall henvendelser i hver tidsbolk
henvendelser_pr_tidspunkt = []
for start, end in tidspunkt_ranges:
    count = sum(start <= tid < end for tid in data['Klokkeslett'])
    henvendelser_pr_tidspunkt.append(count)

# Visualiser resultatet med et sektordiagram
plt.figure(figsize=(8, 8))
plt.pie(henvendelser_pr_tidspunkt, labels=tidspunkt_labels, autopct='%1.1f%%')
plt.title('Henvendelser fordelt i tidsbolker med andel prosent for uke 24')
plt.show()

#%% del f

import pandas as pd

# Last inn data fra Excel-filen
file_path = 'support_uke_24.xlsx'
data = pd.read_excel(file_path)

# Fyll ut manglende ukedager med verdien over
data['Ukedag'] = data['Ukedag'].ffill()

# Filtrer ut rader med manglende tilbakemelding på tilfredshet
tilfredshet_data = data.dropna(subset=['Tilfredshet']).copy()

# Definer funksjon for å kategorisere kundens tilfredshet
def kategoriser_tilfredshet(score):
    if score >= 9:
        return 'Positiv'
    elif score >= 7:
        return 'Nøytral'
    else:
        return 'Negativ'

# Anvend funksjonen på tilfredshet-kolonnen
tilfredshet_data['Kategori'] = tilfredshet_data['Tilfredshet'].apply(kategoriser_tilfredshet)

# Beregn antall i hver kategori
positive_kunder = len(tilfredshet_data[tilfredshet_data['Kategori'] == 'Positiv'])
noytrale_kunder = len(tilfredshet_data[tilfredshet_data['Kategori'] == 'Nøytral'])
negative_kunder = len(tilfredshet_data[tilfredshet_data['Kategori'] == 'Negativ'])
ikke_svar = len(data) - len(tilfredshet_data)

# Beregn prosentandel av hver kategori
total_kunder = len(tilfredshet_data)
prosent_positive = (positive_kunder / total_kunder) * 100
prosent_negative = (negative_kunder / total_kunder) * 100

# Beregn NPS
NPS = prosent_positive - prosent_negative

# Skriv resultatet til skjermen med informativ tekst
print(f'Supportavdelingens NPS for uke 24 er: {NPS:.2f}')
print(f'Antall kunder som er positive (Score 9-10): {positive_kunder}')
print(f'Antall kunder som er nøytrale (Score 7-8): {noytrale_kunder}')
print(f'Antall kunder som er negative (Score 1-6): {negative_kunder}')
print(f'Antall kunder som ikke har svart: {ikke_svar}')


#%% - sjekker rader og koloner  - Testing av innhold & importering av excel-fil

print(data.head())
print(data.dtypes)
#%% Testing av innhold & importering av excel-fil
import pandas as pd

# Last inn data fra Excel-filen
file_path = 'support_uke_24.xlsx'
data = pd.read_excel(file_path)

# Vis alle kolonner og rader i dataene
print(data)

#%% Testing av innhold & importering av excel-fil
import pandas as pd

# Last inn data fra Excel-filen
file_path = 'support_uke_24.xlsx'
data = pd.read_excel(file_path)

# Vis de første rader i dataene for å verifisere innlasting
print(data.head())

# Vis informasjon om dataene
print(data.info())

# Vis en statistisk oppsummering av dataene
print(data.describe())

  
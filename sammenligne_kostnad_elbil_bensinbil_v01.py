# -*- coding: utf-8 -*-
"""
Besvarelse på arbeidskrav 1 i py1010 26H
Sammenligning av årlige kostader ved el- og bensinbil

Created on Tue Sep 15 21:00:34 2026
@author: glennS

Version 01 2026_09_15
"""

#%% Bilbruk

K = 10000.0 # [km/aar] Bilbruk aarlig

D = 365 # [dager] Dager i et år

#%% Forsikring

FEA = 5000.0  # [kr/aar] Forsikring Elbil Aarlig
FBA = 7500.0  # [kr/aar] Forsikring Bensinbil Aarlig

#%% Trafikkforsikringsavgift

T = 8.38  # [kr/dag] Trafikkforsikringsavgift per dag

TA = T * D  # [kr/aar] Trafikkforsikringsavgift Aarlig elbil/bensinbil

#%% Drivstoffbruk

DS = 0.2  # [kWh/km] Strømbruk elbil per kilometer
S = 2.00  # [kr/kWh] Strømpris per kilowattime

DE = DS * S  # [kr/km] Drivstoffkostnad Elbil per kilomenter

DEA = DE * K  # [kr/aar] Drivstoffkostnad Elbil Aarlig


DB = 1.0  # [kr/km] Drivstoffkostnad bensinbil per kilometer

DBA = DB * K  # [kr/km] Drivstoffkostnad Bensinbil Aarlig

#%% Bomavgift

BE = 0.1  # [kr/km] Bomavgift Elbil per kilometer

BEA = BE * K  # [kr/aar] Bomavgift Elbil Aarlig


BB = 0.3  # [kr/km] Bomavgift Bensinbil per kilometer

BBA = BB * K  # [kr/aar] Bomavgift Bensinbil Aarlig

#%% Utregning

SE = FEA + TA + DEA + BEA  # Sum Elbil

SB = FBA + TA + DBA + BBA  # Sum Bensinbil

DF = SB - SE  # Differanse Sum Bensinbil minus Sum Elbil

#%% Print

print('Sammenligning av årlige kostader ved el- og bensinbil')
print(' ')
print('Bilbruk aarlig =', K, 'km')
print('Forsikringskostnad aarlig =', FEA, 'kr (elbil) og', FBA, 'kr (bensinbil)')
print('Trafikkforsikringsavgift aarlig =', TA, 'kr (elbil / bensinbil)')
print('Drivstoffkostnad aarlig =', DEA, 'kr (elbil) og', DBA, 'kr (bensinbil')
print('Bomavgift aarlig =', BEA, 'kr (elbil) og', BBA, 'kr (bensinbil)')
print(' ')
print('Sum elbil =', SE, 'kr aarlig')
print('Sum bensinbil =', SB, 'kr aarlig')
print(' ')
print('Differanse bensinbil - elbil =', DF, 'kr aarlig')
print('Elbil er', DF, 'kroner billigere i året enn bensinbil.')
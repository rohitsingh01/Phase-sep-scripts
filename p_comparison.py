import matplotlib.pyplot as plt
import numpy as np


proteins = ['RHG32', 'ATG9a', 'SKP2', 'GRAP2', 'RND2', 'SRPK2', 'NCK1', 'DAB2P', 'MEFV', 'MITF', 'MYPT1', 'IL3RB', 'MDM4',
            'NMDE3', 'ATX1', 'GLI2', 'ULK1', 'ESR1', 'ACHA4', 'SIK1', 'RON', 'KLC1', 'AKP13', 'TIAM1', 'CDK16', 'LCP2', 'MK07', 
            'ZNRF1', 'RUBIC', 'DDT4L', 'EDC3', 'SLIK1', 'CIC', 'RMD3', 'PKP2', 'MYLK2', 'CENPJ', 'REEP4', 'PAK6', 'RGS18' ,'DTL', 'PI4KB',
            'ERRFI', 'ING1', 'PRP19', 'EXO1', 'GPSM3', 'M3K2', 'LIMBD1', 'RIMS2']
y_14_3_3 = [2.07, 2.15, 1.893, 2.19, 1.998, 2.15, 2.15, 2.11, 1.939, 2.101, 2.045, 2.281, 1.998, 1.873, 1.901, 2.161, 2.01, 1.803, 1.947, 2.142,
            2.144, 2.111, 1.861, 1.796, 1.879, 2.276, 1.773, 2.07, 2.222, 1.722, 1.879, 2.087, 1.964, 1.964, 1.916, 1.904, 2.171, 1.919, 1.986, 1.935
            , 2.137, 1.936, 1.917, 2.006, 1.793, 1.887, 2.323, 1.923, 2.206, 1.945]
y_non_14_3_3 = [1.89, 1.82, 1.876, 1.995, 1.7625, 1.905, 1.815, 1.786, 1.96, 1.9455, 1.889, 1.918, 1.835, 1.872, 1.960,
              1.912, 1.833, 1.841, 1.799, 1.67, 1.855, 1.831, 1.946, 1.866, 1.779, 1.94, 2.04, 1.877, 1.866, 1.719, 1.8735, 1.817, 
              2.034, 1.7625, 1.817, 1.747, 1.840, 1.853, 1.929, 1.806, 1.905, 1.812, 1.9635, 1.79, 1.749, 1.9392, 2.042, 1.977, 1.943, 1.815]

x = np.arange(len(proteins))
width = 0.35


fig, ax = plt.subplots(figsize=(12, 8))
bars_14_3_3 = ax.bar(x - width/2, y_14_3_3, width, label='14-3-3 Site Propensity', color='blue')
bars_non_14_3_3 = ax.bar(x + width/2, y_non_14_3_3, width, label='Non 14-3-3 Sites Average Propensity', color='orange')
ax.set_xlabel('Proteins')
ax.set_ylabel('Phase Separation Propensity')
ax.set_title('Propensity of 14-3-3 and Non 14-3-3 Sites for 14-3-3 Client Proteins')
ax.set_xticks(x)
ax.set_xticklabels(proteins, rotation = 90)
ax.legend()

plt.ylim(1.6, 2.3)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()
print(len(proteins))
count= 0
for i in range(50):
    if (y_14_3_3[i] > y_non_14_3_3[i]):
        count+=1
print(count)       
            
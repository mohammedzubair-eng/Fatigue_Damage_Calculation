# Python program for calculating fatigue damage value related to the stress and steel material grade properties
# Fatigue damage is calculated based on formulae from ASME/API and British standards code.

########################################################################################

# For Material SS304

import numpy as np
ym = 199996
srange = [423.56*1000000, 1]
damage_list = []
amplitude = srange[0] * 0.5 / 1000000
y = np.log10(28.3e3 * (amplitude / ym))
if amplitude <= 40:
    damage = 1e-12
    damage_list.append(damage)
elif (10 ** y) >= 14.4:
    x = (17.0181 - 19.8713 * y + (4.21366 * y ** 2)) / ( 1 - 0.1720606 * y - 0.633592 * (y ** 2))
    n = np.exp(x * np.log(10))
    damage = srange[1] / n
    damage_list.append(damage)
else:
    x = 1 / (- 0.331096 + (4.3261 * np.log(y)) / y ** 2 )
    n = np.exp(x * np.log(10))
    damage = srange[1] / n
    damage_list.append(damage)
print(damage_list)

###########################################################################################

# For Material SA106

import numpy as np
ym = 191000
srange = [241.0*1000000, 1]
damage_list = []
amplitude = srange[0] * 0.5 / 1000000
y = np.log10(28.3e3 * (amplitude / ym))
if amplitude <= 40:
    damage = 1e-12
    damage_list.append(damage)
elif (10 ** y) >= 20:
    x = (-4706.5245 + 1813.6228 * y + (6785.5644 / y) - (368.12404 * y ** 2) - (5133.7345 / y ** 2) + (30.708204 * y ** 3) + (1596.1916 / y ** 3))
    n = np.exp(x * np.log(10))
    damage = srange[1] / n
    damage_list.append(damage)
else:
    x = (38.1309 - (60.17504 * y ** 2) + (25.0352 * y ** 4)) / (1 + (1.80224 * y ** 2) - (4.68904 * y ** 4) + (2.26536 * y ** 6))
    n = np.exp(x * np.log(10))
    damage = srange[1] / n
    damage_list.append(damage)
print(damage_list)

#############################################################################################

# For All Steel BS Standard

import numpy as np
ym = 199996
srange = 46.61
damage_list = []
log_n = 12.2371 - (2*0.2183) - 3*np.log10(srange)
n = 10**log_n
damage = 1 / n
damage_list.append(damage)
life  = 1 / damage
print('damage:', damage_list[0])
print('life:', life)
time = 365*24/48
print('life in years:', life / time)

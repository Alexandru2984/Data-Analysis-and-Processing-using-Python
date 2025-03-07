import numpy as np

startDate = 1899
endDate = 2025
##Este bisect daca este divizibil cu 400
##Este divizibil cu 4 dar nu cu 100

array = np.arange(startDate, endDate+1)

divizibile_cu_400 = array % 400 == 0
divizibile_cu_4 = array % 4 == 0
nedivizibile_cu_100 = array % 100 != 0

print(array[divizibile_cu_400 | (divizibile_cu_4 & nedivizibile_cu_100)])
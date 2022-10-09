

import matplotlib.pyplot as plt

nomes = []
titulos = []

f = open('titulos.txt' , 'r')
for row in f:
    row = row.split('')
    nomes.append(row[0])
    titulos.append(int(row[1]))

plt.bar(nomes , titulos , color = 'g' , label = 'File Data')

plt.xlabel('nomes' , fontsize = 12)
plt.ylabel('titulos' , fontsize = 12)

plt.title('nomes' , fontsize = 20)
plt.legend()
plt.show()











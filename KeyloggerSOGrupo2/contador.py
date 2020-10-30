import collections
import pprint
import subprocess
import platform
import numpy as np
import matplotlib.pyplot as plt

sistema = platform.system()

if(sistema=="Linux"):
	subprocess.call(['sh', './conteo.sh'])
	
if(sistema=="Windows"):
	subprocess.call(['bat', './conteo.bat'])

nombre_archivo = 'reporte2.txt'

with open(nombre_archivo, "r") as f:
    conteo_caracteres = collections.Counter(f.read().upper())
    salida = pprint.pformat(conteo_caracteres)

#print(conteo_caracteres)
archivo = open("conteo.txt", "w")
archivo.write(salida)
archivo.close()

labels, values = zip(*conteo_caracteres.items())

indexes = np.arange(len(labels))
width = 1

plt.bar(indexes, values, width)
plt.xticks(indexes + width * 0.5, labels)
plt.savefig('histograma.png')

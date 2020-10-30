import platform
import subprocess
sistema = platform.system()

if(sistema=="Linux"):
	subprocess.call(['sh', './datos.sh'])
	
if(sistema=="Windows"):

	 p = subprocess.Popen("conteo.bat", cwd=r"C:\Users\andy1\Documents\UNI\7MO CICLO\Sistemas operativos\parcial\expst3142020igrupo2-master\KeyloggerSOGrupo2\datos.bat")
	 stdout, stderr = p.communicate()

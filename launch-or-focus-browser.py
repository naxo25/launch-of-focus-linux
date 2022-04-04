# importing webbrowser python module
import webbrowser
import subprocess

#Assigning URL to be opened
url = "https://nacholabraweb.000webhostapp.com/"
link = subprocess.run(["/home/nax/.miConfig/jumpapp/jumpapp", "brave"])

# Detectar si navegador esta abierto
if (link.returncode == 0):
	print (link.returncode);
else:
	#Open url in default browser
	webbrowser.open(url);

import shutil

# Stringverarbeitung mit Python
# # # Funktionen # # # 
def operate_on_file(myFileName):
	fileObject = open(myFileName, "r")
	print("\nDatei geöffnet:", fileObject)
	
	# Erzeuge Datenstruktur
	print(" Erstelle Dictionary.")
	woerter = {}

	# Iteriere zeilenweise durch
	# fileObject
	print(" Kopiere Schlüssel-Wert Paare in Dictionary")
	for line in fileObject:
		# Methode strip entfernt die Whitespaces
		# Auch Zeilenumbrüche vor und hinter String
		line = line.strip()
		# Methode Split zerlegt zwei Teile der eingelesenen
		# Zeile in eine Liste
		zuordnung = line.split(" ")
		woerter[zuordnung[0]] = zuordnung[1]
	print(woerter)
	fileObject.close()

def leerzeichen_test_01():
	# (1)
	# Quelldatei kopieren
	print("Kopiere Quelldatei.")
	try:
		shutil.copy("whitespaces.txt", "no_Whitespaces.txt")
		print("Quelldatei kopiert.")
	except Exception:
		print("Quelldatei konnte nicht kopiert werden.")

	# (1.1)
	# Kopie der Quelldatei öffnen
	try:
		#fileHandler = open("no_Whitespaces.txt", "rt")

		fileHandlerRead = open("no_Whitespaces.txt", "r")
		fileHandlerWrite = open("no_Whitespaces.txt", "w")

		#print("Datei geöffnet:", fileObject)
		#fileOut = open(no_Whitespaces.txt, "rw")
		#print("Datei geöffnet:", fileOut)
	except Exception:
		print("Datei konnte nicht geoffnet werden.")

	# (2)
	# Stringverarbeitung



	# (2.1)
	# Daten auslesen
	for line in fileHandlerRead:

		# (2.1.1)
		# Rückgabewert der Methode string.strip ist eine Kopie
		# des Strings, bei dem voranstehende und nachfolgende
		# Zeichen entfernt wurden. Leerzeichen werden entfernt.
		counter = 0
		line = line.strip()
		fileHandlerWrite.write(line)
		fileHandlerWrite.write(counter)

		#fileHandler.write(line)
		# Methode Split zerlegt zwei Teile der eingelesenen
		# Zeile in eine Liste
		#zuordnung = line.split(" ")

	# (2.2)
	# In Datei schreiben
	#with fileHandlerWrite as fhw:
	#	fhw.write("Test01.\n")

	#with fileHandlerWrite as fhw:
	#	fhw.write("Test02.\n")

	fileHandlerWrite.write("test01.\n")
	fileHandlerWrite.write("Test02.\n")
	fileHandlerWrite.write("Test03.\n")


	# (3)	
	# Dateien schließen	
	try: 
		fileHandlerRead.close()
		fileHandlerWrite.close()
		#print("Datei geschlossen:", fileObject)
		#fileOut.close()
		#print("Datei geschlossen:", fileOut)
	except Exception:
		print("Datei konnt nicht geschlossen werden.")

	# Lese von Datei
	with open("whitespaces.txt", "r") as myfile:
		firstLine = myfile.readline()
		print(type(firstLine))
		#cap_String = firstLine.capitalize()
		print(firstLine)
		print(myfile.read())
		# Datei schließt automatisch wegen
		# with Schlüsselwort

	# Schreibe in Datei
	myFileHandler = open("no_Whitespaces.txt", "w")
	myFileHandler.write(firstLine)
	myFileHandler.close()

	# (4)
	# Programmende
	print("EXIT 0")

def read_write_test():

	# Handler öffnen
	fileHandlerRead_ws = open("whitespaces.txt", "r")
	fileHandlerRead_no_ws = open("no_whitespaces.txt", "r")
	fileHandlerWrite_no_ws = open("no_Whitespaces.txt", "w")

	# Verarbeite
	myString1 = fileHandlerRead_ws.readline()
	fileHandlerWrite_no_ws.write(myString1)

	myString1 = fileHandlerRead_ws.readline()
	fileHandlerWrite_no_ws.write(myString1)

	myString1 = fileHandlerRead_ws.readline()
	fileHandlerWrite_no_ws.write(myString1)

	myString1 = fileHandlerRead_ws.readline()
	fileHandlerWrite_no_ws.write(myString1)

	fileHandlerWrite_no_ws.write("\nEND_OF_FILE.\n")


	# Handler schließen
	fileHandlerRead_ws.close()
	fileHandlerRead_no_ws.close()
	fileHandlerWrite_no_ws.close()

	

# # # MAIN # # #

# String Dateiname
myFileName = "woerterbuch.txt"

# Funktion mit übergebenem 
# String Argument
operate_on_file(myFileName)

#leerzeichen_test_01()

#read_write_test()
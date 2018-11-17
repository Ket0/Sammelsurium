
# Stringverarbeitung mit Python

# # # Funktionen # # # 
def operate_on_file(myFileName):
	# Öffnen der Datei mit Ausnahmebehandlung
	try:
		fileObject = open(myFileName, "r")
		print("Datei geöffnet:", myFileName)

		# mach was
		Programmlogik(fileObject)

		# Datei muss geschlossen werden
		try: 
			fileObject.close()
			print("Datei geschlossen:", myFileName)
		except Exception:
			print("Datei konnt nicht geschlossen werden.")
	#except Exception, e:
	#	raise
	except Exception:
		print("Datei konnte nicht geoffnet werden. Prüfen Sie Dateiintegrität oder Dateinamen.")
	finally:
		pass
		# mach noch was anderes
	
def Programmlogik(myFileHandler):
	# Operiere auf der Datei
	print("Hier arbeitet die Programmlogik.")
	pass

# # # MAIN # # #

# String Dateiname
myFileName = "woerterbuch.txt"

# Funktion mit übergebenem 
# String Argument
operate_on_file(myFileName)
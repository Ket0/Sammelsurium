def operate_on_file(myFileName):
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
	except Exception:
		print("Datei konnte nicht geoffnet werden. Prüfen Sie Dateiintegrität oder Dateinamen.")
	finally:
		pass
	
def Programmlogik(myFileHandler):
	# Operiere auf der Datei
	print("Hier arbeitet die Programmlogik.")
	pass

# # # MAIN # # #
myFileName = "woerterbuch.txt"
operate_on_file(myFileName)

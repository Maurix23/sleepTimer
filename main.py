import subprocess
from datetime import datetime
import platform

#Checking for current OS
osName = platform.system()


#Grabbing minutes/hours till shutdown
sleepMinutes = input("In wie vielen Minuten soll der PC herunterfahren?: ")
sleepHours = input("In wie vielen Stunden soll der PC herunterfahren?: ")

#timeTillShutdown = sleepHours * 60 * 60 + sleepMinutes * 60

#print("Der PC fährt in " + str(sleepMinutes) + " Minuten und " + str(sleepHours) + " Stunden herunter.")


#subprocess.run(["shutdown", sleepMinutes])
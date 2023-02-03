#- The `createLogFile(restartsDone)` function creates a log file or writes to an existing log file the number of times the Wi-Fi adapter has been restarted today.
#- The `writeToFile(WriteToFileResets, logFile)` function writes to the log file the time the Wi-Fi adapter was restarted and the number of restarts performed.
#- The `currentTime()` function returns the current time.
#- The `restart_wifi_adapterWin()` function restarts the Wi-Fi adapter on Windows, MacOS, or Linux depending on the operating system.
#- The `has_wifi_card()` function returns a Boolean indicating whether the computer has a Wi-Fi network card.


from checkconnection import *
from seleniumtest import *
import os.path
from os import path
from datetime import datetime
import subprocess
import ctypes
import sys
import platform
import json



# 200 = if user's not connected to internet at all / doesn't have internet enabled
# 201 = internet connection problem

#GLOBAL_VARIABLES
current_status = None
no_actions = 0
restartsDone = 0

#Check if the computer has a Wi-Fi network card. Returns True if a Wi-Fi card is found, 
#False otherwise.
def has_wifi_card():
    OS = platform.system()
    if OS == "Windows":
        result = subprocess.run("netsh interface show interface", shell=True, stdout=subprocess.PIPE)
        if "Wi-Fi" in result.stdout.decode():
            return True
        else:
            return False
    elif OS == "Darwin": # Mac OS
        result = subprocess.run("networksetup -listallhardwareports", shell=True, stdout=subprocess.PIPE)
        if "Wi-Fi" in result.stdout.decode():
            return True
        else:
            return False
    elif OS == "Linux":
        result = subprocess.run("iwconfig", shell=True, stdout=subprocess.PIPE)
        if "wlan" in result.stdout.decode():
            return True
        else:
            return False
    else:
        print("Unsupported operating system")
        return False

#Currently in development since I realized that it'd be pretty handy if it finds available SSIDs and then checks 
#if there's connection with the same name and then connect on it
def restart_wifi_adapterWin():
    if not has_wifi_card():
        print("It seems like you don't have Wi-Fi card")
    else:
        OS = platform.system()
        if OS == "Windows":
            subprocess.run("netsh interface set interface \"Wi-Fi\" admin=enable", shell=True, check=True)
        elif OS == "Darwin": # Mac OS
            subprocess.run("networksetup -setairportpower airport on", shell=True, check=True)
            subprocess.run("ifconfig en0 up", shell=True, check=True)
        elif OS == "Linux":
            subprocess.run("nmcli radio wifi on", shell=True, check=True)
            subprocess.run("rfkill unblock wifi", shell=True, check=True)
        else:
            print("Unsupported operating system")

#Vraca trenutno vrijeme
def currentTime():
    return datetime.now().strftime('[%Y-%m-%d %H:%M]')

#This function is used to write to files
def writeToFile(WriteToFileResets,logFile):
    mrkp1 = "===================="
    logFile.write(mrkp1 + "Reboot performed at: " + str(currentTime()) + mrkp1 + "\n" )
    logFile.write(mrkp1 + "Numbers of reboots performed:" + str(WriteToFileResets) + mrkp1 + "\n")
    

#This function is used to createLogFile, in case there's LogFile that exist it will just proceed with writing to file
def createLogFile(restartsDone):
    try:
        # Check if LogFile.txt exists
        if os.path.exists("LogFile.txt"):
            # Get the creation time of the file
            creation_time = os.path.getctime("LogFile.txt")
            # Convert the creation time to date format
            file_date = datetime.fromtimestamp(creation_time).date()
            # Get the current date
            current_date = datetime.now().date()
            # If the file creation date is equal to current date
            if file_date == current_date:
                # Open the file in append mode
                with open("LogFile.txt", "a") as my_log_file:
                    # Call the writeToFile function to write the restartsDone to the file
                    writeToFile(restartsDone, my_log_file)
            else:
                # Open the file in write mode
                with open("LogFile.txt", "w") as my_log_file:
                    # Call the writeToFile function to write the restartsDone to the file
                    writeToFile(restartsDone, my_log_file)
        else:
            # If the file does not exist, open the file in write mode
            with open("LogFile.txt", "w") as my_log_file:
                # Call the writeToFile function to write the restartsDone to the file
                writeToFile(restartsDone, my_log_file)
    except Exception as e:
        print("An error occurred while creating the log file: ", str(e))


#performAction: 1. Reboots router ; 2. Counts how many times restarts're done;
def performAction1():
    restartRouter()
    global restartsDone
    restartsDone = countAction()
    createLogFile(restartsDone)

#Currently in development: Will try to add option to automatically re-enable connection and connect to available network    
def performAction2():
    restart_wifi_adapterWin()
    print("Konekcija nije ostvarena")


#There'll be GUI, so we'll do something with this, probably make some stuff green
def performAction3():
    print("Konekcija uspostavljena i radi")
    
#This one checks how many times something is executed    
def countAction():
    global no_actions
    no_actions += 1
    return no_actions

#It checks if connection is back (had to use this because if we get our wifi off)
def ConnectionBack():
    current_status2 = check_connection()
    return current_status2


#This is kinda main function for now

while True:
    current_status = int(check_connection())
    #if there's conn problem
    if current_status == 201: #jeste 201 == ima problem sa internetom
        performAction1() #performAction(1)
        #uradio je action
        timesexecuted = 0 # setuj ovo na nula
        timesexecuted = countAction() 
        #provjerio je koliko se puta executovo kod
        if timesexecuted >= 1:
            #ukoliko je broj executovanja veci od jedan
            time.sleep(180)
            #stavi aplikaciju da spava
        else:
            continue         
    elif current_status == 200:
        performAction2()
        counter = countAction()
        if counter >= 1: #counter = 1
            stats = ConnectionBack() #200
            while stats == 200:
                time.sleep(1)
                stats = ConnectionBack()  
        else:
            continue        
                
    else:
        performAction3()
